# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['binsize', 'binsize.cli', 'binsize.lib', 'binsize.plugins']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'platformdirs>=2.5.2,<3.0.0',
 'termcolor>=2.0.1,<3.0.0',
 'typing-extensions']

entry_points = \
{'console_scripts': ['binsize = binsize.cli.binsize:cli']}

setup_kwargs = {
    'name': 'binsize',
    'version': '0.1.1',
    'description': 'Tool to analyze the size of a binary from .elf file',
    'long_description': '# Binsize tool\n\nTool for analyzing the sizes of symbols in binaries.\n\nIt can be used to find out which symbols are taking up the most space in a binary.\n\nIt requires `bloaty` and `nm` tools to be installed.\n\nIt analyzes the `.elf` file and optionally also the `.map` file from the binary creation process.\n\n## Tool basic usage\n\nInstallable by `pip install binsize` - see [PyPI](https://pypi.org/project/binsize/).\n\nInstalling this package creates `binsize` command, which has a lot of subcommands seeable by `binsize --help`. For example\n\n```bash\n$ binsize get firmware.elf -d\n$ binsize compare firmware.elf other_firmware.elf\n$ binsize tree firmware.elf\n```\n\n`--help` can be used even on the subcommands, for example `binsize get --help` - to see all available options.\n\nResult will be usually printed into terminal, unless specifying `--output` option which some commands support.\n\n## Setting root directory\nTo resolve all the files properly, the project\'s root directory needs to be set correctly.\n\nThere are couple of possibilities how to do it.\n\nIn the end, all of them are changing the `root` value in `settings.json`, from where everything else gets the value. It needs to be an absolute path.\n\n`settings.json` will be created in a user\'s home directory, based on `platformdirs` library (`~/.config/binsize/settings.json` on `linux`).\n\n### Manually\nJust modifying the `root` in the `settings.json` file.\n\n### Via environmental variable\n`BINSIZE_ROOT_DIR` env variable is checked and when not empty, it will set the root directory.\n\ne.g. `BINSIZE_ROOT_DIR=/home/user/project binsize tree /path/to/file.elf`\n\n### Via CLI argument\n`binsize` accepts `-r / --root-dir` argument, which can be used to set the root directory.\n\nIt has lower priority than the environmental variable.\n\ne.g. `binsize -r /home/user/project tree /path/to/file.elf`\n\n### Via exposed function\n`binsize` exposes `set_root_dir` function, which can be called from any `python` script.\n\ne.g. `binsize.set_root_dir("/home/user/project")`\n\n---\n\nTODO: document all the CLI commands, exportable symbols, basic functioning, ways to extend it, etc.\n',
    'author': 'SatoshiLabs',
    'author_email': 'info@satoshilabs.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/grdddj/binsize',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
