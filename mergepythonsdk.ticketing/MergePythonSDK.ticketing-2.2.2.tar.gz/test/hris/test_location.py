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
from MergePythonSDK.hris.model.country_enum import CountryEnum
from MergePythonSDK.hris.model.location_type_enum import LocationTypeEnum
from MergePythonSDK.hris.model.remote_data import RemoteData
globals()['CountryEnum'] = CountryEnum
globals()['LocationTypeEnum'] = LocationTypeEnum
globals()['RemoteData'] = RemoteData
from MergePythonSDK.hris.model.location import Location
from MergePythonSDK.shared.api_client import ApiClient


class TestLocation(unittest.TestCase):
    """Location unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLocation(self):
        """Test Location"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Location()  # noqa: E501

        """
        No test json responses were defined for Location
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Location,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
