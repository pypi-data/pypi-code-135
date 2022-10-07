# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['segal', 'segal.datasets', 'segal.strategies']

package_data = \
{'': ['*']}

install_requires = \
['albumentations>=1.3.0,<2.0.0',
 'matplotlib>=3.6.0,<4.0.0',
 'scipy>=1.8.0,<2.0.0',
 'segmentation-models-pytorch==0.3.0']

setup_kwargs = {
    'name': 'segal',
    'version': '0.1.0',
    'description': 'Sequence labeling active learning framework for Python',
    'long_description': '# SegAL\n\nSegAL is a semantice segmentation active learning tool.\n\n## Installation\n\nSegAL is available on PyPI:\n\n`pip install seqal`\n\nSegAL officially supports Python 3.8+.\n\n## Usage\n\n```\npython examples/run_al_cycle.py --dataset CamVid  --data_path ./data/CamVid/ --model_name Unet --encoder resnet34 --encoder_weights imagenet --num_classes 12 --strategy LeastConfidence --seed_ratio 0.02 --query_ratio 0.02 --n_epoch 1\n```',
    'author': 'Xu Liang',
    'author_email': 'liangxu006@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tech-sketch/SegAL',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
