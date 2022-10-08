from setuptools import setup, find_packages


setup(
    name='simplecoloredtext',
    version='0.2',
    license='MIT',
    author="J.Alejandro Cabrera Lindsay",
    author_email='alejupiter1994@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/alejup21/coloredtext',
    keywords='simple color text',
    install_requires=[
          'colorama',
      ],

)