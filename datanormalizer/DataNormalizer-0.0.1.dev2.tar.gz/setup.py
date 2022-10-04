import setuptools
import DataNormalizer

with open("requirements.txt", "r", encoding="utf-8") as file:
    requirements = [i.strip() for i in file if i.strip()]

with open("README.md") as file:
        readme = file.read()

setuptools.setup(
    name="DataNormalizer",
    description=DataNormalizer.__doc__,
    author=DataNormalizer.__author__,
    author_email=DataNormalizer.__email__,
    license=DataNormalizer.__license__,
    version=DataNormalizer.__version__,
    keywords="data DataNormalizer",
    long_description=readme,
    packages = ['DataNormalizer'],
    install_requires=requirements
)