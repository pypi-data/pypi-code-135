# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FlagEdit(Model):
    """FlagEdit.

    :param flag_type_id: Type of the flag
     Note: Audit exception flag type id cannot be assigned manually <span
     class='property-internal'>Required (defined)</span>
    :type flag_type_id: int
    :param flag_status_id: Current status of the flag <span
     class='property-internal'>One of 1, 2 </span> <span
     class='property-internal'>Required (defined)</span>
    :type flag_status_id: int
    :param cost_recovery: Cost recovery associated with the issue this flag
     represents <span class='property-internal'>Required (defined)</span>
    :type cost_recovery: float
    :param comment: Event and action that has occurred with this flag <span
     class='property-internal'>Required (defined)</span>
    :type comment: str
    :param assignees: All users currently assigned to this flag <span
     class='property-internal'>Required (defined)</span>
    :type assignees: list[int]
    :param release_export_hold: Determines whether or not the bill will be
     released from export hold when resolving the bill flag
     This property cannot be true if HoldFromExport is true. <span
     class='property-internal'>Required (defined)</span>
    :type release_export_hold: bool
    :param hold_from_export: Determines whether or not the bill will be held
     for export when flagging the bill
     This property cannot be true if ReleaseExportHold is true. <span
     class='property-internal'>Required (defined)</span>
    :type hold_from_export: bool
    """

    _attribute_map = {
        'flag_type_id': {'key': 'flagTypeId', 'type': 'int'},
        'flag_status_id': {'key': 'flagStatusId', 'type': 'int'},
        'cost_recovery': {'key': 'costRecovery', 'type': 'float'},
        'comment': {'key': 'comment', 'type': 'str'},
        'assignees': {'key': 'assignees', 'type': '[int]'},
        'release_export_hold': {'key': 'releaseExportHold', 'type': 'bool'},
        'hold_from_export': {'key': 'holdFromExport', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(FlagEdit, self).__init__(**kwargs)
        self.flag_type_id = kwargs.get('flag_type_id', None)
        self.flag_status_id = kwargs.get('flag_status_id', None)
        self.cost_recovery = kwargs.get('cost_recovery', None)
        self.comment = kwargs.get('comment', None)
        self.assignees = kwargs.get('assignees', None)
        self.release_export_hold = kwargs.get('release_export_hold', None)
        self.hold_from_export = kwargs.get('hold_from_export', None)
