
from setuptools import setup

setup(
    name='shortkeygui',
    version=0.01,
    url='https://sribalaji.rf.gd',
    author='Balaji Santhanam',
    author_email='sribalaji2112@gmail.com',
    description=('ShortkeyGUI is an easy-to-use tool that can press a shortcut key. For Windows, macOS, and Linux, on Python 3 and 2.'),
    long_description=open('README.txt').read() + '\n\n' + open('documentation/index.rst').read() + '\n\n' + open('documentation/install.rst').read(),
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['shortkeygui'],
    test_suite='tests',
    install_requires=['uiaction'],
    keywords="ShortkeyPresser Created by SriBalaji shortcut key GUI",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
    ],
)