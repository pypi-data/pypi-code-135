# -*- coding: utf-8 -*-
from src.aws.common.service_handler_interface import ServiceHandlerInterface
from src.aws.common.paginator import Paginator


class AcmHandler(ServiceHandlerInterface):
    def init_add(self):
        self.vpc = "non-vpc"

    @classmethod
    def get_service_name(cls):
        return "acm"

    @classmethod
    def get_dependencies(cls):
        return ()

    def list_certificates(self):
        CertificateSummaryList = list()
        response = self.client.list_certificates()
        CertificateSummaryList.extend(response["CertificateSummaryList"])
        while True:
            if "NextToken" not in response:
                break
            # 끊겼으면 이어서 계속...
            NextToken = response["NextToken"]
            response = self.client.list_distributions(NextToken=NextToken)
            CertificateSummaryList.extend(response["CertificateSummaryList"])

        return CertificateSummaryList

    def get_certificate(self, CertificateArn: str):
        return self.client.get_certificate(CertificateArn=CertificateArn)

    def describe_certificate(self, CertificateArn: str):
        return self.client.describe_certificate(CertificateArn=CertificateArn)["Certificate"]
