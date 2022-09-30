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
from MergePythonSDK.ticketing.model.debug_model_log_summary import DebugModelLogSummary
globals()['DebugModelLogSummary'] = DebugModelLogSummary
from MergePythonSDK.ticketing.model.debug_mode_log import DebugModeLog
from MergePythonSDK.shared.api_client import ApiClient


class TestDebugModeLog(unittest.TestCase):
    """DebugModeLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDebugModeLog(self):
        """Test DebugModeLog"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DebugModeLog()  # noqa: E501

        raw_json = """
            {"log_id": "99433219-8017-4acd-bb3c-ceb23d663832", "dashboard_view": "https://app.merge.dev/logs/99433219-8017-4acd-bb3c-ceb23d663832", "log_summary": {"url": "https://harvest.greenhouse.io/v1/candidates/", "method": "POST", "status_code": 200}}
        """

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (DebugModeLog,), False)

        assert deserialized is not None

        assert deserialized.log_id is not None
        assert deserialized.dashboard_view is not None
        assert deserialized.log_summary is not None


if __name__ == '__main__':
    unittest.main()
