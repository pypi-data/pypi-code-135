import setuptools

setuptools.setup(
    name="tomspdb",
    version=0.3,
    author="Talwrii",
    author_email="talwrii@gmail.com",
    url="https://github.com/talwrii/tomspdb",
    description="",
    license="MIT",
    keywords="debugger",
    modules=["tomspdb"],
    long_description=open("readme.md").read(),
    entry_points={"console_scripts": ["tomspdb=tomspdb.tomspdb:main"]},
    classifiers=[],
)
