# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class CloudTrailHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "cloudtrail"

    @classmethod
    def get_dependencies(cls):
        return ()

    def list_trails(self):
        response = Paginator.describe_allpages(self.client.list_trails)

        return response

    def get_trail(self, Name: str):
        response = self.client.get_trail(Name=Name)

        return response
