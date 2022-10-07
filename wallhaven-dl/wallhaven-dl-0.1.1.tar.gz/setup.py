import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wallhaven-dl",
    version="0.1.1",
    author="GeekOcean",
    author_email="liuyaanng@gmail.com",
    description="Download wallpaper from wallahaven.cc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liuyaanng/wallhaven-dl",
    packages=setuptools.find_packages(),
    install_requires=['PyYAML == 6.0', 'requests >= 2.21.0', 'rich == 12.6.0'
                      ],
    entry_points={
        'console_scripts': [
            'wallhaven_dl=wallhaven_dl:main'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
