# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceGroupDigestWeatherRankingChild(Model):
    """PlaceGroupDigestWeatherRankingChild.

    :param base_value:
    :type base_value: float
    :param slope_value:
    :type slope_value: float
    :param place_id:
    :type place_id: int
    :param place_code:
    :type place_code: str
    :param place_info:
    :type place_info: str
    :param place_display:
    :type place_display: str
    :param include_in_charts:
    :type include_in_charts: bool
    """

    _attribute_map = {
        'base_value': {'key': 'baseValue', 'type': 'float'},
        'slope_value': {'key': 'slopeValue', 'type': 'float'},
        'place_id': {'key': 'placeId', 'type': 'int'},
        'place_code': {'key': 'placeCode', 'type': 'str'},
        'place_info': {'key': 'placeInfo', 'type': 'str'},
        'place_display': {'key': 'placeDisplay', 'type': 'str'},
        'include_in_charts': {'key': 'includeInCharts', 'type': 'bool'},
    }

    def __init__(self, *, base_value: float=None, slope_value: float=None, place_id: int=None, place_code: str=None, place_info: str=None, place_display: str=None, include_in_charts: bool=None, **kwargs) -> None:
        super(PlaceGroupDigestWeatherRankingChild, self).__init__(**kwargs)
        self.base_value = base_value
        self.slope_value = slope_value
        self.place_id = place_id
        self.place_code = place_code
        self.place_info = place_info
        self.place_display = place_display
        self.include_in_charts = include_in_charts
