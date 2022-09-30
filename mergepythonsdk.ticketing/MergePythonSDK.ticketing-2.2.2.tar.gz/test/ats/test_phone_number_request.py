"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.ats
from MergePythonSDK.ats.model.phone_number_type_enum import PhoneNumberTypeEnum
globals()['PhoneNumberTypeEnum'] = PhoneNumberTypeEnum
from MergePythonSDK.ats.model.phone_number_request import PhoneNumberRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestPhoneNumberRequest(unittest.TestCase):
    """PhoneNumberRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPhoneNumberRequest(self):
        """Test PhoneNumberRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PhoneNumberRequest()  # noqa: E501

        """
        No test json responses were defined for PhoneNumberRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PhoneNumberRequest,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
