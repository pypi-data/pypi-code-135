# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['astronomer', 'astronomer.aeroscope', 'astronomer.aeroscope.plugins']

package_data = \
{'': ['*'], 'astronomer.aeroscope.plugins': ['templates/*']}

entry_points = \
{'airflow.plugins': ['aeroscope = '
                     'astronomer.aeroscope.plugins:AeroscopePlugin']}

setup_kwargs = {
    'name': 'astronomer-aeroscope',
    'version': '0.9.1',
    'description': 'An Airflow Plugin and Operator for alternative methods of running Telescope',
    'long_description': '# Astronomer Aeroscope Provider\n\nThe Astronomer Aeroscope Provider contains a Plugin and Operator from Astronomer. \nThese provide a method to run Telescope in environments where other methods are unavailable \n\n## Installation\nAdd the following line to your `requirements.txt` in your source environment:\n```text\nastronomer-aeroscope\n```\n\n## Usage Option 1) Plugin Usage\n- Navigate to the top navigation bar in your Source Airflow environment.\n- Click the `Astronomer` menu, then `Run Report`\n\n## Usage Option 2) Operator Usage\n- Add the following DAG to your source Airflow environment\n```python\nfrom datetime import datetime\n\nfrom airflow.models import DAG\nfrom astronomer.aeroscope.operators import AeroscopeOperator\n\nwith DAG(\n  dag_id="astronomer_aeroscope",\n  schedule_interval=None,\n  start_date=datetime(2021, 1, 1),\n) as dag:\n  AeroscopeOperator(\n      task_id="run_report",\n      presigned_url=\'{{ dag_run.conf["presigned_url"] }}\',\n      organization=\'{{ dag_run.conf["organization"] }}\',\n  )\n```\n- Trigger the `astronomer_aeroscope` DAG with the configuration given by your Astronomer Representative\n\n```\n{\n\t"presigned_url": "presigned-url-here",\n\t"organization": "organization-name-here"\n}\n```\n',
    'author': 'telescope',
    'author_email': 'cse@astronomer.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3',
}


setup(**setup_kwargs)
