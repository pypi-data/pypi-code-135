# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TotalBillCostDoesNotMatchLineItemTypesSettingResponse(Model):
    """TotalBillCostDoesNotMatchLineItemTypesSettingResponse.

    :param line_item_types: List of observation type codes
     If SettingStatus is set to Skip and no value is provided, EnergyCAP
     default will be set
    :type line_item_types: list[str]
    :param setting_status: The status of the audit setting - Possible values
     Check, Hold, Skip
    :type setting_status: str
    :param setting_code: The setting code
    :type setting_code: str
    :param setting_description: A description of the setting
    :type setting_description: str
    :param minimum_cost: Minimum Bill/Meter Cost.
     This audit wwill run only when the cost meets the specified minimum cost
    :type minimum_cost: int
    :param assignees: List of Assignees.
     UserChildDTO representing the users the flag should get assigned to when
     the audit fails.
    :type assignees: list[~energycap.sdk.models.UserChild]
    """

    _attribute_map = {
        'line_item_types': {'key': 'lineItemTypes', 'type': '[str]'},
        'setting_status': {'key': 'settingStatus', 'type': 'str'},
        'setting_code': {'key': 'settingCode', 'type': 'str'},
        'setting_description': {'key': 'settingDescription', 'type': 'str'},
        'minimum_cost': {'key': 'minimumCost', 'type': 'int'},
        'assignees': {'key': 'assignees', 'type': '[UserChild]'},
    }

    def __init__(self, *, line_item_types=None, setting_status: str=None, setting_code: str=None, setting_description: str=None, minimum_cost: int=None, assignees=None, **kwargs) -> None:
        super(TotalBillCostDoesNotMatchLineItemTypesSettingResponse, self).__init__(**kwargs)
        self.line_item_types = line_item_types
        self.setting_status = setting_status
        self.setting_code = setting_code
        self.setting_description = setting_description
        self.minimum_cost = minimum_cost
        self.assignees = assignees
