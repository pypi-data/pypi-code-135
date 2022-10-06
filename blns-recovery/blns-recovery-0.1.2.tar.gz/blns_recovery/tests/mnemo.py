#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import binascii
from blns_recovery.mnemo import blns_checksum, BlnsMnemonic


class MnemoTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MnemoTest, self).__init__(*args, **kwargs)

    def test_bip39(self):
        mnemo = BlnsMnemonic()
        salt1 = binascii.unhexlify(b'4d1ad86be8086fdbe0a87aac4394004b149169824a25b8a70587a88e33078dd1')
        salt1_checksum = blns_checksum(salt1, BlnsMnemonic.TAG_SALT1)
        mnem_str = mnemo.to_mnemonic(salt1, salt1_checksum)
        self.assertEqual(mnem_str, "escape strategy brain source manage unknown live aunt proof bronze abandon normal "
                                   "empower regular ankle dwarf reward deal giggle extra tobacco long dance critic "
                                   "travel pioneer")

        binary_extracted = mnemo.to_binary(mnem_str, BlnsMnemonic.TAG_SALT1)
        self.assertEqual(salt1, binary_extracted)

        with self.assertRaises(ValueError):
            mnemo.to_binary(mnem_str, BlnsMnemonic.TAG_SALT2)

        salt1_checksum2 = blns_checksum(salt1, BlnsMnemonic.TAG_SALT2)
        mnem_str2 = mnemo.to_mnemonic(salt1, salt1_checksum2)
        self.assertEqual(mnem_str2, "escape strategy brain source manage unknown live aunt proof bronze abandon "
                                    "normal empower regular ankle dwarf reward deal giggle extra tobacco long dance "
                                    "choice only treat")

    def test_bip39_rand(self):
        mnemo = BlnsMnemonic()
        for _ in range(100):
            salt_rand = os.urandom(32)
            checksum = blns_checksum(salt_rand, BlnsMnemonic.TAG_SALT1)
            mnem_str = mnemo.to_mnemonic(salt_rand, checksum)
            extracted = mnemo.to_binary(mnem_str, BlnsMnemonic.TAG_SALT1)
            self.assertEqual(salt_rand, extracted)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
