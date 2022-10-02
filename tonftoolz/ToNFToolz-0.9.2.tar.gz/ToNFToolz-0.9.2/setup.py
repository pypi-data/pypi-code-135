from setuptools import setup, find_packages

requirements = []

with open("requirements.txt", "r") as rf:
    rf = rf.read()
    for rq in rf.split('\n'):
        requirements.append(rq)

setup(
    name='ToNFToolz',
    version='0.9.2',
    packages=find_packages(),
    url='',
    license='MIT',
    author='yungwine',
    author_email='cyrbatoff@gmail.com',
    description='Explore NFT Items in TON Blockchain',
    install_requires=requirements,
)
