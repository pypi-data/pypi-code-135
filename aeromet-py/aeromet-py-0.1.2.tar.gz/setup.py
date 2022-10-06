# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aeromet_py',
 'aeromet_py.database',
 'aeromet_py.reports',
 'aeromet_py.reports.models',
 'aeromet_py.reports.models.base',
 'aeromet_py.reports.models.metar',
 'aeromet_py.reports.models.taf',
 'aeromet_py.utils']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.2.0,<5.0.0']

setup_kwargs = {
    'name': 'aeromet-py',
    'version': '0.1.2',
    'description': 'Python library to parse meteorological information of aeronautical stations.',
    'long_description': '# Aeromet-Py\n\n[![Contributors][contributors-shield]][contributors-url]\n[![Forks][forks-shield]][forks-url]\n[![Stargazers][stars-shield]][stars-url]\n[![Issues][issues-shield]][issues-url]\n[![codecov][coverage-shield]][coverage-url]\n[![MIT License][license-shield]][license-url]\n\n[coverage-shield]: https://codecov.io/gh/TAF-Verification/aeromet-py/branch/main/graph/badge.svg?token=1MUT17FQZY\n[coverage-url]: https://codecov.io/gh/TAF-Verification/aeromet-py\n[contributors-shield]: https://img.shields.io/github/contributors/TAF-Verification/aeromet-py.svg\n[contributors-url]: https://github.com/TAF-Verification/aeromet-py/graphs/contributors\n[forks-shield]: https://img.shields.io/github/forks/TAF-Verification/aeromet-py.svg\n[forks-url]: https://github.com/TAF-Verification/aeromet-py/network/members\n[stars-shield]: https://img.shields.io/github/stars/TAF-Verification/aeromet-py.svg\n[stars-url]: https://github.com/TAF-Verification/aeromet-py/stargazers\n[issues-shield]: https://img.shields.io/github/issues/TAF-Verification/aeromet-py.svg\n[issues-url]: https://github.com/TAF-Verification/aeromet-py/issues\n[license-shield]: https://img.shields.io/github/license/TAF-Verification/aeromet-py.svg\n[license-url]: https://github.com/TAF-Verification/aeromet-py/blob/master/LICENSE\n\nInspired from python-metar, a library writed in Python language to parse Meteorological Aviation Weather Reports (METAR and SPECI).\n\nThis library will parse meteorological information of aeronautical land stations.\nSupported report types:\n* METAR\n* SPECI\n* TAF\n\n## Current METAR reports\n\nThe current report for a station is available at the URL\n\n```\nhttp://tgftp.nws.noaa.gov/data/observations/metar/stations/<station>.TXT\n```\n\nwhere `station` is the ICAO station code of the airport. This is a four-letter code.\nFor all stations at any cycle (i.e., hour) in the last  hours the reports are available\nat the URL\n\n```\nhttp://tgftp.nws.noaa.gov/data/observations/metar/cycles/<cycle>Z.TXT\n```\n\nwhere `cycle` is the 2-digit cycle number (`00` to `23`).\n\n## Usage\n\nA simple usage example:\n\n```python\nfrom aeromet_py import Metar\n\ncode = \'METAR MROC 071200Z 10018KT 3000 R07/P2000N BR VV003 17/09 A2994 RESHRA NOSIG\'\nmetar = Metar(code)\n\n# Get the type of the report\nprint(f"{metar.type}")  # Meteorological Aerodrome Report\n\n# Get the wind speed in knots and direction in degrees\nprint(f"{metar.wind.speed_in_knot} kt")       # 18.0 kt \nprint(f"{metar.wind.direction_in_degrees}°")  # 100.0°\n\n# Get the pressure in hecto pascals\nprint(f"{metar.pressure.in_hPa} hPa")  # 1014.0 hPa\n\n# Get the temperature in Celsius\nprint(f"{metar.temperatures.temperature_in_celsius}°C")  # 17.0°C\n```\n\n## Contributing\n\nContributions are what make the open source community such an amazing place to learn, inspire, and create.\nAny contributions you make are **greatly appreciated**.\n\nIf you have a suggestion that would make this better, please fork the repo and create a pull request.\nYou can also simply open an issue with the tag "enhancement".\nDon\'t forget to give the project a star! Thanks again!\n\n1. Fork the Project\n2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)\n3. Commit your Changes (`git commit -m \'Add some AmazingFeature\'`)\n4. Push to the Branch (`git push origin feature/AmazingFeature`)\n5. Open a Pull Request\n\n## Roadmap\n\n- [x] Add parsers for TAF and METAR reports\n- [ ] Add functions to verificate the TAF with the observations\n- [ ] Add a CLI API to interact with the verification functions\n- [ ] Add parser for SYNOPTIC reports\n- [ ] Add functions to verificate reports with rules of [Annex 3][annex3]\n- [ ] Multi-language Support\n    - [ ] Portuguese\n    - [ ] Spanish\n\n[annex3]: https://www.icao.int/airnavigation/IMP/Documents/Annex%203%20-%2075.pdf\n\n## Features and bugs\n\nPlease file feature requests and bugs at the [issue tracker][tracker].\n\n[tracker]: https://github.com/TAF-Verification/aeromet-py/issues\n\n## Current Sources\n\nThe most recent version of this package is always available via git, only run the\nfollowing command on your terminal:\n\n```\ngit clone https://github.com/TAF-Verification/aeromet-py.git\n```\n\n## Authors\n\nThe `python-metar` library was originaly authored by [Tom Pollard][TomPollard] in january 2005.\nThis package `aeromet-py` for is inspired from his work in 2021 by [Diego Garro][DiegoGarro].\n\n[TomPollard]: https://github.com/tomp\n[DiegoGarro]: https://github.com/diego-garro\n\n## Versioning\n\nThis project uses [Bump2version][bumpversion] tool for versioning, so, if you fork this\nrepository remember install it in your environment.\n\n[bumpversion]: https://pypi.org/project/bump2version/\n\n```\npip install bump2version\n```\n\n## License\n\nDistributed under the MIT License. See `LICENSE` for more information.',
    'author': 'diego-garro',
    'author_email': 'diego.garromolina@yahoo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TAF-Verification/aeromet-py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
