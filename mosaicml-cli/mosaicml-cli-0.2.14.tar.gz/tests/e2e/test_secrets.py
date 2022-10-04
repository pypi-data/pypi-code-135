import datetime as dt
from concurrent.futures import TimeoutError
from typing import List

import pytest
import pytz

import mcli.api.runs as runs_api
import mcli.api.secrets as api
from mcli.api.exceptions import MAPIException
from mcli.models.mcli_secret import Secret, SecretType
from mcli.models.run_config import RunConfig
from mcli.objects.secrets.docker_registry import MCLIDockerRegistrySecret
from mcli.objects.secrets.env_var import MCLIEnvVarSecret
from mcli.objects.secrets.mounted import MCLIMountedSecret
from mcli.objects.secrets.s3 import MCLIS3Secret
from mcli.objects.secrets.ssh import MCLIGitSSHSecret, MCLISFTPSSHSecret, MCLISSHSecret
from mcli.utils.utils_run_status import RunStatus
from tests.e2e.test_runs import wait_for_run_status
from tests.mapi_config import mapi_config

TEST_SECRETS: List[Secret] = [
    MCLIDockerRegistrySecret(name='test-docker',
                             secret_type=SecretType.docker_registry,
                             username='u',
                             password='p',
                             server='s'),
    MCLIEnvVarSecret(name='test-env', secret_type=SecretType.environment, value='foo', key='bar'),
    MCLIGitSSHSecret(name='test-git', secret_type=SecretType.git, value='v', mount_path='mp'),
    MCLIMountedSecret(name='test-mount', secret_type=SecretType.mounted, value='v', mount_path='mp'),
    MCLIS3Secret(name='test-s3', secret_type=SecretType.s3, mount_directory='md', credentials='creds', config='confg'),
    MCLISFTPSSHSecret(name='test-sftp', secret_type=SecretType.sftp, value='v', mount_path='mp'),
    MCLISSHSecret(name='test-ssh', secret_type=SecretType.ssh, value='v', mount_path='mp'),
]


def test_test_secrets():
    """Silly test that confirms all enumerated SecretTypes are tested in this script
    """
    excluded_secret_types = {SecretType.generic}
    known_secret_types = {s.name for s in SecretType if s not in excluded_secret_types}

    test_secret_types = {s.secret_type.value for s in TEST_SECRETS}

    diff = known_secret_types - test_secret_types
    assert not diff


class TestSecrets:

    def teardown_function(self):
        api.delete_secrets()

        runs = runs_api.get_runs()
        runs_api.delete_runs(runs)

    @mapi_config
    @pytest.mark.parametrize('secret', TEST_SECRETS)
    def test_secret_api(self, secret: Secret):
        """Tests all secret types - create, get, and delete
        """
        # Create it
        res = api.create_secret(secret)
        assert res.name == secret.name
        assert res.secret_type == secret.secret_type

        # Get it
        res = api.get_secrets([secret], secret_types=[secret.secret_type])
        assert res
        assert len(res) == 1
        assert res[0].name == secret.name

        # Delete it
        res = api.delete_secrets([secret])
        assert res
        assert len(res) == 1
        assert res[0].name == secret.name

    @mapi_config
    def test_secret_env_var_in_run(self):
        run_config = RunConfig.from_dict({
            'name': 'echo-hello-world-env',
            'cluster': 'microk8s',
            'gpu_type': 'None',
            'image': 'bash',
            'command': 'sleep 2; echo Hello $TEST_ENV_VAR!'
        })

        secret = MCLIEnvVarSecret(
            name='test-echo-this',
            secret_type=SecretType.environment,
            key='TEST_ENV_VAR',
            value='world 🌎',
        )

        api.create_secret(secret)
        run = runs_api.create_run(run_config)

        max_time = dt.datetime.now(tz=pytz.UTC) + dt.timedelta(seconds=120)
        wait_for_run_status(run, RunStatus.COMPLETED, max_time)

        logs = runs_api.follow_run_logs(run)
        for log in logs:
            assert log == 'Hello world 🌎!'

    @mapi_config
    def test_secret_mounted(self):
        mounted_secret = MCLIMountedSecret(
            name='mounted-echo',
            secret_type=SecretType.mounted,
            value='very-secret-value',
        )
        api.create_secret(mounted_secret)

        run_config = RunConfig.from_dict({
            'name': 'echo-mounted-file',
            'cluster': 'microk8s',
            'gpu_type': 'None',
            'image': 'bash',
            'command': "sleep 2; cat '/secrets/mounted-echo/mounted-echo'"
        })
        run = runs_api.create_run(run_config)

        max_time = dt.datetime.now(tz=pytz.UTC) + dt.timedelta(seconds=120)
        wait_for_run_status(run, RunStatus.COMPLETED, max_time)

        logs = runs_api.follow_run_logs(run)
        for log in logs:
            assert log == 'very-secret-value'

    @mapi_config
    def test_secret_duplicate(self):
        secret = MCLIS3Secret(
            name='test-s3-dup',
            secret_type=SecretType.s3,
            mount_directory='md',
            credentials='creds',
            config='confg',
        )
        secret1 = api.create_secret(secret)

        with pytest.raises(MAPIException):
            api.create_secret(secret)

        secret.name += '2'
        secret2 = api.create_secret(secret)

        res = api.delete_secrets([secret1, secret2])
        assert res
        assert len(res) == 2

    @mapi_config
    def test_get_secrets_timeout(self):
        with pytest.raises(TimeoutError):
            _ = api.get_secrets(timeout=0)

    @mapi_config
    def test_create_secrets_timeout(self):
        secret = MCLIEnvVarSecret(name='test-timeout', secret_type=SecretType.environment, value='foo', key='bar')
        with pytest.raises(TimeoutError):
            _ = api.create_secret(secret, timeout=0)

    @mapi_config
    def test_delete_secrets_timeout(self):
        with pytest.raises(TimeoutError):
            _ = api.delete_secrets(timeout=0)
