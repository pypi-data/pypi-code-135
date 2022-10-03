"""间隔特定时间触发器"""


from typing import Any
from vxutils import vxtime, to_timestamp, to_timestring
from vxsched.event import vxTrigger


class vxIntervalTrigger(vxTrigger):
    """间隔特定时间触发器"""

    __slots__ = ("_last_trigger_dt", "_interval", "_start_dt", "_end_dt")

    def __init__(
        self,
        interval: float = 1.0,
        start_dt: Any = None,
        end_dt: Any = None,
    ) -> None:
        super().__init__()
        if interval <= 0:
            raise ValueError(f"间隔时间{interval}必须>0")

        self._interval = interval
        self._start_dt = to_timestamp(start_dt) if start_dt else vxtime.now()
        self._end_dt = to_timestamp(end_dt) if end_dt else float("inf")
        if self._start_dt > self._end_dt:
            raise ValueError(
                f"开始时间{to_timestring(self._start_dt)}大于{to_timestring(self._end_dt)}"
            )

    def get_next_trigger_dt(self) -> float:

        trigger_dt = (
            self.last_trigger_dt + self._interval
            if self.last_trigger_dt
            else max(self._start_dt, vxtime.now())
        )
        return trigger_dt if trigger_dt <= self.end_dt else None

    @property
    def message(self) -> dict:
        """trigger内部内容"""

        return {
            "last_trigger_dt": to_timestring(self.last_trigger_dt),
            "next_trigger_dt": to_timestring(self.get_next_trigger_dt()),
            "start_dt": to_timestring(self._start_dt),
            "end_dt": to_timestring(self._end_dt),
            "interval": self._interval,
            "status": self.status,
        }
