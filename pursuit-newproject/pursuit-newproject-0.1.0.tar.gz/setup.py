from setuptools import setup
from pathlib import Path

# Program metadata

PROGRAM_ID = "newproject"
PROGRAM_VERSION = "0.1.0"


directory = Path(__file__).parent

setup(
    name="pursuit-newproject",
    version=PROGRAM_VERSION,
    packages=[PROGRAM_ID],
    entry_points={
        "console_scripts": [f"{PROGRAM_ID}={PROGRAM_ID}.main:main"],
    },
    author='Pursuit',
    author_email='fr.pursuit@gmail.com',
    description='Project templater',
    long_description=(directory / "README.md").read_text(encoding="utf-8"),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/frPursuit/newproject',
    license='GNU General Public License v3 (GPLv3)',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=['Jinja2>=3.1.2', 'PyYAML>=6.0']
)
