# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FixedDemandRequest(Model):
    """FixedDemandRequest.

    All required parameters must be populated in order to send to Azure.

    :param fixed_demand_amount: Required. Fixed demand amount <span
     class='property-internal'>Required</span> <span class='property-info'>Max
     scale of 6</span>
    :type fixed_demand_amount: float
    :param unit_id: Required. Unit to which demand is applied <span
     class='property-internal'>Required</span>
    :type unit_id: int
    """

    _validation = {
        'fixed_demand_amount': {'required': True},
        'unit_id': {'required': True},
    }

    _attribute_map = {
        'fixed_demand_amount': {'key': 'fixedDemandAmount', 'type': 'float'},
        'unit_id': {'key': 'unitId', 'type': 'int'},
    }

    def __init__(self, *, fixed_demand_amount: float, unit_id: int, **kwargs) -> None:
        super(FixedDemandRequest, self).__init__(**kwargs)
        self.fixed_demand_amount = fixed_demand_amount
        self.unit_id = unit_id
