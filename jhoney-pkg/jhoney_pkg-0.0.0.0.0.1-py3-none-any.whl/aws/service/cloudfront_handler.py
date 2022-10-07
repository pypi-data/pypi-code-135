# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class CloudFrontHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"
        self.isGlobalService = True

    @classmethod
    def get_service_name(cls):
        return "cloudfront"

    @classmethod
    def get_dependencies(cls):
        return ()

    def list_distributions(self):
        DistributionItems = list()
        DistributionList = self.client.list_distributions()["DistributionList"]
        DistributionItems.extend(DistributionList.get("Items", []))
        while True:
            # 끊기지 않았으면 Pass
            if not DistributionList["IsTruncated"]:
                break
            # 끊겼으면 이어서 계속...
            if "NextMarker" in DistributionList:
                Marker = DistributionList["NextMarker"]
                DistributionList = self.client.list_distributions(Marker=Marker)["DistributionList"]
                DistributionItems.extend(DistributionList["Items"])

        return DistributionItems
