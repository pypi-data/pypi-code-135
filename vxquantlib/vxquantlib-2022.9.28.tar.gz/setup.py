# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src',
 'vxsched': 'src/vxsched',
 'vxsched.pubsubs': 'src/vxsched/pubsubs',
 'vxsched.scripts': 'src/vxsched/scripts',
 'vxsched.triggers': 'src/vxsched/triggers',
 'vxutils': 'src/vxutils',
 'vxutils.database': 'src/vxutils/database'}

packages = \
['vxquant',
 'vxquant.mdapi',
 'vxquant.mdapi.hq',
 'vxquant.model',
 'vxquant.model.tools',
 'vxquant.scripts',
 'vxquant.strategy',
 'vxquant.tdapi',
 'vxsched',
 'vxsched.pubsubs',
 'vxsched.scripts',
 'vxsched.triggers',
 'vxutils',
 'vxutils.database']

package_data = \
{'': ['*']}

install_requires = \
['pymongo', 'python-dateutil', 'pyzmq', 'requests', 'six']

setup_kwargs = {
    'name': 'vxquantlib',
    'version': '2022.9.28',
    'description': '基于事件驱动的量化交易基础框架',
    'long_description': '# vxQuant —— 一个简单易用的量化交易工具箱\n\n\n\n## 一、安装教程\n\n1.通过pip 安装\n\n```python\npip install vxquant\n```\n\n2.通过源码编译\n\n```python\ngit clone https://github.com/vxquant/vxquant.git\ncd vxquant/\npython3 setup.py install\n```\n\n## 二、模块介绍\n\n当前版本主要包括以下几个主要模块:\n\n### 1. scheduler --- 调度器 负责量化交易过程中对于各个类型时间的处理\n\n#### 1.1 event类 ---事件类\n\n```python\nvxEvent:\n    # 消息id\n    id: uuid\n    # 消息通道，主要是用于标识消息的来源\n    channel: str \n    # 消息类型，如: on_tick, on_order_status ...\n    type: str \n    # 消息内容\n    data: Any \n    # 定时触发器，即：一个定时触发，或者循环出发的时间\n    trigger: Optional[vxTrigger] \n    # 下次触发事件 通过定义vxTrigger类来确定next_trigger_dt\n    next_trigger_dt: timestamp\n    # 优先级, \n    # next_trigger_dt越早越快触发，next_trigger_dt相同时prority越小越优先\n    priority: int = vxIntField(10)\n\n```\n\n#### vxTrigger类\n\n* vxOnceTrigger ---> 仅触发一次的trigger\n  * 参数: run_time 触发时间\n  \n* vxIntervalTrigger ---> 间隔触发器\n  * 参数: start_dt ---> 开始时间\n  * 参数: end_dt ---> 结束时间\n  * 参数: interval ---> 间隔秒数\n\n* vxDailyTrigger  ---> 每隔interval日的run_time时间执行\n  * 参数: run_time --->每天的运行时间,如："09:30:00"\n  * 参数: interval --->间隔天数，最少为1天\n  * 参数: skip_holiday ---> 是否跳过假日，假日定义可以通过vxtime.is_holiday()判断，通过vxtime.add_holiday() 增加对应的假日\n\n* vxWeeklyTrigger ---> 每周执行\n  * 参数: weekday ---> 星期几，0 表示周日，6表示周六\n  * 参数: run_time\n  * 参数: interval\n  * 参数: skip_holiday\n  \n\n## 软件架构\n软件架构说明\n\n\n## 安装教程\n\npython setup.py build install\n',
    'author': 'vex1023',
    'author_email': 'vex1023@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitee.com/vxquantlib/vxquantlib',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
