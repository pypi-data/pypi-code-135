# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pdc_auth', 'pdc_auth.exceptions', 'pdc_auth.models']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pdc-auth',
    'version': '0.1.1',
    'description': 'pdc authentication manager',
    'long_description': '## PDC AUTH\n\nPDC Authentication Manager\n\n## Installation\nInstallation: To install from PyPI use:\n\n`$ python -m pip install pdc-auth`\n\nAfter installation, import with something like:\n\n```python\nimport pdc_auth as pdca\n```\n\n## Configure Endpoint\nBefore using authenticator configure the endpoint first. Enpoint by default has url "http://localhost:4000" and path "/v2/login". If method `get_host() `called will return "http://localhost:4000/v2/login". Configure to get a custom host.\n\n```python\nfrom pdc_auth.endpoint import EndpointConfig, configure_endpoint\n\n\nurl = "www.myendpoint.com"\npath = "/v1/auth"\nconfigure_endpoint(url, path)\n\nendpoint = EndpointConfig()\nendpoint.get_host() # www.myendpoint.com/v1/auth\n```\n\n## Create Config File\nBy default the configuration file path is "data/config.json". Path can be customized as desired by adding parameters to the authenticator later. However the configuration file must be `json` and include fields like below.\n\n```json\n{\n    "lisensi": {\n        "email": "myemail@custom.com",\n        "pwd": "secret"\n    }\n}\n```\n\n## Authenticator\nAuthenticator is used to check the login to the endpoint according to the previous configuration. With the appropriate email and password listed in the configuration. When the `login()` function is called checking for an error in the login returns an error. If the login is successful it will return the value `True`.\n\n```python\nfrom pdc_auth.authenticator import Authenticator\nfrom pdc_auth.exceptions.login_provider_exc import LoginProviderFailedException\n\nconfig_fname="config/lisensi.json"\nauthenticator = Authenticator(config_fname=config_fname) # config_fname by default is: "data/config.json"\n\ntry:\n    authenticator.login() \nexcept LoginProviderFailedException as e:\n    pass\n```\n\n## Custom Login Provider\nCustomizing the provider on the login authenticator.\n```python\nfrom pdc_auth.authenticator import Authenticator\nfrom pdc_auth.exceptions.login_provider_exc import LoginProviderFailedException\nfrom pdc_auth.login_provider import LoginProvider\n\nprovider = LoginProvider()\nauthenticator = Authenticator(provider=provider)\n\ntry:\n    authenticator.login() \nexcept LoginProviderFailedException as e:\n    pass\n```\n\nSome of the data that can be customized on the provider are as follows:\n\n1. __Custom Bot__\n```python\nfrom pdc_auth.login_provider import LoginProvider\n\nbot_id = 10\nversion = \'3.0.0\'\nprovider = LoginProvider(bot_id=bot_id, version=version)\n```\nor\n```python\nfrom pdc_auth.login_provider import LoginProvider\n\nbot_id = 10\nversion = \'3.0.0\'\nlatest_version = \'3.0.18\'\nprovider = LoginProvider()\nprovider.update_bot(bot_id=bot_id, version=version, latest_version=latest_version)\n```\n\n2. __Custom Headers__\n```python\nfrom pdc_auth.login_provider import LoginProvider\n\ncustom_headers = { "X-Secret-Key": "secret" }\nprovider = LoginProvider()\nprovider.update_headers(custom_headers)\n```',
    'author': 'hfrada',
    'author_email': 'madefrada@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
