from setuptools import setup, find_packages


setup(
    name='resistence',
    version='0.1',
    license='MIT',
    author="Aishik Das",
    author_email='aishik.das08@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='resistence'
)