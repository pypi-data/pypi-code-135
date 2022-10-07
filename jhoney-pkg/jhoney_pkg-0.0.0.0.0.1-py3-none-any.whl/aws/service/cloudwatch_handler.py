# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator
from datetime import timedelta
from src.common._datetime import utc_now


class CloudWatchHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"
        self.isGlobalService = True

    @classmethod
    def get_service_name(cls):
        return "cloudwatch"

    @classmethod
    def get_dependencies(cls):
        return ()

    def get_metric_statistics(self, Namespace, MetricName, Dimensions, StartTime=utc_now() - timedelta(hours=24), EndTime=utc_now(), Period=3600 * 24, Statistics=["Average"]):
        response = self.client.get_metric_statistics(Namespace=Namespace, MetricName=MetricName, Dimensions=Dimensions, StartTime=StartTime, EndTime=EndTime, Period=Period, Statistics=Statistics)
        return response
