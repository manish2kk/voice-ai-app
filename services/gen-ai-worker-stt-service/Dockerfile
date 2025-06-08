# services/gen-ai-worker-stt-service/Dockerfile
FROM python:3.10-slim-buster
WORKDIR /app
COPY ./services/gen-ai-worker-stt-service/requirements.txt /app/requirements.txt 
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./services/gen-ai-worker-stt-service/src /app/src 
COPY shared /app/shared 
# Dummy audio file required by shared/utils.py for simulation
RUN mkdir -p /app/data
COPY ./services/storage-service/data/dummy_output.wav /app/data/dummy_output.wav 
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8006"]