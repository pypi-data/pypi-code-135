"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.accounting
from MergePythonSDK.accounting.api.account_details_api import AccountDetailsApi  # noqa: E501


class TestAccountDetailsApi(unittest.TestCase):
    """AccountDetailsApi unit test stubs"""

    def setUp(self):
        self.api = AccountDetailsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_details_retrieve(self):
        """Test case for account_details_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
