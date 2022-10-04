# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numword_georgia']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'numword-georgia',
    'version': '0.2.1',
    'description': 'Convert numbers to words in Georgian',
    'long_description': '# Numword Georgia\n\n* Converts numbers to words in Georgian\n* Supports number up to millions\n\n```text\nNumber 5909 is \'ხუთი ათას ცხრაას ცხრაი\'\nNumber 9999 is \'ცხრაი ათას ცხრაას ოთხმოცდაცხრამეტი\'\nNumber 7000 is \'შვიდი ათასი\'\nNumber 7707 is \'შვიდი ათას შვიდას შვიდი\'\nNumber 91 is \'ოთხმოცდათერთმეტი\'\n```\n\n## Examples\n\n```python\nfrom numword_georgia import translate\n\ntranslate(0)  # Returns "ნული"\ntranslate(16) # Returns "თექვსმეტი"\n```\n',
    'author': 'Sergei Blinov',
    'author_email': 'blinovsv@gmail.com',
    'maintainer': 'Sergei Blinov',
    'maintainer_email': 'blinovsv@gmail.com',
    'url': 'https://github.com/awnion/numword-georgia',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
