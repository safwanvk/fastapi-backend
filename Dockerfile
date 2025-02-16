# filepath: /home/eps166-epixel/mYPro/fast-back/Dockerfile
FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y build-essential gcc libffi-dev python3-dev libpq-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["sh", "./docker-entrypoint.sh"]