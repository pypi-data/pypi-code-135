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
from MergePythonSDK.ats.model.remote_user import RemoteUser
globals()['RemoteUser'] = RemoteUser
from MergePythonSDK.ats.model.paginated_remote_user_list import PaginatedRemoteUserList
from MergePythonSDK.shared.api_client import ApiClient


class TestPaginatedRemoteUserList(unittest.TestCase):
    """PaginatedRemoteUserList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedRemoteUserList(self):
        """Test PaginatedRemoteUserList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedRemoteUserList()  # noqa: E501

        """
        No test json responses were defined for PaginatedRemoteUserList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedRemoteUserList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
