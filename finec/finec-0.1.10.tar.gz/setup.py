# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['finec']

package_data = \
{'': ['*']}

install_requires = \
['apimoex>=1.2.0,<2.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'folium>=0.2.1,<0.3.0',
 'httpx>=0.22.0,<0.23.0',
 'lxml>=4.9.1,<5.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'pandas==1.3.5',
 'pymongo>=4.1.1,<5.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'requests>=2.23.0,<3.0.0',
 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'finec',
    'version': '0.1.10',
    'description': 'Computational finance from Finec MGIMO',
    'long_description': '<!--\n\nServer unavailable outside Russia\n\n-->\n\n[![Tests](https://github.com/epogrebnyak/finec/actions/workflows/.pytest.yml/badge.svg)](https://github.com/epogrebnyak/finec/actions/workflows/.pytest.yml)\n[![Finec version](https://badgen.net/pypi/v/finec)](https://pypi.org/project/finec/)\n\n# finec\n\nFinancial data and financial computation utilities.\n\n## Demo application\n\n<https://share.streamlit.io/epogrebnyak/finec/main>\n\n## Installation\n\n```console\npip install git+https://github.com/epogrebnyak/finec.git\n```\n\n## Moscow Exchange (MOEX)\n\nDownload Moscow Exchange (MOEX) data for stocks, bonds, currencies and indices as pandas dataframes, CSV or Excel files.\n\n### Stocks\n\n```python\nfrom finec.moex import Stock, Index\n\n# What stocks are part of IMOEX index?\nIndex("IMOEX").composition()\n\n# General information about Aeroflot stock\nStock("AFLT").whoami()\n\n# Ozon stock price history, all dates and columns\nStock("OZON").get_history()\n\n# Yandex stock price, restricted by columns and start date\nStock("YNDX").get_history(columns=["TRADEDATE", "CLOSE"], start="2022-01-01")\n\n# Get dividend history from https://github.com/WLM1ke/poptimizer\nStock("GMKN").get_dividend()\n```\n\n### Bonds\n\n```python\nfrom finec.moex import Bond\n\n# Sistema 2027 bond price and yields from TQCB trading bord\nBond(ticker="RU000A0JXN21", board="TQCB").get_history()\n\n# What data columns are provided for trading history?\nBond(ticker="RU000A101NJ6", board="TQIR").provided_columns()\n```\n\n### Currencies\n\n```python\nfrom finec.moex import Currency, CURRENCIES\n\n# Tickers for usd, euro and yuan exchange rates\nUSDRUR = Currency(ticker=\'USD000UTSTOM\', board=\'CETS\')\nEURRUR = Currency(ticker=\'EUR_RUB__TOM\', board=\'CETS\')\nCNYRUR = Currency(ticker=\'CNYRUB_TOM\', board=\'CETS\')\n\n# USDRUR exchange rate starting 2020\nUSDRUR.get_history(start="2020-01-01")\n```\n\n### Lookup functions\n\n```python\nfrom finec.moex import whoami, find, traded_boards\n\n# General information about ticker\nwhoami("YNDX")\n\n# What boards does a security trade at?\ntraded_boards("MTSS")\n\n# Are there traded securities with *query_str* in description?\nfind(query_str="Челябинский", is_traded=True)\n```\n\n### Engines, markets and boards\n\n```python\nfrom finec.moex import get_engines, Engine, Market, Board\n\nengines = get_engines()\nprint(engines)\n\ne = Engine("forts")\ne.markets()\n\nm = Market(engine="stock", market="shares")\nm.traded_boards()\n\nb = Board(engine="stock", market="shares", board="TQBR")\n\n# trading volumes by board\nb.volumes()\n\n# list securitites by board\nb.securities()\n\n# last trading day quotes by board\nb.history()\n```\n\n### Yield curves\n\n```python\nfrom finec.yield_curve import YieldCurve, get_yields_from_cbr\n\ny = YieldCurve("2022-09-28")\nr1 = y.rate(t=1)\n# 830.2383903307176\n\nrs = get_yields_from_cbr("2022-09-28")\n# {\'0.25\': 8.2, \'0.50\': 8.19, \'0.75\': 8.23, \'1.00\': 8.3, \'2.00\': 8.74, \'3.00\': 9.22, \'5.00\': 9.91, \n#  \'7.00\': 10.27, \'10.00\': 10.5, \'15.00\': 10.69, \'20.00\': 10.8, \'30.00\': 10.9}\n```\n\n### More about MOEX data\n\nReferences:\n\n- MOEX API reference <https://iss.moex.com/iss/reference/?lang=en>\n- Developper manual (2016) <https://fs.moex.com/files/6523>\n\nNotes:\n\n- MOEX is very generious to provide a lot of data for free and without any registration or tokens.\n- MOEX API provided on "as is" basis and some parts are undocumented.\n- June 2022: MOEX statistics server not available for queries from Google Colab or Github Actions:\n  - must use local installation for development\n  - all remote tests on CI fail\n  - streamlit cloud does not start \n\n## Aknowledgements\n\n- We rely on `apimoex.ISSClient` and expertise developped within [apimoex project](https://github.com/WLM1ke/apimoex) by [@WLMike1](https://github.com/WLM1ke).\n- Dividend history relayed from <https://github.com/WLM1ke/poptimizer>\n',
    'author': 'Evgeniy Pogrebnyak',
    'author_email': 'e.pogrebnyak@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.13,<4.0.0',
}


setup(**setup_kwargs)
