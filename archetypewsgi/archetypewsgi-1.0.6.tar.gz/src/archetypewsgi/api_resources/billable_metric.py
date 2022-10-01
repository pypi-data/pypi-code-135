from __future__ import absolute_import, division, print_function

from archetypewsgi.enums import Method
from archetypewsgi.api_resources.api_resource import (
    CreatableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    RetrievableAPIResource,
    api_requestor
)
from archetypewsgi.api_request_thread import requests_loop
import asyncio
class BillableMetric(
    CreatableAPIResource,
    RetrievableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "billable-metric"

    @classmethod
    def Retrieve(cls, billable_metric_id: str, version: int = 1):
        return super().Retrieve(id=billable_metric_id, version=version)

    @classmethod
    def All(cls, version: int = 1, **params):
        return super().All(version=version, **params)

    @classmethod
    def Create(cls, version: int = 1, **params):
        return super().Create(version=version, **params)

    @classmethod
    def Update(self, billable_metric_id: str, version: int = 1, **params):
        return super().Update(id=billable_metric_id, version=version, **params)

    @classmethod
    def LogUsage(self, custom_ud: str, billable_metric_id: str, used_amount: float):
        return asyncio.run_coroutine_threadsafe(api_requestor.create_request(
            Method.POST,
            '/sdk/v4/log-billable-metric-usage',
            data = {
                "custom_uid": custom_ud,
                "billable_metric_id": billable_metric_id,
                "used_amount": used_amount
            }
        ), requests_loop).result()


##Track Utils Here
