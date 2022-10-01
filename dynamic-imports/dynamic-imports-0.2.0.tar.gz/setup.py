# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dynamic_imports']

package_data = \
{'': ['*']}

install_requires = \
['ready-logger>=0.1.5,<0.2.0']

setup_kwargs = {
    'name': 'dynamic-imports',
    'version': '0.2.0',
    'description': 'Dynamically discover and import Python modules and classes.',
    'long_description': "## Dynamically discover and import Python modules and classes\n\n### Import a module via module name or file path\n```python\nfrom dynamic_imports import import_module\nmodule = import_module('my_package.my_module')\n# or\nmodule = import_module('/home/user/my_package/my_module.py')\n```\n### Import a module attribute\n```python\nfrom dynamic_imports import import_module_attr\n\nfunction = import_module_attr('my_package.my_module', 'my_function')\n# or\nfunction = import_module_attr('/home/user/my_package/my_module.py', 'my_function')\n```\n\n### Find all modules in a package or nested packages\n```python\nfrom dynamic_imports import get_modules\n\nmodules = get_modules(\n    package=my_package, # str `my_package' works too.\n    search_subpackages=True,\n    # return the actual module objects, not str names.\n    names_only=False,\n)\n\n```\n\n### Find all implementations of a base class within a module.\n```python\nfrom dynamic_imports import module_class_impl\nfrom my_package.my_module import Base\nfrom my_package import my_module\n\nmy_classes = module_class_impl(\n    base_class=Base, # str 'Base' works too\n    module=my_module,\n    names_only=False\n)\n```\n\n### Find all implementations of a base class within a package.\n```python\nfrom dynamic_imports import pkg_class_impl\nfrom my_package.my_module import Base\nimport my_package\n\nmy_classes = pkg_class_impl(\n    base_class=Base, # str 'Base' works too.\n    package=my_package\n    search_subpackages=True,\n    names_only=False,\n)\n\n```\n\n### Find all instances of a class within a module.\n```python\nfrom dynamic_imports import module_class_inst\nfrom my_package import my_module\nfrom my_package.my_module import MyClass\n\nmy_classes_instances = module_class_inst(\n    module=my_module, # str 'my_package.my_module' works too.\n    class_type=MyClass\n)\n```\n\n### Find all instances of a class within a package.\n```python\nfrom dynamic_imports import pkg_class_inst\nfrom my_package.my_module import MyClass\nimport my_package\n\nmy_classes_instances = pkg_class_inst(\n    class_type=MyClass,\n    package=my_package, # str 'my_package' works too.\n    search_subpackages=True,\n)\n```",
    'author': 'Dan Kelleher',
    'author_email': 'kelleherjdan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/djkelleher/dynamic-imports',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
