# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CalendarizedCalculationResponse(Model):
    """Adding calendarized calculation involving meters.

    :param calendarized_sum: Addition calculation involving meters
    :type calendarized_sum: list[~energycap.sdk.models.MeterChild]
    """

    _attribute_map = {
        'calendarized_sum': {'key': 'calendarizedSum', 'type': '[MeterChild]'},
    }

    def __init__(self, **kwargs):
        super(CalendarizedCalculationResponse, self).__init__(**kwargs)
        self.calendarized_sum = kwargs.get('calendarized_sum', None)
