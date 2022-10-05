from typing import Optional

from kafka import KafkaConsumer
from .configs import AppConfig
from spotfunctions.v1.executor.triggers.kafka import KafkaTriggerRunner
from spotfunctions.v1.executor.bindings.kafka import KafkaBindingRuntime
import logging

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, configs: AppConfig):
        self.configs = configs

    def run(self):
        kafka_binding_runtime = self._get_kafka_binding()
        kafka_binding_parameter_name = None
        if kafka_binding_runtime is not None:
            kafka_binding_parameter_name = self.configs.get_kafka_binding_config()["name"]

        http_trigger = self.configs.get_http_trigger_config()
        if http_trigger is not None:
            logger.info("HTTP Trigger Found.")
            from waitress import serve
            from spotfunctions.v1.executor.triggers.http import HTTPTriggerRunner
            http_trigger_runner = HTTPTriggerRunner(self.configs.get_script_file_name(), http_trigger, kafka_binding_runtime, kafka_binding_parameter_name)

            # Handover to waitress
            logger.info("Starting server listening at 0.0.0.0:8080.")
            serve(http_trigger_runner.run(), host='0.0.0.0', port=8080)

        kafka_trigger = self.configs.get_kafka_trigger_config()
        if kafka_trigger is not None:
            kafka_consumer = self._get_kafka_consumer()
            http_trigger_runner = KafkaTriggerRunner(self.configs.get_script_file_name(), kafka_consumer, kafka_trigger,
                                                     kafka_binding_runtime, kafka_binding_parameter_name)
            logger.info("Kafka Trigger found, ready to receive messages.")
            http_trigger_runner.run()

    def _get_kafka_consumer(self):
        kafka_trigger = self.configs.get_kafka_trigger_config()
        consumer = KafkaConsumer(kafka_trigger["topic"],
                                 group_id="refactorMePlease",
                                 bootstrap_servers=kafka_trigger["brokerList"],
                                 security_protocol=kafka_trigger["protocol"],
                                 sasl_mechanism=kafka_trigger["authenticationMode"],
                                 sasl_plain_username=kafka_trigger["username"],
                                 sasl_plain_password=kafka_trigger["password"])
        logger.info("Kafka Trigger Runtime has been created successfully.")
        return consumer

    def _get_kafka_binding(self) -> Optional[KafkaBindingRuntime]:
        kafka_binding = self.configs.get_kafka_binding_config()
        if kafka_binding is not None:
            kafka_binding_runtime = KafkaBindingRuntime(kafka_binding["brokerList"], kafka_binding["topic"],
                                                        kafka_binding["username"], kafka_binding["password"],
                                                        kafka_binding["protocol"], kafka_binding["authenticationMode"])
            logger.info("Kafka Binding Runtime has been created successfully.")
            return kafka_binding_runtime
        logger.debug("Kafka Binding Runtime is not configured.")
        return None
