"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.model.attachment_request import AttachmentRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestAttachmentRequest(unittest.TestCase):
    """AttachmentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttachmentRequest(self):
        """Test AttachmentRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AttachmentRequest()  # noqa: E501

        """
        No test json responses were defined for AttachmentRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (AttachmentRequest,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
