# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['moonreader_tools',
 'moonreader_tools.datamodel',
 'moonreader_tools.finders',
 'moonreader_tools.finders.dropbox',
 'moonreader_tools.finders.fs',
 'moonreader_tools.parsers']

package_data = \
{'': ['*']}

install_requires = \
['dropbox<12.0']

entry_points = \
{'console_scripts': ['moon_tools = moonreader_tools.main:main']}

setup_kwargs = {
    'name': 'moonreader-tools',
    'version': '2.0.0',
    'description': 'Library allowing to work with MoonReader book formats.',
    'long_description': '[![Build Status](http://mrlokans.com/jenkins/job/moonreader_tools/badge/icon)](http://mrlokans.com/jenkins/job/moonreader_tools/)\n\nDescription - what, why and how\n===========\nThis library allows you to get basic data from Moon+Reader notes and statistics files either local or remote (Dropbox support is currently available).\n\n\n[Moon+Reader](https://play.google.com/store/apps/details?id=com.flyersoft.moonreader) is one of the best ebook readers I\'ve tried for Android OS with lots of functionality.\nThe features I use a lot are creating notes when reading books and having them syncronized with my dropbox account. One day I thought that it would be great to write a library for parsing those files and obtaining data from them, as a result this library is being developed. \n\nInstallation from source\n========================\nThis requires [poetry](https://python-poetry.org/) for the installation\n```bash\ngit clone https://github.com/MrLokans/MoonReader_tools\ncd MoonReader_tools\npoetry build && poetry install\n```\n\nInstallation from PyPI\n======================\n```bash\npip install moonreader_tools\n```\n\nUsage as CLI utility\n====================\nIt is assumed that you\'re the MoonReader+ Pro user and have Dropbox linked to your reader app.\nIf you\'re reading and creating highlights you\'ll be having lots of files in the syncronized folder (e.g. Dropbox/Books/.Moon+/Cache)\n\nTo get JSON data about all of your books you may use CLI entry to get data from dropbox or local folder:\n\n```bash\nmoon_tools --path <path/to/moonreader/cache> --output-file <outfile>.json\n\nmoon_tools --dropbox-token <DROPBOX TOKEN> --output-file <outfile>.json\n```\n\nUsage as library\n================\n\n```python\nimport dropbox\nfrom moonreader_tools.finders import FilesystemFinder, DropboxFinder\n\n# We may look for books in FS directories\nextractor = FilesystemFinder(path="/dir/with/moonreader/files")\nbooks = extractor.get_books()\nfor book in books:\n    print(book.title)\n    for note in book.notes:\n        print(note.text)\n\n# And in the dropbox\n\nclient = dropbox.Dropbox(access_token=\'MYSECRETTOKEN\')\nextractor = DropboxFinder(client, books_path=\'moonreader_save_dir\')\n\nbooks = extractor.get_books()\nfor book in books:\n    print(book.title)\n    for note in book.notes:\n        print(note.text)\n```\n\nRunning tests\n=============\n```\nmake test\n```\n\nFormatting codebase\n==============\n```\nmake format\n```',
    'author': 'MrLokans',
    'author_email': 'mrlokans@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MrLokans/MoonReader_tools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
