# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['verificadores']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyverificadordocs',
    'version': '0.2.0',
    'description': 'Programa para fazer a verificação de documentos nacionais.',
    'long_description': "# 🐍 Rastreador de Encomendas\n\n## Esse programa tem como seu intuito fazer a verificação de CPF e CNPJ.\n\n## Como utilizar?\n\n```shell\n$ pip install pyVerificadorDocs\n```\n\n```Python\nfrom verificadores import CPF, CNPJ\n\n\nasync def main():\n    resultado = CPF('000.000.000-00')\n    print(f'CPF é {resultado}')\n    resultado = CNPJ('00.000.000/0000-00')\n    print(f'CNPJ é {resultado}')\n\n\nmain()\n```\n\n### O que usamos na infraestrutura?\n\n- [Utilizamos a linguagem Python](https://www.python.org/)\n",
    'author': 'Diaszano',
    'author_email': 'lucasdiiassantos@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
