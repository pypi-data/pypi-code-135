import setuptools
import os.path

HERE = os.path.dirname(__file__)

setuptools.setup(
    name="tomspdb",
    version="0.6",
    author="Talwrii",
    author_email="talwrii@gmail.com",
    url="https://github.com/talwrii/tomspdb",
    description="",
    license="MIT",
    keywords="debugger",
    modules=["tomspdb"],
    long_description=open(os.path.join(HERE, "readme.md")).read(),
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["tomspdb=tomspdb.tomspdb:main"]},
    classifiers=[],
)
