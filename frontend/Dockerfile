FROM python:3.10.12-slim

WORKDIR /app

COPY api.py .
COPY index.html .

RUN pip install boto3 fastapi "uvicorn[standard]" Pillow
RUN pip install requests

EXPOSE 7080
CMD [ "python3","api.py"]