#!/usr/bin/env python3
"""
This module contains functions to get data from the Cisco Support APIs.

The functions are ordered as followed:
- Cisco support API call functions in Nornir stdout style
"""


import sys
import json
import time
from cisco_support import SNI, EoX
from cisco_support.utils import getToken as cisco_support_get_token
from nornir_maze.utils import (
    print_task_name,
    task_host,
    task_info,
    task_error,
    iterate_all,
)


#### Cisco API call functions in Nornir stdout style #########################################################


def cisco_support_check_authentication(api_client_creds, verbose=False):
    """
    This function checks to Cisco support API authentication by generating an bearer access token. In case
    of an invalid API client key or secret a error message is printed and the script exits.
    """
    task_name = "CISCO-API check OAuth2 client credentials grant flow"
    print_task_name(text=task_name)

    try:
        # Try to generate an barer access token
        token = cisco_support_get_token(*api_client_creds, verify=None, proxies=None)

        print(task_info(text=task_name, changed="False"))
        print("'Bearer access token generation' -> CISCOAPIResult <Success: True>")
        if verbose:
            print(f"\n-> Bearer token: {token}\n")

    except KeyError:
        ansi_red_bold = "\033[1m\u001b[31m"
        ansi_reset = "\033[0m"
        print(task_error(text=task_name, changed="False"))
        print("'Bearer access token generation' -> CISCOAPIResult <Success: False>")
        print("\n\U0001f4a5 ALERT: INVALID API CREDENTIALS PROVIDED! \U0001f4a5")
        print(f"{ansi_red_bold}-> Verify the API client key and secret{ansi_reset}\n")
        sys.exit(1)


def get_sni_owner_coverage_by_serial_number(serial_dict, api_client_creds, verbose=False):
    """
    This function takes the serial_dict which contains all serial numbers and the Cisco support API creds to
    run get the owner coverage by serial number with the cisco-support library. The printout is in Nornir
    style, but there is no use of Nornir. The result of each serial will be added with a new key to the dict.
    The function returns the updated serials dict. The format of the serials_dict need to be as below.
    "<serial>": {
        "host": "<hostname>",
        ...
    },
    """
    # Backoff sleep and attempt values
    config_attempts = 5
    sleep = 1
    sleep_multiplier = 1.5

    task_text = "CISCO-API get owner coverage status by serial number"
    print_task_name(text=task_text)

    sni = SNI(*api_client_creds)

    # Re-try the Cisco support API call with a backoff again in case of an error
    for _ in range(config_attempts):
        owner_coverage_status = sni.getOwnerCoverageStatusBySerialNumbers(serial_dict.keys())

        # Break out of the range() loop if ErrorResponse is not present
        if "ErrorResponse" not in owner_coverage_status:
            break

        # Sleep and continue with next range() loop attempt
        time.sleep(sleep)
        sleep = sleep * sleep_multiplier

    # Ending for loop as iterable exhausted
    else:
        print(task_error(text=task_text, changed="False"))
        print("'Get SNI data' -> CISCOAPIResult <Success: False>\n")
        for key, value in owner_coverage_status["ErrorResponse"]["APIError"][0].items():
            print(f"-> {key}: {value}")
        print(
            "\n\U0001f4a5 ALERT: GET CISCO SUPPORT API DATA FAILED! \U0001f4a5\n"
            "\033[1m\u001b[31m-> Analyse the error message and identify the root cause\033[0m\n\n"
        )
        sys.exit(1)

    for item in owner_coverage_status["serial_numbers"]:
        sr_no = item["sr_no"]
        serial_dict[sr_no]["SNIgetOwnerCoverageStatusBySerialNumbers"] = item
        print(task_host(host=f"HOST: {serial_dict[sr_no]['host']} / SN: {sr_no}", changed="False"))

        # Verify if the serial number is associated with the CCO ID
        if "YES" in item["sr_no_owner"]:
            print(task_info(text="Verify provided CCO ID", changed="False"))
            print("'Is associated to the provided CCO ID' -> CISCOAPIResult <Success: True>")
        else:
            print(task_error(text="Verify provided CCO ID", changed="False"))
            print("'Is not associated to the provided CCO ID' -> CISCOAPIResult <Success: False>")

        # Verify if the serial is covered by a service contract
        if "YES" in item["is_covered"]:
            print(task_info(text="Verify service contract", changed="False"))
            print("'Is covered by a service contract' -> CISCOAPIResult <Success: True>")
            # Verify the end date of the service contract coverage
            if item["coverage_end_date"]:
                print(task_info(text="Verify service contract end date", changed="False"))
                print(f"'Coverage end date is {item['coverage_end_date']}' -> CISCOAPIResult <Success: True>")
            else:
                print(task_error(text="Verify service contract end date", changed="False"))
                print("'Coverage end date not available' -> CISCOAPIResult <Success: False>")
        else:
            print(task_error(text="Verify service contract", changed="False"))
            print("'Is not covered by a service contract' -> CISCOAPIResult <Success: False>")

        if verbose:
            print("\n" + json.dumps(item, indent=4))

    return serial_dict


