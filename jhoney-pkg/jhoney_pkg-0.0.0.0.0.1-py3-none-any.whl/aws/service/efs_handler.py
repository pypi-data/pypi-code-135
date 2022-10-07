# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator

from .vpc_handler import VpcHandler


class EfsHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "efs"

    @classmethod
    def get_dependencies(cls):
        return ()

    def describe_file_systems(self):
        responses = Paginator.describe_allpages(self.client.describe_file_systems)
        return responses

    def describe_mount_targets(self, FileSystemId):
        responses = Paginator.describe_allpages(self.client.describe_mount_targets, FileSystemId=FileSystemId)
        return responses
