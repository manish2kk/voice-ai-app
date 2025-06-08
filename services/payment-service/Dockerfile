# services/payment-service/Dockerfile
FROM python:3.10-slim-buster
WORKDIR /app
COPY ./services/payment-service/requirements.txt /app/requirements.txt 
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./services/payment-service/src /app/src
COPY shared /app/shared 
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8002"]