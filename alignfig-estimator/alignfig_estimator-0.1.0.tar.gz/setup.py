from setuptools import setup, Extension, find_packages

#with open("README.md", "r") as readme_file:
#    readme = readme_file.read()

requirements = ['pandas', 'numpy', 'biopython', 'psutil', 'sklearn']

__version__ = "0.1.0"


setup(
    name="alignfig_estimator",
    version=__version__,
    author="Narek Engibaryan",
    author_email="narek030601@yandex.ru",
    #url="",
    description="Measuring and estimating tools operation time",
    #long_description=readme,
    #long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
