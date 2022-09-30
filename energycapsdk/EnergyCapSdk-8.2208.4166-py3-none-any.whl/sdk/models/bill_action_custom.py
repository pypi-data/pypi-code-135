# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillActionCustom(Model):
    """BillActionCustom.

    All required parameters must be populated in order to send to Azure.

    :param bill_ids: The list of bill ids on which to perform the custom
     action <span class='property-internal'>Cannot be Empty</span> <span
     class='property-internal'>Required (defined)</span>
    :type bill_ids: list[int]
    :param webhook_id: Required. The webhook identifier that represents the
     custom bill action <span class='property-internal'>Required</span>
    :type webhook_id: int
    """

    _validation = {
        'webhook_id': {'required': True},
    }

    _attribute_map = {
        'bill_ids': {'key': 'billIds', 'type': '[int]'},
        'webhook_id': {'key': 'webhookId', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(BillActionCustom, self).__init__(**kwargs)
        self.bill_ids = kwargs.get('bill_ids', None)
        self.webhook_id = kwargs.get('webhook_id', None)