def get_sni_coverage_summary_by_serial_numbers(serial_dict, api_client_creds, verbose=False):
    """
    This function takes the serial_dict which contains all serial numbers and the Cisco support API creds to
    run get the coverage summary by serial number with the cisco-support library. The printout is in Nornir
    style, but there is no use of Nornir. The result of each serial will be added with a new key to the dict.
    The function returns the updated serials dict. The format of the serials_dict need to be as below.
    "<serial>": {
        "host": "<hostname>",
        ...
    },
    """
    # Backoff sleep and attempt values
    config_attempts = 5
    sleep = 1
    sleep_multiplier = 1.5

    task_text = "CISCO-API get coverage summary data by serial number"
    print_task_name(text=task_text)

    sni = SNI(*api_client_creds)

    # Re-try the Cisco support API call with a backoff again in case of an error
    for _ in range(config_attempts):
        coverage_summary = sni.getCoverageSummaryBySerialNumbers(serial_dict.keys())

        # Break out of the range() loop if ErrorResponse is not present
        if "ErrorResponse" not in coverage_summary:
            break

        # Sleep and continue with next range() loop attempt
        time.sleep(sleep)
        sleep = sleep * sleep_multiplier

    # Ending for loop as iterable exhausted
    else:
        print(task_error(text=task_text, changed="False"))
        print("'Get SNI data' -> CISCOAPIResult <Success: False>\n")
        for key, value in coverage_summary["ErrorResponse"]["APIError"][0].items():
            print(f"-> {key}: {value}")
        print(
            "\n\U0001f4a5 ALERT: GET CISCO SUPPORT API DATA FAILED! \U0001f4a5\n"
            "\033[1m\u001b[31m-> Analyse the error message and identify the root cause\033[0m\n\n"
        )
        sys.exit(1)

    for item in coverage_summary["serial_numbers"]:
        sr_no = item["sr_no"]
        serial_dict[sr_no]["SNIgetCoverageSummaryBySerialNumbers"] = item
        print(task_host(host=f"HOST: {serial_dict[sr_no]['host']} / SN: {sr_no}", changed="False"))

        if "ErrorResponse" in item:
            error_response = item["ErrorResponse"]["APIError"]
            print(task_error(text=task_text, changed="False"))
            print("'Get SNI data' -> CISCOAPIResult <Success: False>")
            print(f"\n-> {error_response['ErrorDescription']} ({error_response['SuggestedAction']})\n")
        else:
            print(task_info(text=task_text, changed="False"))
            print("'Get SNI data' -> CISCOAPIResult <Success: True>")
            print(f"\n-> Orderable pid: {item['orderable_pid_list'][0]['orderable_pid']}")
            print(f"-> Customer name: {item['contract_site_customer_name']}")
            print(f"-> Customer address: {item['contract_site_address1']}")
            print(f"-> Customer city: {item['contract_site_city']}")
            print(f"-> Customer province: {item['contract_site_state_province']}")
            print(f"-> Customer country: {item['contract_site_country']}")
            print(f"-> Is covered by service contract: {item['is_covered']}")
            print(f"-> Covered product line end date: {item['covered_product_line_end_date']}")
            print(f"-> Service contract number: {item['service_contract_number']}")
            print(f"-> Service contract description: {item['service_line_descr']}")
            print(f"-> Warranty end date: {item['warranty_end_date']}")
            print(f"-> Warranty type: {item['warranty_type']}\n")

        if verbose:
            print(json.dumps(item, indent=4))

    return serial_dict


