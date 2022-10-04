from vetl.core import log
from vetl.core.aws.secret import session

default = {
    "bucket": None,
    "arn": None
}

def configDefaultBucket(value):
    _config_default_bucket_(value)

def _config_default_bucket_(value):
    global default
    default["bucket"] = value

def configDefaultARN(value):
    _config_default_arn_(value)

def _config_default_arn_(value):
    global default
    default["arn"] = value

def viewDefaultBucket():
    return default["bucket"]

def viewDefaultARN():
    return default["arn"]
