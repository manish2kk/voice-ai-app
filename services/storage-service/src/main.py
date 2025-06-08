from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from shared.utils import generate_unique_id
import os
import base64

app = FastAPI(
    title="Storage Service",
    description="Manages storage and retrieval of audio files.",
    version="1.0.0"
)

STORAGE_DIR = "/app/data" # Mount point inside Docker container

# Ensure storage directory exists
@app.on_event("startup")
async def startup_event():
    os.makedirs(STORAGE_DIR, exist_ok=True)
    print(f"Storage directory ensured: {STORAGE_DIR}")


@app.get("/health")
async def health_check():
    return {"status": "Storage Service is healthy"}

@app.post("/upload")
async def upload_audio(user_id: str, audio_b64: str, file_name: str = None):
    # In a real scenario, this would handle actual file uploads,
    # potentially via pre-signed URLs or direct file bytes.
    # Here, we simulate storing the base64 content.
    if not file_name:
        file_name = f"audio_{user_id}_{generate_unique_id()}.wav" # Prefix with user_id for better organization
    
    file_path = os.path.join(STORAGE_DIR, file_name)
    
    try:
        audio_bytes = base64.b64decode(audio_b64)
        with open(file_path, "wb") as f:
            f.write(audio_bytes)
        print(f"Uploaded dummy audio for user {user_id} to: {file_path}")
        return {"message": "Audio uploaded successfully (dummy)", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload audio: {e}")

@app.get("/download")
async def download_audio(file_path: str, user_id: str): # user_id is passed to allow potential future ownership checks
    # In a real app, verify user_id ownership of file_path to prevent unauthorized access.
    # For this dummy, we just check existence.
    full_path = os.path.join(STORAGE_DIR, file_path)
    
    # Security check: Prevent path traversal
    if not os.path.abspath(full_path).startswith(os.path.abspath(STORAGE_DIR)):
        raise HTTPException(status_code=400, detail="Invalid file path.")

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    # Return as base64 for simplicity in internal service communication
    try:
        with open(full_path, "rb") as f:
            audio_bytes = f.read()
            return {"audio_b64": base64.b64encode(audio_bytes).decode('utf-8')}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read file: {e}")

@app.delete("/delete")
async def delete_audio(file_path: str, user_id: str): # user_id is passed to allow potential future ownership checks
    # In a real app, verify user_id ownership and handle security carefully
    full_path = os.path.join(STORAGE_DIR, file_path)

    # Security check: Prevent path traversal
    if not os.path.abspath(full_path).startswith(os.path.abspath(STORAGE_DIR)):
        raise HTTPException(status_code=400, detail="Invalid file path.")

    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        os.remove(full_path)
        print(f"Deleted file: {full_path}")
        return {"message": "File deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete file: {e}")
