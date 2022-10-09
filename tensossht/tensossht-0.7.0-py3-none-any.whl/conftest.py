from pytest import fixture
from sybil import Sybil
from sybil.parsers.codeblock import PythonCodeBlockParser
from sybil.parsers.doctest import DocTestParser


@fixture(scope="module")
def sybil_tmpdir(tmp_path_factory):
    return tmp_path_factory.mktemp("sybil")


@fixture(autouse=True, scope="session")
def docstuff(doctest_namespace):
    import numpy as np
    import tensorflow as tf

    doctest_namespace["np"] = np
    doctest_namespace["tensorflow"] = tf


def sybil_setup(namespace):
    import numpy as np
    import tensorflow as tf

    namespace["tf"] = tf
    namespace["tensorflow"] = tf
    namespace["np"] = np


pytest_collect_file = Sybil(
    parsers=[DocTestParser(), PythonCodeBlockParser()],
    fixtures=["sybil_tmpdir"],
    patterns=["*.py", "*.rst"],
    setup=sybil_setup,
).pytest()


@fixture(autouse=True)
def warnings_as_errors():
    from warnings import simplefilter

    simplefilter("error", FutureWarning)
    simplefilter("error", PendingDeprecationWarning)
