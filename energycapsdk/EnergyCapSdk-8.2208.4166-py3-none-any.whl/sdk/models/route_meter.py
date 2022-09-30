# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RouteMeter(Model):
    """RouteMeter.

    All required parameters must be populated in order to send to Azure.

    :param meter_id: Required. The identifier for the meter <span
     class='property-internal'>Required</span>
    :type meter_id: int
    :param display_order: The display order for this route meter
    :type display_order: int
    """

    _validation = {
        'meter_id': {'required': True},
    }

    _attribute_map = {
        'meter_id': {'key': 'meterId', 'type': 'int'},
        'display_order': {'key': 'displayOrder', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(RouteMeter, self).__init__(**kwargs)
        self.meter_id = kwargs.get('meter_id', None)
        self.display_order = kwargs.get('display_order', None)
