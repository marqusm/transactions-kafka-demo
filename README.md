# transactions-kafka-demo

The purpose of this project is to test Kafka cluster in different environments and situations. As a basic case, there is
idea about many transactions between bank accounts.

## Kafka cluster

Run local Confluent All-In-One Kafka cluster \
`docker-compose -f docker-compose/docker-compose-confluent-kafka.yaml --env-file project.properties up -d`

Stop local Confluent All-In-One Kafka cluster \
`docker-compose -f docker-compose/docker-compose-confluent-kafka.yaml --env-file project.properties down`

## Python

Install necessary packages \
`pip3 install -r src/main/python/requirements.txt`

Run Python producer \
`python3 src/main/python/kafka-producer.py`

Run Python producer (full command example) \
`python3 src/main/python/kafka-producer.py --producer-name producer_1 --bootstrap-servers localhost:9092 --batch-size 1 --thread-count 10`

## Python docker

_Hint: To run commands in Docker container, you have to specify real IP address (your local machine's) instead of
**localhost**
in **project.properties** file._

Create docker images \
`bash bash/build-python-dockers.sh`

Run Python producer in a docker container \
`docker run -t -i --rm --name producer_1 python-kafka-producer`
