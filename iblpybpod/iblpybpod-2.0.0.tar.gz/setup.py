import sys
from pathlib import Path

from setuptools import setup, find_packages

IBLPYBPOD_CURRENT_VERSION = "2.0.0"
CURRENT_DIRECTORY = Path(__file__).parent
CURRENT_PYTHON_VERSION = sys.version_info[:2]
REQUIRED_PYTHON_VERSION = (3, 8)
VER_ERR_MSG = """
==========================
Unsupported Python version
==========================
This version of iblutil requires Python {}.{}, but you're trying to
install it on Python {}.{}.
"""
if CURRENT_PYTHON_VERSION < REQUIRED_PYTHON_VERSION:
    sys.stderr.write(VER_ERR_MSG.format(*REQUIRED_PYTHON_VERSION + CURRENT_PYTHON_VERSION))
    sys.exit(1)

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    require = [x.strip() for x in f.readlines() if not x.startswith('git+')]

setup(
    name='iblpybpod',
    version=IBLPYBPOD_CURRENT_VERSION,
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON_VERSION),
    description='IBL implementation of pybpod software',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='IBL Staff',
    url='https://github.com/int-brain-lab/iblpybpod/',
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=['scratch', 'tests']),  # same as name
    include_package_data=True,
    install_requires=require,
    entry_points={"console_scripts": ["start-pybpod=pybpodgui_plugin.__main__:start"]},
    scripts=[]
)
