# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator

from .vpc_handler import VpcHandler

# from Common_Function import (
#     get_EC2_InstanceTypes_AllocatedRamSize_MiB,
#     get_EC2_CPUCreditBalance_Max,
#     get_Bytes_from_XiB,
# )


class Ec2Handler(ServiceHandlerInterface):
    @classmethod
    def get_service_name(cls):
        return "ec2"

    @classmethod
    def get_dependencies(cls):
        return (VpcHandler.get_service_name(),)

    def describe_instances(self, Filters: list = []):
        responses = Paginator.describe_allpages(self.client.describe_instances, Filters=Filters)

        Instances = list()
        for response in responses:
            Instances.extend(response["Instances"])

        return Instances

    def describe_volumes(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_volumes, Filters=Filters)
        return response

    def describe_images(self, Filters: list = []):
        response = Paginator.describe_allpages(self.client.describe_images, Filters=Filters)
        return response
