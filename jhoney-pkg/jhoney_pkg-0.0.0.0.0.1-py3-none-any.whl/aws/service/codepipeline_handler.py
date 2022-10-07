# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class CodePipelineHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "codepipeline"

    @classmethod
    def get_dependencies(cls):
        return ()

    def list_pipelines(self):
        response = Paginator.describe_allpages(self.client.list_pipelines)

        return response

    def get_pipeline(self, name: str):
        response = self.client.get_pipeline(name=name)

        return response["pipeline"]

    def list_pipeline_executions(self, pipelineName: str):
        response = Paginator.describe_allpages(self.client.list_pipeline_executions, pipelineName=pipelineName)

        return response
