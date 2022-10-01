# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['guards']

package_data = \
{'': ['*']}

install_requires = \
['typing-inspect>=0.8.0,<0.9.0']

setup_kwargs = {
    'name': 'guards',
    'version': '1.0.0',
    'description': 'Tools for guarding Defaults, Null and creating Singletons.',
    'long_description': '- [Overview](#overview)\n- [Install](#install)\n- [Singleton Object](#singleton-object)\n    * [Singleton Example](#singleton-example)\n- [Null Object](#null-object)\n    * [Null Example](#null-example)\n- [Default Object](#default-object)\n    * [Default Example](#default-example)\n- [Licensing](#licensing)\n\n\n# Overview\n\nVarious objects that allow for sentinel-like guards for various purposes, includeing:\n\n- Easily create your own custom singletons/sentinels.\n- Use pre-created ones, such as:\n  - Default\n  - Null\n\n\n# Install\n\n```bash\n# via pip\npip install guards\n\n# via poetry\npoetry add guards\n```\n\n# Singleton Object\n\nAllows for creation of formal custom special sentinel types,\nsimilar to how `None` and `NoneType` are like.\nEnsures there can only ever be one instance, fi you try to allocate a new one or even try to \ncopy it, will still be the same single instance, no matter what.\n\nUsed for sentinel values `Null`, and `Default`, which are detailed further below in this readme..\n\nThe Singleton class can also easily be used as needed to create true singleton for other\npurposes than just being sentinels.\n\n## Singleton Example\n\nHere is an example of using Singleton to easily make a safe sentinel object:\n\n```python\nfrom guards import Singleton\nimport os\n\nclass DefaultType(Singleton):\n    pass\n\n# You can import this into other places and know there can only ever by one\n# instance of DefaultType (and so can safely use the `is` operator with it):\nDefault = DefaultType()\n\n# Ensures there can only ever by one \'instance\' of the Singleton subclass:\nassert Default is DefaultType()\n\n...\n\n# Example use Default Sentinel:\n\ndef my_method(some_param = Default):\n    # Can tell the difference between `None` and `Default` via sentinel object,\n    # So we can resolve the `Default` value however we wish that makes sense:\n    if some_param is Default:\n        some_param = os.environ.get("SOME_PARAM", None)\n    # Do something with `some_param`, now that any `Default` value has been resolved.\n    ...\n```\n\n# Null Object\n\nA sentinel object modeled after `None` called `Null`. \n\n`Null` evaluates as a `False`-like object. Its purpose is for when you need to know\nthe difference between Null and None, like for a dataclass that represents a JSON document.\n\nIf for example one needs to know if the value was absent from the JSON document vs the value being set to Null.\nFor a normal object, its simpler to have the attribute set to a Null or None value\nthen it is to remove the attribute entirely from the object that represents this theoretical\nJSON document.\n\n## Null Example\n\nHere is an example of using `Null`:\n\n```python\nfrom guards import Null\n\nclass SomeClass:\n    nullable_str = \'default-str\'\n    some_int = 3\n    \n    def json_dict(self):\n        json_dict = {}\n        if self.nullable_str is not None:\n            json_dict[\'nullable_str\'] = self.nullable_str\n        if self.some_int is not None:\n            json_dict[\'some_int\'] = self.some_int\n        \n        return {k: v if v is not Null else None for k, v in json_dict.items()}\n\nobj = SomeClass()\nobj.nullable_str = Null\nobj.some_int = None\n\n# When getting the json_dict value of object, the original None value in some_int is absent,\n# and None replaced the Null; which is what was intended.\n# Now when json_dict is converted to json-string, python will convert the `None` to json `null` value.\nassert obj.json_dict() == {\'nullable_str\': None}\n```\n\nIn the above example, we have a class that can have None or Null values, which control how\nthe object is in-turn represented in a json-dict value of its self.\n\n\n# Default Object\n\nA sentinel object modeled after `None` called `Default`. \n\n`Default` evaluates as a `False`-like object. Its purpose is for when you need to know\nif the caller set None on a method param or attribute vs not setting anything at all.\n\n\n\nIn other-words, if you need to know the difference between the user supplying a value of `None`\nor not supplying a value in the first place.\n\nWhen the user does not supply any value for an attribute or method parameter,\nthe underlying code that uses that value may want to supply a sensible default value\nto use instead.\n\nThe `Default` sentential value can help you do this easily.\n\n## Default Example\n\nHere is an example of using `Default`:\n\n```python\nfrom guards import Default\nimport os\n\ndef my_method(some_param = Default):\n    # Can tell the difference between `None` and `Default` via sentinel object,\n    # So we can resolve the `Default` value however we wish that makes sense:\n    if some_param is Default:\n        some_param = os.environ.get("SOME_PARAM", None)\n    # Do something with `some_param`, now that any `Default` value has been resolved.\n    ...\n```\n\nThe above example will attempt to lookup a default value via a environmental variable\nif the user does not pass anything into the function (ie: value for `some_param` is still at `Default`).\n\n\n\n# Licensing\n\nMIT\n',
    'author': 'Josh Orr',
    'author_email': 'josh@orr.blue',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xyngular/py-guards',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
