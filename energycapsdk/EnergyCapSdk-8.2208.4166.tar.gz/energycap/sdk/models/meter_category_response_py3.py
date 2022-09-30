# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeterCategoryResponse(Model):
    """MeterCategoryResponse.

    :param meter_group_category_id: The meter category identifier
    :type meter_group_category_id: int
    :param meter_group_category_code: The meter category code
    :type meter_group_category_code: str
    :param meter_group_category_info: The meter category name
    :type meter_group_category_info: str
    :param auto_group: Is this category an automatically maintained one?
    :type auto_group: bool
    :param number_of_groups: Number of groups within this category
    :type number_of_groups: int
    :param number_of_groups_with_visible_members: Number of groups within this
     category with members the logged in can see
    :type number_of_groups_with_visible_members: int
    """

    _attribute_map = {
        'meter_group_category_id': {'key': 'meterGroupCategoryId', 'type': 'int'},
        'meter_group_category_code': {'key': 'meterGroupCategoryCode', 'type': 'str'},
        'meter_group_category_info': {'key': 'meterGroupCategoryInfo', 'type': 'str'},
        'auto_group': {'key': 'autoGroup', 'type': 'bool'},
        'number_of_groups': {'key': 'numberOfGroups', 'type': 'int'},
        'number_of_groups_with_visible_members': {'key': 'numberOfGroupsWithVisibleMembers', 'type': 'int'},
    }

    def __init__(self, *, meter_group_category_id: int=None, meter_group_category_code: str=None, meter_group_category_info: str=None, auto_group: bool=None, number_of_groups: int=None, number_of_groups_with_visible_members: int=None, **kwargs) -> None:
        super(MeterCategoryResponse, self).__init__(**kwargs)
        self.meter_group_category_id = meter_group_category_id
        self.meter_group_category_code = meter_group_category_code
        self.meter_group_category_info = meter_group_category_info
        self.auto_group = auto_group
        self.number_of_groups = number_of_groups
        self.number_of_groups_with_visible_members = number_of_groups_with_visible_members
