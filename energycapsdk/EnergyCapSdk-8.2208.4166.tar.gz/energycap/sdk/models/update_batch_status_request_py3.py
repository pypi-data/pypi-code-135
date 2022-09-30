# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateBatchStatusRequest(Model):
    """UpdateBatchStatusRequest.

    All required parameters must be populated in order to send to Azure.

    :param batch_status: Required. The status to set on the batch <span
     class='property-internal'>Required</span> <span
     class='property-internal'>One of Open, Pending, Closed </span>
    :type batch_status: str
    :param note: The batch note, referred to as a comment in the application
     when setting state to pending.
     If opening another user's batch, the note will only be applied to the
     requesting user's open batch that is being set to pending (if any).
     If null, the note will not be updated. Set to an empty string to remove
     the current note. <span class='property-internal'>Must be between 0 and
     255 characters</span> <span class='property-internal'>Required
     (defined)</span>
    :type note: str
    """

    _validation = {
        'batch_status': {'required': True},
        'note': {'max_length': 255, 'min_length': 0},
    }

    _attribute_map = {
        'batch_status': {'key': 'batchStatus', 'type': 'str'},
        'note': {'key': 'note', 'type': 'str'},
    }

    def __init__(self, *, batch_status: str, note: str=None, **kwargs) -> None:
        super(UpdateBatchStatusRequest, self).__init__(**kwargs)
        self.batch_status = batch_status
        self.note = note
