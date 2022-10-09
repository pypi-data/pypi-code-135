from setuptools import setup

setup(
    name='downdroid',
    description='A CLI tool to download android versions',
    author="Dpbm",
    url="https://github.com/Dpbm/downdroid",
    scripts=["bin/downdroid"],
    license="MIT",
    readme="readme.md",
    license_files="LICENSE*",
    keywords=[
        "android",
        "android-X86",
        "ISO",
        "systems",
        "linux",
        "virtualization",
        "CLI",
        "cli-tool"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    version='0.0.3',
    packages=[
        "downdroid",
        "downdroid.utils",
    ],
    install_requires=[
        'requests-html',
        'tqdm'
    ],
)
