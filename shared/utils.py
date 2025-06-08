# shared/utils.py
import jwt
import os
from datetime import datetime, timedelta
import uuid

# In a real application, keep this secret secure (e.g., environment variable)
SECRET_KEY = "your-super-secret-key" # CHANGE THIS IN PRODUCTION
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}

def generate_unique_id():
    return str(uuid.uuid4())

# Dummy audio content (a very short silent WAV file, base64 encoded)
# This is a placeholder. For actual dummy files, you'd read them from disk.
DUMMY_AUDIO_B64 = "UklGRiQAAABXQVZFZm10IBIAAAABAAEARKwAAABAAAEBGGFjdGEBAAA=" # A tiny base64 encoded WAV header + 0 bytes of data

def get_dummy_audio_b64_from_file(file_path: str):
    """
    Reads a dummy audio file from a given path and returns its base64 encoded content.
    """
    try:
        with open(file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            return base64.b64encode(audio_bytes).decode('utf-8')
    except FileNotFoundError:
        print(f"Warning: Dummy audio file not found at {file_path}. Using hardcoded dummy_audio_b64.")
        return DUMMY_AUDIO_B64
    except Exception as e:
        print(f"Error reading dummy audio file {file_path}: {e}. Using hardcoded dummy_audio_b64.")
        return DUMMY_AUDIO_B64

import base64
import time

def simulate_processing(input_b64: Optional[str] = None, duration: int = 2):
    """Simulates AI processing by pausing and returning dummy output."""
    time.sleep(duration)
    # In a real scenario, you would pass input_b64 to your AI model
    # and get actual processed audio/text.
    # Here, we just return a dummy output.
    dummy_output_b64 = get_dummy_audio_b64_from_file("/app/data/dummy_output.wav")
    dummy_output_text = "This is a dummy transcription."
    return dummy_output_b64, dummy_output_text