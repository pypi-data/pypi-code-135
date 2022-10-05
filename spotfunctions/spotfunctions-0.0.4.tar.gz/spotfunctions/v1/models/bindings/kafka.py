from typing import List, Tuple

from kafka import KafkaProducer


class KafkaBinding:
    def __init__(self, kafka_producer: KafkaProducer, topic: str):
        """An abstraction over a Kafka Producer.

        Arguments:
            kafka_producer (KafkaProducer): A kafka-python KafkaProducer instance.
            topic (str): topic where the messages will be published
        """
        self.kafka_producer = kafka_producer
        self.topic = topic

    def send(self, key: bytearray, data: bytearray, headers: List[Tuple[str, bytearray]], timeout_seconds: int = 10) -> None:
        """Publish a message to the topic.

        Arguments:
            data (bytearray): message value. Must be type bytes.
            key (int): a key to associate with the message. Can be used to
                determine which partition to send the message to.
                Must be type bytes.
            headers (List[(str, bytearray)]): a list of header key value pairs. List items
                are tuples of str key and bytes value.
            timeout_seconds (int): the method is synchronous and waits at most timeout_seconds.

        Returns:
            Exception: in case the message could not be delivered to the kafka topic.
        """
        try:
            # TODO: get result and return it to the user.
            self.kafka_producer.send(self.topic, data, key, headers).get(timeout_seconds)
        except Exception as e:
            raise Exception("Could not deliver the message due to " + str(e))
        return
