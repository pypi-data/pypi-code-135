# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VendorDigestActualYearlyResponseCommodityData(Model):
    """VendorDigestActualYearlyResponseCommodityData.

    :param commodity_code: The commodity code
    :type commodity_code: str
    :param commodity_info: The commodity info
    :type commodity_info: str
    :param commodity_id: The commodity identifier
    :type commodity_id: int
    :param common_use_unit:
    :type common_use_unit: ~energycap.sdk.models.UnitChild
    :param cost_unit:
    :type cost_unit: ~energycap.sdk.models.UnitChild
    :param results: An array of yearly data
    :type results:
     list[~energycap.sdk.models.VendorDigestActualYearlyResponseCommodityResults]
    """

    _attribute_map = {
        'commodity_code': {'key': 'commodityCode', 'type': 'str'},
        'commodity_info': {'key': 'commodityInfo', 'type': 'str'},
        'commodity_id': {'key': 'commodityId', 'type': 'int'},
        'common_use_unit': {'key': 'commonUseUnit', 'type': 'UnitChild'},
        'cost_unit': {'key': 'costUnit', 'type': 'UnitChild'},
        'results': {'key': 'results', 'type': '[VendorDigestActualYearlyResponseCommodityResults]'},
    }

    def __init__(self, **kwargs):
        super(VendorDigestActualYearlyResponseCommodityData, self).__init__(**kwargs)
        self.commodity_code = kwargs.get('commodity_code', None)
        self.commodity_info = kwargs.get('commodity_info', None)
        self.commodity_id = kwargs.get('commodity_id', None)
        self.common_use_unit = kwargs.get('common_use_unit', None)
        self.cost_unit = kwargs.get('cost_unit', None)
        self.results = kwargs.get('results', None)
