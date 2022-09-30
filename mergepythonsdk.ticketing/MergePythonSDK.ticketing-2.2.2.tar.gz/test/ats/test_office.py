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
from MergePythonSDK.ats.model.remote_data import RemoteData
globals()['RemoteData'] = RemoteData
from MergePythonSDK.ats.model.office import Office
from MergePythonSDK.shared.api_client import ApiClient


class TestOffice(unittest.TestCase):
    """Office unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOffice(self):
        """Test Office"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Office()  # noqa: E501

        raw_json = """
            {"id": "9871b4a9-f5d2-4f3b-a66b-dfedbed42c46", "remote_id": "876556788", "name": "SF Office", "location": "Embarcadero Center 2", "remote_data": [{"path": "/locations", "data": {"example": "Varies by platform"}}]}
        """

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Office,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
