# read version from installed package
from importlib.metadata import version
from . import artist
from . import utility

__version__ = version("py_chartmetric_api")
