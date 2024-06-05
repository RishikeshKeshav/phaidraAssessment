FROM python:3.9-slim


RUN pip install fastapi uvicorn prometheus-client httpx


COPY main.py /app/main.py

WORKDIR /app


CMD ["python","main.py"]
