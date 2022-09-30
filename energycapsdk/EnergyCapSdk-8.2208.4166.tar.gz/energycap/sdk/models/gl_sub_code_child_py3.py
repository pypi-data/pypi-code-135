# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GLSubCodeChild(Model):
    """GLSubCodeChild.

    :param sub_code_index: Index of this subcode (01-20)
    :type sub_code_index: str
    :param sub_code_name: Name for this SubCode
    :type sub_code_name: str
    :param value: The value assigned to the subcode
    :type value: str
    """

    _attribute_map = {
        'sub_code_index': {'key': 'subCodeIndex', 'type': 'str'},
        'sub_code_name': {'key': 'subCodeName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, sub_code_index: str=None, sub_code_name: str=None, value: str=None, **kwargs) -> None:
        super(GLSubCodeChild, self).__init__(**kwargs)
        self.sub_code_index = sub_code_index
        self.sub_code_name = sub_code_name
        self.value = value
