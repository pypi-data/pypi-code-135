# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class DirectConnectHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"
        self.isGlobalService = True

    @classmethod
    def get_service_name(cls):
        return "directconnect"

    @classmethod
    def get_dependencies(cls):
        return ()

    def describe_connections(self, connectionId=None):
        if connectionId:
            responses = self.client.describe_connections(connectionId=connectionId)
        else:
            responses = self.client.describe_connections()
        return responses["connections"]

    def describe_virtual_interfaces(self, connectionId=None):
        if connectionId:
            responses = self.client.describe_virtual_interfaces(connectionId=connectionId)
        else:
            responses = self.client.describe_virtual_interfaces()
        return responses["virtualInterfaces"]

    def describe_locations(self):
        responses = self.client.describe_locations()
        return responses["locations"]
