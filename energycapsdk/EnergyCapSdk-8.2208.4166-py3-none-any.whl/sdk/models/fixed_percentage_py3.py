# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FixedPercentage(Model):
    """FixedPercentage.

    All required parameters must be populated in order to send to Azure.

    :param destination_account_id: Required. Destination account ID <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Topmost (CostCenter)</span>
    :type destination_account_id: int
    :param destination_meter_id: Required. Destination meter ID
     The DestinationMeterId commodity must match the commodity <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Topmost (LogicalDevice)</span>
    :type destination_meter_id: int
    :param split_percentage: Required. Fixed percentage to apply in bill split
     for this account and meter
     Pass the percentage value
     For example 50.5% should be 50.5 <span class='property-info'>Max scale of
     8</span> <span class='property-internal'>Required</span>
    :type split_percentage: float
    """

    _validation = {
        'destination_account_id': {'required': True},
        'destination_meter_id': {'required': True},
        'split_percentage': {'required': True},
    }

    _attribute_map = {
        'destination_account_id': {'key': 'destinationAccountId', 'type': 'int'},
        'destination_meter_id': {'key': 'destinationMeterId', 'type': 'int'},
        'split_percentage': {'key': 'splitPercentage', 'type': 'float'},
    }

    def __init__(self, *, destination_account_id: int, destination_meter_id: int, split_percentage: float, **kwargs) -> None:
        super(FixedPercentage, self).__init__(**kwargs)
        self.destination_account_id = destination_account_id
        self.destination_meter_id = destination_meter_id
        self.split_percentage = split_percentage
