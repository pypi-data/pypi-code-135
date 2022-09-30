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
from MergePythonSDK.ats.model.activity_type_enum import ActivityTypeEnum
from MergePythonSDK.ats.model.remote_data import RemoteData
from MergePythonSDK.ats.model.visibility_enum import VisibilityEnum
globals()['ActivityTypeEnum'] = ActivityTypeEnum
globals()['RemoteData'] = RemoteData
globals()['VisibilityEnum'] = VisibilityEnum
from MergePythonSDK.ats.model.activity import Activity
from MergePythonSDK.shared.api_client import ApiClient


class TestActivity(unittest.TestCase):
    """Activity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testActivity(self):
        """Test Activity"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Activity()  # noqa: E501

        """
        No test json responses were defined for Activity
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Activity,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
