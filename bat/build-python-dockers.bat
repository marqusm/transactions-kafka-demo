@echo off
echo Creating python docker images
echo.

docker build -f docker/Dockerfile-python-kafka-producer -t python-kafka-producer:latest .

echo.
echo Images created
