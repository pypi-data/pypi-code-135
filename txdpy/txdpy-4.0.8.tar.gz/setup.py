from distutils.core import setup

packages = ['txdpy']

setup(name='txdpy',
    version='4.0.8',
    author='唐旭东',
    install_requires=['mmh3','pymysql','loguru','redis','lxml'],
    packages=packages,
    package_dir={'requests': 'requests'})