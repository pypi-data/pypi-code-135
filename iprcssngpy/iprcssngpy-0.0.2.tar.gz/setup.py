from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    page_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='iprcssngpy',
    version="0.0.2",
    author='Romário Pereira Marinho',
    author_email='eng.romariopmarinho@gmail.com',
    description="Package creation and image processing study",
    long_description=page_description,
    long_description_content_type="text/markdown; charset=UTF-8;",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)
