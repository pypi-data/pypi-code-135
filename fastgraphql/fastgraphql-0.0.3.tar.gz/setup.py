# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastgraphql']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

extras_require = \
{'ariadne': ['ariadne>=0.16.1,<0.17.0'], 'fastapi': ['fastapi>=0.85.0,<0.86.0']}

setup_kwargs = {
    'name': 'fastgraphql',
    'version': '0.0.3',
    'description': 'FastGraphQL is intended to help developer create code driven GraphQL APIs',
    'long_description': '# FastGraphQL\nFastGraphQL is intended to help developer create code driven GraphQL APIs.\n\n![pypi](https://img.shields.io/pypi/v/fastgraphql)\n![Python Versions](https://img.shields.io/pypi/pyversions/fastgraphql.svg?color=%2334D058)\n![License](https://img.shields.io/pypi/l/fastgraphql)\n\n[![codecov](https://codecov.io/gh/hugowschneider/fastgraphql/branch/main/graph/badge.svg?token=FCC5LMA0IQ)](https://codecov.io/gh/hugowschneider/fastgraphql)\n![tests](https://github.com/hugowschneider/fastgraphql/actions/workflows/test.yaml/badge.svg)\n\n\n[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=bugs)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=hugowschneider_fastgraphql&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=hugowschneider_fastgraphql)\n\n# Disclaimer\n\n*This is still a work in progress*\n\n# Motivation\n\nSo far most of the projects that uses GraphQL need to duplicate\nmany definitions to be able to have a consistent GraphQL API schema \nalongside well-defined models that governs the development and the application.\n\nFastGraphQL tries to shortcut the path between python models and GraphQL schema\nusing **Pydantic** models. This ensures not only a single source of truth when comes to \ntype, inputs, query and mutation definition reflected in classes and methods, but also the\nability to use **Pydantic** to validate models.\n\n# Installation\n\n```commandline\npip install fastgraphql\n```\n\n\n# Usage\n\n## GraphQL Types and Inputs\n\nUsing annotation driven definitions and **Pydantic**, defining GraphQL types\nand inputs can be done by simple annotating **Pydantic** models with `FastGraphQL.graphql_type()`\nof `FastGraphQL.graphql_input()`\n\n```python\nfrom datetime import datetime\nfrom typing import Optional\nfrom pydantic import BaseModel\nfrom fastgraphql import FastGraphQL\n\nfast_graphql = FastGraphQL()\n\n@fast_graphql.graphql_type()\nclass Model(BaseModel):\n    t_int: int\n    t_opt_int: Optional[int]\n    t_str: str\n    t_opt_str: Optional[str]\n    t_float: float\n    t_opt_float: Optional[float]\n    t_datatime: datetime\n    t_opt_datatime: Optional[datetime]\n    t_boolean: bool\n    t_opt_boolean: Optional[bool]\n\n@fast_graphql.graphql_type()\nclass Input(BaseModel):\n    t_int: int\n    \nprint(fast_graphql.render())\n```\n\nThe above code example generates a schema as follows:\n\n```graphql\nscalar DateTime\n\ntype Model {\n    t_int: Int!\n    t_opt_int: Int\n    t_str: String!\n    t_opt_str: String\n    t_float: Float!\n    t_opt_float: Float\n    t_datatime: DateTime!\n    t_opt_datatime: DateTime\n    t_boolean: Boolean!\n    t_opt_boolean: Boolean\n}\n\ntype Input {\n    t_int: Int!\n}\n```\n\n## Query and Mutation\n\nFollowing the same approach with annotation driven defitions, query and mutations can\neasily be defined using `FastGraphQL.graphql_query` and `FastGraphQL.mutation`.\n\nNote that all function arguments annotated with `FastGraphQL.graphql_query_field`\nare considered to be input arguments for the GraphQL API and simples types and \n**Pydantic** models can be used and arguments and also as return type and they don\'t \nneed to be explicitly annotated.\n\n```python\nfrom fastgraphql import FastGraphQL\nfrom pydantic import BaseModel\nfast_graphql = FastGraphQL()\n\nclass Model(BaseModel):\n    param: str\n\n@fast_graphql.graphql_query()\ndef my_first_query(\n        model: Model = fast_graphql.graphql_query_field(),\n        param: str = fast_graphql.graphql_query_field()\n) -> str:\n    ...\n\nprint(fast_graphql.render())\n\n```\n\nThe above code example generates a schema as follows:\n\n```graphql\ninput Model {\n    param: String!\n}\ntype Query {\n    my_first_query(model: Model!, param: String!): String!\n}\n```\n\n# Dependecy Injection\nQuery and Mutation can have dependencies injected using `FastGraphQL.depende(...)` as showed bellow:`\n```python\nfrom fastgraphql import FastGraphQL\nfrom pydantic import BaseModel\nfast_graphql = FastGraphQL()\n\nclass Model(BaseModel):\n    param: str\n\ndef create_dependency() -> str:\n    return ""\n    \n@fast_graphql.graphql_query()\ndef my_first_query(\n        model: Model = fast_graphql.graphql_query_field(),\n        dependecy: str = fast_graphql.depends(create_dependency)\n) -> str:\n    ...\n\n```\nIn this example the parameter `dependecy` will be injected once the query is called. \n\n# Integrations\n\n## Ariadne\n...\n\n## FastAPI\n...\n\n# Acknowledgment\n\nThanks [FastAPI](https://fastapi.tiangolo.com) for inpirations',
    'author': 'Hugo Wruck Schneider',
    'author_email': 'hugowschneider@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hugowschneider/fastgraphql',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
