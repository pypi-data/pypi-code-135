# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GHGFactorsResponse(Model):
    """GHGFactorsResponse.

    :param ghg_factor_id: The identifier for ghg factor
    :type ghg_factor_id: int
    :param ghg_factor: The ghg factor
    :type ghg_factor: float
    :param ghg_co2_factor: The ghg CO2 factor
    :type ghg_co2_factor: float
    :param start_date: The start date
    :type start_date: datetime
    :param end_date: The end date
    :type end_date: datetime
    :param description: The description
    :type description: str
    :param memo: The notes
    :type memo: str
    :param ghg_type:
    :type ghg_type: ~energycap.sdk.models.GHGTypeChild
    :param commodity_unit:
    :type commodity_unit: ~energycap.sdk.models.UnitChild
    :param ghg_unit:
    :type ghg_unit: ~energycap.sdk.models.UnitChild
    :param commodity:
    :type commodity: ~energycap.sdk.models.CommodityChild
    """

    _attribute_map = {
        'ghg_factor_id': {'key': 'ghgFactorId', 'type': 'int'},
        'ghg_factor': {'key': 'ghgFactor', 'type': 'float'},
        'ghg_co2_factor': {'key': 'ghgCO2Factor', 'type': 'float'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'memo': {'key': 'memo', 'type': 'str'},
        'ghg_type': {'key': 'ghgType', 'type': 'GHGTypeChild'},
        'commodity_unit': {'key': 'commodityUnit', 'type': 'UnitChild'},
        'ghg_unit': {'key': 'ghgUnit', 'type': 'UnitChild'},
        'commodity': {'key': 'commodity', 'type': 'CommodityChild'},
    }

    def __init__(self, *, ghg_factor_id: int=None, ghg_factor: float=None, ghg_co2_factor: float=None, start_date=None, end_date=None, description: str=None, memo: str=None, ghg_type=None, commodity_unit=None, ghg_unit=None, commodity=None, **kwargs) -> None:
        super(GHGFactorsResponse, self).__init__(**kwargs)
        self.ghg_factor_id = ghg_factor_id
        self.ghg_factor = ghg_factor
        self.ghg_co2_factor = ghg_co2_factor
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.memo = memo
        self.ghg_type = ghg_type
        self.commodity_unit = commodity_unit
        self.ghg_unit = ghg_unit
        self.commodity = commodity
