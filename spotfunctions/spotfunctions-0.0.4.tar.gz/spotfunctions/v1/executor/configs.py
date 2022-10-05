import json


class AppConfig:
    def __init__(self, path: str):
        with open(path) as f:
            function_definition = json.loads(f.read())
            bindings = function_definition["bindings"]
            self.http_trigger = next(filter(lambda x: x["direction"] == "in" and x["type"] == "httpTrigger", bindings), None)
            self.kafka_trigger = next(filter(lambda x: x["direction"] == "in" and x["type"] == "kafka", bindings), None)
            self.kafka_binding = next(filter(lambda x: x["direction"] == "out" and x["type"] == "kafka", bindings), None)
            self.script_file = function_definition["scriptFile"]

    def get_script_file_name(self):
        return self.script_file

    def get_http_trigger_config(self):
        return self.http_trigger

    def get_kafka_trigger_config(self):
        return self.kafka_trigger

    def get_kafka_binding_config(self):
        return self.kafka_binding
