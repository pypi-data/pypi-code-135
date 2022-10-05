from importlib.metadata import entry_points
from setuptools import setup
import subprocess
import sys


def get_version():
    # get latest tag on branch
    result = subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(result.stderr.decode('utf-8'), file=sys.stderr)
        raise RuntimeError('Could not get version from git')
    return result.stdout.decode('utf-8').strip()


setup(name='auterion-cli',
    version=get_version(),
    description='CLI tool to interact with AuterionOS devices and apps',
    url='https://github.com/Auterion/auterion-cli',
    author='Auterion',
    author_email='support@auterion.com',
    license='proprietary',
    packages=['auterioncli'],
    install_requires=['tabulate', 'requests', 'docker'],
    python_requires='>=3.6',
    zip_safe=False,
    entry_points={
        'console_scripts': ['auterion-cli=auterioncli.main:main']
    })
