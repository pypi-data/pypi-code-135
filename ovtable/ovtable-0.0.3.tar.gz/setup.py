import setuptools

with open("README.md", encoding="utf-8") as f:
    long_description = f.read().strip()

with open("./ovtable/__init__.py") as f:
    for line in f.readlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            version = line.split(delim)[1]
            break
    else:
        print("Can't find version! Stop Here!")
        exit(1)

def get_install_requires() -> str:
    return [
        "windows-curses ; sys_platform=='win32'"
    ]

setuptools.setup(
    name="ovtable",
    version=version,
    author="Piper Liu",
    author_email="piperliu@qq.com",
    description="based on curses, ovtable is a table displayed in the terminal with Python API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PiperLiu/ovtable",
    packages=setuptools.find_packages(
        exclude=[
            '*.tests',
            '*.tests.*',
            'tests.*',
            'tests',
            '*.examples',
            '*.examples.*',
            'examples.*',
            'examples',
        ]
    ),
    # for https://img.shields.io/pypi/pyversions
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    install_requires=get_install_requires(),
)
