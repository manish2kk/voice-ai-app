
# shared/models.py
from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class User(BaseModel):
    id: str
    username: str
    email: str
    password: str # In real app, only hash stored
    role: str = "user"
    paid_status: bool = False
    minutes_remaining: int = 0

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AudioJob(BaseModel):
    job_id: str
    user_id: str
    input_audio_path: Optional[str] = None
    output_audio_path: Optional[str] = None
    requested_capability: str
    chosen_model: str
    status: str = "pending"
    metadata: Dict[str, Any] = {}

class PaymentRequest(BaseModel):
    user_id: str
    amount: float
    currency: str
    plan_name: str

class PaymentStatusUpdate(BaseModel):
    transaction_id: str
    status: str
    user_id: str
    minutes_added: Optional[int] = None

class Notification(BaseModel):
    user_id: str
    message: str
    notification_type: str # e.g., "job_complete", "payment_success"

class AudioProcessRequest(BaseModel):
    user_id: str
    input_audio_b64: Optional[str] = None # Base64 encoded audio string
    input_text: Optional[str] = None
    capability: str # e.g., "tts", "stt", "noise_removal"
    model_name: str
    parameters: Optional[Dict[str, Any]] = {} # Model-specific parameters

class AudioProcessResponse(BaseModel):
    job_id: str
    status: str
    output_audio_b64: Optional[str] = None
    output_text: Optional[str] = None
    message: Optional[str] = None
