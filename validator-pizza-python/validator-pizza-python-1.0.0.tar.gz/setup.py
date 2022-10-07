import re
from setuptools import setup, find_packages

with open("validator_pizza_python/__init__.py", "r", encoding="utf-8") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="validator-pizza-python",
    version=version,
    packages=find_packages(),
    url="https://github.com/teixeirazeus/validator-pizza-python",
    project_urls={
        "Issue tracker": "https://github.com/teixeirazeus/validator-pizza-python/issues"
    },
    license="MIT",
    author="teixeirazeus",
    description="Validator Pizza Python is a library for validator.pizza which detects disposable email addresses.",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=["aiohttp", "requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
