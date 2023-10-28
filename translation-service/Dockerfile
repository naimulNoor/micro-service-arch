FROM python:3.10.12-slim

WORKDIR /app

COPY api.py .

RUN pip install boto3 fastapi "uvicorn[standard]" Pillow

EXPOSE 8082
CMD [ "python3","api.py"]