# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ListActionVoid(Model):
    """ListActionVoid.

    :param void:  <span class='property-internal'>Required (defined)</span>
    :type void: bool
    """

    _attribute_map = {
        'void': {'key': 'void', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ListActionVoid, self).__init__(**kwargs)
        self.void = kwargs.get('void', None)
