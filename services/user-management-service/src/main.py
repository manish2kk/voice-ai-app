from fastapi import FastAPI, HTTPException, Depends
from passlib.context import CryptContext
from shared.models import User, UserRegister, UserLogin, Token
from shared.utils import create_access_token, decode_access_token, generate_unique_id
import httpx # For internal calls to payment service
from datetime import timedelta

app = FastAPI(
    title="User Management Service",
    description="Handles user authentication, registration, and profile.",
    version="1.0.0"
)

# In-memory storage for users (replace with database in production)
# {user_id: User object}
users_db: dict[str, User] = {}
# Add a dummy admin user for testing
admin_user_id = generate_unique_id()
users_db[admin_user_id] = User(
    id=admin_user_id,
    username="admin",
    email="admin@example.com",
    password="admin_password_raw", # Will be hashed on first run
    role="admin",
    paid_status=True,
    minutes_remaining=99999
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Hash admin password on startup if not already hashed
@app.on_event("startup")
async def startup_event():
    for user_id, user_data in users_db.items():
        # Check if password is not already hashed (e.g., starts with $2b$)
        if not user_data.password.startswith("$2b$"): 
            users_db[user_id].password = hash_password(user_data.password)
            print(f"Hashed password for user: {user_data.username}")

# --- Utility to get current user (for internal authentication checks) ---
# This is for internal service-to-service calls or for admin access.
# For regular user profile/status, the API Gateway already passed validated token.
async def get_current_user_internal(token: str) -> dict:
    payload = decode_access_token(token)
    if "error" in payload:
        raise HTTPException(status_code=401, detail=payload["error"])
    user_id = payload.get("sub")
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return payload

# --- Endpoints ---

@app.get("/health")
async def health_check():
    return {"status": "User Management Service is healthy"}

@app.post("/register")
async def register_user(user: UserRegister):
    for u in users_db.values():
        if u.username == user.username:
            raise HTTPException(status_code=400, detail="Username already registered")
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    new_user_id = generate_unique_id()
    new_user = User(
        id=new_user_id,
        username=user.username,
        email=user.email,
        password=hashed_password,
        role="user",
        paid_status=False, # New users start as unpaid
        minutes_remaining=0
    )
    users_db[new_user_id] = new_user
    return {"message": "User registered successfully", "user_id": new_user_id}

@app.post("/login", response_model=Token)
async def login_user(user_login: UserLogin):
    user = next((u for u in users_db.values() if u.username == user_login.username), None)
    if not user or not verify_password(user_login.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=30) # Use the constant from shared.utils if preferred
    access_token = create_access_token(
        data={"sub": user.id, "username": user.username, "role": user.role},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/profile/{user_id}")
async def get_user_profile(user_id: str): # API Gateway handles token validation for this endpoint
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Return user details without the hashed password
    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "paid_status": user.paid_status,
        "minutes_remaining": user.minutes_remaining
    }

@app.get("/account-status/{user_id}")
async def get_account_status(user_id: str): # API Gateway handles token validation for this endpoint
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "user_id": user.id,
        "paid_status": user.paid_status,
        "minutes_remaining": user.minutes_remaining
    }

@app.post("/update-minutes")
async def update_user_minutes(user_id: str, minutes_change: int):
    # This endpoint is designed for internal service-to-service calls (e.g., from Payment Service)
    # In production, this would be protected by internal service authentication, not JWT from client.
    # For this demo, it's open for calls from Payment Service (which is itself not strictly authenticated in this demo).
    
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.minutes_remaining += minutes_change
    if user.minutes_remaining < 0:
        user.minutes_remaining = 0 # Prevent negative minutes
    
    # If minutes added, mark as paid. If it goes to 0, might revert to unpaid.
    if user.minutes_remaining > 0:
        user.paid_status = True
    else:
        user.paid_status = False
    
    print(f"User {user_id} minutes updated to: {user.minutes_remaining} (Paid: {user.paid_status})")
    return {"message": "Minutes updated successfully", "new_minutes": user.minutes_remaining}

# Admin Endpoints (simplified permissions, relies on API Gateway role check)
@app.get("/admin/users")
async def admin_get_all_users(): # API Gateway handles token validation and role check
    # Return users without passwords
    return [
        {
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "role": u.role,
            "paid_status": u.paid_status,
            "minutes_remaining": u.minutes_remaining
        } for u in users_db.values()
    ]