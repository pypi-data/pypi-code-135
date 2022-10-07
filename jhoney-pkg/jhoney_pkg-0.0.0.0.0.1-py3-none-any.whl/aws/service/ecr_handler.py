# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class EcrHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "ecr"

    @classmethod
    def get_dependencies(cls):
        return ()

    def describe_repositories(self):
        responses = Paginator.describe_allpages(self.client.describe_repositories)
        return responses
