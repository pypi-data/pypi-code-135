# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator
from src.common._datetime import change_tzinfo
from datetime import datetime


class CodeCommitHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "codecommit"

    @classmethod
    def get_dependencies(cls):
        return ()

    def list_repositories(self):
        response = Paginator.describe_allpages(self.client.list_repositories)

        return response

    def get_repository(self, repositoryName: str):
        response = self.client.get_repository(repositoryName=repositoryName)

        return response["repositoryMetadata"]

    def list_branches(self, repositoryName: str):
        response = Paginator.describe_allpages(self.client.list_branches, repositoryName=repositoryName)

        return response

    def get_branch(self, repositoryName: str, branchName: str):
        response = self.client.get_branch(repositoryName=repositoryName, branchName=branchName)

        return response["branch"]

    def get_commit(self, repositoryName: str, commitId: str):
        response = self.client.get_commit(repositoryName=repositoryName, commitId=commitId)
        commit = response["commit"]
        commit["author"]["date"] = change_tzinfo(datetime.fromtimestamp(float(commit["author"]["date"].split(" ")[0])), tz="utc")
        commit["committer"]["date"] = change_tzinfo(datetime.fromtimestamp(float(commit["committer"]["date"].split(" ")[0])), tz="utc")
        return commit
