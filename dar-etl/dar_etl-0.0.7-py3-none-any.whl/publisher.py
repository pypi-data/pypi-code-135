import logging

from kafka import KafkaProducer

from dar_etl.config import Config
from dar_etl.schemas.base_model import DarBaseModel


class DarEntryPublisher:
    def __init__(self, config: Config) -> None:
        host = config.kafka.host
        port = config.kafka.port
        self.producer = KafkaProducer(bootstrap_servers=f"{host}:{port}")

    def publish(self, dar_entry: DarBaseModel, topic: str) -> None:
        encoded_dar_entry = dar_entry.json().encode("utf-8")
        if dar_entry.id_local:
            key = dar_entry.id_local.encode("utf-8")
        else:
            key = None
        self.producer.send(topic=topic, key=key, value=encoded_dar_entry)
        self.producer.flush()
        logging.debug("[PUBLISHED] Entry")
