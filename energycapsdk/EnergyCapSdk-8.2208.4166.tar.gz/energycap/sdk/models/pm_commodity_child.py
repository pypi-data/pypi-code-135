# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PmCommodityChild(Model):
    """PmCommodityChild.

    :param pm_commodity_code: Commodity code from Portfolio Manager
    :type pm_commodity_code: str
    :param is_default: When true, auto-created Portfolio Manager meters will
     be of this commodity
    :type is_default: bool
    """

    _attribute_map = {
        'pm_commodity_code': {'key': 'pmCommodityCode', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(PmCommodityChild, self).__init__(**kwargs)
        self.pm_commodity_code = kwargs.get('pm_commodity_code', None)
        self.is_default = kwargs.get('is_default', None)
