import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="dataframetranslationscoring",  # Replace with your own username
    version="0.0.5",
    author="Nabil Berjaoui",
    author_email="nabil.berjaoui@adm.com",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    description="A translation quality package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dev.azure.com/ADM-Production-CorpIT1/Incremental%20Strategic%20Delivery/_git/ISD_Translation",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
