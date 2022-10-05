from setuptools import setup
import KeyConfig

setup(
    name='KeyConfig',
    version=KeyConfig.__version__,    
    description='KeyConfig is a very simple module to read simple configuration files.',
    url='https://github.com/JHubi1/KeyConfig',
    author='JHubi',
    author_email='info@jh-web.xyz',
    license='APACHE LICENSE, VERSION 2.0',
    packages=['KeyConfig'],
    install_requires=[],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
    ],
)