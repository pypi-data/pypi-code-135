from setuptools import setup, find_packages

setup(
    name="messager_client",
    version="0.0.1",
    description="client_for_messeger",
    author="KolesnikIvan",
    packages=find_packages(),
    install_requires=["PyQt5", "sqlalchemy", "pycryptodome", "pycryptodomex"]
)
