# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['melvil_booklist',
 'melvil_booklist.appFile',
 'melvil_booklist.book',
 'melvil_booklist.booklist',
 'melvil_booklist.helper',
 'melvil_booklist.reading',
 'melvil_booklist.search']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'inquirer>=2.10.0,<3.0.0',
 'python-Levenshtein>=0.12.2,<0.13.0',
 'regex>=2022.8.17,<2023.0.0',
 'requests>=2.28.1,<3.0.0',
 'thefuzz>=0.19.0,<0.20.0',
 'tqdm>=4.64.0,<5.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['melvil = melvil.main:app']}

setup_kwargs = {
    'name': 'melvil-booklist',
    'version': '1.0.0',
    'description': '',
    'long_description': '# Melvil\n\n[//]: <> (TODO: Add quote from Melvil Dewey here)\n\n## The Command-line Book Management Tool\n\nMelvil is a command line tool for managing books and booklists.\n\nInstall with `pip install booklist-melvil`\n\n### Dependencies:\n\n* `python`\n* `typer`\n* `thefuzz`\n\n## Features:\n\nMelvil stores your books in a JSON file. Each book contains information about:\n\n* A title\n* An author\n* A series of tags that describe its genre \n* A state of being read\n* A priority (Position in the list)\n\nThere are many features that make your life easier:\n\n* Smooth command line interaction with [Typer](https://github.com/tiangolo/typer) and [Inquirer](https://github.com/kazhala/InquirerPy)\n* Fuzzy searching for book titles for nearly all commands, so you don\'t have to type the whole title every time. Don\'t remember a title name? No problem, fuzzy search by tag is available, too.\n* Flags for more common commands allow the user to define how much info they want Melvil to track.\n\n[//]: <> (TODO: Insert video demonstrating Melvil\'s features. You\'ll want a short GIF here similar to what you did for the time tracker, but you might also want to record a full-length video to better demonstrate your work.)\n\n### Commands:\n\n* `init` makes a new book list\n* `add` adds a new book\n* `remove` gets rid of a book\n* `list` prints out all the books from greatest to least priority\n* `skim` lists the attributes of a book\n* `untag` removes the target tag from the given book\n* `lookup` searches by title\n* `compile` searches by tag\n* `delete` clears the booklist\n* `reading` delivers the book you are reading now, defined as the book with the highest priority in the reading states.\n* `next` delivers the book you want to read next, defined as the book with the highest priority in the "to-read" state.\n* `change` Changes one of the book\'s attributes. Use "change --help" for more.\n* `transcribe` Add books from a CSV file in the format of "book title", "book author" to the book list.\n* `classify` Prints list of all tags.\n* `count` Prints list length.',
    'author': 'Sean',
    'author_email': 'sean14520@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
