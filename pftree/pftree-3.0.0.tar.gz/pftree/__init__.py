from importlib.metadata import Distribution

__pkg = Distribution.from_name(__package__)
__version__ = __pkg.version


# try:
#     from .pftree    import pftree
# except:
#     from pftree     import pftree
