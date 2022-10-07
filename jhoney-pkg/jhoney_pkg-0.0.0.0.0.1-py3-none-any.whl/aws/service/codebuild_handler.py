# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class CodeBuildHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "codebuild"

    @classmethod
    def get_dependencies(cls):
        return ()

    def list_projects(self):
        response = Paginator.describe_allpages(self.client.list_projects)

        return response

    def batch_get_projects(self, projectNames: list):
        response = Paginator.describe_allpages(self.client.batch_get_projects, names=projectNames)
        return response

    def list_builds_for_project(self, projectName: list):
        response = Paginator.describe_allpages(self.client.list_builds_for_project, projectName=projectName)
        return response

    def batch_get_builds(self, buildIds: list):
        response = Paginator.describe_allpages(self.client.batch_get_builds, ids=buildIds)
        return response
