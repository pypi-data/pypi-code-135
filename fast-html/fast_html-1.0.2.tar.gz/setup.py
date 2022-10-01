# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fast_html']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fast-html',
    'version': '1.0.2',
    'description': 'A fast, minimalist HTML generator',
    'long_description': 'fast_html is a fast, minimalist HTML generator.\n\nIt is an alternative to templating engines, like Jinja,\nfor use with, e.g., `htmx <https://htmx.org/>`__.\n\nPros:\n\n- use familiar python syntax\n\n- use efficient concatenation techniques\n\n- optional automatic indentation\n\nUnlike other HTML generators (e.g. `Dominate <https://pypi.org/project/dominate/>`__) that use python objects to represent HTML snippets,\nfast_html represents HTML snippets using string `generators <https://docs.python.org/3/glossary.html#term-generator>`__\nthat can be rendered extremely fast using ``join``.\n(see `here <https://python.plainenglish.io/concatenating-strings-efficiently-in-python-9bfc8e8d6f6e>`__)\n\nLike other HTML generators, one needs to remember:\n\n- the name of some tags and attributes is changed (e.g., ``class_`` instead of ``class``, due to Python parser)\n\n- there may be conflicts of function names with your code base\n\n\nInstallation\n------------\n``pip install fast_html`` or copy the (single) source file in your project.\n\nDon\'t forget to `add a star on GitHub <https://github.com/pcarbonn/fast_html>`_ ! Thanks.\n\n\nTutorial:\n---------\n\n>>> from fast_html import *\n\nA tag is created by calling a function of the corresponding name,\nand rendered using ``render``:\n\n>>> print(render(p("text")))\n<p>text</p>\n\n\nTag attributes are specified using named arguments:\n\n>>> print(render(br(id="1")))\n<br id="1">\n\n>>> print(render(br(id=None)))\n<br>\n\n>>> print(render(ul(li("text", selected=True))))\n<ul><li selected>text</li></ul>\n\n>>> print(render(ul(li("text", selected=False))))\n<ul><li>text</li></ul>\n\nThe python parser introduces some constraints:\n\n- The following tags require a trailing underscore: ``del_``, ``input_``, ``map_``, ``object_``.\n\n- The following tag attributes require a trailing underscore: ``class_``, ``for_`` (and possibly others).\n\nIn fact, the trailing underscore in attribute names is always removed by fast_html,\nand other underscores are replaced by ``-``.\nFor example, the htmx attribute ``hx-get`` is set using ``hx_get="url"``.\n\n>>> print(render(object_("text", class_="s12", hx_get="url")))\n<object class="s12" hx-get="url">text</object>\n\n>>> print(render(button("Click me", hx_post="/clicked", hx_swap="outerHTML")))\n<button hx-post="/clicked" hx-swap="outerHTML">Click me</button>\n\n\nThe innerHTML can be a list:\n\n>>> print(render(div(["text", span("item 1"), span("item 2")])))\n<div>text<span>item 1</span><span>item 2</span></div>\n\nThe innerHTML can also be a list of lists:\n\n>>> print(render(div(["text", [span(f"item {i}") for i in [1,2]]])))\n<div>text<span>item 1</span><span>item 2</span></div>\n\n\nThe innerHTML can also be specified using the ``i`` parameter,\nafter the other attributes, to match the order of rendering:\n\n>>> print(render(ul(class_="s12", i=[\n...                 li("item 1"),\n...                 li("item 2")]\n...      )))\n<ul class="s12"><li>item 1</li><li>item 2</li></ul>\n\nYou can create your own tag using the ``tag`` function:\n\n>>> def my_tag(inner=None, **kwargs):\n...     yield from tag("my_tag", inner, **kwargs)\n>>> print(render(my_tag("text")))\n<my_tag>text</my_tag>\n\n\nWhen debugging your code, you can set global variable ``indent`` to ``True``\n(or call ``indent_it(True)``) to obtain HTML with tag indentation, e.g.,\n\n>>> indent_it(True); print(render(div(class_="s12", i=["text", span("item 1"), span("item 2")])))\n<div class="s12">\n  text\n  <span>\n    item 1\n  </span>\n  <span>\n    item 2\n  </span>\n</div>\n<BLANKLINE>\n',
    'author': 'Pierre',
    'author_email': 'pierre.carbonnelle@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pcarbonn/fast_html',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
