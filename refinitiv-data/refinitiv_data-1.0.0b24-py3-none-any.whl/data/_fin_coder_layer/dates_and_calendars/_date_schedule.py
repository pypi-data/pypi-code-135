import numpy as np
from typing import List, Optional, Union

from ...content._types import OptDateTime
from ...content.ipa._enums import DateScheduleFrequency, DayOfWeek
from ...content.ipa.dates_and_calendars.date_schedule import Definition


def date_schedule(
    frequency: Union[DateScheduleFrequency, str] = None,
    start_date: "OptDateTime" = None,
    end_date: "OptDateTime" = None,
    calendar_day_of_month: Optional[int] = None,
    calendars: Optional[List[str]] = None,
    currencies: Optional[List[str]] = None,
    day_of_week: Optional[Union[DayOfWeek, str]] = None,
    count: Optional[int] = None,
) -> List[np.datetime64]:
    response = Definition(
        frequency=frequency,
        start_date=start_date,
        end_date=end_date,
        calendar_day_of_month=calendar_day_of_month,
        calendars=calendars,
        currencies=currencies,
        day_of_week=day_of_week,
        count=count,
    ).get_data()

    return response.data.dates
