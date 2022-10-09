import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DGR-package",
    version="0.0.1",
    author="Anakha Ganesh",
    author_email="anakhag07@gmail.com",
    description="A DGR-finding package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/The-Paul-Lab/DGR_package.git",
    project_urls={
        "Bug Tracker": "https://github.com/The-Paul-Lab/DGR_package.git",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    package_data={"DGR_package":["data/*.hmm"]}
)
