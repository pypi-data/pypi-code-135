# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tfyolo', 'tfyolo.configs', 'tfyolo.dataset', 'tfyolo.layers', 'tfyolo.models']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib',
 'optuna>=2.3.0,<3.0.0',
 'pandas>=1.3.0,<2.0.0',
 'scikit-learn>=0.24,<1.2',
 'scipy>=1.8,<2.0',
 'tensorflow>=2.4.1,<3.0.0']

setup_kwargs = {
    'name': 'tfyolo',
    'version': '0.0.1',
    'description': 'Series yolo detection in TensorFlow',
    'long_description': '[license-image]: https://img.shields.io/badge/license-Anti%20996-blue.svg\n[license-url]: https://github.com/996icu/996.ICU/blob/master/LICENSE\n[pypi-image]: https://badge.fury.io/py/tfts.svg\n[pypi-url]: https://pypi.python.org/pypi/tfts\n[build-image]: https://github.com/LongxingTan/Time-series-prediction/actions/workflows/test.yml/badge.svg?branch=master\n[build-url]: https://github.com/LongxingTan/Time-series-prediction/actions/workflows/test.yml?query=branch%3Amaster\n[docs-image]: https://readthedocs.org/projects/time-series-prediction/badge/?version=latest\n[docs-url]: https://time-series-prediction.readthedocs.io/en/latest/\n\n<h1 align="center">\n<img src="./docs/source/_static/logo.svg" width="490" align=center/>\n</h1><br>\n\n-------------------------------------------------------------------------\n\n[![LICENSE][license-image]][license-url]\n[![PyPI Version][pypi-image]][pypi-url]\n[![Build Status][build-image]][build-url]\n[![Docs Status][docs-image]][docs-url]\n\n**[Documentation](https://time-series-prediction.readthedocs.io)** | **[Tutorials](https://time-series-prediction.readthedocs.io/en/latest/tutorials.html)** | **[Release Notes](https://time-series-prediction.readthedocs.io/en/latest/CHANGELOG.html)** | **[中文](https://github.com/LongxingTan/Time-series-prediction/blob/master/README_CN.md)**\n\ntfyolo is a YOLO (You only look once) library implemented by TensorFlow2 <br>\n\n![demo](examples/data/sample/demo1.png)\n\n## Key Features\n- minimal Yolov5 by pure tensorflow2\n- yaml file to configure the model\n- custom data training\n- mosaic data augmentation\n- label encoding by iou or wh ratio of anchor\n- positive sample augment\n- multi-gpu training\n- detailed code comments\n- full of drawbacks with huge space to improve\n\n## Tutorial\n\n### prepare the data\n\n```\n$ bash data/scripts/get_voc.sh\n$ cd yolo\n$ python dataset/prepare_data.py\n```\n\n<!-- ### Download COCO\n```\n$ cd data/\n$ bash get_coco_dataset.sh\n``` -->\n\n### Clone and install requirements\n\n```\n$ git clone git@github.com:LongxingTan/Yolov5.git\n$ cd Yolov5/\n$ pip install -r requirements.txt\n```\n<!-- ### Download pretrained weights\n```\n$ cd weights/\n$ bash download_weights.sh\n``` -->\n\n### Train\n\n```\n$ python train.py\n```\n\n### Inference\n\n```\n$ python detect.py\n$ python test.py\n```\n\n### Train on custom data\n\nIf you want to train on custom dataset, PLEASE note the input data should like this:\n```\nimage_dir/001.jpg x_min, y_min, x_max, y_max, class_id x_min2, y_min2, x_max2, y_max2, class_id2\n```\nAnd maybe new anchor need to be created, don\'t forget to change the nc(number classes) in yolo-yaml.\n```\n$ python dataset/create_anchor.py\n```\n\n## Performance\n\n| Model | Size | AP<sup>val</sup> | AP<sub>50</sub><sup>val</sup> | AP<sub>75</sub><sup>val</sup> |  cfg | weights |\n| :-- | :-: | :-: | :-: | :-: | :-: | :-: |\n| YOLOV5s | 672 | 47.7% |52.6% | 61.4% | [cfg](https://github.com/WongKinYiu/PyTorch_YOLOv4/blob/master/cfg/yolov4.cfg) | [weights](https://drive.google.com/file/d/137U-oLekAu-J-fe0E_seTblVxnU3tlNC/view?usp=sharing) |\n| YOLOV5m | 672 | 47.7% |52.6% | 61.4% | [cfg](https://github.com/WongKinYiu/PyTorch_YOLOv4/blob/master/cfg/yolov4.cfg) | [weights](https://drive.google.com/file/d/137U-oLekAu-J-fe0E_seTblVxnU3tlNC/view?usp=sharing) |\n| YOLOV5l | 672 | 47.7% |52.6% | 61.4% | [cfg](https://github.com/WongKinYiu/PyTorch_YOLOv4/blob/master/cfg/yolov4.cfg) | [weights](https://drive.google.com/file/d/137U-oLekAu-J-fe0E_seTblVxnU3tlNC/view?usp=sharing) |\n| YOLOV5x | 672 | 47.7% |52.6% | 61.4% | [cfg](https://github.com/WongKinYiu/PyTorch_YOLOv4/blob/master/cfg/yolov4.cfg) | [weights](https://drive.google.com/file/d/137U-oLekAu-J-fe0E_seTblVxnU3tlNC/view?usp=sharing) |\n|  |  |  |  |  |  |  |\n\n\n## Citation\n\nIf you find tf-yolo project useful in your research, please consider cite:\n\n```\n@misc{tfyolo2021,\n    title={TFYOLO: yolo series benchmark in tensorflow},\n    author={Longxing Tan},\n    howpublished = {\\url{https://github.com/longxingtan/tfyolo}},\n    year={2021}\n}\n```\n',
    'author': 'Longxing Tan',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://tfyolo.readthedocs.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
