import setuptools

setuptools.setup(
    name="tomspdb",
    version=0.2,
    author="Talwrii",
    author_email="talwrii@gmail.com",
    description="",
    license="MIT",
    keywords="debugger",
    modules=["tomspdb"],
    long_description=open("readme.md").read(),
    entry_points={"console_scripts": ["tomspdb=tomspdb.tomspdb:main"]},
    classifiers=[],
)
