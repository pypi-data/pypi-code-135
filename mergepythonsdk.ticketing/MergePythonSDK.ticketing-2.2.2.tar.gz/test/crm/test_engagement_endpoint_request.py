"""
    Merge CRM API

    The unified API for building rich integrations with multiple CRM platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.crm
from MergePythonSDK.crm.model.engagement_request import EngagementRequest
globals()['EngagementRequest'] = EngagementRequest
from MergePythonSDK.crm.model.engagement_endpoint_request import EngagementEndpointRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestEngagementEndpointRequest(unittest.TestCase):
    """EngagementEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEngagementEndpointRequest(self):
        """Test EngagementEndpointRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EngagementEndpointRequest()  # noqa: E501

        """
        No test json responses were defined for EngagementEndpointRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (EngagementEndpointRequest,), False)

        assert deserialized is not None

        assert deserialized.model is not None


if __name__ == '__main__':
    unittest.main()
