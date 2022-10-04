import setuptools

setuptools.setup(
    include_package_data=True,
    name="gnssanalysis",
    version="0.0.4",
    description="basic python module for gnss analysis",
    author="Geoscience Australia",
    author_email="GNSSAnalysis@ga.gov.au",
    packages=setuptools.find_packages(),
    install_requires=[
        "boto3",
        "click",
        "matplotlib",
        "numpy",
        "pandas",
        "plotext",
        "pytest",
        "scipy",
        "tqdm",
        "unlzw@git+https://github.com/bmatv/python-unlzw.git",
    ],
)
