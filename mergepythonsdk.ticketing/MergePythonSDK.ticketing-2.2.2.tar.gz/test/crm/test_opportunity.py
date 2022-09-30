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
from MergePythonSDK.crm.model.opportunity_status_enum import OpportunityStatusEnum
from MergePythonSDK.crm.model.remote_data import RemoteData
globals()['OpportunityStatusEnum'] = OpportunityStatusEnum
globals()['RemoteData'] = RemoteData
from MergePythonSDK.crm.model.opportunity import Opportunity
from MergePythonSDK.shared.api_client import ApiClient


class TestOpportunity(unittest.TestCase):
    """Opportunity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOpportunity(self):
        """Test Opportunity"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Opportunity()  # noqa: E501

        """
        No test json responses were defined for Opportunity
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Opportunity,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
