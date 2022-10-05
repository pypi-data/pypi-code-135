# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['traefik_certificate_exporter']

package_data = \
{'': ['*']}

install_requires = \
['docker-pycreds>=0.4.0,<0.5.0',
 'docker>=6.0.0,<7.0.0',
 'requests>=2.28.1,<3.0.0',
 'watchdog>=2.1.9,<3.0.0']

entry_points = \
{'console_scripts': ['traefik-certificate-exporter = '
                     'traefik_certificate_exporter.app:main']}

setup_kwargs = {
    'name': 'traefik-certificate-exporter',
    'version': '0.0.8',
    'description': 'Watches for changes to traefik acme json files and extracts certificates to a specific folder',
    'long_description': '# Overview\n\n[![Github Tags](https://img.shields.io/github/v/tag/ravensorb/traefik-certificate-exporter?logo=github&logoColor=white)](https://github.com/ravensorb/traefik-certificate-exporter) [![PyPi Version](https://img.shields.io/pypi/v/traefik-certificate-exporter?color=g&label=pypi%20package&logo=pypi&logoColor=white)](https://pypi.org/project/traefik-certificate-exporter/) [![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://hub.docker.com/r/ravensorb/traefik-certificate-exporter)\n\n\n\nThis tool can be used to extract acme certificates (ex: lets encrupt) from traefik json files. The tool is design to watch for changes to a folder for any files that match a filespec (defaults to *,json however can be set to a specific file name) and when changes are detected it will process the file and extract any certificates that are in it to the specified output path\n\n# Installation\n\n## Python Script/Tool\nInstallation can be done via the python package installer tool pip\n```\n$ pip install traefik-certificate-exporter\n```\n\n# Usage\n\n```bash\nusage: traefik-certificate-exporter [-h] [-c CONFIGFILE] [-d DATAPATH] [-w] [-fs FILESPEC] [-o OUTPUTPATH] [--traefik-resolver-id TRAEFIKRESOLVERID] [-f] [-r] [--dry-run] [-id [INCLUDEDOMAINS [INCLUDEDOMAINS ...]] | -xd\n                                    [EXCLUDEDOMAINS [EXCLUDEDOMAINS ...]]]\n\nExtract traefik letsencrypt certificates.\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -c CONFIGFILE, --config-file CONFIGFILE\n                        the path to watch for changes (default: None)\n  -d DATAPATH, --data-path DATAPATH\n                        the path that contains the acme json files (default: ./)\n  -w, --watch-for-changes\n                        If specified, monitor and watch for changes to acme files\n  -fs FILESPEC, --file-spec FILESPEC\n                        file that contains the traefik certificates (default: *.json)\n  -o OUTPUTPATH, --output-directory OUTPUTPATH\n                        The folder to exports the certificates in to (default: ./certs)\n  --traefik-resolver-id TRAEFIKRESOLVERID\n                        Traefik certificate-resolver-id.\n  -f, --flat            If specified, all certificates into a single folder\n  -r, --restart_container\n                        If specified, any container that are labeled with \'com.github.ravensorb.traefik-certificate-exporter.domain-restart=<DOMAIN>\' will be restarted if the domain name of a generated certificates matches the value\n                        of the lable. Multiple domains can be seperated by \',\'\n  --dry-run             Don\'t write files and do not restart docker containers.\n  -id [INCLUDEDOMAINS [INCLUDEDOMAINS ...]], --include-domains [INCLUDEDOMAINS [INCLUDEDOMAINS ...]]\n                        If specified, only certificates that match domains in this list will be extracted\n  -xd [EXCLUDEDOMAINS [EXCLUDEDOMAINS ...]], --exclude-domains [EXCLUDEDOMAINS [EXCLUDEDOMAINS ...]]\n                        If specified. certificates that match domains in this list will be ignored\n```\n\n## Examples\nWatch the letsencrypt folder for any changes to files matching acme-*.json and export any certs managed by the resolver called "resolver-http"\n\n## Script\nRun it once and exite\n```bash\ntraefik-certificate-exporter \\\n                            -d /mnt/traefik-data/letsencrypt \\\n                            -o /mnt/certs \\\n                            -fs "acme-*.json" \\\n                            --traefik-resolver-id "resolver-http" \n```\n\nRun it and watch for changes to the files\n```bash\ntraefik-certificate-exporter \\\n                            -d /mnt/traefik-data/letsencrypt \\\n                            -o /mnt/certs \\\n                            -fs "acme-*.json" \\\n                            --traefik-resolver-id "resolver-http" \\\n                            -w\n```\n\n# Credits\nThis tool is HEAVLY influenced by the excellent work of [DanielHuisman](https://github.com/DanielHuisman) and [Marc Brückner](https://github.com/SnowMB)',
    'author': 'Shawn Anderson',
    'author_email': 'sanderson@eye-catcher.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ravensorb/traefik-certificate-exporter',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
