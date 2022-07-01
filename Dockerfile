# syntax=docker/dockerfile:1.2
# To build the image use :-
# $ DOCKER_BUILDKIT=1 docker build .
FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime

# metainformation
LABEL version="0.0.1"
LABEL maintainer="Lukas Scheucher"
LABEL org.opencontainers.image.source = "https://github.com/scheuclu/style-transfer"

# Helpers
ARG DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . .

# Install Python3.8
RUN apt-get update && apt-get install -y --no-install-recommends \
		python3.8 \
		python3-pip \
		python3.8-dev \
		build-essential \
		&& apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3.8 -m pip install --no-cache-dir --upgrade pip setuptools wheel
RUN python3.8 -m pip install --no-cache-dir -r requirements.txt

ENV PATH /opt/conda/bin:$PATH