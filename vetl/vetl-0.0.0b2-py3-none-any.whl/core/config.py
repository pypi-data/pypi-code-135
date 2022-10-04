from operator import itemgetter

from vetl.core import file
from vetl.core.aws.s3 import configDefaultBucket, configDefaultARN
from vetl.core.aws.secret import getSecret
from vetl.core.database import setDB
from vetl.core.tunnel import setTunnel

'''
    {
        "aws": {
            "s3":{
                "bucket": "bucket_name",
                "arn": "arn_name"
            }
        },
        "tunnel": {
            "alias": {
                "host": "host_credential",
                "port": "port_credential",
                "username": "username_credential",
                "password": "password_credential",
                "password_mode": "password_mode_credential",
                "remote_address": "remote_address_credential"
            }
        }
        "tunnel_aws_secret": {
            "data": {
                "alias": "id"
            },
            "map": {
                "host": "host_key_in_secret",
                "port": "port_key_in_secret",
                "username": "username_key_in_secret",
                "password": "password_key_in_secret",
                "password_mode": "password_mode_key_in_secret",
                "remote_address": "remote_address_key_in_secret"
            }
        },
        "database: {
            "alias": {
                "host": "host_credential",
                "port": "port_credential",
                "dbname": "database_credential",
                "username": "username_credential",
                "password": "password_credential",
                "engine": "engine_credential"
            }
        },
        "database_aws_secret": {
            "data": {
                "alias": "id"
            },
            "map": {
                "host": "host_aws_secret",
                "port": "port_aws_secret",
                "dbname": "database_aws_secret",
                "username": "username_aws_secret",
                "password": "password_aws_secret",
                "engine": "engine_aws_secret"
            }
        }

    }    
'''

def set(arg):
    config = None
    if type(arg) == str:
        if arg.__contains__(".json"):
            config = file.open(arg)
    if type(arg) == dict:
        config = arg
    if config != None:
        if "aws" in config.keys():
            if "s3" in config["aws"].keys():
                if "bucket" in config["aws"]["s3"].keys():
                    configDefaultBucket(config["aws"]["s3"]["bucket"])
                if "arn" in config["aws"]["s3"].keys():
                    configDefaultARN(config["aws"]["s3"]["arn"])
        if "tunnel" in config.keys():
            for alias, value in config["tunnel"].items():
                host, port, username, password, password_mode, address_list = itemgetter("host", "port", "username", "password", "password_mode", "remote_address")(value)
                setTunnel(host, port, username, password, password_mode, address_list, alias)
        if "tunnel_aws_secret" in config.keys():
            for alias, id in config["tunnel_aws_secret"]["data"].items():
                secret = getSecret(id)
                map = config["tunnel_aws_secret"]["map"]
                for cred in ["host", "port", "username", "password", "password_mode", "remote_address"]:
                    if cred not in map.keys():
                        map[cred] = cred
                host, port, username, password, password_mode, address_list = itemgetter(map["host"], map["port"], map["username"], map["password"], map["password_mode"], map["remote_address"])(secret)
                setTunnel(host, port, username, password, password_mode, address_list, alias)
        if "database" in config.keys():
            for alias, value in config["database"].items():
                host, port, dbname, username, password, engine = itemgetter("host", "port", "dbname", "username", "password", "engine")(value)
                setDB(host, port, dbname, username, password, engine, alias)
        if "database_aws_secret" in config.keys():
            for alias, id in config["database_aws_secret"]["data"].items():
                secret = getSecret(id)
                map = config["database_aws_secret"]["map"]
                for cred in ["host", "port", "dbname", "username", "password", "engine"]:
                    if cred not in map.keys():
                        map[cred] = cred
                host, port, dbname, username, password, engine = itemgetter(map["host"], map["port"], map["dbname"], map["username"], map["password"], map["engine"])(secret)
                setDB(host, port, dbname, username, password, engine, alias)



