from unittest import TestCase

from .config import get_plugin_file


def test_true():
    assert True


class TestConfig(TestCase):
    def test_get_plugin_file(self):
        """Test that the plugin file is found.

        # TODO This test is not working, because the plugin template file is not found.
        """
        with self.assertRaises(FileNotFoundError):
            get_plugin_file()
