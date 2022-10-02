import cicd.logger as logger
import subprocess
import os
import json

import cicd.secret as secret

def get_version():
    f = open('package.json')
    data = json.load(f)
    return data['version']
