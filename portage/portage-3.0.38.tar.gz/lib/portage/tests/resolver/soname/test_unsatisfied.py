# Copyright 2015 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

from __future__ import print_function
import sys

from portage.const import SUPPORTED_GENTOO_BINPKG_FORMATS
from portage.tests import TestCase
from portage.tests.resolver.ResolverPlayground import (
    ResolverPlayground,
    ResolverPlaygroundTestCase,
)
from portage.output import colorize


class SonameUnsatisfiedTestCase(TestCase):
    def testSonameUnsatisfied(self):

        binpkgs = {
            "app-misc/A-1": {
                "EAPI": "5",
                "PROVIDES": "x86_32: libA.so.1",
            },
            "app-misc/A-2": {
                "EAPI": "5",
                "PROVIDES": "x86_32: libA.so.2",
            },
            "app-misc/B-0": {
                "DEPEND": "app-misc/A",
                "RDEPEND": "app-misc/A",
                "REQUIRES": "x86_32: libA.so.2",
            },
        }

        installed = {
            "app-misc/A-2": {
                "EAPI": "5",
                "PROVIDES": "x86_32: libA.so.2",
            },
            "app-misc/B-0": {
                "DEPEND": "app-misc/A",
                "RDEPEND": "app-misc/A",
                "REQUIRES": "x86_32: libA.so.1",
            },
        }

        world = ["app-misc/B"]

        test_cases = (
            # Demonstrate bug #439694, where a broken
            # soname dependency needs to trigger a reinstall.
            ResolverPlaygroundTestCase(
                ["@world"],
                options={
                    "--deep": True,
                    "--ignore-soname-deps": "n",
                    "--update": True,
                    "--usepkgonly": True,
                },
                success=True,
                mergelist=["[binary]app-misc/B-0"],
            ),
            # This doesn't trigger a reinstall, since there's no version
            # change to trigger complete graph mode, and initially
            # unsatisfied deps are ignored in complete graph mode anyway.
            ResolverPlaygroundTestCase(
                ["app-misc/A"],
                options={
                    "--ignore-soname-deps": "n",
                    "--oneshot": True,
                    "--usepkgonly": True,
                },
                success=True,
                mergelist=["[binary]app-misc/A-2"],
            ),
        )

        for binpkg_format in SUPPORTED_GENTOO_BINPKG_FORMATS:
            with self.subTest(binpkg_format=binpkg_format):
                print(colorize("HILITE", binpkg_format), end=" ... ")
                sys.stdout.flush()
                playground = ResolverPlayground(
                    binpkgs=binpkgs,
                    debug=False,
                    installed=installed,
                    world=world,
                    user_config={
                        "make.conf": ('BINPKG_FORMAT="%s"' % binpkg_format,),
                    },
                )

                try:
                    for test_case in test_cases:
                        playground.run_TestCase(test_case)
                        self.assertEqual(
                            test_case.test_success, True, test_case.fail_msg
                        )
                finally:
                    # Disable debug so that cleanup works.
                    playground.debug = False
                    playground.cleanup()
