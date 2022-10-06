from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='primeiropacotepypi_10_22',
    version='0.0.1',
    url='https://github.com/marco-112358/primeiropacotepypi_10_22',
    license='MIT License',
    author='Marco Aurélio',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='marcoaurelioandrade4@gmail.com',
    keywords='Pacote',
    description=u'Repositório para teste de publicação de pacote no PyPI',
    packages=['primeiropacotepypi_10_22'],
    install_requires=['numpy'],)