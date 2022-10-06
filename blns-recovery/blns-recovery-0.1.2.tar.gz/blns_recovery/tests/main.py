#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii
import unittest
import os
import binascii

from mnemonic import Mnemonic

from blns_recovery.mnemo import blns_checksum, BlnsMnemonic
from blns_recovery.recovery import recover_seed


class MainTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MainTest, self).__init__(*args, **kwargs)

    def test_main(self):
        mnemonic = BlnsMnemonic()
        bip_mnemonic = Mnemonic('english')

        part1 = mnemonic.to_binary('balns1 useless hire reunion color turkey priority wedding net fall script stomach '
                                   'motion rib gaze initial payment suit essay vintage prison enforce recipe item '
                                   'welcome obey grocery')
        self.assertEqual(part1, binascii.unhexlify('f00d82e116deab55fe3ca552383758c82b8ec15cfd0dd909a7d0d584a3675db7'))

        part2 = mnemonic.to_binary('blns2 today crash brown pipe baby surge gesture push glue absorb jungle provide '
                                   'noble nurse goat drift share south bulk action burden surface swallow exile sock '
                                   'liberty')
        self.assertEqual(part2, binascii.unhexlify('e3464c7452a111b4985d7563e019e456795b2f190216c53a04780141e9b476c2'))

        seed = recover_seed(part1, part2)
        seed_mnemo = bip_mnemonic.to_mnemonic(seed)

        self.assertEqual(seed, binascii.unhexlify('8965d25a72bd47935aa54b81dd456a744c8e5fa02d68388c717f80ea6cf89d76'))
        self.assertEqual(seed_mnemo, 'maximum company notable tornado stamp situate hedgehog practice limb tuition '
                                     'fold trigger similar cool level public decade glory garment achieve plug labor '
                                     'into soap')

    def test_main2(self):
        mnemonic = BlnsMnemonic()
        bip_mnemonic = Mnemonic('english')

        part1 = mnemonic.to_binary('balns1 road there connect clap divert nothing hunt angle slush lesson glide lunar '
                                   'vocal scrub bubble clean unique hammer charge wreck satoshi glare surge urge '
                                   'memory gather')
        self.assertEqual(part1, binascii.unhexlify('bafc0cbc94e3fd2d9bd846cc500d8c428f5583875152ed8d109a7f1bf6c5b697'))

        part2 = mnemonic.to_binary('blns2 quit exchange miracle winter cupboard solve wing zero this leader auction '
                                   'result firm manage they total mimic stadium host borrow spray list canyon brick '
                                   'refuse april')
        self.assertEqual(part2, binascii.unhexlify('afc9d635fe035d9dfeeffde0cfd03bdbe5750df8272e8cda7db80d0d2f04c870'))

        seed = recover_seed(part1, part2)
        seed_mnemo = bip_mnemonic.to_mnemonic(seed)

        self.assertEqual(seed, binascii.unhexlify('c166420301445f404a92acf30b39370aa0ed39991a5b27b7116ef7546bcc9936'))
        self.assertEqual(seed_mnemo, 'scrap craft liar action echo parent clean few vessel flush evidence best attract '
                                     'orphan good enter chicken review forum upgrade effort town gospel shell')


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
