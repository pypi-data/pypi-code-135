from setuptools import setup, find_packages


setup(
    name='KS_Constants',
    version='1.0',
    license='MIT',
    author="Steven Su",
    author_email='ks2devteam@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/kerrigan-survival-team/ks_constants_pyi'
)