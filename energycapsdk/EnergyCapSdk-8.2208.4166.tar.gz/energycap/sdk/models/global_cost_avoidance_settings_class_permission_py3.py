# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GlobalCostAvoidanceSettingsClassPermission(Model):
    """GlobalCostAvoidanceSettingsClassPermission.

    :param view:
    :type view: bool
    :param manage:
    :type manage: bool
    """

    _attribute_map = {
        'view': {'key': 'view', 'type': 'bool'},
        'manage': {'key': 'manage', 'type': 'bool'},
    }

    def __init__(self, *, view: bool=None, manage: bool=None, **kwargs) -> None:
        super(GlobalCostAvoidanceSettingsClassPermission, self).__init__(**kwargs)
        self.view = view
        self.manage = manage
