# This file is placed in the Public Domain.


"irc"


import unittest


from gcid.irc import IRC


class TestIRC(unittest.TestCase):

    def test_irc(self):
        i = IRC()
        self.assertEqual(type(i), IRC)
