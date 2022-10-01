# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lohrasb',
 'lohrasb.abstracts',
 'lohrasb.base_classes',
 'lohrasb.decorators',
 'lohrasb.examples',
 'lohrasb.factories',
 'lohrasb.mediators',
 'lohrasb.utils']

package_data = \
{'': ['*']}

install_requires = \
['catboost>=1.0.6,<2.0.0',
 'category-encoders>=2.5.0,<3.0.0',
 'feature-engine>=1.4.1,<2.0.0',
 'imblearn>=0.0,<0.1',
 'lightgbm>=3.3.2,<4.0.0',
 'nox>=2022.1.7,<2023.0.0',
 'numpy>=1.20,<2.0',
 'optuna>=2.10.1,<3.0.0',
 'pandas>=1.4,<2.0',
 'scipy>=1.5,<2.0',
 'sklearn>=0.0,<0.1',
 'xgboost>=1.6.1,<2.0.0']

setup_kwargs = {
    'name': 'lohrasb',
    'version': '1.4.0',
    'description': 'Using optuna search optimizer to estimate best tree based estimator compatible with scikit-learn',
    'long_description': '# lohrasb\n\nlohrasb is a package built to ease machine learning development. It uses [Optuna](https://optuna.readthedocs.io/en/stable/index.html), [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html), and [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html) to tune most of the tree-based estimators of sickit-learn. It is compatible with [scikit-learn](https://scikit-learn.org) pipeline.\n\n\n## Introduction\n\nBaseModel of the Lohrasb package can receive various parameters. From an estimator class to its tunning parameters and GridsearchCV, RandomizedSearchCV, or Optuna to their parameters. Samples will be split to train and validation set, and then optimization will estimate optimal related parameters using these optimizing engines.\n\n## Installation\n\nlohrasb package is available on PyPI and can be installed with pip:\n\n```sh\npip install lohrasb\n```\n\n\n## Supported estimators for this package\nAlmost all machine learning estimators for classification and regression supported by Lohrasb.\n\n## Usage\n\n- Tunning best parameters of a machine learning model using [Optuna](https://optuna.readthedocs.io/en/stable/index.html) , [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) or [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html).\n\n## Factories\nFor ease of use of BestModel, some factories are available to build associated instances corresponding to each optimization engine. For example, the following factory can be used for  GridSearchCV:\n\n```\nobj = BaseModel.bestmodel_factory.using_gridsearch(\n            estimator=XGBClassifier(),\n            estimator_params = {\n                "eval_metric": ["auc"],\n                "max_depth": [4, 5],\n            },\n            measure_of_accuracy="f1_score",\n            verbose=3,\n            n_jobs=-1,\n            random_state=42,\n            cv=KFold(2),\n        )\n```\n\n## One example : Computer Hardware \n\n#### Import some required libraries\n```\nfrom lohrasb.best_estimator import BaseModel\nimport xgboost\nfrom optuna.pruners import HyperbandPruner\nfrom optuna.samplers._tpe.sampler import TPESampler\nfrom sklearn.model_selection import KFold,train_test_split\nimport pandas as pd\nimport numpy as np\nimport optuna\nfrom sklearn.pipeline import Pipeline\nfrom feature_engine.imputation import (\n    CategoricalImputer,\n    MeanMedianImputer\n    )\nfrom category_encoders import OrdinalEncoder\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import (\n    classification_report,\n    confusion_matrix,\n    f1_score)\nfrom sklearn.metrics import f1_score, mean_absolute_error,r2_score\nfrom sklearn.linear_model import *\nfrom sklearn.svm import *\nfrom xgboost import *\nfrom sklearn.linear_model import *\nfrom catboost import *\nfrom lightgbm import *\nfrom sklearn.neural_network import *\nfrom imblearn.ensemble import *\nfrom sklearn.ensemble import *\n\n```\n#### Computer Hardware Data Set (a regression problem)\n  \nhttps://archive.ics.uci.edu/ml/datasets/Computer+Hardware\n\n```\nurldata= "https://archive.ics.uci.edu/ml/machine-learning-databases/cpu-performance/machine.data"\n# column names\ncol_names=[\n    "vendor name",\n    "Model Name",\n    "MYCT",\n    "MMIN",\n    "MMAX",\n    "CACH",\n    "CHMIN",\n    "CHMAX",\n    "PRP"\n]\n# read data\ndata = pd.read_csv(urldata,header=None,names=col_names,sep=\',\')\ndata\n```\n#### Train test split\n\n```\nX = data.loc[:, data.columns != "PRP"]\ny = data.loc[:, data.columns == "PRP"]\ny = y.values.ravel()\n\n\nX_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.33, random_state=42)\n\n```\n#### Find feature types for later use\n\n```\nint_cols =  X_train.select_dtypes(include=[\'int\']).columns.tolist()\nfloat_cols =  X_train.select_dtypes(include=[\'float\']).columns.tolist()\ncat_cols =  X_train.select_dtypes(include=[\'object\']).columns.tolist()\n```\n\n####  Define estimator and set its arguments  \n```\nestimator = LinearRegression()\nestimator_params= {\n        "fit_intercept": [True, False],\n    }\n```\n#### Use factory\n\n```\nobj = BaseModel.bestmodel_factory.using_optuna(\n            estimator=estimator,\n            estimator_params=estimator_params,\n            measure_of_accuracy="r2_score",\n            verbose=3,\n            n_jobs=-1,\n            random_state=42,\n            # optuna params\n            # optuna study init params\n            study=optuna.create_study(\n                storage=None,\n                sampler=TPESampler(),\n                pruner=HyperbandPruner(),\n                study_name=None,\n                direction="maximize",\n                load_if_exists=False,\n                directions=None,\n            ),\n            # optuna optimization params\n            study_optimize_objective=None,\n            study_optimize_objective_n_trials=10,\n            study_optimize_objective_timeout=600,\n            study_optimize_n_jobs=-1,\n            study_optimize_catch=(),\n            study_optimize_callbacks=None,\n            study_optimize_gc_after_trial=False,\n            study_optimize_show_progress_bar=False,\n        )\n```\n####  Build sklearn pipeline\n```\npipeline =Pipeline([\n            # int missing values imputers\n            (\'intimputer\', MeanMedianImputer(\n                imputation_method=\'median\', variables=int_cols)),\n            # category missing values imputers\n            (\'catimputer\', CategoricalImputer(variables=cat_cols)),\n            #\n            (\'catencoder\', OrdinalEncoder()),\n            # regression model \n            (\'obj\', obj),\n\n\n ])\n\n```\n#### Run Pipeline\n\n```\npipeline.fit(X_train,y_train)\ny_pred = pipeline.predict(X_test)\n```\n#### Check performance of the pipeline\n\n```\nprint(\'r2 score : \')\nprint(r2_score(y_test,y_pred))\n```\n\nThere are some examples  available in the [examples](https://github.com/drhosseinjavedani/lohrasb/tree/main/lohrasb/examples). \n\n## License\nLicensed under the [BSD 2-Clause](https://opensource.org/licenses/BSD-2-Clause) License.',
    'author': 'drhosseinjavedani',
    'author_email': 'h.javedani@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/drhosseinjavedani/lohrasb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
