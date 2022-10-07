# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class CodeDeployHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "codedeploy"

    @classmethod
    def get_dependencies(cls):
        return ()

    def list_applications(self):
        response = Paginator.describe_allpages(self.client.list_applications)

        return response

    def get_application(self, applicationName: str):
        response = self.client.get_application(applicationName=applicationName)

        return response["application"]

    def list_deployment_groups(self, applicationName: str):
        response = Paginator.describe_allpages(self.client.list_deployment_groups, applicationName=applicationName)

        return response

    def batch_get_deployment_groups(self, applicationName: str, deploymentGroupNames: list):
        response = self.client.batch_get_deployment_groups(applicationName=applicationName, deploymentGroupNames=deploymentGroupNames)

        return response["deploymentGroupsInfo"]
