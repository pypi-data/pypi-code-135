from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    name="hc_log_tools",
    version="v1.0.4",
    author="xukai.shi",
    author_email="shixukai@163.com",
    entry_points={
        'console_scripts': [
            'hc_log_tools = src.entry:entry',
        ]
    },
)