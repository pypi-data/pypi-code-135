# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mmodel']

package_data = \
{'': ['*']}

install_requires = \
['graphviz>=0.16', 'h5py>=3.6.0', 'networkx>=2.8.3']

extras_require = \
{'docs': ['sphinx>=4.5.0,<5.0.0',
          'sphinx-book-theme>=0.3.3,<0.4.0',
          'nbsphinx>=0.8.8,<0.9.0'],
 'test': ['pytest>=7.1.1', 'pytest-cov>=3.0.0']}

setup_kwargs = {
    'name': 'mmodel',
    'version': '0.4.0',
    'description': 'Modular modeling framework for nonlinear scientific models',
    'long_description': 'MModel\n======\n\n|GitHub version| |PyPI version shields.io| |PyPI pyversions| |CircleCI|\n|Docs|\n\nMModel is a lightweight and modular model building framework\nfor small-scale and nonlinear models. The package aims to solve\nscientific program prototyping and distribution difficulties, making\nit easier to create modular, fast, and user-friendly packages.\nThe package is fully tested.\n\nQuickstart\n----------\n\nTo create a nonlinear model that has the result of\n`(x + y)log(x + y, base)`:\n\n.. code-block:: python\n\n    from mmodel import ModelGraph, Model, MemHandler\n    import math\n\n    def func_a(x, y):\n        return x + y\n\n    def func_b(sum_xy, base):\n        return math.log(sum_xy, base)\n\n    def func_c(sum_xy, log_xy):\n        return sum_xy * log_xy\n\n    # create graph links\n\n    grouped_edges = [\n        ("func a", ["func b", "func c"]),\n        ("func b", "func c"),\n    ]\n\n    node_objects = [\n        ("func a", func_a, ["sum_xy"]),\n        ("func b", func_b, ["log_xy"]),\n        ("func c", func_c, ["result"]),\n    ]\n\n    graph = ModelGraph(name="example_graph")\n    graph.add_grouped_edges_from(grouped_edges)\n    graph.set_node_objects_from(node_objects)\n\n    example_model = Model("example_model", graph, handler=(MemHandler, {}))\n\n    >>> print(example_model)\n    example_model(base, x, y)\n      signature: \n      returns: result\n      handler: MemHandler, {}\n      modifiers: none\n\n    >>> example_model(2, 5, 3) # (5 + 3)log(5 + 3, 2)\n    24.0\n\nThe resulting ``example_func`` is callable.\n\nOne key feature of ``mmodel`` is modifiers, which modify callables post\ndefinition. To loop the "base" parameter.\n\n.. code-block:: python \n\n    from mmodel import subgraph_by_parameters, modify_subgraph, loop_modifier\n\n    subgraph = subgraph_by_parameters(graph, ["base"])\n    loop_node = Model(\n        "loop_node",\n        subgraph,\n        (MemHandler, {}),\n        modifiers=[(loop_modifier, {"parameter": "base"})],\n    )\n    looped_graph = modify_subgraph(graph, subgraph, "loop node", loop_node)\n    looped_model = Model("loop_model", looped_graph, loop_node.handler)\n\n    >>> print(looped_model)\n    loop_model(base, x, y)\n        returns: result\n        handler: MemHandler, {}\n        modifiers: []\n    \n    >>> looped_model([2, 4], 5, 3) # (5 + 3)log(5 + 3, 2)\n    [24.0, 12.0]\n\n\nModifiers can also be added to the whole model or a single node.\n\nTo draw the graph or the underlying graph of the model:\n\n.. code-block:: python\n\n    from mmodel import draw_plain_graph\n    graph.draw(method=draw_plain_graph)\n    example_model.draw(method=draw_plain_graph)\n\nInstallation\n------------\n\nGraphviz installation\n^^^^^^^^^^^^^^^^^^^^^\n\nTo view the graph, Graphviz needs to be installed:\n`Graphviz Installation <https://graphviz.org/download/>`_\nFor windows installation, please choose "add Graphviz to the\nsystem PATH for all users/current users" during the setup.\n\nMModel installation\n^^^^^^^^^^^^^^^^^^^^^^^\n\n.. code-block::\n\n    pip install mmodel\n\nDevelopment installation\n^^^^^^^^^^^^^^^^^^^^^^^^\nMModel uses `poetry <https://python-poetry.org/docs/>`_ as\nthe build system. The package works with both pip and poetry\ninstallation. \n\nTo install test and docs, despondencies run::\n\n    pip install .[test] .[docs]\n\nTo run the tests in different python environments and cases \n(py38, py39, py310, coverage and docs)::\n\n    tox\n\nTo create the documentation, run under the "/docs" directory::\n\n    make html\n\n\n.. |GitHub version| image:: https://badge.fury.io/gh/peterhs73%2FMModel.svg\n   :target: https://github.com/peterhs73/MModel\n\n.. |PyPI version shields.io| image:: https://img.shields.io/pypi/v/mmodel.svg\n   :target: https://pypi.python.org/pypi/mmodel/\n\n.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/mmodel.svg\n\n.. |CircleCI| image:: https://circleci.com/gh/peterhs73/MModel.svg?style=shield\n    :target: https://circleci.com/gh/peterhs73/MModel\n\n.. |Docs| image:: https://img.shields.io/badge/Documentation--brightgreen.svg\n    :target: https://peterhs73.github.io/mmodel-docs/\n',
    'author': 'Peter Sun',
    'author_email': 'hs859@cornell.edu',
    'maintainer': 'Peter Sun',
    'maintainer_email': 'hs859@cornell.edu',
    'url': 'https://peterhs73.github.io/mmodel-docs/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
