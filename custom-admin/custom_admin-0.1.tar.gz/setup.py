from setuptools import setup

from custom_admin import name, __version__

author = "avryhof"

readme = open("README.md").read()

setup(
    name=name,
    version=__version__,
    packages=[name],
    include_package_data=True,
    url=f"https://github.com/{author}/{name}",
    project_urls={
        "GitHub Repo": f"https://github.com/{author}/{name}",
    },
    license="MIT",
    author="Amos Vryhof",
    author_email="amos@vryhofresearch.com",
    description="A base toolkit for building a custom Django amin theme.",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=["Django", "bleach"],
)
