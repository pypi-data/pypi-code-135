from setuptools import find_packages, setup

__version__ = "0.0.5"

setup(
    name='magic-eden-py',
    packages=['magic_eden', 'magic_eden.api'],
    version=__version__,
    description='Python wrap for NFT marketplace api MagicEden',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    project_urls={
        "Source Code": "https://github.com/ivannnnnnnnnn/magic-eden-py",
    },
    author='ivan.srshtn.crypto@gmail.com',
    license='MIT',
    install_requires=[
        'requests==2.26.0'
    ]
)
