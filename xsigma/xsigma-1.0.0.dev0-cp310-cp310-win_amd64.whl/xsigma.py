"""This is the xsigma module."""
import sys

if sys.version_info < (3, 5):
    # imp is deprecated in 3.4
    import imp, importlib

    # import xsigmamodules package.
    xsigmamodules_m = importlib.import_module("xsigmamodules")

    # import xsigmamodules.all
    all_m = importlib.import_module("xsigmamodules.all")

    # create a clone of the `xsigmamodules.all` module.
    xsigma_m = imp.new_module(__name__)
    for key in dir(all_m):
        if not hasattr(xsigma_m, key):
            setattr(xsigma_m, key, getattr(all_m, key))

    # make the clone of `xsigmamodules.all` act as a package at the same location
    # as xsigmamodules. This ensures that importing modules from within the xsigmamodules package
    # continues to work.
    xsigma_m.__path__ = xsigmamodules_m.__path__
    xsigma_m.__version__ = xsigmamodules_m.__version__
    # replace old `xsigma` module with this new package.
    sys.modules[__name__] = xsigma_m

else:
    import importlib

    # import xsigmamodules.all
    all_m = importlib.import_module("xsigmamodules.all")

    # import xsigmamodules
    xsigmamodules_m = importlib.import_module("xsigmamodules")

    # make xsigmamodules.all act as the xsigmamodules package to support importing
    # other modules from xsigmamodules package via `xsigma`.
    all_m.__path__ = xsigmamodules_m.__path__
    all_m.__version__ = xsigmamodules_m.__version__

    # replace old `xsigma` module with the `all` package.
    sys.modules[__name__] = all_m
