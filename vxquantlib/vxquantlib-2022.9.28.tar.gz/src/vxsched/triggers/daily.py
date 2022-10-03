"""每日触发器"""

from typing import Any
from vxutils import vxtime, to_timestring, to_timestamp
from vxsched.event import vxTrigger


class vxDailyTrigger(vxTrigger):
    """每日触发器"""

    __slots__ = (
        "_last_trigger_dt",
        "_interval",
        "_run_time",
        "_skip_holiday",
    )

    def __init__(
        self,
        run_time: str = "00:00:00",
        interval: int = 1,
        skip_holiday: bool = True,
        end_dt: Any = None,
    ) -> None:
        super().__init__()
        if interval <= 0:
            raise ValueError(f"时间间隔{interval} 必须>=1.")

        self._interval = interval * 60 * 60 * 24
        self._run_time = run_time
        self._skip_holiday = skip_holiday
        self._end_dt = to_timestamp(end_dt) if end_dt else float("inf")

    def get_next_trigger_dt(self):

        if not self._last_trigger_dt:
            trigger_dt = vxtime.today(self._run_time)
            if trigger_dt < vxtime.now():
                trigger_dt += self._interval
        else:
            trigger_dt = self.last_trigger_dt + self._interval

        while trigger_dt <= self._end_dt:
            if any(
                (self._skip_holiday is False, vxtime.is_holiday(trigger_dt) is False)
            ):
                return trigger_dt

            trigger_dt += self._interval

        return None

    @property
    def message(self) -> dict:
        """trigger内部内容"""

        return {
            "last_trigger_dt": to_timestring(self.last_trigger_dt),
            "next_trigger_dt": to_timestring(self.get_next_trigger_dt()),
            "end_dt": to_timestring(self.end_dt),
            "status": self.status,
            "run_time": self._run_time,
            "interval": int(self._interval // (60 * 60 * 24)),
        }
