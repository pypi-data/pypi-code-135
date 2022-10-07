# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator
from src.aws.common._session import connect_aws_session


class GlobalAcceleratorHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"
        self.isGlobalService = True
        self.session = connect_aws_session(region_name="us-west-2", **self.aws_connect_key_dict)  # 이 서비스는 오직 "us-west-2" 만 된다.
        self.client = self.session.client(self.get_service_name())

    @classmethod
    def get_service_name(cls):
        return "globalaccelerator"

    @classmethod
    def get_dependencies(cls):
        return ()

    # Type: Standard
    def list_accelerators(self):
        response = Paginator.describe_allpages(self.client.list_accelerators)

        return response

    # Type: Custom
    def list_custom_routing_accelerators(self):
        response = Paginator.describe_allpages(self.client.list_custom_routing_accelerators)

        return response
