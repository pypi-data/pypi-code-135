# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['acsaver', 'acsaver.utils']

package_data = \
{'': ['*'], 'acsaver': ['templates/*', 'templates/part/*']}

install_requires = \
['acfunsdk>=0.9.5,<0.10.0',
 'click>=8.1,<9.0',
 'filetype>=1.1,<2.0',
 'jinja2>=3.1,<4.0',
 'rich>=12.5,<13.0']

entry_points = \
{'console_scripts': ['acsaver = acsaver.__main__:cli']}

setup_kwargs = {
    'name': 'acsaver',
    'version': '0.1.3',
    'description': 'acfunsdk - AcSaver',
    'long_description': '# acfunsdk - AcSaver\n\n<br />\n\n<p align="center">\n<a href="https://github.com/dolaCmeo/acfunSDK">\n<img height="100" src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" alt="">\n<img height="100" src="https://ali-imgs.acfun.cn/kos/nlav10360/static/common/widget/header/img/acfunlogo.11a9841251f31e1a3316.svg" alt="">\n</a>\n</p>\n\n<br />\n\nacfunsdk是 **非官方的 [AcFun弹幕视频网][acfun.cn]** Python库。\n\n> `acsaver` 是`acfunsdk`的附属组件，提供内容离线保存支持。\n\n- - -\n\n\n<details>\n<summary>依赖库</summary>\n\n>内置+修改: 位于 `libs` 文件夹内\n>\n>+ [`ffmpeg_progress_yield`](https://github.com/slhck/ffmpeg-progress-yield)\n\n**依赖: 包含在 `requirements.txt` 中**\n\n下载及html页面渲染:\n+ [`acfunsdk`](https://pypi.org/project/acfunsdk/)`>=0.9.5`\n+ [`filetype`](https://pypi.org/project/filetype/)`>=1.1`\n+ [`jinja2`](https://pypi.org/project/jinja2/)`>=3.1`\n+ [`rich`](https://pypi.org/project/rich/)`>=12.5`\n+ [`click`](https://pypi.org/project/click/)`>=8.1`\n\n</details>\n\n- - -\n\n## About Me\n\n[![ac彩娘-阿部高和](https://tx-free-imgs2.acfun.cn/kimg/bs2/zt-image-host/ChQwODliOGVhYzRjMTBmOGM0ZWY1ZRCIzNcv.gif)][dolacfun]\n[♂ 整点大香蕉🍌][acfunsdk_page]\n<img alt="AcFunCard" align="right" src="https://discovery.sunness.dev/39088">\n\n- - - \n\n[dolacfun]: https://www.acfun.cn/u/39088\n[acfunsdk_page]: https://www.acfun.cn/a/ac37416587\n\n[acfun.cn]: https://www.acfun.cn/\n[Issue]: https://github.com/dolaCmeo/acfunSDK/issues\n[python]: https://www.python.org/downloads/\n[venv]: https://docs.python.org/zh-cn/3.8/library/venv.html\n',
    'author': 'dolacmeo',
    'author_email': 'dolacmeo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/acsaver/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
