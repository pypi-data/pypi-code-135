# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['manageritm',
 'manageritm.client',
 'manageritm.server',
 'manageritm.server.scripts']

package_data = \
{'': ['*']}

install_requires = \
['Flask',
 'mitmproxy>=8.0.0,<9.0.0',
 'pytest-mock>=3.7.0,<4.0.0',
 'requests-mock>=1.9.3,<2.0.0',
 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['manageritm = manageritm.app:cli']}

setup_kwargs = {
    'name': 'manageritm',
    'version': '0.1.0',
    'description': 'Manage processes via an HTTP based API',
    'long_description': '# manageritm\n\nManage a mitmproxy service on another system over a RESTful API\n\n## Getting Started\n\n1. Install manageritm.\n   ```python\n   pip install manageritm gunicorn\n   ```\n2. Start manageritm server on port 8000.\n   ```python\n   gunicorn --bind 0.0.0.0:8000 --workers 1 --log-level debug "manageritm.app:main()"\n   ```\n3. In Python, create a client, start the mitmproxy service, stop the mitmproxy service\n   ```python\n\n   import manageritm\n\n   manageritm_addr = "localhost"\n   manageritm_port = "8000"\n\n   # create a manageritm client\n   mc = manageritm.client.ManagerITMClient(f\'http://{manageritm_addr}:{manageritm_port}\')\n   proxy_details = mc.client()\n\n   print(f"proxy port: {proxy_details[\'port\']}")\n   print(f"proxy webport: {proxy_details[\'webport\']}")\n\n   # start a proxy server\n   mc.proxy_start()\n\n   # set your application to use the proxy\n   #  host: "localhost"\n   #  port: f"{proxy_details[\'port\']}"\n\n   # do some work...\n\n   # stop the proxy server\n   mc.proxy_stop()\n   ```\n\n## Local Development\n\n1. Check out this repository\n2. Create a virtual environment\n   ```bash\n   make pyenv\n   ```\n3. Install Python dependencies\n   ```bash\n   make install\n   ```\n4. Start the server\n   ```bash\n   make server\n   ```\n5. Start a client, in a Python interpreter:\n   ```python\n\n   import manageritm\n\n   manageritm_addr = "localhost"\n   manageritm_port = "8000"\n\n   # create a manageritm client\n   mc = manageritm.client.ManagerITMClient(f\'http://{manageritm_addr}:{manageritm_port}\')\n   proxy_details = mc.client()\n\n   print(f"proxy port: {proxy_details[\'port\']}")\n   print(f"proxy webport: {proxy_details[\'webport\']}")\n\n   # start a proxy server\n   mc.proxy_start()\n   ```\n6. Navigate a web browser to `http://localhost:<proxy webport>` to watch the traffic\n7. Configure a web browser to use the proxy port.\n8. Stop the client\n   ```python\n   # stop the proxy server\n   mc.proxy_stop()\n   ```\n\n\n### Helpful Commands\n\nTo build a package for the development version:\n```python\nmake all\n```\n\nTo install a copy into your local python virtualenv\n```python\nmake install\n```\n\nTo run the test cases:\n```python\nmake test\n```\n\nTo run the development version of the service:\n```python\nmake run\n```\n',
    'author': 'dskard',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://github.com/dskard/manageritm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
