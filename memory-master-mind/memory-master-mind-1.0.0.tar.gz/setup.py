# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['memory_master_mind', 'memory_master_mind.components']

package_data = \
{'': ['*'], 'memory_master_mind': ['assets/*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'textual>=0.1.18,<0.2.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['memory-master-mind = memory_master_mind.runner:main',
                     'mmm = memory_master_mind.runner:main']}

setup_kwargs = {
    'name': 'memory-master-mind',
    'version': '1.0.0',
    'description': 'MMM - Memory Master Mind - memory training in the terminal',
    'long_description': '# MMM - Memory Master Mind\n\nMemory training in the terminal\n\nInstall with pip:\n\n``` shell\npip install memory-master-mind\n```\n\nRun with the `mmm` command.\n\n## Help and Challenges Info\n\n- [App Help](mmm/assets/mmm_help.md)\n- [Static Number Sequence](mmm/assets/static_number_sequence.md)\n- [Timed Number Sequence](mmm/assets/timed_number_sequence.md)\n- [Math (Arithmetic)](mmm/assets/math_arithmetic.md)\n- [Quotes and Verses](mmm/assets/quotes_and_verses.md)\n\n![Home Menu](docs/mmm-home.png)\n\n![Static Number Sequence](docs/mmm-static.png)\n\n![Timed Number Sequence](docs/mmm-timed.png)\n\n![Math (Arithmetic)](docs/mmm-math.png)\n\n![Quotes and Verses](docs/mmm-quotes.png)\n\n## Preferences\n\n![App Preferences](docs/mmm-app-prefs.png)\n\n![Preferences: Static Number Sequence](docs/mmm-static-prefs.png)\n\n## Links\n\nPowered by the [textual](https://github.com/Textualize/textual) TUI framework\n\n<https://github.com/profound-labs/memory-master-mind>\n',
    'author': 'Gambhiro',
    'author_email': 'profound.labs@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/profound-labs/memory-master-mind',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
