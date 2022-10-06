# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['free_ssl_proxies']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'free-ssl-proxies',
    'version': '0.1.1',
    'description': 'A minimal python library that scrapes ssl proxies from https://sslproxies.org.',
    'long_description': '## Description\n\n`free-ssl-proxies` is a lightweight Python library that scrapes `ssl` proxies from `https://sslproxies.org/`, \nand provides some convenient objects and caching methods for working with the retrieved proxies. This library \nrequires no external Python dependencies to work.\n\n\n## Usage\n\n### Installation\n\n```commandline\npip3 install .\n```\n\n### Importing\n\n```python3\nfrom free_ssl_proxies import proxy_list as pl\n```\n\n### First time retrieval\n\nYou can iterate through all the proxies currently available on `sslproxies.org` with the following code:\n- `profile`: If True, we will attempt to connect through each proxy\n- `timeout`: If the timeout is exceeded the proxy object will contain `None` for the `avg_request_time` (relatively slow proxy)\n\n```python3\nproxies = pl.ProxyList.from_ssl_proxies_org(profile=True, timeout=1)\n\nfor proxy in proxies:\n    print(proxy.ip_address, proxy.port, proxy.cc, proxy.country, proxy.google, proxy.avg_request_time)\n```\n\n\n### Caching\n`sslproxies.org` refreshes their list every 10 minutes, so it doesn\'t make sense to constantly hammer their page with \nrequests. This package offers a simple caching mechanism that can be used like so:\n\n```python3\nproxies = pl.ProxyList.from_ssl_proxies_org(profile=True, timeout=1)\n\npl.write_proxy_list_to_cache(proxies)\n```\n\nTo access the cache later:\n\n```python3\nproxies = pl.ProxyList.from_cache()\n```\n\n\n### Access\n\n#### By country\n\nYou can use either the `country` name `cc` to find proxies.\n\n```python3\nfor us_proxy in proxies.get_by_country("us"):\n    print(us_proxy)\n```\n\n#### Fastest\n\nYou can get a sorted list of the fastest proxies if profiling has been done.\n\n```python3\nfor fast_proxy in proxies.get_fastest():\n    print(fast_proxy)\n```\n\n\n#### Random\n\nYou can get a random proxy selected from the fastest proxies if profiling has been done. If profiling has not been done\nthen we will pick from the entire pool of available proxies.\n\n```\nproxy = proxies.random()\n```',
    'author': 'Jamin Becker',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
