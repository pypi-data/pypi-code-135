# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillsAndBatchesClassPermission(Model):
    """BillsAndBatchesClassPermission.

    :param view:
    :type view: bool
    :param create:
    :type create: bool
    :param edit:
    :type edit: bool
    :param delete:
    :type delete: bool
    :param manage:
    :type manage: bool
    """

    _attribute_map = {
        'view': {'key': 'view', 'type': 'bool'},
        'create': {'key': 'create', 'type': 'bool'},
        'edit': {'key': 'edit', 'type': 'bool'},
        'delete': {'key': 'delete', 'type': 'bool'},
        'manage': {'key': 'manage', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(BillsAndBatchesClassPermission, self).__init__(**kwargs)
        self.view = kwargs.get('view', None)
        self.create = kwargs.get('create', None)
        self.edit = kwargs.get('edit', None)
        self.delete = kwargs.get('delete', None)
        self.manage = kwargs.get('manage', None)
