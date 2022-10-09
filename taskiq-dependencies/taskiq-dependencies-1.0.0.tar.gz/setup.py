# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['taskiq_dependencies']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.9"': ['graphlib-backport>=1.0.3,<2.0.0']}

setup_kwargs = {
    'name': 'taskiq-dependencies',
    'version': '1.0.0',
    'description': 'FastAPI like dependency injection implementation',
    'long_description': "# Taskiq dependencies\n\nThis project is used to add FastAPI-like dependency injection to projects.\n\nThis project is a part of the taskiq, but it doesn't have any dependencies,\nand you can easily integrate it in any project.\n\n# Installation\n\n```bash\npip install taskiq-dependencies\n```\n\n# Usage\n\nLet's imagine you want to add DI in your project. What should you do?\nAt first we need to create a dependency graph, check if there any cycles\nand compute the order of dependencies. This can be done with DependencyGraph.\nIt does all of those actions on create. So we can remember all graphs at the start of\nour program for later use. Or we can do it when needed, but it's less optimal.\n\n```python\nfrom taskiq_dependencies import Depends\n\n\ndef dep1() -> int:\n    return 1\n\n\ndef target_func(some_int: int = Depends(dep1)):\n    print(some_int)\n    return some_int + 1\n\n```\n\nIn this example we have a function called `target_func` and as you can see, it depends on `dep1` dependency.\n\nTo create a dependnecy graph have to write this:\n```python\nfrom taskiq_dependencies import DependencyGraph\n\ngraph = DependencyGraph(target_func)\n```\n\nThat's it. Now we want to resolve all dependencies and call a function. It's simple as this:\n\n```python\nwith graph.sync_ctx() as ctx:\n    graph.target(**ctx.resolve_kwargs())\n```\n\nVoila! We resolved all dependencies and called a function with no arguments.\nThe `resolve_kwargs` function will return a dict, where keys are parameter names, and values are resolved dependencies.\n\n\n### Async usage\n\nIf your lib is asynchronous, you should use async context, it's similar to sync context, but instead of `with` you should use `async with`. But this way your users can use async dependencies and async generators. It's not possible in sync context.\n\n\n```python\nasync with graph.async_ctx() as ctx:\n    kwargs = await ctx.resolve_kwargs()\n```\n\n## Q&A\n\n> Why should I use `with` or `async with` statements?\n\nBecuase users can use generator functions as dependencies.\nEverything before `yield` happens before injecting the dependency, and everything after `yield` is executed after the `with` statement is over.\n\n> How to provide default dependencies?\n\nIt maybe useful to have default dependencies for your project.\nFor example, taskiq has `Context` and `State` classes that can be used as dependencies. `sync_context` and `async_context` methods have a parameter, where you can pass a dict with precalculated dependencies.\n\n\n```python\nfrom taskiq_dependencies import Depends, DependencyGraph\n\n\nclass DefaultDep:\n    ...\n\n\ndef target_func(dd: DefaultDep = Depends()):\n    print(dd)\n    return 1\n\n\ngraph = DependencyGraph(target_func)\n\nwith graph.sync_ctx({DefaultDep: DefaultDep()}) as ctx:\n    print(ctx.resolve_kwargs())\n\n```\n\nYou can run this code. It will resolve dd dependency into a `DefaultDep` variable you provide.\n",
    'author': 'Pavel Kirilin',
    'author_email': 'win10@list.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
