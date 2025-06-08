# services/storage-service/Dockerfile
FROM python:3.10-slim-buster
WORKDIR /app
COPY ./services/storage-service/requirements.txt /app/requirements.txt 
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./services/storage-service/src /app/src 
COPY shared /app/shared 
# Create data directory and copy dummy files
RUN mkdir -p /app/data
COPY ./services/storage-service/data/dummy_input.wav /app/data/dummy_input.wav 
COPY ./services/storage-service/data/dummy_output.wav /app/data/dummy_output.wav 
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8003"]