# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class StsHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "sts"

    @classmethod
    def get_dependencies(cls):
        return ()

    def get_aws_account_id(self):
        return self.get_sts_identity("Account")

    def get_user_name(self):
        arn = self.get_sts_identity("Arn")
        return arn.split("/", 1)[1]

    def get_sts_identity(self, item):
        return self.client.get_caller_identity()[item]
