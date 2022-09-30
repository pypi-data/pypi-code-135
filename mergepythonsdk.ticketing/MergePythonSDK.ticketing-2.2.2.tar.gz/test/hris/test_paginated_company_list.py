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
from MergePythonSDK.hris.model.company import Company
globals()['Company'] = Company
from MergePythonSDK.hris.model.paginated_company_list import PaginatedCompanyList
from MergePythonSDK.shared.api_client import ApiClient


class TestPaginatedCompanyList(unittest.TestCase):
    """PaginatedCompanyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedCompanyList(self):
        """Test PaginatedCompanyList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedCompanyList()  # noqa: E501

        """
        No test json responses were defined for PaginatedCompanyList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedCompanyList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
