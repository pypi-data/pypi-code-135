from kafka import KafkaProducer

from ftp_receiver.config import Config


class KafkaPublisher:
    def __init__(self, config: Config) -> None:
        self.topic = "ftp-downloader"
        self.key = config.ftp.host.encode("utf-8")
        host = config.kafka.host
        port = config.kafka.port
        self.producer = KafkaProducer(bootstrap_servers=f"{host}:{port}")

    def publish(self, filename: str) -> None:
        self.producer.send(
            topic=self.topic,
            key=self.key,
            value=filename.encode("utf-8"),
        )
        self.producer.flush()
