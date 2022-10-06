# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bdnotice']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['bdnotice = bdnotice:main']}

setup_kwargs = {
    'name': 'bdnotice',
    'version': '0.1.0',
    'description': 'Generate Notice file from Blackduck in JSON, TEXT or HTML format',
    'long_description': '# BDNOTICE\n\nGenerate Notice file from Blackduck in JSON, TEXT or HTML format\n\n## Description\n\nThis is intended for generating Notice file from Blackduck in JSON, TEXT or HTML format\n\n## Getting Started\n\n### Dependencies\n\n- Blackduck\n- importlib-resources\n\n### Installing\n\n- pip install bdnotice\n\n### Executing program\n\n- How to run the program\n\n```\n<!-- on the folder it is running place this blackduck config file for blackduck library-->\n.restconfig.json\n{\n    <!-- make sure Blackduck_url should not end with slash -->\n  "baseurl": "Blackduck_url",\n  "api_token": "API_KEY",\n  "insecure": true,\n  "debug": false\n}\n\npip install bdnotice\nex:\nbdnotice PJ PV -f C:\\DIR\\Blackduck_report -r HTML -c\nbdnotice PJ PV -f C:\\DIR\\Blackduck_report -r TEXT -c\n```\n\n## Help\n\nAny advise for common problems or issues.\n\n```\n\n```\n\n## Authors\n\nDinesh Ravi\n\n## Version History\n\n- 0.1.0\n  - Initial Release\n\n## License\n\nThis project is licensed under the MIT License - see the [MIT](LICENSE) file for details\n\n## Acknowledgments\n\n- [Blackduck](https://pypi.org/project/blackduck/)\n- [importlib-resources](https://pypi.org/project/importlib-resources/)\n',
    'author': 'dineshr93gmail.com',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
