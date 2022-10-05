
import json
import os.path
import boto3
import string
import botocore.exceptions
import logging
import filelock

logger = logging.getLogger(__name__)

PROCESSING_TOKENS_TEMPLATE = "/global/processing/tokens/{environment}/{username}"

__all__ = ['SSMStore', 'FileStore']


class SSMStore:

    def __init__(self, environment, username):
        self.environment = environment
        self.username = self.clean_username(username)

    @staticmethod
    def clean_username(username):
        return ''.join([c if c in string.ascii_letters + string.digits else '_' for c in username])

    def get_tokens(self):
        ssm = boto3.client('ssm')
        parameter = ssm.get_parameter(
            Name=PROCESSING_TOKENS_TEMPLATE.format(environment=self.environment, username=self.username),
            WithDecryption=True
        )
        return json.loads(parameter['Parameter']['Value'])

    def store_tokens(self, tokens):
        try:
            ssm = boto3.client('ssm')
            ssm.put_parameter(
                Name=PROCESSING_TOKENS_TEMPLATE.format(environment=self.environment, username=self.username),
                Value=json.dumps(tokens),
                Type='SecureString',
                Overwrite=True
            )
        except botocore.exceptions.ClientError as e:
            # Boto3 classifies all AWS service errors and exceptions as ClientError exceptions
            logger.warning(f"Failed to store token to the parameter store with exception {e.response['Error']['Code']}")


class FileStore:

    def __init__(self, environment, username, path=None):
        self.environment = environment
        self.username = username
        self.token_path = path if path is not None else os.path.expanduser(f'~/.agmri.{environment}.tokens')
        self.token_lock_path = self.token_path + '.lock'

    def get_tokens(self):
        with filelock.FileLock(self.token_lock_path):
            with open(self.token_path, 'r') as fp:
                return json.load(fp)

    def store_tokens(self, tokens):
        with filelock.FileLock(self.token_lock_path):
            with open(self.token_path, 'w') as fp:
                json.dump(tokens, fp)

