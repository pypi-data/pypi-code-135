# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator

from .vpc_handler import VpcHandler


class ElastiCacheHandler(ServiceHandlerInterface):
    @classmethod
    def get_service_name(cls):
        return "elasticache"

    @classmethod
    def get_dependencies(cls):
        return (VpcHandler.get_service_name(),)

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elasticache.html
    def describe_replication_groups(self, ReplicationGroupId=None):
        if ReplicationGroupId:
            responses = Paginator.describe_allpages(self.client.describe_replication_groups, ReplicationGroupId=ReplicationGroupId)
        else:
            responses = Paginator.describe_allpages(self.client.describe_replication_groups)
        return responses

    def describe_cache_clusters(self, ShowCacheNodeInfo=True):
        responses = Paginator.describe_allpages(self.client.describe_cache_clusters, ShowCacheNodeInfo=ShowCacheNodeInfo)
        return responses

    def describe_cache_subnet_groups(self, CacheSubnetGroupName=None):
        if CacheSubnetGroupName:
            responses = Paginator.describe_allpages(self.client.describe_cache_subnet_groups, CacheSubnetGroupName=CacheSubnetGroupName)
        else:
            responses = Paginator.describe_allpages(self.client.describe_cache_subnet_groups)
        return responses
