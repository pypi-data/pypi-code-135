# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GroupDisplaySetting(Model):
    """Display settings for the user when viewing benchmark charts.

    :param period_type: Date period type
     Possible value include 1 (Last Twelve Months), 2 (Last Calendar Year), 3
     (Last Fiscal Year), 4 (User Defined Range) <span
     class='property-internal'>One of 1, 2, 3, 4 </span>
    :type period_type: int
    :param user_defined_range_start_period: Benchmark Chart Start Period when
     using Period Type 4 (User Defined Range)
     Will return null for all other period types <span
     class='property-internal'>Required when PeriodType is set to 4</span>
    :type user_defined_range_start_period: int
    :param user_defined_range_end_period: Benchmark Chart End Period when
     using Period Type 4 (User Defined Range)
     Will return null for all other period types <span
     class='property-internal'>Required when PeriodType is set to 4</span>
    :type user_defined_range_end_period: int
    :param data_view: Data view (actual, calendarized, normalized) <span
     class='property-internal'>One of actual, calendarized, normalized </span>
    :type data_view: str
    :param commodity_id: Unique identifier of the commodity by which benchmark
     charts will be filtered
    :type commodity_id: int
    :param show_excluded_members: Indicates whether or not to show excluded
     group members
    :type show_excluded_members: bool
    :param show_zero_averages: Indicates whether or not to show zero averages
     in benchmark charts
    :type show_zero_averages: bool
    """

    _attribute_map = {
        'period_type': {'key': 'periodType', 'type': 'int'},
        'user_defined_range_start_period': {'key': 'userDefinedRangeStartPeriod', 'type': 'int'},
        'user_defined_range_end_period': {'key': 'userDefinedRangeEndPeriod', 'type': 'int'},
        'data_view': {'key': 'dataView', 'type': 'str'},
        'commodity_id': {'key': 'commodityId', 'type': 'int'},
        'show_excluded_members': {'key': 'showExcludedMembers', 'type': 'bool'},
        'show_zero_averages': {'key': 'showZeroAverages', 'type': 'bool'},
    }

    def __init__(self, *, period_type: int=None, user_defined_range_start_period: int=None, user_defined_range_end_period: int=None, data_view: str=None, commodity_id: int=None, show_excluded_members: bool=None, show_zero_averages: bool=None, **kwargs) -> None:
        super(GroupDisplaySetting, self).__init__(**kwargs)
        self.period_type = period_type
        self.user_defined_range_start_period = user_defined_range_start_period
        self.user_defined_range_end_period = user_defined_range_end_period
        self.data_view = data_view
        self.commodity_id = commodity_id
        self.show_excluded_members = show_excluded_members
        self.show_zero_averages = show_zero_averages
