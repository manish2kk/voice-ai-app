# services/api-gateway/Dockerfile
FROM python:3.10-slim-buster
WORKDIR /app
COPY ./services/api-gateway/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./services/api-gateway/src /app/src
COPY shared /app/shared 
# Copy shared utilities
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]