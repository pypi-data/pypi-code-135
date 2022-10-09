"""
Created on Mar 04, 2021

@author: Siro

"""
from atwork.atframework.web.common.maps.bo.bo_header_elements_maps import BoHeaderElementsMaps
from atwork.atframework.web.common.maps.bo.bo_login_elements_maps import BoLoginElementsMaps
from atwork.atframework.web.common.maps.bo.bo_rebate_elements_maps import BoRebateElementsMaps
from atwork.atframework.web.common.maps.bo.bo_voucher_elements_maps import BoVoucherElementsMaps
from atwork.atframework.web.common.maps.bo.bo_helpdesk_elements_maps import BoHelpdeskElementsMaps
from atwork.atframework.web.common.maps.bo.bo_dashboard_elements_maps import BoDashboardElementsMaps
from atwork.atframework.web.common.maps.bo.bo_report_elements_maps import BoReportElementsMaps
from atwork.atframework.web.common.maps.bo.bo_menu_elements_maps import BoMenuElementsMaps
from atwork.atframework.web.common.maps.bo.bo_blacklist_elements_maps import BoBlacklistElementsMaps
from atwork.atframework.web.common.maps.bo.bo_alarms_elements_maps import BoAlarmsElementsMaps
from atwork.atframework.web.common.maps.bo.bo_billfold_configuration_elements_maps import BoBillfoldConfigurationElementsMaps
from atwork.atframework.web.common.maps.bo.bo_payment_elements_maps import BoPaymentElementsMaps
from atwork.atframework.web.common.maps.bo.bo_game_transaction_elements_maps import BoGameTransactionElementsMaps
from atwork.atframework.web.common.maps.bo.bo_campaign_elements_maps import BoCampaignElementsMaps


class ElementsMaps(BoHeaderElementsMaps, BoLoginElementsMaps, BoRebateElementsMaps, BoVoucherElementsMaps,
                   BoHelpdeskElementsMaps, BoDashboardElementsMaps, BoReportElementsMaps, BoMenuElementsMaps,
                   BoBlacklistElementsMaps, BoAlarmsElementsMaps, BoBillfoldConfigurationElementsMaps, BoPaymentElementsMaps,
                   BoGameTransactionElementsMaps, BoCampaignElementsMaps):
    """
    Integrate all model to this class, Use this class to call elements
    """
