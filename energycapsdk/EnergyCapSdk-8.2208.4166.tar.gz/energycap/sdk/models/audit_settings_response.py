# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AuditSettingsResponse(Model):
    """AuditSettingsResponse.

    All required parameters must be populated in order to send to Azure.

    :param bill_contains_line_item_descriptions:
    :type bill_contains_line_item_descriptions:
     ~energycap.sdk.models.BillContainsLineItemDescriptionsSettingResponse
    :param bill_contains_line_item_types:
    :type bill_contains_line_item_types:
     ~energycap.sdk.models.BillContainsLineItemTypesSettingResponse
    :param total_bill_cost_does_not_match_line_item_types:
    :type total_bill_cost_does_not_match_line_item_types:
     ~energycap.sdk.models.TotalBillCostDoesNotMatchLineItemTypesSettingResponse
    :param billing_period_outside_start_end_dates:
    :type billing_period_outside_start_end_dates:
     ~energycap.sdk.models.AuditSettingResponse
    :param bill_overlaps_with_other_account_bill:
    :type bill_overlaps_with_other_account_bill:
     ~energycap.sdk.models.AuditSettingResponse
    :param gap_between_bill_and_previous_bill_on_account:
    :type gap_between_bill_and_previous_bill_on_account:
     ~energycap.sdk.models.AuditSettingResponse
    :param bill_ends_in_future:
    :type bill_ends_in_future: ~energycap.sdk.models.AuditSettingResponse
    :param account_has_multiple_bills_in_billing_period:
    :type account_has_multiple_bills_in_billing_period:
     ~energycap.sdk.models.AuditSettingResponse
    :param statement_date_before_end_date:
    :type statement_date_before_end_date:
     ~energycap.sdk.models.AuditSettingResponse
    :param due_date_before_end_date:
    :type due_date_before_end_date: ~energycap.sdk.models.AuditSettingResponse
    :param bill_significantly_shorter_or_longer_than_previous:
    :type bill_significantly_shorter_or_longer_than_previous:
     ~energycap.sdk.models.BillSignificantlyShorterOrLongerThanPreviousSettingResponse
    :param too_many_consecutive_estimated_bills:
    :type too_many_consecutive_estimated_bills:
     ~energycap.sdk.models.TooManyConsecutiveEstimatedBillsSettingResponse
    :param due_date_too_long_after_bill_end: Required.
    :type due_date_too_long_after_bill_end:
     ~energycap.sdk.models.DueDateTooLongAfterBillEndSettingResponse
    :param statement_date_too_long_after_bill_end: Required.
    :type statement_date_too_long_after_bill_end:
     ~energycap.sdk.models.StatementDateTooLongAfterBillEndSettingResponse
    :param invoice_number_is_repeated_on_account:
    :type invoice_number_is_repeated_on_account:
     ~energycap.sdk.models.AuditSettingResponse
    :param likely_duplicate_bill_on_account:
    :type likely_duplicate_bill_on_account:
     ~energycap.sdk.models.AuditSettingResponse
    :param total_meter_cost_is_percentage_higher_than_past_year:
    :type total_meter_cost_is_percentage_higher_than_past_year:
     ~energycap.sdk.models.AuditSettingResponse
    :param total_meter_use_is_percentage_higher_than_past_year:
    :type total_meter_use_is_percentage_higher_than_past_year:
     ~energycap.sdk.models.AuditSettingResponse
    :param serial_number_does_not_match_import_file:
    :type serial_number_does_not_match_import_file:
     ~energycap.sdk.models.AuditSettingResponse
    :param rate_code_does_not_match_import_file:
    :type rate_code_does_not_match_import_file:
     ~energycap.sdk.models.AuditSettingResponse
    :param import_file_start_date_adjusted_to_prevent_gaps:
    :type import_file_start_date_adjusted_to_prevent_gaps:
     ~energycap.sdk.models.AuditSettingResponse
    :param account_alert_exists_on_account_in_import_file:
    :type account_alert_exists_on_account_in_import_file:
     ~energycap.sdk.models.AuditSettingResponse
    :param abnormal_bill_cost_with_outlier_analysis:
    :type abnormal_bill_cost_with_outlier_analysis:
     ~energycap.sdk.models.AbnormalBillCostWithOutlierAnalysisSettingResponse
    :param abnormal_bill_use_with_outlier_analysis: Required.
    :type abnormal_bill_use_with_outlier_analysis:
     ~energycap.sdk.models.AbnormalBillUseWithOutlierAnalysisSettingResponse
    :param abnormal_bill_demand_with_outlier_analysis: Required.
    :type abnormal_bill_demand_with_outlier_analysis:
     ~energycap.sdk.models.AbnormalBillDemandWithOutlierAnalysisSettingResponse
    """

    _validation = {
        'due_date_too_long_after_bill_end': {'required': True},
        'statement_date_too_long_after_bill_end': {'required': True},
        'abnormal_bill_use_with_outlier_analysis': {'required': True},
        'abnormal_bill_demand_with_outlier_analysis': {'required': True},
    }

    _attribute_map = {
        'bill_contains_line_item_descriptions': {'key': 'billContainsLineItemDescriptions', 'type': 'BillContainsLineItemDescriptionsSettingResponse'},
        'bill_contains_line_item_types': {'key': 'billContainsLineItemTypes', 'type': 'BillContainsLineItemTypesSettingResponse'},
        'total_bill_cost_does_not_match_line_item_types': {'key': 'totalBillCostDoesNotMatchLineItemTypes', 'type': 'TotalBillCostDoesNotMatchLineItemTypesSettingResponse'},
        'billing_period_outside_start_end_dates': {'key': 'billingPeriodOutsideStartEndDates', 'type': 'AuditSettingResponse'},
        'bill_overlaps_with_other_account_bill': {'key': 'billOverlapsWithOtherAccountBill', 'type': 'AuditSettingResponse'},
        'gap_between_bill_and_previous_bill_on_account': {'key': 'gapBetweenBillAndPreviousBillOnAccount', 'type': 'AuditSettingResponse'},
        'bill_ends_in_future': {'key': 'billEndsInFuture', 'type': 'AuditSettingResponse'},
        'account_has_multiple_bills_in_billing_period': {'key': 'accountHasMultipleBillsInBillingPeriod', 'type': 'AuditSettingResponse'},
        'statement_date_before_end_date': {'key': 'statementDateBeforeEndDate', 'type': 'AuditSettingResponse'},
        'due_date_before_end_date': {'key': 'dueDateBeforeEndDate', 'type': 'AuditSettingResponse'},
        'bill_significantly_shorter_or_longer_than_previous': {'key': 'billSignificantlyShorterOrLongerThanPrevious', 'type': 'BillSignificantlyShorterOrLongerThanPreviousSettingResponse'},
        'too_many_consecutive_estimated_bills': {'key': 'tooManyConsecutiveEstimatedBills', 'type': 'TooManyConsecutiveEstimatedBillsSettingResponse'},
        'due_date_too_long_after_bill_end': {'key': 'dueDateTooLongAfterBillEnd', 'type': 'DueDateTooLongAfterBillEndSettingResponse'},
        'statement_date_too_long_after_bill_end': {'key': 'statementDateTooLongAfterBillEnd', 'type': 'StatementDateTooLongAfterBillEndSettingResponse'},
        'invoice_number_is_repeated_on_account': {'key': 'invoiceNumberIsRepeatedOnAccount', 'type': 'AuditSettingResponse'},
        'likely_duplicate_bill_on_account': {'key': 'likelyDuplicateBillOnAccount', 'type': 'AuditSettingResponse'},
        'total_meter_cost_is_percentage_higher_than_past_year': {'key': 'totalMeterCostIsPercentageHigherThanPastYear', 'type': 'AuditSettingResponse'},
        'total_meter_use_is_percentage_higher_than_past_year': {'key': 'totalMeterUseIsPercentageHigherThanPastYear', 'type': 'AuditSettingResponse'},
        'serial_number_does_not_match_import_file': {'key': 'serialNumberDoesNotMatchImportFile', 'type': 'AuditSettingResponse'},
        'rate_code_does_not_match_import_file': {'key': 'rateCodeDoesNotMatchImportFile', 'type': 'AuditSettingResponse'},
        'import_file_start_date_adjusted_to_prevent_gaps': {'key': 'importFileStartDateAdjustedToPreventGaps', 'type': 'AuditSettingResponse'},
        'account_alert_exists_on_account_in_import_file': {'key': 'accountAlertExistsOnAccountInImportFile', 'type': 'AuditSettingResponse'},
        'abnormal_bill_cost_with_outlier_analysis': {'key': 'abnormalBillCostWithOutlierAnalysis', 'type': 'AbnormalBillCostWithOutlierAnalysisSettingResponse'},
        'abnormal_bill_use_with_outlier_analysis': {'key': 'abnormalBillUseWithOutlierAnalysis', 'type': 'AbnormalBillUseWithOutlierAnalysisSettingResponse'},
        'abnormal_bill_demand_with_outlier_analysis': {'key': 'abnormalBillDemandWithOutlierAnalysis', 'type': 'AbnormalBillDemandWithOutlierAnalysisSettingResponse'},
    }

    def __init__(self, **kwargs):
        super(AuditSettingsResponse, self).__init__(**kwargs)
        self.bill_contains_line_item_descriptions = kwargs.get('bill_contains_line_item_descriptions', None)
        self.bill_contains_line_item_types = kwargs.get('bill_contains_line_item_types', None)
        self.total_bill_cost_does_not_match_line_item_types = kwargs.get('total_bill_cost_does_not_match_line_item_types', None)
        self.billing_period_outside_start_end_dates = kwargs.get('billing_period_outside_start_end_dates', None)
        self.bill_overlaps_with_other_account_bill = kwargs.get('bill_overlaps_with_other_account_bill', None)
        self.gap_between_bill_and_previous_bill_on_account = kwargs.get('gap_between_bill_and_previous_bill_on_account', None)
        self.bill_ends_in_future = kwargs.get('bill_ends_in_future', None)
        self.account_has_multiple_bills_in_billing_period = kwargs.get('account_has_multiple_bills_in_billing_period', None)
        self.statement_date_before_end_date = kwargs.get('statement_date_before_end_date', None)
        self.due_date_before_end_date = kwargs.get('due_date_before_end_date', None)
        self.bill_significantly_shorter_or_longer_than_previous = kwargs.get('bill_significantly_shorter_or_longer_than_previous', None)
        self.too_many_consecutive_estimated_bills = kwargs.get('too_many_consecutive_estimated_bills', None)
        self.due_date_too_long_after_bill_end = kwargs.get('due_date_too_long_after_bill_end', None)
        self.statement_date_too_long_after_bill_end = kwargs.get('statement_date_too_long_after_bill_end', None)
        self.invoice_number_is_repeated_on_account = kwargs.get('invoice_number_is_repeated_on_account', None)
        self.likely_duplicate_bill_on_account = kwargs.get('likely_duplicate_bill_on_account', None)
        self.total_meter_cost_is_percentage_higher_than_past_year = kwargs.get('total_meter_cost_is_percentage_higher_than_past_year', None)
        self.total_meter_use_is_percentage_higher_than_past_year = kwargs.get('total_meter_use_is_percentage_higher_than_past_year', None)
        self.serial_number_does_not_match_import_file = kwargs.get('serial_number_does_not_match_import_file', None)
        self.rate_code_does_not_match_import_file = kwargs.get('rate_code_does_not_match_import_file', None)
        self.import_file_start_date_adjusted_to_prevent_gaps = kwargs.get('import_file_start_date_adjusted_to_prevent_gaps', None)
        self.account_alert_exists_on_account_in_import_file = kwargs.get('account_alert_exists_on_account_in_import_file', None)
        self.abnormal_bill_cost_with_outlier_analysis = kwargs.get('abnormal_bill_cost_with_outlier_analysis', None)
        self.abnormal_bill_use_with_outlier_analysis = kwargs.get('abnormal_bill_use_with_outlier_analysis', None)
        self.abnormal_bill_demand_with_outlier_analysis = kwargs.get('abnormal_bill_demand_with_outlier_analysis', None)
