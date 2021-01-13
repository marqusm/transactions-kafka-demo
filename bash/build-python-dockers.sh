#!/bin/bash

echo "Creating python docker images"

docker build -f docker/Dockerfile-python-kafka-producer -t python-kafka-producer:latest .

echo "Images created"
