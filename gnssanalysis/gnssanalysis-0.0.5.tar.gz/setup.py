import setuptools

setuptools.setup(
    include_package_data=True,
    name="gnssanalysis",
    version="0.0.5",
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
        "plotext==4.2",
        "plotly",
        "pymongo",
        "pytest",
        "scipy",
        "tqdm",
        "unlzw",
    ],
)
