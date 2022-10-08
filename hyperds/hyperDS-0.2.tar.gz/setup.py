
from setuptools import setup, find_packages

classifiers = ['License :: OSI Approved :: MIT License', 'Development Status :: 4 - Beta', 'Intended Audience :: Developers', 'Programming Language :: Python :: 3']
setup(
    name='hyperDS',
    version='0.2',
    description='HyperDS is used to store data similar to python representation (like json and xml) and also can store python objects like CLASSES!',
    long_description='''


Copyright 2022 AbdulWahab

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                          
                          ''',
    url='',
    author='AbdulWahab',
    author_email='undeadneon2008@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['pickle'],
    packages=find_packages(),
    install_requires=[]
)
