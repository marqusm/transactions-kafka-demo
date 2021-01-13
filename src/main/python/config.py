import os

__CONFIG_FILE = "project.properties"
KAFKA_TOPIC_NAME = "KAFKA_TOPIC_NAME"
KAFKA_PRODUCER_BOOTSTRAP_SERVERS = "KAFKA_PRODUCER_BOOTSTRAP_SERVERS"


def get_properties_file_path():
    if os.path.exists(__CONFIG_FILE):
        return __CONFIG_FILE
    elif os.path.exists("../../../" + __CONFIG_FILE):
        return "../../../" + __CONFIG_FILE
    else:
        raise ValueError("Config cannot load")


class Configuration:
    def __init__(self):
        with open(get_properties_file_path()) as stream:
            parsed_lines = [line.split("=") for line in stream.readlines() if
                            line[0] != '#' and len(line.split("=")) == 2]
            self.values = {key.strip(): value.strip() for key, value in parsed_lines}


config = Configuration()


def get_str_value(key):
    return config.values[key]
