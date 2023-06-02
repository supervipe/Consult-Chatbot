FROM python:3.9.5-slim AS build_stage

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt 
RUN python -m rasa train

ENTRYPOINT bash -c "python -m rasa run actions & python -m rasa run --enable-api"
