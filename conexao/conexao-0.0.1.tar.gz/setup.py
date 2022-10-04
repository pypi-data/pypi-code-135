"""
Setup.
"""

import setuptools

setuptools.setup(
    name="conexao",
    version="0.0.1",
    description="A connection helper.",
    packages=setuptools.find_packages(exclude=["tests*"]),
    scripts=['bin/conexao'],
    # install_requires=[],
)
