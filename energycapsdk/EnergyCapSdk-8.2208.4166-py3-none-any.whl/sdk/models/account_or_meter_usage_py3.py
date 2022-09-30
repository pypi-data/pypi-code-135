# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountOrMeterUsage(Model):
    """AccountOrMeterUsage.

    :param chargeback: Number of chargeback accounts or meters.
    :type chargeback: int
    :param non_chargeback: Number of non-chargeback accounts or meters.
    :type non_chargeback: int
    :param inactive: Number of inactive accounts or meters.
    :type inactive: int
    """

    _attribute_map = {
        'chargeback': {'key': 'chargeback', 'type': 'int'},
        'non_chargeback': {'key': 'nonChargeback', 'type': 'int'},
        'inactive': {'key': 'inactive', 'type': 'int'},
    }

    def __init__(self, *, chargeback: int=None, non_chargeback: int=None, inactive: int=None, **kwargs) -> None:
        super(AccountOrMeterUsage, self).__init__(**kwargs)
        self.chargeback = chargeback
        self.non_chargeback = non_chargeback
        self.inactive = inactive