def get_eox_by_serial_numbers(serial_dict, api_client_creds, verbose=False):
    """
    This function takes the serial_dict which contains all serial numbers and the Cisco support API creds to
    run get the end of life data by serial number with the cisco-support library. The printout is in Nornir
    style, but there is no use of Nornir. The result of each serial will be added with a new key to the dict.
    The function returns the updated serials dict. The format of the serials_dict need to be as below.
    "<serial>": {
        "host": "<hostname>",
        ...
    },
    """
    # Backoff sleep and attempt values
    config_attempts = 5
    sleep = 1
    sleep_multiplier = 1.5

    task_text = "CISCO-API get EoX data by serial number"
    print_task_name(text=task_text)

    eox = EoX(*api_client_creds)

    # Re-try the Cisco support API call with a backoff again in case of an error
    for _ in range(config_attempts):
        end_of_life = eox.getBySerialNumbers(serial_dict.keys())

        # Break out of the range() loop if ErrorResponse is not present
        if "ErrorResponse" not in end_of_life:
            break

        # Sleep and continue with next range() loop attempt
        time.sleep(sleep)
        sleep = sleep * sleep_multiplier

    # Ending for loop as iterable exhausted
    else:
        print(task_error(text=task_text, changed="False"))
        print("'Get EoX data' -> CISCOAPIResult <Success: False>\n")
        for key, value in end_of_life["ErrorResponse"]["APIError"][0].items():
            print(f"-> {key}: {value}")
        print(
            "\n\U0001f4a5 ALERT: GET CISCO SUPPORT API DATA FAILED! \U0001f4a5\n"
            "\033[1m\u001b[31m-> Analyse the error message and identify the root cause\033[0m\n\n"
        )
        sys.exit(1)

    for item in end_of_life["EOXRecord"]:
        sr_no = item["EOXInputValue"]
        serial_dict[sr_no]["EOXgetBySerialNumbers"] = item
        print(task_host(host=f"HOST: {serial_dict[sr_no]['host']} / SN: {sr_no}", changed="False"))

        if "EOXError" in item:
            if "No product IDs were found" in item["EOXError"]["ErrorDescription"]:
                print(task_error(text=task_text, changed="False"))
                print("'Get EoX data' -> CISCOAPIResult <Success: False>")
                print(f"\n-> {item['EOXError']['ErrorDescription']} (Serial number does not exist)\n")
            elif "EOX information does not exist" in item["EOXError"]["ErrorDescription"]:
                print(task_info(text=task_text, changed="False"))
                print("'Get EoX data' -> CISCOAPIResult <Success: True>")
                print(f"\n-> {item['EOXError']['ErrorDescription']}\n")
        else:
            print(task_info(text=task_text, changed="False"))
            print(
                f"'Get EoX data (Update timestamp {item['UpdatedTimeStamp']['value']})' "
                + "-> CISCOAPIResult <Success: True>"
            )
            print(f"\n-> EoL product ID: {item['EOLProductID']}")
            print(f"-> Product ID description: {item['ProductIDDescription']}")
            print(f"-> EoL announcement date: {item['EOXExternalAnnouncementDate']['value']}")
            print(f"-> End of sale date: {item['EndOfSaleDate']['value']}")
            print(f"-> End of maintenance release: {item['EndOfSWMaintenanceReleases']['value']}")
            print(f"-> End of vulnerability support: {item['EndOfSecurityVulSupportDate']['value']}")
            print(f"-> Last day of support: {item['LastDateOfSupport']['value']}\n")

        if verbose:
            print(json.dumps(item, indent=4))

    return serial_dict


def verify_cisco_support_api_data(serials_dict, verbose=False):
    """
    This function verifies the serials_dict which has been filled with data by various functions of these
    module like eox_by_serial_numbers, sni_get_coverage_summary_by_serial_numbers, etc. and verifies that
    there are no invalid serial numbers. In case of invalid serial numbers, the script quits with an error
    message.
    """
    failed = False
    task_text = "Verify Cisco support API data"
    print_task_name(text=task_text)

    # Verify that the serials_dict dictionary contains no wrong serial numbers
    for value in iterate_all(iterable=serials_dict, returned="value"):
        if value is not None:
            if "No product IDs were found" in value or "No records found" in value:
                failed = True
                break

    if failed:
        print(task_error(text=task_text, changed="False"))
        print(f"'{task_text}' -> Result <Success: False>")
        print(
            "\n\U0001f4a5 ALERT: INVALID SERIAL NUMBERS PROVIDED! \U0001f4a5\n"
            "\033[1m\u001b[31m"
            "-> Analyse the output for failed tasks to identify the invalid serial numbers\n"
            "-> Run the script with valid serial numbers only again\033[0m\n\n"
        )
        sys.exit(1)

    print(task_info(text=task_text, changed="False"))
    print(f"'{task_text}' -> Result <Success: True>")
    if verbose:
        print("\n" + json.dumps(serials_dict, indent=4))
