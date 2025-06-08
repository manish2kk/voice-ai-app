from fastapi import FastAPI, HTTPException
from shared.models import AudioProcessRequest, AudioProcessResponse
from shared.utils import simulate_processing # Import the dummy processing function

app = FastAPI(
    title="GenAI Noise Removal Worker Service",
    description="Removes noise from audio using dummy models.",
    version="1.0.0"
)

@app.get("/health")
async def health_check():
    return {"status": "Noise Removal Worker Service is healthy"}

@app.post("/noise_removal", response_model=AudioProcessResponse)
async def process_noise_removal(req: AudioProcessRequest):
    if not req.input_audio_b64:
        raise HTTPException(status_code=400, detail="Input audio is required for noise removal.")

    print(f"Processing Noise Removal for audio (first 20 bytes): '{req.input_audio_b64[:20]}...' using model: {req.model_name}")
    
    # Simulate AI model processing (Demucs, RNNoise)
    # In a real app, integrate actual noise removal models here.
    output_audio_b64, _ = simulate_processing(input_b64=req.input_audio_b64, duration=2)

    return AudioProcessResponse(
        job_id="dummy_noise_removal_job",
        status="completed",
        output_audio_b64=output_audio_b64,
        message=f"Noise removal completed for model {req.model_name}"
    )