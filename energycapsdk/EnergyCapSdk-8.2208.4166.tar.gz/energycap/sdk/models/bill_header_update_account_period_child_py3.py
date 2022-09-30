# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillHeaderUpdateAccountPeriodChild(Model):
    """Account Period.

    All required parameters must be populated in order to send to Azure.

    :param account_period:  <span class='property-internal'>Must be between
     190001 and 209913</span> <span class='property-internal'>Required
     (defined)</span>
    :type account_period: int
    :param update: Required. Indicates whether or not the header value is
     being updated <span class='property-internal'>Required</span>
    :type update: bool
    """

    _validation = {
        'account_period': {'maximum': 209913, 'minimum': 190001},
        'update': {'required': True},
    }

    _attribute_map = {
        'account_period': {'key': 'accountPeriod', 'type': 'int'},
        'update': {'key': 'update', 'type': 'bool'},
    }

    def __init__(self, *, update: bool, account_period: int=None, **kwargs) -> None:
        super(BillHeaderUpdateAccountPeriodChild, self).__init__(**kwargs)
        self.account_period = account_period
        self.update = update
