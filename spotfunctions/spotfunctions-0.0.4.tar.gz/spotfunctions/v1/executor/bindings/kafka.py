from spotfunctions.v1.models.bindings.kafka import KafkaBinding
from kafka import KafkaProducer

class KafkaBindingRuntime:
    def __init__(self, bootstrap_servers: str, topic: str, sasl_plain_username: str, sasl_plain_password: str,
                 security_protocol: str = "SASL_SSL", sasl_mechanism:str = "PLAIN"):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic,
        self.sasl_plain_username = sasl_plain_username
        self.sasl_plain_password = sasl_plain_password
        self.security_protocol = security_protocol
        self.sasl_mechanism = sasl_mechanism

    def get_kafka_producer(self):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                 security_protocol=self.security_protocol,
                                 sasl_mechanism=self.sasl_mechanism,
                                 sasl_plain_username=self.sasl_plain_username,
                                 sasl_plain_password=self.sasl_plain_password)

        return KafkaBinding(producer, self.topic)
