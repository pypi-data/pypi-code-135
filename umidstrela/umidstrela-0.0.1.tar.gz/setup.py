from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='umidstrela',
    version='0.0.1',
    description='Convert csv to txt',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Umidyor Asomov',
    author_email='actualnew001@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='coverted_data',
    packages=find_packages(),
    install_requires=['']
)