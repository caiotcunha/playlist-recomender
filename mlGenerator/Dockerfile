FROM python:3.9-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python3", "./app.py", "--host=0.0.0.0"]
