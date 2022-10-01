# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['span_extructure']

package_data = \
{'': ['*']}

extras_require = \
{':sys_platform != "darwin"': ['spacy>=3.4.1,<4.0.0'],
 ':sys_platform == "darwin"': ['spacy[apple]>=3.4.1,<4.0.0']}

entry_points = \
{'spacy_factories': ['make_span_extructure = '
                     'span_extructure:make_span_extructure']}

setup_kwargs = {
    'name': 'span-extructure',
    'version': '0.1.1',
    'description': 'A spaCy custom component to extract structural information from text using the SpanRuler and regex patterns.',
    'long_description': '# Span Extructure\n\n[![codecov](https://codecov.io/gh/mr-bjerre/span-extructure/branch/main/graph/badge.svg?token=MSMW9LZLA0)](https://codecov.io/gh/mr-bjerre/span-extructure)\n\nYou might think the name is mispelled but it ain\'t. It is a word play on [spaCy\'s](https://spacy.io/) `Span`, _extract_ and _structure_. `span_exctructure` is a spaCy component that builds upon `SpanRuler` and regex to extract structured information, e.g. dates, amounts with currency and multipliers etc.\n\n## Installation\n\n```\npip install span_extructure\n```\n\n## Usage\n\n```py\nimport spacy\n\nnlp = spacy.blank("en")\n\n# Optionally add config if varying from default values\nconfig = {\n    "overwrite": False,       # default: False\n    "rules": [\n        {\n            "patterns": [[{"SHAPE": "dd.dd.dddd"}]],\n            "extruct": r"(?P<day>[0-3]\\d).(?P<month>0[1-9]|1[0-2]).(?P<year>20[0-5]\\d|19\\d\\d)",\n            "label": "DATE",\n        }\n    ]\n}\nnlp.add_pipe("span_extructure", config=config)\n\ndoc = nlp("This date 21.04.1986 will be a DATE entity while the structured information will be extracted to `Span._.extructure`")\nfor e in doc.ents:\n    print(f"{e.text}\\t{e.label_}\\t{e._.extructure}")\n```\n\n```bash\n>>> 21.04.1986      DATE    {\'day\': \'21\', \'month\': \'04\', \'year\': \'1986\'}\n```\n',
    'author': 'Nicolai Bjerre Pedersen',
    'author_email': 'None',
    'maintainer': 'Nicolai Bjerre Pedersen',
    'maintainer_email': 'None',
    'url': 'https://github.com/mr-bjerre/span-extructure',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
