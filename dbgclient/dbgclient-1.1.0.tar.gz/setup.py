import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "dbgclient",
    version = "1.1.0",
    license = 'MIT',
    author = "DBG ID",
    author_email = "me@dbgidofficial.my.id",
    description = "a simple script to create bot using HTTP API",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = [
      "dbgid",
      "dbgid.core",
      "dbgid.utils",
      ],
    url = "https://gitlab.com/dbgid/dbgclient",
    keyword = ['Bot builder','http client'],
    install_requires = ['faker==14.2.0','requests==2.28.1','urllib3==1.26.12','bs4==0.0.1'],
    include_package_data = True,
    zip_safe = False,
    project_urls = {
        "issues": "https://gitlab.com/dbgid/dbgclient/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.9"
)