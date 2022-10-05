#!python3
# https://nagios-plugins.org/doc/guidelines.html

# Import required libs for sharepointhealth
from .azure_alerts_check import AzureAlerts
import argparse
import sys

# Return codes expected by Nagios
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

status = OK

# Return message
message = {
    'status': OK,
    'summary': 'Alerts summary',
    'perfdata': 'label1=0;;;; '  # 'label'=value[UOM];[warn];[crit];[min];[max] 
}

# For multiple perdata, ensure to add space after each perfdata
# message['perfdata'] = 'label1=x;;;; '
# message['perfdata'] += 'label2=x;;;; '

# Function to parse arguments
def parse_args(args):
    """
    Information extracted from: https://mkaz.com/2014/07/26/python-argparse-cookbook/
    https://docs.python.org/3/library/argparse.html
    :return: parse.parse_args(args) object
    You can use obj.option, example:
    options = parse_args(args)
    options.user # to read username
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, 
        description='Nagios plugin to check azure alerts')

    parser.add_argument('--tenant_id', dest='tenant_id', nargs='?', default=None, const=None, help='Header tenant ID of Azure \n')
    parser.add_argument('--client_id', dest='client_id', nargs='?', default=None, const=None, help='Header client_id \n')
    parser.add_argument('--client_secret', dest='client_secret', nargs='?', default=None, const=None, help='Header client_secret \n')
    parser.add_argument('--suscription_id', dest='suscription_id', nargs='?', default=None, const=None, help='Header suscription id of Azure \n')
    parser.add_argument('--time_range', dest='time_range' , nargs='?', default='1d', const=None, help='Time range for alerts - default=1d (accepted values: 1d, 1h, 30d, 7d) \n')
    parser.add_argument('-e', '--extra_args', dest='extra_args', nargs='?', default='', const=None, help='extra args to add to curl, see curl manpage  \n')

    if not args:
        raise SystemExit(parser.print_help())

    return parser.parse_args(args)

# Function to execute cli commands
def cli_execution(options):
    """
    : param: options: arguments from parse.parse_args(args) (see parse_args function)
    """
    #variables
    auth_args = '' 
    retrcode = OK
    
    if not options.tenant_id:
            sys.exit('param tenant_id is required  when using azure alerts check ')
    if not options.client_secret:
            sys.exit('param client_secret is required  when using azure alerts check ')
    if not options.client_id:
            sys.exit('param client_id is required  when using azure alerts check ')
    if not options.suscription_id:
            sys.exit('param suscription_id is required  when using azure alerts check ')

    # Get list of Azure alerts
    azure_alerts_obj = AzureAlerts(tenant_id = options.tenant_id, client_id = options.client_id,client_secret = options.client_secret,suscription_id = options.suscription_id, time_range = options.time_range)	

    azure_alerts_tuple = azure_alerts_obj.get_alerts()
    
    summary_alerts = azure_alerts_tuple[0]
    response_http_code = azure_alerts_tuple[1]   
    retrcode =  azure_alerts_tuple[2]   

    #if '200' not in response_http_code:        
    if response_http_code != 200:
        sys.exit('Error getting data from {} http_code != 200, http_code: {}'.format(response_http_code))

    def check(retrcode):
        if retrcode == 2:            
            message['summary'] = 'CRITICAL: ' + str(summary_alerts)
        else:
            global status 
            status = OK
            message['summary'] = 'OK: No alerts' 
        return status

    # Check logic starts here    
    message['status'] = check(retrcode)

    # Print the message
    print("{summary}".format(
        summary=message.get('summary'),
    ))

    # Exit with status code
    raise SystemExit(message['status'])

# Argument parser
# https://docs.python.org/3.5/library/argparse.html

def main():
    """
    Main function
    """
    # Get options with argparse
    options = parse_args(sys.argv[1:])
    # Execute program functions passing the options collected
    cli_execution(options)


if __name__ == "__main__":
    main()
