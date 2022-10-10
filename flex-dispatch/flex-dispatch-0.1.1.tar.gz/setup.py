# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['__init__']
setup_kwargs = {
    'name': 'flex-dispatch',
    'version': '0.1.1',
    'description': "Dynamic dispatch for python similar to clojure's multimethod.",
    'long_description': 'flex_dispatch\n==============================\n\nA super flexible dynamic dispatch implementation for python, inspired by Clojure\'s multimethod.\n\nInstall with: `pip install flex-dispatch`\n\nTo use: `from flex_dispatch import Dispatcher` and annotate any callable with `@Dispatcher`\n\nExample\n------------\n```\nfrom flex_dispatch import Dispatcher\n\n\n@Dispatcher\ndef greet(*args):\n    if len(args) == 1:\n        return \'_just_name\'\n    elif len(args) == 2:\n        return \'_name_msg\'\n\n\n@greet.map(\'_just_name\')\ndef say_hey(name):\n    print(f\'Hello, {name}!\')\n\n\n@greet.map(\'_name_msg\')\ndef say_message(name, msg):\n    print(f\'{msg} {name}\')\n\n\ngreet(\'Chris\')   # calls say_hey and prints "Hello, Chris!"\ngreet(\'Bob\', \'Boo\')  # calls say_message and prints "Boo Bob"\n\ngreet(\'b\', \'b\', 3)  # greet returns none as a dispatch value, and DispatchError is raised.\n```\n\nAny callable decorated with @Dispatcher becomes a dispatcher function.  It should inspect its arguments and return a "dispatch value"; i.e., a value used\nto determine which callable to dispatch the call to.  Callables decorated with `@<dispatcher>.map(<value>)` (like `@greet.map(\'_just_name\')` above) register the decorated function as the dispatch target for the given value.\n\nIn other words, when `greet(\'Chris\')` is called, first the `greet` function is called to return a dispatch value, in this case `\'_just_name\'`.  Since `say_hey` was decorated with `@greet.amp(\'_just_name\')`, it was registered as the target function to call when `greet` returns the dispatch value `\'_just_name\'`.\n\n',
    'author': 'Chris Blades',
    'author_email': 'chrisdblades@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cblades/flex_dispatch',
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
