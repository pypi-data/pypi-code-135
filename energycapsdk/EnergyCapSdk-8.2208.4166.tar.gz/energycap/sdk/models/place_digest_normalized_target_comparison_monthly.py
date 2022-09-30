# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceDigestNormalizedTargetComparisonMonthly(Model):
    """PlaceDigestNormalizedTargetComparisonMonthly.

    :param target_year: Target Year
    :type target_year: int
    :param target_label: Target Label
    :type target_label: str
    :param results: Monthly Target Data
    :type results:
     list[~energycap.sdk.models.PlaceDigestNormalizedTargetComparisonMonthlyResults]
    """

    _attribute_map = {
        'target_year': {'key': 'targetYear', 'type': 'int'},
        'target_label': {'key': 'targetLabel', 'type': 'str'},
        'results': {'key': 'results', 'type': '[PlaceDigestNormalizedTargetComparisonMonthlyResults]'},
    }

    def __init__(self, **kwargs):
        super(PlaceDigestNormalizedTargetComparisonMonthly, self).__init__(**kwargs)
        self.target_year = kwargs.get('target_year', None)
        self.target_label = kwargs.get('target_label', None)
        self.results = kwargs.get('results', None)
