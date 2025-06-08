from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from shared.models import AudioJob, AudioProcessRequest, AudioProcessResponse, Notification
from shared.utils import generate_unique_id, decode_access_token, get_dummy_audio_b64_from_file
import httpx
import asyncio # For simulating async processing
from typing import Dict, Any

app = FastAPI(
    title="Audio Processing Orchestrator Service",
    description="Manages and dispatches audio processing jobs.",
    version="1.0.0"
)

# In-memory storage for jobs (replace with database in production)
# {job_id: AudioJob object}
jobs_db: Dict[str, AudioJob] = {}

# Simplified service URLs (replace with environment variables/discovery in production)
STORAGE_SERVICE_URL = "http://storage-service:8003"
USER_MANAGEMENT_SERVICE_URL = "http://user-management-service:8001"
PAYMENT_SERVICE_URL = "http://payment-service:8002"
NOTIFICATION_SERVICE_URL = "http://notification-service:8008"

# Map capabilities to worker service URLs
WORKER_SERVICES = {
    "tts": "http://gen-ai-worker-tts-service:8005",
    "stt": "http://gen-ai-worker-stt-service:8006",
    "noise_removal": "http://gen-ai-worker-noise-removal-service:8007",
    # Add other workers here as you implement them
    # "voice_changer": "http://gen-ai-worker-voice-changer-service:80XX",
    # "accent_changer": "http://gen-ai-worker-accent-changer-service:80YY",
    # "language_dub": "http://gen-ai-worker-dubbing-service:80ZZ",
    # "voice_edit": "http://gen-ai-worker-voice-editor-service:80AA",
    # "background_music": "http://gen-ai-worker-music-generation-service:80BB",
    # "sound_effect": "http://gen-ai-worker-sound-effect-service:80CC",
    # "vibe_music": "http://gen-ai-worker-vibe-music-service:80DD",
}

# --- Utility to get current user (for internal authentication checks) ---
# This is for internal service-to-service calls or for admin access through API Gateway.
async def get_current_user_orchestrator(token: str) -> dict:
    payload = decode_access_token(token)
    if "error" in payload:
        raise HTTPException(status_code=401, detail=payload["error"])
    return payload

# --- Endpoints ---

@app.get("/health")
async def health_check():
    return {"status": "Audio Processing Orchestrator Service is healthy"}

async def _process_audio_in_background(job_id: str, req: AudioProcessRequest):
    """Simulates sending a job to a worker and updating status."""
    job = jobs_db[job_id]
    
    worker_url = WORKER_SERVICES.get(req.capability)
    if not worker_url:
        job.status = "failed"
        job.metadata["error"] = f"No worker found for capability: {req.capability}"
        print(f"Job {job_id} failed: {job.metadata['error']}")
        return

    job.status = "processing"
    print(f"Job {job_id}: Processing started for capability {req.capability} using {req.model_name}")

    async with httpx.AsyncClient() as client:
        try:
            # Prepare payload for worker
            worker_payload = {
                "input_audio_b64": req.input_audio_b64,
                "input_text": req.input_text,
                "model_name": req.model_name,
                "parameters": req.parameters
            }
            
            # Send to appropriate worker service
            worker_resp = await client.post(
                f"{worker_url}/{req.capability}", # e.g., /tts, /stt, /noise_removal
                json=worker_payload,
                timeout=300 # Allow long processing times for AI models
            )
            worker_resp.raise_for_status()
            worker_output = AudioProcessResponse(**worker_resp.json())

            if worker_output.status == "completed":
                job.status = "completed"
                # Store output audio if available
                if worker_output.output_audio_b64:
                    output_filename = f"output_{job_id}.wav"
                    # Call Storage Service to save the output audio
                    store_resp = await client.post(
                        f"{STORAGE_SERVICE_URL}/upload",
                        json={"user_id": req.user_id, "audio_b64": worker_output.output_audio_b64, "file_name": output_filename}
                    )
                    store_resp.raise_for_status()
                    job.output_audio_path = store_resp.json()["file_path"]
                    job.metadata["output_text"] = worker_output.output_text # Store text if STT
                print(f"Job {job_id} completed successfully. Output saved to {job.output_audio_path}")
            else:
                job.status = "failed"
                job.metadata["error"] = worker_output.message or "Worker reported failure."
                print(f"Job {job_id} failed: Worker error: {job.metadata['error']}")

        except httpx.HTTPStatusError as e:
            job.status = "failed"
            job.metadata["error"] = f"Worker communication error: {e.response.text}"
            print(f"Job {job_id} failed: HTTP error: {job.metadata['error']}")
        except Exception as e:
            job.status = "failed"
            job.metadata["error"] = f"An unexpected error occurred during processing: {e}"
            print(f"Job {job_id} failed: Unexpected error: {job.metadata['error']}")
        finally:
            # Notify user regardless of success or failure
            notification_type = "job_complete" if job.status == "completed" else "job_failed"
            notification_message = f"Your audio processing job '{job_id}' for '{req.capability}' is {job.status}."
            if job.status == "failed" and job.metadata.get("error"):
                notification_message += f" Reason: {job.metadata['error']}"
            
            async with httpx.AsyncClient() as client:
                try:
                    await client.post(
                        f"{NOTIFICATION_SERVICE_URL}/send",
                        json=Notification(user_id=req.user_id, message=notification_message, notification_type=notification_type).dict()
                    )
                except Exception as e:
                    print(f"Error sending notification for job {job_id}: {e}")


