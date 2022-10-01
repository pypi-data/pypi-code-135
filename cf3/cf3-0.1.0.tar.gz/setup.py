# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cf3']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.9.1,<5.0.0']

entry_points = \
{'console_scripts': ['cf3 = cf3.cf3:run']}

setup_kwargs = {
    'name': 'cf3',
    'version': '0.1.0',
    'description': 'Calculate the CF3 hashes for an html page',
    'long_description': '# CF3\n\n*fingerprinting censors, one blockpage at a time.*\n\n## what\n\nThis tool attempts to extract unique features in blockpages in a compact way.\n\n```\n❯ for f in corpus/*; do ./cf3 $f hash; done > hashes\n❯ wc -l hashes\n136 hashes\n❯ uniq hashes | wc -l\n135\n# almost! :)\n```\n\n## verbose\n\n```\n❯ ./cf3 corpus/prod_comodo_securedns_warning.html\ntitle size: 17\nmeta: 2\nscript: 2\nhead size: 2048\nbody size: 1024\ntotal size: 4096\ntag vector summary: 88\ntag vector: html,head,title,link,style,meta,meta,body,div,img,div,img,div,button,div,div,h1,h2,p,br,ul,li,a,img,br,br,p,a,div,div,p,script,script\n\nCF3: 17-2-2-33-88-2048-1024-4096\nmd5: 12c27a55433b1813c02a8a92dd4b3bff\n```\n\n## dynamic content\n\nThe algorithm tries to be invariant under pages that share a well-defined structure but for which dynamic content, js nonces and other quirks result in highly variable content. YMMV.\n\n```\n❯ mkdir tmp && cd tmp\n❯ for i in {1..10}; do curl -L --silent https://www.youtube.com/ > yt$i.html; done\n❯ for f in *; do ../cf3 $f hash; done\n993522ccea4b8e11857ff4bb1917a77d\n993522ccea4b8e11857ff4bb1917a77d\n993522ccea4b8e11857ff4bb1917a77d\n993522ccea4b8e11857ff4bb1917a77d\n993522ccea4b8e11857ff4bb1917a77d\n993522ccea4b8e11857ff4bb1917a77d\n993522ccea4b8e11857ff4bb1917a77d\n993522ccea4b8e11857ff4bb1917a77d\n993522ccea4b8e11857ff4bb1917a77d\n993522ccea4b8e11857ff4bb1917a77d\n```\n\n# license\n\nThis code is deposited in the public domain.\n\n\n\n',
    'author': 'Ain Ghazal',
    'author_email': 'ainghazal42@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ainghazal/cf3',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
