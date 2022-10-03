# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['second_opinion_ruler']

package_data = \
{'': ['*']}

extras_require = \
{':sys_platform != "darwin"': ['spacy>=3.4.1,<4.0.0'],
 ':sys_platform == "darwin"': ['spacy[apple]>=3.4.1,<4.0.0']}

entry_points = \
{'spacy_factories': ['make_second_opinion_ruler = '
                     'second_opinion_ruler:make_second_opinion_ruler']}

setup_kwargs = {
    'name': 'second-opinion-ruler',
    'version': '0.1.0',
    'description': 'A spaCy custom component that extends the SpanRuler with a second opinion',
    'long_description': '# Second Opinion Ruler\n\n`second_opinion_ruler` is a [spaCy](https://spacy.io/) component that extends [`SpanRuler`](https://spacy.io/usage/rule-based-matching#spanruler) with a second opinion. For _each_ pattern you can provide a callback (available in [`registry.misc`](https://spacy.io/api/top-level/#registry)) on the matched [`Span`](https://spacy.io/api/span/#_title) - with this you can decide to discard the match, add additional spans to the match and/or mutate the matched span, e.g. add a parsed `datetime` to a custom attribute.\n\n## Installation\n\n```\npip install second_opinion_ruler\n```\n\n## Usage\n\n```python\nimport spacy\nfrom spacy.tokens import Span\nfrom spacy.util import registry\n\n# create date as custom attribute extension\nSpan.set_extension("date", default=None)\n\n# add datetime parser to registry.misc\n# IMPORTANT: first argument has to be Span and the return type has to be list[Span]\n@registry.misc("to_datetime.v1")\ndef to_datetime(span: Span, format: str, attr: str = "date") -> list[Span]:\n\n    # parse the date\n    date = datetime.datetime.strptime(span.text, format)\n\n    # add the parsed date to the custom attribute\n    span._.set(attr, date)\n\n    # just return matched span\n    return [span]\n\n# load a model\nnlp = spacy.blank("en")\n\n# add the second opinion ruler\nruler = nlp.add_pipe("second_opinion_ruler", config={\n    "validate": True,\n    "annotate_ents": True,\n})\n\n# add a pattern with a second opinion handler (on_match)\nruler.add_patterns([\n    {\n        "label": "DATE",\n        "pattern": "21.04.1986",\n        "on_match": {\n            "id": "to_datetime.v1",\n            "kwargs": {"format": "%d.%m.%Y", "attr": "my_date"},\n        },\n    }\n])\n\ndoc = nlp("This date 21.04.1986 will be a DATE entity while the structured information will be extracted to `Span._.extructure`")\n\n# verify\nassert doc.ents[0]._.date == datetime.datetime(1986, 4, 21)\n```\n',
    'author': 'Nicolai Bjerre Pedersen',
    'author_email': 'None',
    'maintainer': 'Nicolai Bjerre Pedersen',
    'maintainer_email': 'None',
    'url': 'https://github.com/mr-bjerre/second-opinion-ruler',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
