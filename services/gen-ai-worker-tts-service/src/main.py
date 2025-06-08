from fastapi import FastAPI, HTTPException
from shared.models import AudioProcessRequest, AudioProcessResponse
from shared.utils import simulate_processing # Import the dummy processing function

app = FastAPI(
    title="GenAI TTS Worker Service",
    description="Converts text to speech using dummy models.",
    version="1.0.0"
)

@app.get("/health")
async def health_check():
    return {"status": "TTS Worker Service is healthy"}

@app.post("/tts", response_model=AudioProcessResponse)
async def process_tts(req: AudioProcessRequest):
    if not req.input_text:
        raise HTTPException(status_code=400, detail="Input text is required for TTS.")

    print(f"Processing TTS for text: '{req.input_text[:50]}...' using model: {req.model_name}")
    
    # Simulate AI model processing (Tacotron2, WaveGlow)
    # In a real app, integrate actual TTS models here.
    # The `input_b64` to simulate_processing is just a dummy argument here,
    # as TTS takes text, but simulate_processing expects audio_b64.
    # For actual TTS, you'd pass text to the real model.
    output_audio_b64, _ = simulate_processing(input_b64=req.input_text.encode('utf-8').hex(), duration=3) 

    return AudioProcessResponse(
        job_id="dummy_tts_job", # This would be provided by orchestrator in real setup
        status="completed",
        output_audio_b64=output_audio_b64,
        message=f"Text-to-speech completed for model {req.model_name}"
    )