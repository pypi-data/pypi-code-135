# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kinopoisk_dev', 'kinopoisk_dev.models']

package_data = \
{'': ['*']}

install_requires = \
['grequests>=0.6.0,<0.7.0', 'pydantic>=1.9.2,<2.0.0', 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'kinopoisk-dev',
    'version': '0.1.2',
    'description': 'Реализация Api для сервиса kinopoisk.dev',
    'long_description': '<div align="center">\n    <h1>Kinopoisk Dev Api</h1>\n    <p>Python-модуль для взаимодействия с неофициальным <a href="https://kinopoisk.dev/">API КиноПоиска</a></p>\n</div>\n\n### Установка\n\n```\n$ pip install kinopoisk-dev\n```\n\n### Получение токена\n\nДля получения токена необходимо перейти [kinopoisk.dev](https://kinopoisk.dev/documentation.html) и написать по\nконтактам.\n\n### Movie\n\nМетоды для работы с данными о фильмах\n\n#### Получить данные о фильме по Kinopoisk ID\n\nВозвращает информацию о фильме.\n\n* `Эндпоинт` - /movie\n* `Метод` - movie\n\n```python\nkp = KinopoiskDev(token=TOKEN)\ndata = kp.movie(field=Field.KP, search="301")\n```\n\n#### Получить данные о списке фильмов по Kinopoisk ID\n\nВозвращает информацию о списке фильмов\n\n* `Эндпоинт` - /movie\n* `Метод` - movie_ids\n\n```python\nkp = KinopoiskDev(token=TOKEN)\ndatas = kp.movie_ids(field=Field.KP,\n                     ids=["301", "1209527", "1400126", "1445165", "4489530", "4396744", "4963617", "1435399",\n                          "4400160", "4397602", \'542352345\', ])\n```\n\n### Параметры\n\n#### Field\n\n| Поля       | Значение   | Описание |\n| ---------- |:----------:| :-----|\n| KP    | id              | Поиск по id kinopoisk |\n| IMDB  | externalId.imdb | Поиск по id imdb |\n| TMDB  | externalId.tmdb | Поиск по id tmdb |',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/odi1n/kinopoisk_dev',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
