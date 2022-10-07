from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='jwt_eddsa_base44',
    version='0.0.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Implementation of EdDSA JWT with base44 encoding",
    url='https://github.com/ocordeiro/jwt-eddsa-b44',
    author='ocordeiro',
    author_email='alan@cordeiro.me',
    license='MIT',
    package_dir={'':'src'},
    install_requires=["cryptography"]
)