import setuptools

setuptools.setup(
    name="CDLparser",
    version="0.24",
    author="Ben Sanderson",
    description="A python3 netcdf CDL parser",
    install_requires=[
          'ply',
      ],
    packages=["cdlparser"]
    )
