from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
import httpx
import json
from shared.utils import decode_access_token
from shared.models import Token

app = FastAPI(
    title="API Gateway",
    description="Central entry point for all client requests.",
    version="1.0.0"
)

# --- Service Discovery (Simplified: Hardcoded URLs) ---
# These hostnames correspond to the service names in docker-compose.yml
SERVICES = {
    "user_management": "http://user-management-service:8001",
    "payment": "http://payment-service:8002",
    "storage": "http://storage-service:8003",
    "orchestrator": "http://audio-processing-orchestrator-service:8004",
    "tts_worker": "http://gen-ai-worker-tts-service:8005",
    "stt_worker": "http://gen-ai-worker-stt-service:8006",
    "noise_removal_worker": "http://gen-ai-worker-noise-removal-service:8007",
    "notification": "http://notification-service:8008",
}

# --- Middleware for JWT Authentication (Simplified) ---
async def verify_token(request: Request):
    auth_header = request.headers.get("Authorization")
    
    # Allow /register and /login to pass through without token
    if request.url.path in ["/api/users/register", "/api/users/login"]:
        return {"sub": "anonymous", "role": "guest"} # Return dummy info for unauthenticated access
    
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    try:
        scheme, token = auth_header.split(" ")
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authentication scheme")
        
        payload = decode_access_token(token)
        if "error" in payload:
            raise HTTPException(status_code=401, detail=payload["error"])
        
        request.state.user = payload # Attach user payload to request state
        return payload
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token format")
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Authentication error: {e}")

# --- Health Check ---
@app.get("/health")
async def health_check():
    return {"status": "API Gateway is healthy"}

# --- Proxy Endpoints ---

# User Management Endpoints
@app.post("/api/users/register")
async def register_user(request: Request):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{SERVICES['user_management']}/register", json=await request.json())
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

@app.post("/api/users/login", response_model=Token)
async def login_user(request: Request):
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{SERVICES['user_management']}/login", json=await request.json())
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

@app.get("/api/users/profile")
async def get_user_profile(request: Request, user_info: dict = Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": request.headers.get("Authorization")}
        resp = await client.get(f"{SERVICES['user_management']}/profile/{user_info['sub']}", headers=headers)
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

@app.get("/api/users/account-status")
async def get_account_status(request: Request, user_info: dict = Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": request.headers.get("Authorization")}
        resp = await client.get(f"{SERVICES['user_management']}/account-status/{user_info['sub']}", headers=headers)
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

# Admin - User Management (requires admin role - simplified, not enforced by gateway yet)
@app.get("/api/admin/users")
async def get_all_users(request: Request, user_info: dict = Depends(verify_token)):
    if user_info.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden: Admin access required")
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": request.headers.get("Authorization")}
        resp = await client.get(f"{SERVICES['user_management']}/admin/users", headers=headers)
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

# Payment Endpoints
@app.post("/api/payments/create-checkout-session")
async def create_checkout_session(request: Request, user_info: dict = Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        payload = await request.json()
        payload['user_id'] = user_info['sub'] # Ensure user_id from token
        resp = await client.post(f"{SERVICES['payment']}/create-checkout-session", json=payload)
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

@app.post("/api/payments/webhook") # Webhook from payment gateway (no token needed here)
async def payment_webhook(request: Request):
    # In a real app, verify webhook signature
    async with httpx.AsyncClient() as client:
        # Pass the full request body directly
        resp = await client.post(f"{SERVICES['payment']}/webhook", json=await request.json())
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

@app.get("/api/payments/transactions")
async def get_transactions(request: Request, user_info: dict = Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": request.headers.get("Authorization")}
        resp = await client.get(f"{SERVICES['payment']}/transactions/{user_info['sub']}", headers=headers)
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

# Audio Processing Endpoints (Orchestrator)
@app.post("/api/audio/process-audio")
async def process_audio(request: Request, user_info: dict = Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        payload = await request.json()
        payload['user_id'] = user_info['sub'] # Ensure user_id from token
        resp = await client.post(f"{SERVICES['orchestrator']}/process-audio", json=payload)
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

@app.get("/api/audio/job-status/{job_id}")
async def get_job_status(job_id: str, request: Request, user_info: dict = Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": request.headers.get("Authorization")}
        resp = await client.get(f"{SERVICES['orchestrator']}/job-status/{job_id}?user_id={user_info['sub']}", headers=headers)
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

@app.get("/api/audio/download-audio/{job_id}")
async def download_audio(job_id: str, request: Request, user_info: dict = Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": request.headers.get("Authorization")}
        # Orchestrator handles payment deduction and fetches from storage
        resp = await client.get(f"{SERVICES['orchestrator']}/download-audio/{job_id}?user_id={user_info['sub']}", headers=headers)
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json()) # Returns audio b64 or URL

# Storage Endpoints (Used internally or for direct file uploads/downloads by clients if needed)
@app.post("/api/storage/upload-audio")
async def upload_audio(request: Request, user_info: dict = Depends(verify_token)):
    # This would typically be a pre-signed URL flow, but for simplicity, we proxy it.
    async with httpx.AsyncClient() as client:
        payload = await request.json()
        payload['user_id'] = user_info['sub']
        resp = await client.post(f"{SERVICES['storage']}/upload", json=payload)
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

@app.get("/api/storage/download-audio")
async def download_audio_from_storage(file_path: str, request: Request, user_info: dict = Depends(verify_token)):
    # This might be restricted to internal service use, or require specific permissions.
    # For simplified demo, assuming any authenticated user can request their own file.
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": request.headers.get("Authorization")}
        resp = await client.get(f"{SERVICES['storage']}/download?file_path={file_path}&user_id={user_info['sub']}", headers=headers)
        resp.raise_for_status()
        return JSONResponse(status_code=resp.status_code, content=resp.json())

# API for developers (simplified - just checks paid status)
@app.get("/api/developers/paid-api-access")
async def check_developer_access(user_info: dict = Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{SERVICES['user_management']}/account-status/{user_info['sub']}")
        resp.raise_for_status()
        account_status = resp.json()
        if account_status.get("paid_status"):
            return {"message": "API access granted for paid user.", "user_id": user_info['sub']}
        raise HTTPException(status_code=403, detail="Forbidden: Only paid users have developer API access.")
