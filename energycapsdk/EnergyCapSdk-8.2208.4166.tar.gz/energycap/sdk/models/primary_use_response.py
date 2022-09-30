# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PrimaryUseResponse(Model):
    """PrimaryUseResponse.

    :param primary_use_id:
    :type primary_use_id: int
    :param primary_use_code:
    :type primary_use_code: str
    :param primary_use_info:
    :type primary_use_info: str
    :param primary_use_type:
    :type primary_use_type: str
    """

    _attribute_map = {
        'primary_use_id': {'key': 'primaryUseId', 'type': 'int'},
        'primary_use_code': {'key': 'primaryUseCode', 'type': 'str'},
        'primary_use_info': {'key': 'primaryUseInfo', 'type': 'str'},
        'primary_use_type': {'key': 'primaryUseType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PrimaryUseResponse, self).__init__(**kwargs)
        self.primary_use_id = kwargs.get('primary_use_id', None)
        self.primary_use_code = kwargs.get('primary_use_code', None)
        self.primary_use_info = kwargs.get('primary_use_info', None)
        self.primary_use_type = kwargs.get('primary_use_type', None)
