import setuptools

setuptools.setup(
    name="tomspdb",
    version="0.4",
    author="Talwrii",
    author_email="talwrii@gmail.com",
    url="https://github.com/talwrii/tomspdb",
    description="",
    license="MIT",
    keywords="debugger",
    modules=["tomspdb"],
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["tomspdb=tomspdb.tomspdb:main"]},
    classifiers=[],
)
