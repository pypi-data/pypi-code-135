from setuptools import setup, find_packages


setup(
    name='groupcrawler',
    version='0.7',
    license='MIT',
    author="Jose Enriquez",
    author_email='joseaenriqueza@hotmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://dev.azure.com/joseaenriqueza/_git/groupcrawler',
    keywords='example project',
    install_requires=[
          'pandas',
      ],

)
