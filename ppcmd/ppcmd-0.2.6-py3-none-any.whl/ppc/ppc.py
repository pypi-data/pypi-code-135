from colorama import init
import fire

from ppcmd.ppc.ppc_processor import PpcProcessor

processor = PpcProcessor()


class PPC(object):
    def update(self):
        """Update ppc command."""
        processor.update()

    def test(self):
        """Run unit test."""
        processor.test()

    def cov(self):
        """Run coverage report."""
        processor.coverage()

    def lint(self):
        """Run lint report."""
        processor.lint()


def main_():
    fire.Fire(PPC)
    init()
