# transactions-kafka-demo
The purpose of this project is to test Kafka cluster in different environments and situations.
As a basic case, there is idea about many transactions between bank accounts.



## Commands
Run local Confluent All-In-One Kafka cluster \
`docker-compose -f docker-compose/docker-compose-confluent-kafka.yaml up -d`



### Python

#### Preparation
Install necessary packages \
`pip3 install -r src/main/python/requirements.txt`

OR

Create docker image \
`docker build -f docker/Dockerfile-python-producer -t python-producer:latest .`

#### Running
Run Python producer \
`python3 src/main/python/kafka-producer.py --producer-name producer_1`
