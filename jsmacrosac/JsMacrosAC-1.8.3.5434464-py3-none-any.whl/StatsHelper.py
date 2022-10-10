from typing import overload
from typing import List
from typing import TypeVar
from typing import Mapping
from .BaseHelper import BaseHelper

StatHandler = TypeVar["net.minecraft.stat.StatHandler"]
Text = TypeVar["net.minecraft.text.Text"]

class StatsHelper(BaseHelper):

	@overload
	def __init__(self, base: StatHandler) -> None:
		pass

	@overload
	def getStatList(self) -> List[str]:
		pass

	@overload
	def getStatText(self, statKey: str) -> Text:
		pass

	@overload
	def getRawStatValue(self, statKey: str) -> int:
		pass

	@overload
	def getFormattedStatValue(self, statKey: str) -> str:
		pass

	@overload
	def getFormattedStatMap(self) -> Mapping[str, str]:
		pass

	@overload
	def getRawStatMap(self) -> Mapping[str, int]:
		pass

	pass


