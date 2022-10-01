import setuptools

setuptools.setup(
    name='Indrajeet',
    version='0.1',
    author="Indrajeet Singh Yadav",
    author_email="inderjityadav93@gmail.com",
    description="My Personal Package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="Proprietary",
    url="https://github.com/javatechy/dokr",
    packages=setuptools.find_packages(),
    # py_modules=['my_modules'],
    install_requires=[
        'numpy>=1.19.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: Other/Proprietary License',
        "Operating System :: OS Independent",
    ],
 )