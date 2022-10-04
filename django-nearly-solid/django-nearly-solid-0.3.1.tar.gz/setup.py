from setuptools import setup, find_packages

version = '0.3.1'

packages = find_packages()

with open("../README.md", "r") as file:
    long_description = file.read()

setup(
    name='django-nearly-solid',
    version=version,
    author="Artem Romanukov",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    packages=packages,
    requires=[
        'django',
        'pydantic',
    ],
    url="https://github.com/romanukov/django-nearly-solid",
)
