import logging
from pathlib import Path
from typing import Iterable

from kafka import KafkaConsumer

from dar_etl.config import Config


class NewDarFileNotificationConsumer:
    def __init__(self, config: Config) -> None:
        host = config.kafka.host
        port = config.kafka.port

        self.input_dir = config.app.input_directory
        self.client_id = f"new-dar-file-notification-consumer-{config.version}"
        self.consumer = KafkaConsumer(
            config.kafka.topic,
            bootstrap_servers=f"{host}:{port}",
            client_id=self.client_id,
            group_id="dar-etl",
            enable_auto_commit=True,
            auto_offset_reset="earliest",
        )

    def consume(self) -> Iterable[Path]:
        for message in self.consumer:
            filename_bytes: bytes = message.value
            filename = filename_bytes.decode("utf-8")
            logging.info(f"[CONSUMED] {filename}")
            yield self.input_dir.joinpath(filename)
