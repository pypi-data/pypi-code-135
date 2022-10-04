# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydantic_remote_config',
 'pydantic_remote_config.aws',
 'pydantic_remote_config.config',
 'pydantic_remote_config.enum']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.0.0,<2.0.0']

extras_require = \
{'aws': ['boto3>=1.0.0,<2.0.0']}

setup_kwargs = {
    'name': 'pydantic-remote-config',
    'version': '0.1.0',
    'description': 'Utility to fetch configuration values from remote sources that integrates with Pydantic settings models',
    'long_description': '# pydantic-remote-config\n\nLibrary that extends [pydantic\'s BaseSettings model](https://pydantic-docs.helpmanual.io/usage/settings/)\nand integrates with various remote sources to fetch application secrets & configuration.\nSupported remote sources include:\n* [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)\n* [AWS SSM Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)\n\n## Installation\nFor AWS services support:\n```bash\n$ pip install pydantic-remote-config[aws]\n```\n\n## Usage\n\n### Simple Example\n```python\nfrom pydantic_remote_config.aws import SecretsManager, SSMParam\nfrom pydantic_remote_config import RemoteSettings\n\nclass Settings(RemoteSettings):\n    param_1: str = SSMParam("/foo/bar/param")\n    param_2: int = SSMParam("/foo/bar/num_param")\n    secret: str = SecretsManager("test-secret")\n\nsettings = Settings()\nprint(settings)\n#> Settings(param_1="remote param", param_2=101, secret="super secret code")\n```\n\n### Templating strings\n\nStrings can be templated using attributes that have been defined in the class and have\ncorresponding environment variables set. This is useful in cases where a value is\nstored under a different path depending on the environment.\n\nIn this example if the environment variable `ENV` is set to `dev`, the\n`/app-name/dev/db_password` value will be retrieved.\n\n```python\nfrom pydantic_remote_config.aws import SSMParam\nfrom pydantic_remote_config import RemoteSettings\n\n\nclass Settings(RemoteSettings):\n    env: str\n\n    db_password: str = SSMParam("/app-name/{env}/db_password")\n```\n\n\n\n### Accessing Nested Values\n\nKey value pairs can be accessed by specifying the `key` arg. The example below\nillustrates an example where only the database password is retrieved from a json\nobject.\n\nSSM Param value for `/app-name/database_info`:\n```json\n{\n  "host": "foo.rds.aws.com",\n  "port": 5432,\n  "username": "db_user",\n  "password": "super-secret-password"\n}\n```\n\nRemote config implementation:\n```python\nfrom pydantic_remote_config.aws import SSMParam\nfrom pydantic_remote_config import RemoteSettings\n\n\nclass Settings(RemoteSettings):\n    db_password: str = SSMParam("/app-name/database_info", key="password")\n```\n\n### Class Configuration\n\nEach remote source or class of sources has its own configuration class that\ncan be set.\n\n#### AWS\n\nThe AWS config class supports specifying an aws region to fetch configuration\nfrom. Note that this will override the default aws region configured on the\nmachine or boto3.\n\n```python\nfrom pydantic_remote_config.aws import SecretsManager, SSMParam\nfrom pydantic_remote_config import RemoteSettings\nfrom pydantic_remote_config.config import AWSConfig\n\n\nclass Settings(RemoteSettings):\n    env: str\n    param: str = SSMParam("/foo/bar")\n    secret: dict = SecretsManager("test-secret")\n\n    class Config:\n        aws = AWSConfig(region=\'us-west-2\')\n```\n\n### MyPy Support\nThis library works with mypy!\n\n## Roadmap\nThis library aims to be the one stop shop for python applications that need\nto fetch configuration from remote sources regardless of source. Services\nthat are supported or on the roadmap are listed below.\n- [x] AWS Secrets Manager\n- [x] AWS SSM Parameter Store\n- [ ] Hashicorp Vault\n- [ ] Hashicorp Consul\n- [ ] Azure Key Vault\n\nIf you\'d like to add a service to our roadmap, please open an issue and we\'ll\nbe happy to get it added.\n\n## Contributing\nWIP\n\n### Development Dependencies\n* `asdf` for managing multiple python version\n* `pre-commit` for formatting & linting code before commits\n* `poetry` managing dependencies & publishing the package\n\n### Installing Development Dependencies\n',
    'author': 'nplutt',
    'author_email': 'nplutt@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nplutt/pydantic-remote-config',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
