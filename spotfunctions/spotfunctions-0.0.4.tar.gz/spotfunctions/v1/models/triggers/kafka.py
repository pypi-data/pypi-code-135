from kafka.consumer.fetcher import ConsumerRecord


class KafkaTrigger:
    def __init__(self, message: ConsumerRecord):
        self.message = message

    def get_data(self) -> bytearray:
        return self.message.value

    def get_key(self) -> bytearray:
        return self.message.key

    def get_headers(self) -> [(str, bytearray)]:
        return self.message.headers


