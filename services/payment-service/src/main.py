from fastapi import FastAPI, HTTPException
from shared.models import PaymentRequest, PaymentStatusUpdate, Notification
from shared.utils import generate_unique_id
import httpx # For internal calls to User Management and Notification services

app = FastAPI(
    title="Payment Service",
    description="Handles payment processing and subscription management.",
    version="1.0.0"
)

# In-memory storage for transactions (replace with database in production)
# {transaction_id: {user_id, amount, status, ...}}
transactions_db = {}

# Simplified service URLs (replace with environment variables/discovery in production)
USER_MANAGEMENT_SERVICE_URL = "http://user-management-service:8001"
NOTIFICATION_SERVICE_URL = "http://notification-service:8008"

# --- Endpoints ---

@app.get("/health")
async def health_check():
    return {"status": "Payment Service is healthy"}

@app.post("/create-checkout-session")
async def create_checkout_session(req: PaymentRequest):
    transaction_id = generate_unique_id()
    transactions_db[transaction_id] = {
        "user_id": req.user_id,
        "amount": req.amount,
        "currency": req.currency,
        "plan_name": req.plan_name,
        "status": "pending",
        "gateway_url": f"https://dummy-payment-gateway.com/checkout?id={transaction_id}&amount={req.amount}" # Dummy URL
    }
    print(f"Payment session created for user {req.user_id}, transaction {transaction_id}. Status: PENDING.")
    return {
        "message": "Checkout session created (dummy)",
        "transaction_id": transaction_id,
        "redirect_url": transactions_db[transaction_id]["gateway_url"]
    }

@app.post("/webhook")
async def payment_webhook(update: PaymentStatusUpdate):
    # This endpoint simulates a webhook notification from a payment gateway
    transaction = transactions_db.get(update.transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    if transaction["status"] == "completed":
        print(f"Transaction {update.transaction_id} already completed. Ignoring webhook.")
        return {"message": "Transaction already processed"}

    transaction["status"] = update.status
    print(f"Webhook received for transaction {update.transaction_id}. New status: {update.status}")

    if update.status == "completed":
        # Update user's minutes in User Management Service
        user_id_to_update = update.user_id if update.user_id else transaction["user_id"]
        minutes_to_add = update.minutes_added if update.minutes_added is not None else 60 # Default 60 mins for $20
        
        async with httpx.AsyncClient() as client:
            try:
                # In a real app, this internal call would be authenticated (e.g., service-to-service token)
                resp = await client.post(
                    f"{USER_MANAGEMENT_SERVICE_URL}/update-minutes",
                    json={"user_id": user_id_to_update, "minutes_change": minutes_to_add}
                )
                resp.raise_for_status()
                print(f"Updated minutes for user {user_id_to_update}: added {minutes_to_add} minutes.")
                
                # Send notification
                notification_msg = f"Your payment for {transaction['plan_name']} was successful! You've received {minutes_to_add} minutes."
                await client.post(
                    f"{NOTIFICATION_SERVICE_URL}/send",
                    json=Notification(user_id=user_id_to_update, message=notification_msg, notification_type="payment_success").dict()
                )
            except httpx.HTTPStatusError as e:
                print(f"Error updating user minutes or sending notification: {e.response.text}")
                raise HTTPException(status_code=500, detail=f"Internal service error: {e.response.text}")
            except Exception as e:
                print(f"Unexpected error in payment webhook: {e}")
                raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
    
    return {"message": f"Webhook processed, transaction {update.transaction_id} status updated to {update.status}"}

@app.post("/debit-minutes")
async def debit_minutes(user_id: str, minutes: int):
    # This endpoint is called by the Audio Processing Orchestrator when a download occurs
    if minutes <= 0:
        raise HTTPException(status_code=400, detail="Minutes to debit must be positive.")

    async with httpx.AsyncClient() as client:
        try:
            # Internal call to User Management Service
            resp = await client.post(
                f"{USER_MANAGEMENT_SERVICE_URL}/update-minutes",
                json={"user_id": user_id, "minutes_change": -minutes} # Negative to debit
            )
            resp.raise_for_status()
            return {"message": f"Debited {minutes} minutes from user {user_id}", "status": "success"}
        except httpx.HTTPStatusError as e:
            print(f"Error debiting minutes for user {user_id}: {e.response.text}")
            if e.response.status_code == 404:
                raise HTTPException(status_code=404, detail="User not found for debit.")
            # Re-raise the original status code if it's not 404 for more specific error handling upstream
            raise HTTPException(status_code=e.response.status_code, detail=f"Failed to debit minutes: {e.response.text}")
        except Exception as e:
            print(f"Unexpected error in debit_minutes: {e}")
            raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")

@app.get("/transactions/{user_id}")
async def get_user_transactions(user_id: str):
    user_transactions = [
        {"transaction_id": tid, **data} for tid, data in transactions_db.items()
        if data["user_id"] == user_id
    ]
    return user_transactions