from contextvars import ContextVar
from typing import Optional

from django.contrib.auth.models import User

authorized_user: ContextVar[Optional[User]] = ContextVar('user', default=None)
