# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['investiny']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0']

extras_require = \
{'docs': ['mkdocs>=1.4.0,<2.0.0', 'mkdocs-material>=8.5.4,<9.0.0']}

setup_kwargs = {
    'name': 'investiny',
    'version': '0.2.0',
    'description': '🤏🏻 `investpy` but made tiny.',
    'long_description': '# 🤏🏻 `investpy` but made tiny\n\nSuuuuuuuper simple and tiny `investpy` replacement while I try to fix it! Here I\'ll try\nto add more or less the same functionality that was developed for `investpy` while keeping this\npackage tiny and up-to-date, as some solutions just work temporarily.\n\nEveryone using `investiny` please go thank @ramakrishnamekala129 for proposing this solution\nthat seems to be stable and working fine so far (fingers crossed!). Also take the chance to explore\nany other solution proposed by the `investpy` users at https://github.com/alvarobartt/investpy/issues.\n\nI\'m currently waiting to have a conversation with Investing.com so as to see whether we can get\nto some sort of an agreement in order to keep `investpy` alive.\n\nIn the meantime you can follow me at https://twitter.com/alvarobartt as I post updates there, and\nI highly appreciate your feedback.\n\n@adelRosal, an `investpy` user created a change.org site so as to show some support, so please sign\nthe petition as it may be useful towards the continuity of `investpy` at https://www.change.org/p/support-from-investing-com-for-the-continuity-of-investpy-library\n\nFinally, remember that `investiny` is super simple and tiny and shouldn\'t be considered reliable, it\'s\nworking fine so far, but it may be discontinued, so please use it carefully.\n\n---\n\n## 🛠️ Installation\n\n🤏🏻 `investiny` requires Python 3.9+ and can be installed with `pip` as it follows:\n\n`pip install investiny`\n\n---\n\n## 💻 Usage\n\nRetrieve historical data from Investing.com using the Investing.com ID of the asset\nthat you want to retrieve the data from.\n\n```python\nfrom investiny import historical_data\n\ndata = historical_data(investing_id=6408, from_date="09/01/2022", to_date="10/01/2022") # Returns AAPL historical data as JSON (without date)\n```\n\nAnd, also retrive recent data (no need to specify dates, it\'s just the last 30 days) from\nInvesting.com using the Investing.com ID of the asset that you want to retrieve the data from.\n\n```python\nfrom investiny import recent_data\n\ndata = recent_data(investing_id=6408) # Returns AAPL recent data as JSON (without date)\n```\n\n---\n\n## 🔮 TODOs\n\n- [ ] Add Search API as also available https://tvc4.investing.com/.../search?limit=30&query=USD&type=&exchange= (thanks again @ramakrishnamekala129) (also requested in [#4](https://github.com/alvarobartt/investiny/issues/4))\n- [ ] Include date formatted as %m/%d/%Y in output JSON\n- [ ] Add simple scraper for Investing.com IDs?\n- [ ] Add error basic error handling\n- [ ] Should `historical_data` work without `from_date` and `to_date` inheriting `recent_data` behavior?\n- [ ] Even though it\'s working fine so far and it seems stable, should we run stress tests?\n- [ ] Ideally we should keep the lenght of `investiny` code to less than 200 lines total?\n- [ ] Add more issues so that community can contribute (also Hacktoberfest 2022 is starting?)\n',
    'author': 'Alvaro Bartolome',
    'author_email': 'alvarobartt@yahoo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alvarobartt/investiny',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
