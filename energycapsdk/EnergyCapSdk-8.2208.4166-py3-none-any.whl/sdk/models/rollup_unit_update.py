# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RollupUnitUpdate(Model):
    """RollupUnitUpdate.

    :param common_rollups: List of commodities and their rollup units to
     update <span class='property-internal'>Required (defined)</span>
    :type common_rollups:
     list[~energycap.sdk.models.RollupUnitUpdateCommonUnit]
    :param global_rollup_unit_id: The global rollup unit. Automatically
     assigned to ENERGY commodity. Pass in null to leave alone. <span
     class='property-internal'>Required (defined)</span>
    :type global_rollup_unit_id: int
    """

    _attribute_map = {
        'common_rollups': {'key': 'commonRollups', 'type': '[RollupUnitUpdateCommonUnit]'},
        'global_rollup_unit_id': {'key': 'globalRollupUnitId', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(RollupUnitUpdate, self).__init__(**kwargs)
        self.common_rollups = kwargs.get('common_rollups', None)
        self.global_rollup_unit_id = kwargs.get('global_rollup_unit_id', None)
