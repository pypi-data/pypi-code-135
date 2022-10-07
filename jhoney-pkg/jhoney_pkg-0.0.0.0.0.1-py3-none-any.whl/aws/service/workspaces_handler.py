# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class WorkspacesHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "workspaces"

    @classmethod
    def get_dependencies(cls):
        return ()

    def describe_workspaces(self):
        responses = Paginator.describe_allpages(self.client.describe_workspaces)
        return responses
