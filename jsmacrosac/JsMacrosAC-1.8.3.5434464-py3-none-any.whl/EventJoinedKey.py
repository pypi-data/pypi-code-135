from typing import overload
from .EventKey import EventKey


class EventJoinedKey(EventKey):
	cancel: bool

	@overload
	def __init__(self, action: int, key: str, mods: str) -> None:
		pass

	pass


