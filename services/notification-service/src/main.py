from fastapi import FastAPI
from shared.models import Notification

app = FastAPI(
    title="Notification Service",
    description="Simulates sending email/push notifications.",
    version="1.0.0"
)

@app.get("/health")
async def health_check():
    return {"status": "Notification Service is healthy"}

@app.post("/send")
async def send_notification(notification: Notification):
    # In a real application, integrate with email (SendGrid, Mailgun),
    # SMS (Twilio), or push notification (Firebase Cloud Messaging) services.
    print(f"\n--- NEW NOTIFICATION ---")
    print(f"To User: {notification.user_id}")
    print(f"Type: {notification.notification_type}")
    print(f"Message: {notification.message}")
    print(f"------------------------\n")
    return {"message": "Notification sent (simulated)"}