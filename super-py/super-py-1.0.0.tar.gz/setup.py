# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['super_py']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'super-py',
    'version': '1.0.0',
    'description': 'Features that Python should have in the standard library',
    'long_description': '# SuperPy\n\n[![Downloads](https://pepy.tech/badge/super-py)](https://pepy.tech/project/super-py)\n[![Downloads](https://pepy.tech/badge/super-py/month)](https://pepy.tech/project/super-py)\n[![Downloads](https://pepy.tech/badge/super-py/week)](https://pepy.tech/project/super-py)\n\nThere are 5 sub modules:\n- sp.logging\n- sp.testing\n- sp.concurrency\n- sp.dicts\n- sp.disk\n- sp.string\n\n\n## sp.logging\n\nSuperPy\'s logging system is a simple abstraction from the standard library logging module.\nIt also provides some nice extra functionalities.\nHere are some examples:\n\n### Logging messages\n\n``` python\nimport super_py as sp\n\nlog = sp.logging.Logger("info",\n    ts_color="bright_green",\n    terminal=True,\n    files=["info.log", "combined.log"],\n)\n\nlog("This is a simple log!")\n```\n\nThis will write the following log line to the terminal, and the files `info.log` and `comnined.log`:\n```\n[info        ] 2022-10-04 15:53:09            This is a simple log!\n```\nwhere the name and timestamp will be colored in `bright_green`.\n\n### Logging function benchmarks\n\nYou can also use the provided decorator to log benchmarks of your functions:\n\n``` python\nimport super_py as sp\n\nlog = sp.logging.Logger("benchmark",\n    ts_color="bright_green",\n    terminal=True,\n)\n\n@log.benchmark(with_args=[0])\ndef wait(seconds):\n    time.sleep(seconds)\n\nfor i in range(10):\n    wait(i / 10)\n```\n\nThis will write the following log lines:\n```\n[benchmark   ] 2022-10-04 16:03:39     0.0ms  wait((0.0))\n[benchmark   ] 2022-10-04 16:03:39   105.1ms  wait((0.1))\n[benchmark   ] 2022-10-04 16:03:39   205.1ms  wait((0.2))\n[benchmark   ] 2022-10-04 16:03:40   308.3ms  wait((0.3))\n[benchmark   ] 2022-10-04 16:03:40   403.5ms  wait((0.4))\n[benchmark   ] 2022-10-04 16:03:40   505.1ms  wait((0.5))\n[benchmark   ] 2022-10-04 16:03:41   605.1ms  wait((0.6))\n[benchmark   ] 2022-10-04 16:03:42   705.1ms  wait((0.7))\n[benchmark   ] 2022-10-04 16:03:43   804.1ms  wait((0.8))\n[benchmark   ] 2022-10-04 16:03:43   903.3ms  wait((0.9))\n```\n\nYou can use benchmark without calling the decorator, it will still work:\n``` python\n@log.benchmark\ndef wait(seconds):\n    time.sleep(seconds)\n```\n\nThe benchmark decorator takes the following keyword arguments:\n- `with_args: list[int]`: The list of indices of function arguments which should be logged.\n- `with_kwargs: list[str]`: The list of keyword argument names of the function which should be logged.\n',
    'author': 'Marcel Kröker',
    'author_email': 'kroeker.marcel@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mkrd/SuperPy',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
