from setuptools import setup, find_packages

setup(
    name='hc_log_tools',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hc_log_tools = main:main',
        ]
    },
)