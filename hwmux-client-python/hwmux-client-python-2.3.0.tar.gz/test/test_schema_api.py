"""
    HW Mux Reservation System

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1.6
    Generated by: https://openapi-generator.tech
"""


import unittest

import hwmux_client
from hwmux_client.api.schema_api import SchemaApi  # noqa: E501


class TestSchemaApi(unittest.TestCase):
    """SchemaApi unit test stubs"""

    def setUp(self):
        self.api = SchemaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_schema_download_retrieve(self):
        """Test case for schema_download_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
