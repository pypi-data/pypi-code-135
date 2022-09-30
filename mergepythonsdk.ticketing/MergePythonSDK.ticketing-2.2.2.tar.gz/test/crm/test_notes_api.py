"""
    Merge CRM API

    The unified API for building rich integrations with multiple CRM platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.crm
from MergePythonSDK.crm.api.notes_api import NotesApi  # noqa: E501


class TestNotesApi(unittest.TestCase):
    """NotesApi unit test stubs"""

    def setUp(self):
        self.api = NotesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_notes_create(self):
        """Test case for notes_create

        """
        pass

    def test_notes_list(self):
        """Test case for notes_list

        """
        pass

    def test_notes_meta_post_retrieve(self):
        """Test case for notes_meta_post_retrieve

        """
        pass

    def test_notes_retrieve(self):
        """Test case for notes_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
