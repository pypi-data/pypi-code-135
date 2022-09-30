# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SpecialAdjustmentCreate(Model):
    """SpecialAdjustmentCreate.

    All required parameters must be populated in order to send to Azure.

    :param special_adjustment_method_id: Required. Special adjustment method
     identifier <span class='property-internal'>Required</span>
    :type special_adjustment_method_id: int
    :param comments: Required. Reason for making the special adjustment <span
     class='property-internal'>Required</span>
    :type comments: str
    :param value: Amount
     See special adjustment method list for acceptable precision
     Precision of -1 means the value should not be passed in
    :type value: float
    :param special_adjustment_type_id: Required. Special adjustment type
     identifier <span class='property-internal'>Required</span>
    :type special_adjustment_type_id: int
    :param frequency: Required. Frequency type <span
     class='property-internal'>One of Recurring, Continuous </span> <span
     class='property-internal'>Required</span>
    :type frequency: str
    :param start_date: Required. Start date <span
     class='property-internal'>Required</span>
    :type start_date: datetime
    :param end_date: Required. End date <span
     class='property-internal'>Required</span>
    :type end_date: datetime
    :param annual_cycle_start_mmdd: Frequency start period
     Should only be passed when Frequency type is Recurring <span
     class='property-internal'>Required when frequency is set to
     recurring</span>
    :type annual_cycle_start_mmdd: int
    :param annual_cycle_end_mmdd: Frequency end period
     Should only be passed when Frequency type is Recurring <span
     class='property-internal'>Required when frequency is set to
     recurring</span>
    :type annual_cycle_end_mmdd: int
    """

    _validation = {
        'special_adjustment_method_id': {'required': True},
        'comments': {'required': True},
        'special_adjustment_type_id': {'required': True},
        'frequency': {'required': True},
        'start_date': {'required': True},
        'end_date': {'required': True},
    }

    _attribute_map = {
        'special_adjustment_method_id': {'key': 'specialAdjustmentMethodId', 'type': 'int'},
        'comments': {'key': 'comments', 'type': 'str'},
        'value': {'key': 'value', 'type': 'float'},
        'special_adjustment_type_id': {'key': 'specialAdjustmentTypeId', 'type': 'int'},
        'frequency': {'key': 'frequency', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'annual_cycle_start_mmdd': {'key': 'annualCycleStartMMDD', 'type': 'int'},
        'annual_cycle_end_mmdd': {'key': 'annualCycleEndMMDD', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(SpecialAdjustmentCreate, self).__init__(**kwargs)
        self.special_adjustment_method_id = kwargs.get('special_adjustment_method_id', None)
        self.comments = kwargs.get('comments', None)
        self.value = kwargs.get('value', None)
        self.special_adjustment_type_id = kwargs.get('special_adjustment_type_id', None)
        self.frequency = kwargs.get('frequency', None)
        self.start_date = kwargs.get('start_date', None)
        self.end_date = kwargs.get('end_date', None)
        self.annual_cycle_start_mmdd = kwargs.get('annual_cycle_start_mmdd', None)
        self.annual_cycle_end_mmdd = kwargs.get('annual_cycle_end_mmdd', None)
