from setuptools import setup, find_packages


setup(
    name='bubblesort_publish_pypi_medium',
    version='0.6',
    license='NIL',
    author="Vidyasagar Dandetikar",
    author_email='vidyasagarvidyasagar2002@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/vidyasagar777/bubblesort-publish-pypi',
    keywords='bubblesort project',
    install_requires=[
          'scikit-learn',
      ],

)