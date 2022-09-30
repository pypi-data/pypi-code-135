# low priority
# repbot docs

# do later. Very Later. Extreme dread
# replapi-it actual repl connection editing

from .bot import Bot, Button, app
from .client import *
from .param import Param
from .exceptions import NonRequiredParamsMustHaveDefault, InvalidSid, NamesMustBeAlphanumeric, MustBeOnReplit
from .post_ql import post
from .queries import q

__version__ = "1.1.5"
__license__ = "MIT"