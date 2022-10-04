# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['th2_cli',
 'th2_cli.cli',
 'th2_cli.cli.mgr',
 'th2_cli.templates',
 'th2_cli.templates.install',
 'th2_cli.templates.install.values',
 'th2_cli.utils',
 'th2_cli.utils.helm',
 'th2_cli.utils.install_config',
 'th2_cli.utils.install_config.infra_mgr']

package_data = \
{'': ['*']}

install_requires = \
['avionix>=0.4.5,<0.5.0',
 'cassandra-driver>=3.25.0,<4.0.0',
 'colorama>=0.4.5,<0.5.0',
 'cryptography>=37.0.4,<38.0.0',
 'dataclass-wizard[yaml]>=0.22.1,<0.23.0',
 'deepmerge>=1.0.1,<2.0.0',
 'fire>=0.4.0,<0.5.0',
 'halo>=0.0.31,<0.0.32',
 'kubernetes>=24.2.0,<25.0.0',
 'requests>=2.28.1,<3.0.0',
 'simple-term-menu>=1.5.0,<2.0.0',
 'urllib3>=1.26.12,<2.0.0']

entry_points = \
{'console_scripts': ['th2 = th2_cli:cli']}

setup_kwargs = {
    'name': 'th2-cli',
    'version': '1.7.2',
    'description': '👨\u200d💻 CLI for managing th2 infrastructure in Kubernetes cluster',
    'long_description': 'Works with th2 1.7.3\n\n## Using\n\nInstall:\n\n```commandline\npip install th2-cli\n```\n\n### Install th2\n\nIf you already have configurations in `th2-cli-install-config.yaml` or `secrets.yaml`, it will be convenient to run process from the directory with these files.\nIn other case CLI will create these config files during installation.\n\n```commandline\nth2 install\n```\n\n### Delete th2\n\n```commandline\nth2 delete\n```\n\n### Update th2\n\n```commandline\nth2 delete\n```\n\nWait until all required namespaces are terminated.\n\n```commandline\nth2 install\n```\n\n### Get th2 status\n\nDisplay information about all th2-related namespaces in Kubernetes.\n\n```commandline\nth2 status\n```\n\n### infra-mgr\n\nDisplay status of infra-mgr pod:\n\n```commandline\nth2 mgr status\n```\n\nDisplay last logs of infra-mgr pod:\n\n```commandline\nth2 mgr logs\n```\n\n## Configurations templates\n\n### th2-cli-install-config.yaml\n\n```yaml\ncassandra:\n  datacenter: datacenter1\n  host: host.minikube.internal\ninfra-mgr:\n  git:\n    http-auth-password: pat_token\n    http-auth-username: pat_token\n    repository: https://github.com/schema/repository\nkubernetes:\n  host: 192.168.49.2\n  pvs-node: minikube\n```\n\n### secrets.yaml\n\n```yaml\n# required only for images from a private registry, will be attached as the first PullSecret to deployments\n#productRegistry:\n#  username: user\n#  password: password\n#  name: private-registry-1.example.com # core components registry\n\n# required only for images from a private registry, will be attached as the second PullSecret to deployments\n#solutionRegistry:\n#  username: user\n#  password: password\n#  name: private-registry-2.example.com # components registry\n\n# required only for images from a private registry, will be attached as the third PullSecret to deployments\n#proprietaryRegistry:\n#  username: user\n#  password: password\n#  name: private-registry-3.example.com # components registry\n\ncassandra:\n# set credentials for the existing Cassandra cluster\n  dbUser:\n    user: cassandra\n    password: cassandra\n\nrabbitmq:\n# set admin user credentials, it will be created during deployment\n  rabbitmqUsername: th2\n  rabbitmqPassword: rab-pass\n  # must be random string\n  rabbitmqErlangCookie: cookie\n```\n\n## Development\n\n```\npoetry install\npoetry shell\n```\n\n```commandline\nth2 install\n```',
    'author': 'Nikolay Dorofeev',
    'author_email': 'dorich2000@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/d0rich/th2-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
