from fastapi import FastAPI, HTTPException
from shared.models import AudioProcessRequest, AudioProcessResponse
from shared.utils import simulate_processing # Import the dummy processing function

app = FastAPI(
    title="GenAI STT Worker Service",
    description="Converts speech to text using dummy models.",
    version="1.0.0"
)

@app.get("/health")
async def health_check():
    return {"status": "STT Worker Service is healthy"}

@app.post("/stt", response_model=AudioProcessResponse)
async def process_stt(req: AudioProcessRequest):
    if not req.input_audio_b64:
        raise HTTPException(status_code=400, detail="Input audio is required for STT.")

    print(f"Processing STT for audio (first 20 bytes): '{req.input_audio_b64[:20]}...' using model: {req.model_name}")
    
    # Simulate AI model processing (Whisper, NeMo, Vosk, Wav2Vec2)
    # In a real app, integrate actual STT models here.
    _, output_text = simulate_processing(input_b64=req.input_audio_b64, duration=4)
    output_audio_b64 = None # STT typically doesn't return audio, but we set it as Optional in model

    return AudioProcessResponse(
        job_id="dummy_stt_job",
        status="completed",
        output_text=output_text,
        output_audio_b64=output_audio_b64,
        message=f"Speech-to-text completed for model {req.model_name}"
    )