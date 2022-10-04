import boto3

from vetl.core import log

session = boto3.session.Session()

# Global Variable
data = {}

def getSecret(*id):
    import json
    result = {}
    for i in id:
        data[i] = json.loads(session.client('secretsmanager').get_secret_value(SecretId=i)['SecretString'])
        if len(id) == 1:
            result = data[i]
        if len(id) > 1:
            result[i] = data[i]
    return result