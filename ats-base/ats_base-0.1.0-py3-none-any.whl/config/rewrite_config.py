import configparser
import os

CONFIG = configparser.ConfigParser()

if os.path.exists('config.ini'):
    os.remove('config.ini')

# CONFIG CONTENT
CONFIG['URL'] = {}
CONFIG['URL']['URL'] = 'http://10.10.5.108:8888/'
CONFIG['URL']['API'] = 'api'
CONFIG['URL']['MANUAL'] = 'manual'


CONFIG['SERVICE'] = {}
CONFIG['SERVICE']['tcc'] = 'tcc'
CONFIG['SERVICE']['pro'] = 'pro'
CONFIG['SERVICE']['mm'] = 'mm'
CONFIG['SERVICE']['db'] = 'db'
CONFIG['SERVICE']['gw698'] = 'gw698'
CONFIG['SERVICE']['dlms'] = 'dlms'
CONFIG['SERVICE']['dlt645'] = 'dlt645'
CONFIG['SERVICE']['dvs'] = 'dvs'


CONFIG['EM'] = {}
CONFIG['EM']['ip'] = '10.10.101.233'
CONFIG['EM']['port'] = '4445'


with open('config.ini', 'w') as file:
    CONFIG.write(file)