# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['invertedai', 'invertedai.simulators', 'invertedai.simulators.data']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0']

setup_kwargs = {
    'name': 'invertedai',
    'version': '0.0.3rc0',
    'description': 'Client SDK for InvertedAI',
    'long_description': '[pypi-badge]: https://badge.fury.io/py/invertedai.svg\n[pypi-link]: https://pypi.org/project/invertedai/\n\n\n[![Documentation Status](https://readthedocs.org/projects/inverted-ai/badge/?version=latest)](https://inverted-ai.readthedocs.io/en/latest/?badge=latest)\n[![PyPI][pypi-badge]][pypi-link]\n\n# InvertedAI\n## Overview\n<!-- start elevator-pitch -->\nInverted AI has trained cutting-edge realistic behavioral driving models that are human-like and close the SIM2Real. Our API provides access to these behavioral models and can be useful for several tasks in autonomous vehicle (AV) research and development.\n\n![](docs/images/top_camera.gif)\n<!-- end elevator-pitch -->\n\n# Get Started\n<!-- start quickstart -->\nIn this quickstart tutorial, you’ll run a simple sample AV simulation with Inverted AI Python API. Along the way, you’ll learn key concepts and techniques that are fundamental to using the API for other tasks. In particular, you will be familiar with two main Inverted AI models:\n\n- DRIVE\n- INITIALIZE\n\n## Quick Start\n- **Goolge Colab***: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/inverted-ai/invertedai-drive/blob/develop/examples/Colab-Demo.ipynb)\n\n- **Locally**: Download the \n<a href="https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/inverted-ai/invertedai/tree/master/examples" target="_blank">examples directory</a>, navigate to the unzipped directory in terminal and run \n\n```\npython3 -m venv .venv\nsource .venv/bin/activate\npip install --upgrade pip\npip install -r requirements.txt\n.venv/bin/jupyter notebook Drive-Demo.ipynb\n```\n\n## Installation\n\n[pypi-badge]: https://badge.fury.io/py/invertedai.svg\n[pypi-link]: https://pypi.org/project/invertedai/\n\nTo install use [![PyPI][pypi-badge]][pypi-link]:\n\n```bash\npip install invertedai\n```\n\n## Setting up\n\nImport the _invertedai_ package and set the API key with **add_apikey** method.\n\nRefer to the [product page](https://www.inverted.ai) to get your API key (or recharge for more tokens).\n\n```python\n\nimport invertedai as iai\niai.add_apikey("XXXXXXXXXXXXXX")\n```\n\n## Browse through available maps (location)\nInverted AI provides an assortment of diverse road configurations and geometries, including real-world locations and maps from simulators (CARLA, Huawei SMARTS, ...).\\\nTo search the catalog use **iai.available_maps** method by providing keywords\n```python\niai.available_maps("roundabout", "carla")\n```\n\nTo get information about a scene use **iai.get_map**.\n```python\niai.get_map**("CARLA:Town03:Roundabout")\n```\nThe scene information include the map in [Lanelet2](https://github.com/fzi-forschungszentrum-informatik/Lanelet2) format, map in JPEG format, maximum number of allowed (driveable) vehicles, latitude longitude coordinates (for real-world locations), id and list of traffic light and signs (if any exist in the map), etc.\n\n## INITIALIZE\nTo run the simulation, the map must be first populated with agents.\nInverted AI provides the **INITIALIZE**, a state-of-the-art model trained with real-life driving scenarios which can generate realistic positions for the initial state of the simulation.\\\nHaving realistic, complicated and diverse initial conditions are particularly crucial to observer interesting and informative interaction between the agents, i.e., the ego vehicle and NPCs (non-player characters).\n\nYou can use **INITIALIZE** in two modes:\n- _Initialize all agents_: generates initial conditions (position and speed) for all the agents including the ego vehicle\n```python\nresponse = iai.initialize(\n    location="CARLA:Town03:Roundabout",\n    agent_count=10,\n)\n```\n- _Initialize NPCs_: generates initial conditions (position and speed) only for the NPCs according to the provided state of the ego vehicle.\n```python\nresponse = iai.initialize(\n    location="CARLA:Town03:Roundabout",\n    agent_count=10,\n)\n```\n> _response_ is a dictionary of _states_, and _agent-attribute_  (_recurrent-states_ is also returned for compatibility with **drive**)\\\n> _response["states"]_ is a list of agent states, by default the first on the list is always the ego vehicle.\n\n## DRIVE\n**DRIVE** is Inverted AI\'s cutting-edge realistic driving model trained on millions of miles of traffic data.\nThis model can drive all the agents with only the current state of the environment, i.e., one step observations (which could be obtained from **INITIALIZE**) or with multiple past observations.\n```python\nresponse = iai.drive(\n    location="CARLA:Town03:Roundabout",\n    agent_attributes=response["attributes"],\n    states=response["states"],\n    recurrent_states=response["recurrent_states"],\n    traffic_states_id=response["traffic_states_id"],\n    steps=1,\n    get_birdviews=True,\n    get_infractions=True,\n)\n```\n>For convenience and to reduce data overhead, ***drive** also returns _recurrent-states_ which can be feedbacked to the model instead of providing all the past observations.\\\n>Furthermore, **drive** drive all the agents for $steps\\times \\frac{1}{FPS}$ where by default $FPS=10[frames/sec]$, should you require other time resolutions [contact us](mailto:info@inverted.ai).\n\n<!-- end quickstart -->\n',
    'author': 'Inverted AI',
    'author_email': 'info@inverted.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
