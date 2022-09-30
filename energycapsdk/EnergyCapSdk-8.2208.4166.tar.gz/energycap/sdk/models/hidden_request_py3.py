# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HiddenRequest(Model):
    """HiddenRequest.

    All required parameters must be populated in order to send to Azure.

    :param hidden: Required. Set a system user role to be hidden or shown
     Roles Manage permission is required to access hidden roles <span
     class='property-internal'>Required</span>
    :type hidden: bool
    """

    _validation = {
        'hidden': {'required': True},
    }

    _attribute_map = {
        'hidden': {'key': 'hidden', 'type': 'bool'},
    }

    def __init__(self, *, hidden: bool, **kwargs) -> None:
        super(HiddenRequest, self).__init__(**kwargs)
        self.hidden = hidden
