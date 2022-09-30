# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AllInstalledReports(Model):
    """AllInstalledReports.

    :param view:
    :type view: bool
    :param permission_id:
    :type permission_id: int
    :param permission_code:
    :type permission_code: str
    :param permission_name:
    :type permission_name: str
    :param description:
    :type description: str
    :param permission_category_name:
    :type permission_category_name: str
    :param is_licensed:
    :type is_licensed: bool
    """

    _attribute_map = {
        'view': {'key': 'view', 'type': 'bool'},
        'permission_id': {'key': 'permissionId', 'type': 'int'},
        'permission_code': {'key': 'permissionCode', 'type': 'str'},
        'permission_name': {'key': 'permissionName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'permission_category_name': {'key': 'permissionCategoryName', 'type': 'str'},
        'is_licensed': {'key': 'isLicensed', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(AllInstalledReports, self).__init__(**kwargs)
        self.view = kwargs.get('view', None)
        self.permission_id = kwargs.get('permission_id', None)
        self.permission_code = kwargs.get('permission_code', None)
        self.permission_name = kwargs.get('permission_name', None)
        self.description = kwargs.get('description', None)
        self.permission_category_name = kwargs.get('permission_category_name', None)
        self.is_licensed = kwargs.get('is_licensed', None)
