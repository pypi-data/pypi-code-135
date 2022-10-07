# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class Route53Handler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"
        self.isGlobalService = True

    @classmethod
    def get_service_name(cls):
        return "route53"

    @classmethod
    def get_dependencies(cls):
        return ()

    def list_hosted_zones(self):
        response = Paginator.describe_allpages(self.client.list_hosted_zones)

        return response
