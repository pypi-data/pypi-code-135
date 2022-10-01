from Paperl.Paperc import prDebug, prDebugging, prError, prWarring, prSuccess, checkSystem, checkPython
from Paperl.Paperui import *
from Paperl.Papers import *


try:
    from Padevel import *
except:
    pass


__version__ = "0.0.2a2"


checkSystem()
checkPython()