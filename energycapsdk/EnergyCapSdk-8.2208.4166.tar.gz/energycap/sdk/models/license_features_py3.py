# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LicenseFeatures(Model):
    """LicenseFeatures.

    :param accounting_export: Whether accounting export is available on the
     user's the license.
    :type accounting_export: bool
    :param bill_accruals: Whether bill accruals are available on the user's
     license.
    :type bill_accruals: bool
    :param chargebacks: Whether chargebacks are available on the user's
     license.
    :type chargebacks: bool
    :param cost_avoidance: Whether cost avoidance is available on the user's
     license.
    :type cost_avoidance: bool
    :param custom_benchmarks: Whether custom benchmarks are available on the
     user's license.
    :type custom_benchmarks: bool
    :param interval_data_analysis: Whether interval data analysis is available
     on the user's license.
    :type interval_data_analysis: bool
    :param report_designer: Whether report designer is available on the user's
     license.
    :type report_designer: bool
    :param report_distribution: Whether report distribution is available on
     the user's license.
    :type report_distribution: bool
    """

    _attribute_map = {
        'accounting_export': {'key': 'accountingExport', 'type': 'bool'},
        'bill_accruals': {'key': 'billAccruals', 'type': 'bool'},
        'chargebacks': {'key': 'chargebacks', 'type': 'bool'},
        'cost_avoidance': {'key': 'costAvoidance', 'type': 'bool'},
        'custom_benchmarks': {'key': 'customBenchmarks', 'type': 'bool'},
        'interval_data_analysis': {'key': 'intervalDataAnalysis', 'type': 'bool'},
        'report_designer': {'key': 'reportDesigner', 'type': 'bool'},
        'report_distribution': {'key': 'reportDistribution', 'type': 'bool'},
    }

    def __init__(self, *, accounting_export: bool=None, bill_accruals: bool=None, chargebacks: bool=None, cost_avoidance: bool=None, custom_benchmarks: bool=None, interval_data_analysis: bool=None, report_designer: bool=None, report_distribution: bool=None, **kwargs) -> None:
        super(LicenseFeatures, self).__init__(**kwargs)
        self.accounting_export = accounting_export
        self.bill_accruals = bill_accruals
        self.chargebacks = chargebacks
        self.cost_avoidance = cost_avoidance
        self.custom_benchmarks = custom_benchmarks
        self.interval_data_analysis = interval_data_analysis
        self.report_designer = report_designer
        self.report_distribution = report_distribution
