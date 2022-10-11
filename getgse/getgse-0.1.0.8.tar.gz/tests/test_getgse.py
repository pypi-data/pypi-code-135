import unittest
from getgse import *
from ..getgse.getgse import cli

class TestCalss(unittest.TestCase):
    def SetUp(self):
        self.instance = cli()

    def tearDown(self):
        self.instance.dispost()

    # def test_result(self):
        # reseult=self.instance.