@app.post("/process-audio")
async def process_audio(req: AudioProcessRequest, background_tasks: BackgroundTasks, user_info: dict = Depends(get_current_user_orchestrator)):
    job_id = generate_unique_id()
    
    # Store initial job details
    job = AudioJob(
        job_id=job_id,
        user_id=req.user_id,
        requested_capability=req.capability,
        chosen_model=req.model_name,
        metadata=req.parameters or {}
    )
    
    # If input audio is base64, save it first via Storage Service
    if req.input_audio_b64:
        async with httpx.AsyncClient() as client:
            try:
                input_filename = f"input_{job_id}.wav"
                store_resp = await client.post(
                    f"{STORAGE_SERVICE_URL}/upload",
                    json={"user_id": req.user_id, "audio_b64": req.input_audio_b64, "file_name": input_filename}
                )
                store_resp.raise_for_status()
                job.input_audio_path = store_resp.json()["file_path"]
            except httpx.HTTPStatusError as e:
                raise HTTPException(status_code=500, detail=f"Failed to upload input audio: {e.response.text}")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Unexpected error during input audio upload: {e}")
    
    jobs_db[job_id] = job
    
    # Run processing in the background
    background_tasks.add_task(_process_audio_in_background, job_id, req)
    
    return {"job_id": job_id, "status": "Job accepted, processing in background."}

@app.get("/job-status/{job_id}")
async def get_job_status(job_id: str, user_id: str, current_user_payload: dict = Depends(get_current_user_orchestrator)):
    # Ensure user can only check their own job status (or admin)
    if current_user_payload.get("sub") != user_id and current_user_payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden: You can only check your own job status.")

    job = jobs_db.get(job_id)
    if not job or job.user_id != user_id: # Also check ownership
        raise HTTPException(status_code=404, detail="Job not found or not owned by user.")
    
    # Return a simplified view of the job
    return {
        "job_id": job.job_id,
        "status": job.status,
        "output_available": job.status == "completed" and job.output_audio_path is not None,
        "output_text": job.metadata.get("output_text"), # For STT jobs
        "error_message": job.metadata.get("error")
    }

@app.get("/download-audio/{job_id}")
async def download_audio(job_id: str, user_id: str, current_user_payload: dict = Depends(get_current_user_orchestrator)):
    # Ensure user can only download their own audio (or admin)
    if current_user_payload.get("sub") != user_id and current_user_payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden: You can only download your own audio.")

    job = jobs_db.get(job_id)
    if not job or job.user_id != user_id: # Also check ownership
        raise HTTPException(status_code=404, detail="Job not found or not owned by user.")
    
    if job.status != "completed" or not job.output_audio_path:
        raise HTTPException(status_code=400, detail="Audio processing not complete or output not available.")

    # Check user's paid status and minutes remaining
    async with httpx.AsyncClient() as client:
        try:
            user_status_resp = await client.get(f"{USER_MANAGEMENT_SERVICE_URL}/account-status/{user_id}")
            user_status_resp.raise_for_status()
            user_status = user_status_resp.json()
            
            if not user_status.get("paid_status") or user_status.get("minutes_remaining", 0) <= 0:
                raise HTTPException(status_code=402, detail="Payment required to download audio. Please purchase minutes.")
            
            # Simulate calculating audio length for debiting (for real, use a library)
            # Assuming a dummy audio is 1 minute for simplicity of debiting 1 min
            # Or you can hardcode a fixed amount per download.
            audio_length_minutes = 1 # DUMMY: Replace with actual audio length calculation (e.g., using pydub or similar)
            
            # Debit minutes
            debit_resp = await client.post(
                f"{PAYMENT_SERVICE_URL}/debit-minutes",
                json={"user_id": user_id, "minutes": audio_length_minutes}
            )
            debit_resp.raise_for_status()
            print(f"Debited {audio_length_minutes} minutes from user {user_id} for job {job_id}.")

            # Fetch audio from Storage Service
            download_resp = await client.get(
                f"{STORAGE_SERVICE_URL}/download?file_path={job.output_audio_path}&user_id={user_id}"
            )
            download_resp.raise_for_status()
            audio_data = download_resp.json()
            
            return {"message": "Audio downloaded successfully", "audio_b64": audio_data["audio_b64"]}

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 402: # Payment required from Payment Service
                raise HTTPException(status_code=402, detail="Payment required to download audio. Please purchase minutes.")
            print(f"Internal service error during download for job {job_id}: {e.response.text}")
            raise HTTPException(status_code=500, detail=f"Internal service error during download: {e.response.text}")
        except Exception as e:
            print(f"An unexpected error occurred during download for job {job_id}: {e}")
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
