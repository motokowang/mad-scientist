# syntax=docker/dockerfile:1
FROM python:3.11.0
COPY . /たこ
WORKDIR /たこ
RUN pip install --verbose --no-cache-dir -r requirements.txt && rm -rf /var/lib/apt/lists/*
EXPOSE 80
ENTRYPOINT [ "uvicorn", "thing1.routes:app", "--host", "0.0.0.0", "--port", "80"]