# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RateDigestActualYearlyResponseResults(Model):
    """RateDigestActualYearlyResponseResults.

    :param year: Year
    :type year: str
    :param total_cost: Total Cost
    :type total_cost: float
    :param global_use: Global Use
    :type global_use: float
    :param global_use_unit_cost: Global Use Unit Cost
    :type global_use_unit_cost: float
    """

    _attribute_map = {
        'year': {'key': 'year', 'type': 'str'},
        'total_cost': {'key': 'totalCost', 'type': 'float'},
        'global_use': {'key': 'globalUse', 'type': 'float'},
        'global_use_unit_cost': {'key': 'globalUseUnitCost', 'type': 'float'},
    }

    def __init__(self, *, year: str=None, total_cost: float=None, global_use: float=None, global_use_unit_cost: float=None, **kwargs) -> None:
        super(RateDigestActualYearlyResponseResults, self).__init__(**kwargs)
        self.year = year
        self.total_cost = total_cost
        self.global_use = global_use
        self.global_use_unit_cost = global_use_unit_cost
