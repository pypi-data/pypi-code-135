from skbuild import setup

setup(
    name="mumpropagator",
    version="1.0.0",
    description="A python interface to Muon Propagator package MUM, developed by Igor Sokalski",
    license="MIT",
    packages=['mumpropagator'],
    cmake_args=['-DSKBUILD=ON']
)
