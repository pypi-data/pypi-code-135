# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['r_todolist']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['todo = r_todolist.main:app']}

setup_kwargs = {
    'name': 'r-todolist',
    'version': '0.1.1',
    'description': '',
    'long_description': '\n# todolist\n\n[typer](https://typer.tiangolo.com/)で遊ぶ目的で作ったcliのtodolistです。必要最小限のものしか実装していません。\n\n## install\n\n```\npip install r-todolist\n```\n\nhttps://pypi.org/project/r-todolist/\n\n## 仕様\n\n4つのサブコマンドがあり、以下のことができます。\n\n* add: タスクの追加\n* ls: タスクの一覧参照\n* done: 完了したタスクを完了済みにする\n* rm: タスクの削除\n\n### add: タスクの追加\n\n```\n$ todo add\nTask: buy a shampoo # prompt\nadded.\n```\n\n### add: タスクの一覧\n\n```\n$ todo ls\n- [] 2. "buy a shampoo"\n\n$ todo ls --done\n- [x] 1. "go to the bank"\n```\n\n### done: 完了したタスクを完了済みにする\n\n```\n$ todo done 2\n2. "buy a shampoo" is done🎉\n```\n\n### rm: タスクの削除\n\n```\n$ todo rm 1 2\nremoved: 1,2.\n```',
    'author': 'reiichii',
    'author_email': '20413226+reiichii@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
