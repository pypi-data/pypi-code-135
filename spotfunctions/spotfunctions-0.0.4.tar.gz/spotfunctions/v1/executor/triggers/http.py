from flask import request
from flask import Flask
from spotfunctions.v1.models.triggers.http import HTTPTrigger
from spotfunctions.v1.executor.bindings.kafka import KafkaBindingRuntime
from importlib import import_module
import logging

logger = logging.getLogger(__name__)

class HTTPTriggerRunner:
    def __init__(self, main_file_name: str, config, binding: KafkaBindingRuntime = None, binding_name: str = None):
        self.config = config
        self.binding = binding
        self.binding_name = binding_name
        self.app = Flask(__name__)
        self.app.before_request(self._intercept_requests)
        self.user_main_function = getattr(import_module(main_file_name.replace(".py", "")), "main")

    def run(self):
        return self.app.wsgi_app

    def _intercept_requests(self):
        logger.debug("New request on path %s and method %s." % (request.path, request.method))
        if request.method in self.config["methods"] and request.path == self.config["path"]:
            logger.info("New request on path %s and method %s matched a SpotFunction. Calling user's function."
                        % (request.method, request.path))
            trigger = HTTPTrigger(request._get_current_object())
            if self.binding is None:
                response = self.user_main_function(**{self.config["name"]: trigger})
            else:
                response = self.user_main_function(**{self.config["name"]: trigger, self.binding_name: self.binding})
            logger.info("Request has been properly processed by user's function.")
            return response
        return "NOT FOUND", 404  # refactor to handle METHOD NOT ALLOWED
