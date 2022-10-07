# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class S3Handler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "s3"

    @classmethod
    def get_dependencies(cls):
        return ()

    def list_buckets(self, Buckets=[], Owner={}):
        response = self.client.list_buckets(Buckets=Buckets, Owner=Owner)
        return response["Buckets"]

    def get_bucket_lifecycle(self, Bucket):
        responses = self.client.get_bucket_lifecycle(Bucket=Bucket)
        return responses

    def get_bucket_location(self, Bucket):
        responses = self.client.get_bucket_location(Bucket=Bucket)
        return responses

    def get_public_access_block(self, Bucket):
        responses = self.client.get_public_access_block(Bucket=Bucket)
        return responses

    def get_bucket_policy(self, Bucket):
        responses = self.client.get_bucket_policy(Bucket=Bucket)
        return responses

    def get_bucket_policy_status(self, Bucket):
        responses = self.client.get_bucket_policy_status(Bucket=Bucket)
        return responses

    def get_bucket_acl(self, Bucket):
        responses = self.client.get_bucket_acl(Bucket=Bucket)
        return responses
