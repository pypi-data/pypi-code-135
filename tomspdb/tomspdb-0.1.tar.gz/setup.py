import setuptools

setuptools.setup(
    name="tomspdb",
    version=0.1,
    author="Talwrii",
    author_email="talwrii@gmail.com",
    description="",
    license="GPLv3",
    keywords="debugger",
    modules=["tomspdb"],
    long_description=open("readme.md").read(),
    entry_points={"console_scripts": ["tomspdb=tomspdb.tomspdb:main"]},
    classifiers=[],
)
