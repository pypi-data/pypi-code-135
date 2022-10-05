##
## documentation:
import requests
import json
import jinja2
from requests import post

## Return codes expected by Nagios
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

status = OK

class AzureAlerts:
    def __init__(self, tenant_id, client_id, client_secret, suscription_id, time_range):  
        ## initialization
        ## At the beginning, the code will get the alerts information

        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.suscription_id = suscription_id
        self.time_range = time_range

    def get_alerts(self):


        ## Vars
        api_version = '2019-03-01'
        alert_state = 'New'
        monitor_condition = 'Fired'
        authorization_token = self.get_token()

        text_to_print = ''
        counter = 0

        url_alerts = f'https://management.azure.com/subscriptions/{self.suscription_id}/providers/Microsoft.AlertsManagement/alerts?api-version={api_version}&alertState={alert_state}&timeRange={self.time_range}&monitorCondition={monitor_condition}'

        ## Headers
        headers_alerts = {
            'Authorization': "Bearer " + authorization_token,
            'Content-Type': 'application/json'
        }

        ## Retrive JSON
        response_alerts = requests.get(url=url_alerts, headers=headers_alerts)
        ## Checks if http error exit with traceback and error / https://stackoverflow.com/questions/61463224/when-to-use-raise-for-status-vs-status-code-testing
        ## https://www.codegrepper.com/code-examples/python/raise_for_status%28%29+requests
        try:
            response_alerts.raise_for_status()
            response_alerts_body = response_alerts.json()

            environment = jinja2.Environment()
            template = environment.from_string("""
            Name: {{ alert_name }}
            targetResourceName: {{ alert_targetResourceName }}
            targetResourceGroup: {{ alert_targetResourceGroup }}
            startDateTime: {{ alert_startDateTime }}
            Description: {{ alert_description }}

            """
            )            

            ## Start processing the json
            ## and generate the string to print
            ## Read the list of alerts from key 'value'
            for alert in response_alerts_body['value']:
                status = CRITICAL
                counter += 1
                alert_name = alert.get('name')
                alert_targetResourceName = alert.get('properties').get('essentials').get('targetResourceName')
                alert_targetResourceGroup = alert.get('properties').get('essentials').get('targetResourceGroup')
                alert_startDateTime = alert.get('properties').get('essentials').get('startDateTime')
                alert_description = alert.get('properties').get('essentials').get('description')

                ## Start concatenating the text template rendered with the values:
                text_to_print += template.render(
                    alert_name = alert_name,
                    alert_targetResourceName = alert_targetResourceName,
                    alert_targetResourceGroup = alert_targetResourceGroup,
                    alert_startDateTime = alert_startDateTime,
                    alert_description = alert_description
                )

                if counter == 10:
                    break

        except requests.exceptions.HTTPError as error:

            status = CRITICAL

            ## Example error output
            """"
            {"error":
                {"code":"AuthenticationFailedMissingToken","message":"Authentication failed. The 'Authorization' header is missing the access token."}
            }
            """                       
            
            ## Retrieve error message and code of request failed
            error_json = error.response.json()
            error_message = error_json['error']['message'] 
            error_code = error_json['error']['code'] 

            # Print the message
            print("Error request: " + error_message + "\nCode: " + error_code)
            
            ## Exit with message and code of error
            raise SystemExit(status)
            

        return text_to_print, response_alerts.status_code, status

    def get_token(self):

        ## Headers
        headers_token = {
            'Host': 'login.microsoftonline.com',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        ## Body
        body = {
            'client_id': self.client_id,
            'scope': 'https://management.azure.com//.default',
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials',
            'tenant': self.tenant_id
        }

        login_url = f'https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token'

        ## Retrive JSON
        response_token = post(url=login_url, headers=headers_token, data=body)
        ## Checks if http error exit with traceback and error / https://stackoverflow.com/questions/61463224/when-to-use-raise-for-status-vs-status-code-testing
        ## https://www.codegrepper.com/code-examples/python/raise_for_status%28%29+requests
        try:
            response_token.raise_for_status() 
            response_alerts_body = response_token.json()
            ## Take token from json
            authorization_token = f"{response_alerts_body['access_token']}"
        except:
            authorization_token = ""

        return authorization_token
