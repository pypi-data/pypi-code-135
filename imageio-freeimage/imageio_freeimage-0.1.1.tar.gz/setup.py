# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imageio_freeimage']

package_data = \
{'': ['*']}

install_requires = \
['imageio>=2.19.3,<3.0.0']

setup_kwargs = {
    'name': 'imageio-freeimage',
    'version': '0.1.0',
    'description': 'A plugin for ImageIO that wraps the FreeImage library',
    'long_description': '# ImageIO FreeImage\n\n[![CI](https://github.com/imageio/imageio-freeimage/actions/workflows/ci.yaml/badge.svg?branch=master)](https://github.com/imageio/imageio-freeimage/actions/workflows/ci.yaml)\n\n> **Warning**\n> \n> This repo is licensed under the *FreeImage Open Source Dual-License* and\n> **not** the typical *BSD-2* license we use for everything else. Check out the\n> LICENSE document in this repo and make sure you understand the consequences.\n\nImageIO FreeImage is a ImageIO plugin for the FreeImage library. In other words,\nit allows using [FreeImage](https://freeimage.sourceforge.io/) with\n[ImageIO](https://github.com/imageio/imageio).\n\n## Installation\n\n```\npip install imageio-freeimage\npython -c "imageio.plugins.freeimage.download()"\n```\n\n## Usage (and Examples)\n\nTo use it simply import the library. It will auto-register with ImageIO.\n\n```python\nimport imageio.v3 as iio\nimport imageio_freeimage\n\nimg = iio.imread("imageio:chelsea.png", plugin="PNG-FI")\n```\n\n## Why ImageIO FreeImage\n\nBased on discussions over at ImageIO\'s main repository, we have decided to spin\nout the FreeImage plugin. This was done for two reasons\n\n1. It is/was unclear how permissible the FreeImage license is, how exactly it\ninteracts with BSD (ImageIO\'s license), and what that means for downstream users\nwho don\'t need FreeImage. Instead of having to deal with the fallout of this\ninteraction, we decided to spin out the FreeImage plugin. This way, users don\'t\nhave to worry, unless they explicitly need FreeImage, in which case they will\nlikely be aware of how FreeImage is licensed, and what it means for their\nproject.\n\n2. The FreeImage bindings we provide are based on ctypes. In many cases this is\nnot a problem; however, for some users it causes complications, because they,\nfor example, use pypy or other non-cpython interpreters or they want to complile\ntheir python code in a browser via pyodide. Those use-cases are more prone to\nproblems when ctypes are involved and having them in a dedicated optional\ndependency make this situation easier.\n\n3. We can add plumbing to compile FreeImage in CD and ship it precompiled\n   without the need for any post-install actions.',
    'author': 'ImageIO collaborators',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/imageio/imageio-freeimage',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
