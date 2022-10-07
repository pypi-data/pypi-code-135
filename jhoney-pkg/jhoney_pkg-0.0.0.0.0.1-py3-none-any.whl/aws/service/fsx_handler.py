# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class FsxHandler(ServiceHandlerInterface):
    @classmethod
    def get_service_name(cls):
        return "fsx"

    @classmethod
    def get_dependencies(cls):
        return ()

    def describe_file_systems(self):
        responses = Paginator.describe_allpages(self.client.describe_file_systems)
        return responses
