# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chapter_marker', 'fakenotify2']

package_data = \
{'': ['*'], 'chapter_marker': ['res/*']}

install_requires = \
['docopt', 'notify2', 'pynput', 'pyqt5', 'requests']

entry_points = \
{'console_scripts': ['bgt-current-show = chapter_marker.bgt_current_show:main',
                     'bgt-get-titles = chapter_marker.bgt_get_titles:main',
                     'bgt-replace-text = chapter_marker.bgt_replace_text:main',
                     'chapter-marker = chapter_marker.tray:main']}

setup_kwargs = {
    'name': 'chapter-marker',
    'version': '1.0.2',
    'description': 'chapter-marking utility',
    'long_description': '# Chapter-marker\n\nWrite a chaptermark file for your podcast. The focus is the [binaergewitter podcast](https://blog.binaergewitter.de)\nChapter-marker is to be used with hotkeys.\n\n\n## Installation\n\n```bash\npip install chapter-marker\n```\n\n## Workflow\n\n### For Binärgewitter\n```\nexport PAD_APIKEY=<add-apikey-for-pad-here> \n\nCURRENT_SHOW=$(bgt-current-show)\nshowtitles="titles${CURRENT_SHOW}.lst"\nbgt-get-titles "${CURRENT_SHOW}" > "$showtitles"\n\nchapter-marker "$showtitles" "${CURRENT_SHOW}"\n# ctrl-j -> start the show at "H" of Hallihallo, also start next chapter\n# check by clicking left on the tray icon which is the next chapter\n\n# finish up the show by right clicking on the tray and choose [save] \n# the chapter mark file is now stored at ~/.local/share/chapter-marker/${CURRENT_SHOW}_chapters.txt\n```\n\n## Development\n\n### NixOS\n\n```bash\nnix-shell\n# or build and test the whole thing\nnix-build\nresult/bin/chapter-marker\n```\n\n\n### Legacy OS\n\nRequires python headers:\n\n```bash\nsudo dnf install python3-devel\nsudo apt install python3-dev\n```\n\n```bash\npoetry install\npoetry run chapter-marker "$showtitles" "${CURRENT_SHOW}"\n```\n\n# License\nSource Code under MIT (see `License`)\n\nThe Icons are Licensed under Apache 2.0, from https://github.com/Templarian/MaterialDesign/\n',
    'author': 'Felix Richter',
    'author_email': 'github@krebsco.de',
    'maintainer': 'Felix Richter',
    'maintainer_email': 'github@krebsco.de',
    'url': 'https://github.com/Binaergewitter/chapter-marker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
