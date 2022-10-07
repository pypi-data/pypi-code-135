# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator

from .vpc_handler import VpcHandler


class RdsHandler(ServiceHandlerInterface):
    @classmethod
    def get_service_name(cls):
        return "rds"

    @classmethod
    def get_dependencies(cls):
        return (VpcHandler.get_service_name(),)

    def describe_db_instances(self, Filters: list = []):
        responses = Paginator.describe_allpages(self.client.describe_db_instances, Filters=Filters)
        return responses

    def describe_db_clusters(self, Filters: list = []):
        responses = Paginator.describe_allpages(self.client.describe_db_clusters, Filters=Filters)
        return responses
