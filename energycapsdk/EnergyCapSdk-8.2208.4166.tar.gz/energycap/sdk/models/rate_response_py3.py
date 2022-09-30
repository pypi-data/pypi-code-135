# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RateResponse(Model):
    """RateResponse.

    :param rate_id:
    :type rate_id: int
    :param name:
    :type name: str
    :param note:
    :type note: str
    :param vendor:
    :type vendor: ~energycap.sdk.models.VendorChild
    :param commodity:
    :type commodity: ~energycap.sdk.models.CommodityChild
    :param versions:
    :type versions: list[~energycap.sdk.models.VersionResponse]
    """

    _attribute_map = {
        'rate_id': {'key': 'rateId', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'note': {'key': 'note', 'type': 'str'},
        'vendor': {'key': 'vendor', 'type': 'VendorChild'},
        'commodity': {'key': 'commodity', 'type': 'CommodityChild'},
        'versions': {'key': 'versions', 'type': '[VersionResponse]'},
    }

    def __init__(self, *, rate_id: int=None, name: str=None, note: str=None, vendor=None, commodity=None, versions=None, **kwargs) -> None:
        super(RateResponse, self).__init__(**kwargs)
        self.rate_id = rate_id
        self.name = name
        self.note = note
        self.vendor = vendor
        self.commodity = commodity
        self.versions = versions
