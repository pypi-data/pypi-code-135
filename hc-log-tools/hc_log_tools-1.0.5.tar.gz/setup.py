from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

setup(
    packages=find_packages(),
    name="hc_log_tools",
    version="v1.0.5",
    author="xukai.shi",
    author_email="shixukai@163.com",
    install_reqs = parse_requirements('requirements.txt', session='hack'),
    entry_points={
        'console_scripts': [
            'hc_log_tools = src.entry:entry',
        ]
    },
)