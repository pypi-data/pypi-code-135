# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator

from .vpc_handler import VpcHandler


class ElbHandler(ServiceHandlerInterface):
    def init_add(self):
        self.client2 = self.get_aws_client("elbv2")

    @classmethod
    def get_service_name(cls):
        return "elb"

    @classmethod
    def get_dependencies(cls):
        return (VpcHandler.get_service_name(),)

    def describe_load_balancers(self):
        responses = Paginator.describe_allpages(self.client.describe_load_balancers)
        return responses

    def describe_load_balancers2(self):
        responses = Paginator.describe_allpages(self.client2.describe_load_balancers)
        return responses
