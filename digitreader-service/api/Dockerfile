FROM python:3.10.12-slim

WORKDIR /app

COPY api.py .
COPY handwriting.keras .

RUN pip install tensorflow numpy mnist keras fastapi "uvicorn[standard]" Pillow

EXPOSE 8081
CMD [ "python3","api.py"]