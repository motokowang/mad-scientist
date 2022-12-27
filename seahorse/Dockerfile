# syntax=docker/dockerfile:1
FROM python:3.10.7
COPY . /thing2
WORKDIR /thing2
RUN pip freeze > requirements.txt && rm -rf /var/lib/apt/lists/*
EXPOSE 7776
COPY . /app