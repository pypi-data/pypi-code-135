from setuptools import setup, find_packages
import sys 
sys.path.append("./src/spdlogger/")
from version import __version__

setup(
    name="SPDLogger",
    version=__version__,
    package_dir={"": "src"},
    package_data={
        "spdlogger": ["config/*","config/.*"]
    },
    packages=find_packages(where='src',exclude=['tests*','example*']),
    python_requires = ">=3.6",
    # setup_requires = [
    #     "cython",
    #     "scipy==1.7.3",
    #     "pandas==1.3",
    # ],
    install_requires=[
        "sentry-sdk==1.9.3",
        "neptune-client==0.16.5",
        "dynaconf==3.1.9",
        "mlflow==1.27.0",
        "toml==0.10.2"
    ],
)
