"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.hris
from MergePythonSDK.hris.model.sync_status_status_enum import SyncStatusStatusEnum
globals()['SyncStatusStatusEnum'] = SyncStatusStatusEnum
from MergePythonSDK.hris.model.sync_status import SyncStatus
from MergePythonSDK.shared.api_client import ApiClient


class TestSyncStatus(unittest.TestCase):
    """SyncStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyncStatus(self):
        """Test SyncStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyncStatus()  # noqa: E501

        raw_json = """
            {"model_name": "Candidate", "model_id": "ats.Candidate", "last_sync_start": "2021-03-30T19:44:18.695973Z", "next_sync_start": "2021-03-30T20:44:18.662942Z", "status": "SYNCING", "is_initial_sync": true}
        """

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (SyncStatus,), False)

        assert deserialized is not None

        assert deserialized.model_name is not None
        assert deserialized.model_id is not None
        assert deserialized.status is not None
        assert deserialized.is_initial_sync is not None


if __name__ == '__main__':
    unittest.main()
