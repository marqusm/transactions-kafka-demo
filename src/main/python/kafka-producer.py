import argparse
import datetime
import json
import random
import threading
import time
import uuid

import confluent_kafka

import config
import model
import util


def main():
    args = parse_args()
    producer_name = args[0]
    bootstrap_servers = args[1]
    batch_size = args[2]
    thread_count = args[3]
    producer_conf = {'bootstrap.servers': bootstrap_servers,
                     'client.id': producer_name}
    print(producer_conf)
    producer = confluent_kafka.Producer(producer_conf)

    if thread_count <= 1:
        generate_transactions(producer, producer_name, batch_size)
    else:
        for i in range(20):
            x = threading.Thread(target=generate_transactions, args=(producer, producer_name, batch_size))
            x.start()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--producer-name', nargs='*', default=["producer_{}".format(random.randint(0, 10000))])
    parser.add_argument('--bootstrap-servers', nargs='*', default=[""])
    parser.add_argument('--batch-size', nargs='*', default=[1])
    parser.add_argument('--thread-count', nargs='*', default=[1])
    args = parser.parse_args()

    print(args)

    producer_name = args.producer_name[0]
    bootstrap_servers = args.bootstrap_servers[0] if len(args.bootstrap_servers[0]) > 0 \
        else config.get_str_value(config.KAFKA_PRODUCER_BOOTSTRAP_SERVERS)
    batch_size = int(args.batch_size[0])
    thread_count = int(args.thread_count[0])

    return producer_name, bootstrap_servers, batch_size, thread_count


def generate_transactions(producer, producer_name, batch_size, accounts_count=100, min_value=0, max_value=100):
    start_time = time.time()
    count = 0
    start_leap_time = start_time
    start_leap_count = count
    try:
        while True:
            transaction_uuid = uuid.uuid4()
            src_account_id = random.randint(0, accounts_count)
            dst_account_id = random.randint(0, accounts_count)
            while src_account_id == dst_account_id:
                dst_account_id = random.randint(0, accounts_count)
            amount = round(random.uniform(min_value, max_value), 2)
            timestamp = datetime.datetime.now().isoformat()
            transaction = model.Transaction(transaction_uuid, src_account_id, dst_account_id, amount, timestamp)
            transaction_json = json.dumps(transaction.__dict__, cls=util.JsonEncoder)

            producer.produce(config.get_str_value(config.KAFKA_TOPIC_NAME), key=str(transaction.transaction_id),
                             value=transaction_json, callback=ack)
            if count % batch_size == 0:
                producer.flush()
            count += 1

            current_time = time.time()
            if current_time - start_leap_time > 1:
                current_leap_time = current_time - start_leap_time
                current_count = count - start_leap_count
                current_rate = round(current_count / current_leap_time, 1)
                print("Producer: {}. Created transactions: {}. Current rate: {} tr/s"
                      .format(producer_name, count, current_rate))
                start_leap_time = current_time
                start_leap_count = count
    except KeyboardInterrupt:
        print()


def ack(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))


main()
