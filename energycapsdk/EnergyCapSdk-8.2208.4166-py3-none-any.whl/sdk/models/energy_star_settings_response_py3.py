# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EnergyStarSettingsResponse(Model):
    """EnergyStarSettingsResponse.

    :param pm_account_manager_full_name: Full name of Portfolio Account
     Manager
    :type pm_account_manager_full_name: str
    :param pm_account_manager_user_name: User name of Portfolio Account
     Manager
    :type pm_account_manager_user_name: str
    :param earliest_submission_period: The earliest period to submit
    :type earliest_submission_period: int
    :param unlinked_property_count: Number of Portfolio Manager properties
     that are not linked to any buildings in EnergyCAP
    :type unlinked_property_count: int
    :param linked_property_count: Number of Portfolio Manager properties that
     are linked to a building in EnergyCAP
    :type linked_property_count: int
    :param is_energy_star_available: True if this client is configured for
     ENERGY STAR and Portfolio manager is available. False indicates an issue.
     EnergyStarConfigurationErrorMessage will contain details
    :type is_energy_star_available: bool
    :param energy_star_configuration_error_message: If IsEnergystarAvailable
     is false, this reports the error
    :type energy_star_configuration_error_message: str
    :param is_energy_star_disabled: True if running offline mode or if ENERGY
     STAR has been disabled for this client, false otherwise
    :type is_energy_star_disabled: bool
    :param is_energy_star_configured: True if ENERGY STAR has been configured
    :type is_energy_star_configured: bool
    """

    _attribute_map = {
        'pm_account_manager_full_name': {'key': 'pmAccountManagerFullName', 'type': 'str'},
        'pm_account_manager_user_name': {'key': 'pmAccountManagerUserName', 'type': 'str'},
        'earliest_submission_period': {'key': 'earliestSubmissionPeriod', 'type': 'int'},
        'unlinked_property_count': {'key': 'unlinkedPropertyCount', 'type': 'int'},
        'linked_property_count': {'key': 'linkedPropertyCount', 'type': 'int'},
        'is_energy_star_available': {'key': 'isEnergyStarAvailable', 'type': 'bool'},
        'energy_star_configuration_error_message': {'key': 'energyStarConfigurationErrorMessage', 'type': 'str'},
        'is_energy_star_disabled': {'key': 'isEnergyStarDisabled', 'type': 'bool'},
        'is_energy_star_configured': {'key': 'isEnergyStarConfigured', 'type': 'bool'},
    }

    def __init__(self, *, pm_account_manager_full_name: str=None, pm_account_manager_user_name: str=None, earliest_submission_period: int=None, unlinked_property_count: int=None, linked_property_count: int=None, is_energy_star_available: bool=None, energy_star_configuration_error_message: str=None, is_energy_star_disabled: bool=None, is_energy_star_configured: bool=None, **kwargs) -> None:
        super(EnergyStarSettingsResponse, self).__init__(**kwargs)
        self.pm_account_manager_full_name = pm_account_manager_full_name
        self.pm_account_manager_user_name = pm_account_manager_user_name
        self.earliest_submission_period = earliest_submission_period
        self.unlinked_property_count = unlinked_property_count
        self.linked_property_count = linked_property_count
        self.is_energy_star_available = is_energy_star_available
        self.energy_star_configuration_error_message = energy_star_configuration_error_message
        self.is_energy_star_disabled = is_energy_star_disabled
        self.is_energy_star_configured = is_energy_star_configured
