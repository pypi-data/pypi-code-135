# from .eventbroker import run_eventbroker
# from .tdgateway import run_tdgateway
# from .gmagent import run_gmagent

from . import eventbroker
from . import tdgateway
from . import gmagent
from vxutils import storage


storage("scripts", "gmagent", gmagent.run_gmagent)
storage("scripts", "eventbroker", eventbroker.run_eventbroker)
storage("scripts", "tdgateway", tdgateway.run_tdgateway)

__all__ = ["storage"]
