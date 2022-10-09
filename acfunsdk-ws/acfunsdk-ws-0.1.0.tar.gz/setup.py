# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['acfunsdk_ws',
 'acfunsdk_ws.blackboxprotobuf',
 'acfunsdk_ws.blackboxprotobuf.libs',
 'acfunsdk_ws.blackboxprotobuf.libs.types',
 'acfunsdk_ws.models',
 'acfunsdk_ws.models.Im',
 'acfunsdk_ws.models.Live']

package_data = \
{'': ['*'],
 'acfunsdk_ws': ['protos/*',
                 'protos/Im/Basic/*',
                 'protos/Im/Cloud/Channel/*',
                 'protos/Im/Cloud/Config/*',
                 'protos/Im/Cloud/Data/Update/*',
                 'protos/Im/Cloud/Message/*',
                 'protos/Im/Cloud/Profile/*',
                 'protos/Im/Cloud/Search/*',
                 'protos/Im/Cloud/SessionFolder/*',
                 'protos/Im/Cloud/SessionTag/*',
                 'protos/Im/Cloud/Voice/Call/*',
                 'protos/Im/Message/*',
                 'protos/zt.live.interactive/*']}

install_requires = \
['acfunsdk>=0.9.7,<0.10.0',
 'filetype>=1.1,<2.0',
 'proto-plus==1.22.1',
 'protobuf==3.20.1',
 'pycryptodome>=3.15,<4.0',
 'websocket-client>=1.4,<2.0']

setup_kwargs = {
    'name': 'acfunsdk-ws',
    'version': '0.1.0',
    'description': 'acfunsdk - websocket',
    'long_description': '# acfunSDK - websocket\n\n<br />\n\n<p align="center">\n<a href="https://github.com/dolaCmeo/acfunSDK">\n<img height="100" src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" alt="">\n<img height="100" src="https://ali-imgs.acfun.cn/kos/nlav10360/static/common/widget/header/img/acfunlogo.11a9841251f31e1a3316.svg" alt="">\n</a>\n</p>\n\n<br />\n\nacfunsdk是 **非官方的 [AcFun弹幕视频网][acfun.cn]** Python库。\n\n> `acfunsdk-ws` 是`acfunsdk`的附属组件，提供websocket通信支持。\n\n- - -\n\n\n<details>\n<summary>依赖库</summary>\n\n**依赖: 包含在 `requirements.txt` 中**\n\n+ [`acfunsdk`](https://pypi.org/project/acfunsdk/)`>=0.9.7`\n\nWebSocket通信及数据处理:\n+ [`websocket-client`](https://pypi.org/project/websocket-client/)`>=1.4`\n+ [`pycryptodome`](https://pypi.org/project/pycryptodome/)`>=3.15`\n+ [`protobuf`](https://pypi.org/project/protobuf/)`==3.20.1`\n+ [`proto-plus`](https://pypi.org/project/proto-plus/)`==1.22.1`\n+ [`filetype`](https://pypi.org/project/filetype/)`>=1.1`\n\n>内置+修改: \n>\n>+ [`blackboxprotobuf`](https://pypi.org/project/blackboxprotobuf/)\n\n</details>\n\n- - -\n\n## About Me\n\n[![ac彩娘-阿部高和](https://tx-free-imgs2.acfun.cn/kimg/bs2/zt-image-host/ChQwODliOGVhYzRjMTBmOGM0ZWY1ZRCIzNcv.gif)][dolacfun]\n[♂ 整点大香蕉🍌][acfunsdk_page]\n<img alt="AcFunCard" align="right" src="https://discovery.sunness.dev/39088">\n\n- - - \n\n[dolacfun]: https://www.acfun.cn/u/39088\n[acfunsdk_page]: https://www.acfun.cn/a/ac37416587\n\n[acfun.cn]: https://www.acfun.cn/\n[Issue]: https://github.com/dolaCmeo/acfunSDK/issues\n[python]: https://www.python.org/downloads/\n[venv]: https://docs.python.org/zh-cn/3.8/library/venv.html\n',
    'author': 'dolacmeo',
    'author_email': 'dolacmeo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/acfunsdk-ws/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
