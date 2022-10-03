# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['yacs_stubgen']

package_data = \
{'': ['*']}

install_requires = \
['yacs>=0.1.4,<0.2.0']

setup_kwargs = {
    'name': 'yacs-stubgen',
    'version': '0.1.2',
    'description': 'Generate stub file for yacs config.',
    'long_description': '# yacs-stubgen\n\nAdd typing support for your yacs config by generating stub file.\n\n## Install\n\n<details>\n\n```sh\npip install yacs-stubgen\n```\n\nor install from this repo:\n\n```sh\npip install git+github.com/JamzumSum/yacs-stubgen.git\n```\n\n</details>\n\n## Usage\n\nAdd typing support for your yacs config by appending two lines:\n\n```py\n_C.MODEL.DEVICE = \'cuda\'\n...\n# your config items above\n\nfrom yacs_stubgen import build_pyi\n# this line can be moved to the import header\nbuild_pyi(_C, __file__, var_name=\'_C\')\n# _C is the CfgNode object, "_C" should be its name correctly\n```\n\n**After** any run/import of this file, a stub file (*.pyi) will be generated.\nThen you will get typing and auto-complete support **if your IDE supports stub files**.\n\n## License\n\n- MIT\n',
    'author': 'JamzumSum',
    'author_email': 'zzzzss990315@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JamzumSum/yacs-stubgen',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
