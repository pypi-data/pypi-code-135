# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReadingImportProfileColumn(Model):
    """ReadingImportProfileColumn.

    All required parameters must be populated in order to send to Azure.

    :param column_number: The number of the column <span
     class='property-internal'>Must be between 1 and 2147483647</span>
    :type column_number: int
    :param observation_type_code: Required. The observation type code of the
     reading <span class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 16 characters</span>
    :type observation_type_code: str
    :param unit_code: Required. The unit code of the reading <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 16 characters</span>
    :type unit_code: str
    """

    _validation = {
        'column_number': {'maximum': 2147483647, 'minimum': 1},
        'observation_type_code': {'required': True, 'max_length': 16, 'min_length': 0},
        'unit_code': {'required': True, 'max_length': 16, 'min_length': 0},
    }

    _attribute_map = {
        'column_number': {'key': 'columnNumber', 'type': 'int'},
        'observation_type_code': {'key': 'observationTypeCode', 'type': 'str'},
        'unit_code': {'key': 'unitCode', 'type': 'str'},
    }

    def __init__(self, *, observation_type_code: str, unit_code: str, column_number: int=None, **kwargs) -> None:
        super(ReadingImportProfileColumn, self).__init__(**kwargs)
        self.column_number = column_number
        self.observation_type_code = observation_type_code
        self.unit_code = unit_code
