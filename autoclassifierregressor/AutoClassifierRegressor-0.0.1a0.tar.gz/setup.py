from setuptools import setup, find_packages


REQUIREMENTS = ['time', 'pandas', 'numpy', 'sklearn',
                'xgboost', 'lightgbm', 'tensorflow', 'keras', 'catboost']


# calling the setup function
setup(name='AutoClassifierRegressor',
      version='0.0.1a',
      description='Analysis of all algorithms',
      long_description='Implementation of all important classifiers and regressors',
      url='https://github.com/anagha-bhople/auto_classifier_regressor',
      author='Anagha Bhople',
      author_email='bhoplea34@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=REQUIREMENTS,
      keywords='ML classifier regressor neural network sklearn analysis'
      )
