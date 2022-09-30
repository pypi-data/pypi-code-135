"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.accounting
from MergePythonSDK.accounting.model.credit_note_line_item import CreditNoteLineItem
from MergePythonSDK.accounting.model.credit_note_status_enum import CreditNoteStatusEnum
from MergePythonSDK.accounting.model.currency_enum import CurrencyEnum
from MergePythonSDK.accounting.model.remote_data import RemoteData
globals()['CreditNoteLineItem'] = CreditNoteLineItem
globals()['CreditNoteStatusEnum'] = CreditNoteStatusEnum
globals()['CurrencyEnum'] = CurrencyEnum
globals()['RemoteData'] = RemoteData
from MergePythonSDK.accounting.model.credit_note import CreditNote
from MergePythonSDK.shared.api_client import ApiClient


class TestCreditNote(unittest.TestCase):
    """CreditNote unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreditNote(self):
        """Test CreditNote"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CreditNote()  # noqa: E501

        """
        No test json responses were defined for CreditNote
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (CreditNote,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
