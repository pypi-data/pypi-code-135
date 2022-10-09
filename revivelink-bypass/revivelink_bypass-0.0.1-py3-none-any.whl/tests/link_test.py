import random

from revivelink_bypass import get_links
from revivelink_bypass.tests.conftest import RevivelinkBypassTest


class TestGetUrl(RevivelinkBypassTest):
    def setUp(self):
        super().setUp()
        random.seed(0)

    def test_get_urls(self) -> None:
        links = get_links("http://revivelink.com/BYPASS")

        self.assertEqual(2, len(links))

        self.assertEqual("Google", links[0].platform)
        self.assertEqual("https://www.google.com/", links[0].url)
        self.assertEqual("Bing", links[1].platform)
        self.assertEqual("https://www.bing.com/", links[1].url)
