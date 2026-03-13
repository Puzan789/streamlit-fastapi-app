# Dockerfile for FastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY ./backend /app/backend
COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "backend.chat:app", "--host", "0.0.0.0", "--port", "80"]