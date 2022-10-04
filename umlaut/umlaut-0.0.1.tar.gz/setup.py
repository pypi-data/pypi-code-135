# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['umlaut', 'umlaut.model_helpers']

package_data = \
{'': ['*']}

install_requires = \
['mlflow==1.28.0']

setup_kwargs = {
    'name': 'umlaut',
    'version': '0.0.1',
    'description': 'Umlaut is a library for training and querying ML models',
    'long_description': '# uMLaut\n\nThe uMLaut library simplifies model deployment and querying. It provides a single\naccess point for all of your organizations models and an interface to interact with all of them in the same way. Umlaut `models` can be as extensive as deep learning models or as simple as a reusable code block.\n\n- Simple model lifecycle management\n- Easily maintain and access multiple versions of the same model\n- Quickly share business logic in reusable modules\n- User interface with `MLflow`\n- Audit tracking history (roadmap)\n- Auto-deployed models that can be queried through an API (roadmap)\n\n____\n## Umlaut Class\nA Python class to assist with saving and querying business logic.\n\n- `track_model`: Converts a block of business logic into an Umlaut compatible `model`\n- `query_model`: Queries a previously trained `model` and saves audit metadata\n- `track_dataset`: Saves reporting datasets along with the initial query and underlying data that built it (roadmap)\n- `audit_model (roadmap)`: Retrieve the results of a model run for a historic date\n- `audit_dataset (roadmap)`: Retrieve a dataset as it was on a historic date\n\n### Developing models with Umlaut\nCustom `models` can be saved from any repository. Ensure the code block is in a Python `Class` and follow the example below.\n\n```\nfrom umlaut.core import Umlaut\n\nclass ExampleModel():\n    """Example business logic that can be wrapped into a model.\n       The class _must_ contain a \'predict\' method.\n    """\n    def business_logic(self, record: dict) -> bool:\n        if record.get("sales") > 5:\n            return True\n        else:\n            return False\n\n    def predict(self, model_input: dict) -> bool:\n        return self.business_logic()\n\nif __name__ == "__main__":\n    from umlaut.core import Umlaut\n\n    model = Umlaut(model_name="example model")\n    model.track_model(ExampleModel())\n```\n\nThis will push the latest changes of `ExampleModel()` to MLflow as a new model version. Navigate to the MLflow Tracking Server to find the latest push and associate it to the MLflow model.\n',
    'author': 'Andrew Dunkel',
    'author_email': 'andrew.dunkel1@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/andrewdunkel/uMLaut',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.12,<4.0',
}


setup(**setup_kwargs)
