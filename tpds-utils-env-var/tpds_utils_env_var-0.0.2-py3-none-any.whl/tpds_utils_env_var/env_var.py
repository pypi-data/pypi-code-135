import boto3
import os
import datetime


def get_local_env_var(var_group: str, var_name: str) -> str:
    """
    Get environment variable from local environment. Local variables must be of the form: GROUP_NAME_VARIABLE_NAME = VARIABLE_VALUE
    """
    env_var = f'{var_group}_{var_name}'
    return os.environ.get(env_var.lower()) or os.environ.get(env_var.upper())

def get_aws_creds() -> dict:
    '''
    Gets local aws env variables for call to PS
    '''
    return {'region_name' : get_local_env_var('aws', 'region_name'),
            'aws_access_key_id' : get_local_env_var('aws', 'access_key_id'),
            'aws_secret_access_key' : get_local_env_var('aws', 'secret_access_key')}

def get_sys_env_var() -> str:
    '''
    Gets local environment name value
    '''
    return get_local_env_var('environment', 'name')

def get_ps_env_var(var_group: str, var_name: str, local_creds: bool = False, prefix: str = None) -> (str, Exception):
    '''
    Gets environment variable from Parameter Store if that fails, it will try to find locally.

    Can specify if you want to use local AWS credentials or default to role-based credentials.

    Ensure the following environment variable is defined locally: SYSTEMS_ENVIRONMENT

    If using local AWS credentials, ensure these evnironment variables are also defined locally: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION_NAME

    Returns tuple of: (environment variable value, Exception object)
    '''
    try:
        store = create_store(prefix, local_creds)
        return (store[var_group.lower()][var_name.lower()], None)
    except Exception as err:
        return (get_local_env_var(var_group, var_name), err)

def set_ps_env_var(var_group: str, var_name: str, var_val: str, local_creds: bool = None, prefix: str = None) -> (bool, Exception):
    '''
    Sets variable value in Paramter Store. Supply variable group, name, and new variable value

    Returns (True, None) for success and (False, Exception) for failure
    '''
    try:
        store = create_store(prefix, local_creds)
        store[var_group.lower()][var_name.lower()] = var_val
        return (True, None)
    except Exception as err:
        return (False, err)

def create_client(local_creds: bool):
    '''
    Creates boto3 SSM client. If credentials are provided, the client will connect with credentials.
    '''
    if local_creds:
        creds = get_aws_creds()
        return boto3.client('ssm',
                            aws_access_key_id=creds['aws_access_key_id'],
                            aws_secret_access_key=creds['aws_secret_access_key'],
                            region_name=creds['region_name'])
    return boto3.client('ssm', region_name=get_local_env_var('AWS', 'REGION'))

def create_store(prefix, local_creds):
    '''
    Creates SSMParameterStore object
    '''
    if not prefix:
        prefix = f"/{get_sys_env_var().capitalize()}/Tpds/"
    ssm_client = create_client(local_creds)
    return SSMParameterStore(prefix=prefix, ssm_client=ssm_client)


class SSMParameterStore(object):
    """
    Provide a dictionary-like interface to access AWS SSM Parameter Store

    References:
        https://nqbao.medium.com/how-to-use-aws-ssm-parameter-store-easily-in-python-94fda04fea84
        https://gist.github.com/nqbao/9a9c22298a76584249501b74410b8475
    """
    def __init__(self, prefix=None, ssm_client=None, ttl=None):
        self._prefix = (prefix or '').rstrip('/') + '/'
        self._client = ssm_client
        self._keys = None
        self._substores = {}
        self._ttl = ttl

    def get(self, name, **kwargs):
        assert name, 'Name can not be empty'
        if self._keys is None:
            self.refresh()

        abs_key = "%s%s" % (self._prefix, name)
        if name not in self._keys:
            if 'default' in kwargs:
                return kwargs['default']

            raise KeyError(name)
        elif self._keys[name]['type'] == 'prefix':
            if abs_key not in self._substores:
                store = self.__class__(prefix=abs_key, ssm_client=self._client, ttl=self._ttl)
                store._keys = self._keys[name]['children']
                self._substores[abs_key] = store

            return self._substores[abs_key]
        else:
            return self._get_value(name, abs_key)

    def set(self, key, val):
        if self._keys is None:
            self.refresh()

        if key not in self._keys:
            raise KeyError(key)

        abs_key = f'{self._prefix}{key}'

        self._client.put_parameter(Name=abs_key, Value=val, Overwrite=True)


    def refresh(self):
        self._keys = {}
        self._substores = {}

        paginator = self._client.get_paginator('describe_parameters')
        pager = paginator.paginate(
            ParameterFilters=[
                dict(Key="Path", Option="Recursive", Values=[self._prefix])
            ]
        )

        for page in pager:
            for p in page['Parameters']:
                paths = p['Name'][len(self._prefix):].split('/')
                self._update_keys(self._keys, paths)

    @classmethod
    def _update_keys(cls, keys, paths):
        name = paths[0]

        # this is a prefix
        if len(paths) > 1:
            if name not in keys:
                keys[name] = {'type': 'prefix', 'children': {}}

            cls._update_keys(keys[name]['children'], paths[1:])
        else:
            keys[name] = {'type': 'parameter', 'expire': None}

    def keys(self):
        if self._keys is None:
            self.refresh()

        return self._keys.keys()

    def _get_value(self, name, abs_key):
        entry = self._keys[name]

        # simple ttl
        if self._ttl == False or (entry['expire'] and entry['expire'] <= datetime.datetime.now()):
            entry.pop('value', None)

        if 'value' not in entry:
            parameter = self._client.get_parameter(Name=abs_key, WithDecryption=True)['Parameter']
            value = parameter['Value']
            if 'Type' not in parameter: # This line exists to assist in unit testing but shouldn't need use in production.
                parameter['Type'] = 'String'
            if parameter['Type'] == 'StringList':
                value = value.split(',')

            entry['value'] = value

            if self._ttl:
                entry['expire'] = datetime.datetime.now() + datetime.timedelta(seconds=self._ttl)
            else:
                entry['expire'] = None

        return entry['value']

    def __contains__(self, name):
        try:
            self.get(name)
            return True
        except:
            return False

    def __getitem__(self, name):
        return self.get(name)

    def __setitem__(self, key, val):
        return self.set(key, val)

    def __delitem__(self, name):
        raise NotImplementedError()

    def __repr__(self):
        return 'ParameterStore[%s]' % self._prefix
