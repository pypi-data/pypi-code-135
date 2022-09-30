"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.accounting
from MergePythonSDK.accounting.api.transactions_api import TransactionsApi  # noqa: E501


class TestTransactionsApi(unittest.TestCase):
    """TransactionsApi unit test stubs"""

    def setUp(self):
        self.api = TransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_transactions_list(self):
        """Test case for transactions_list

        """
        pass

    def test_transactions_retrieve(self):
        """Test case for transactions_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
