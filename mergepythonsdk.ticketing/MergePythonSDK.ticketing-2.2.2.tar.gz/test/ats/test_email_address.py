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
from MergePythonSDK.ats.model.email_address_type_enum import EmailAddressTypeEnum
globals()['EmailAddressTypeEnum'] = EmailAddressTypeEnum
from MergePythonSDK.ats.model.email_address import EmailAddress
from MergePythonSDK.shared.api_client import ApiClient


class TestEmailAddress(unittest.TestCase):
    """EmailAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmailAddress(self):
        """Test EmailAddress"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EmailAddress()  # noqa: E501

        """
        No test json responses were defined for EmailAddress
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (EmailAddress,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
