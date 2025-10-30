FROM python:3.9-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /data

CMD ["python3", "./generator.py"]
