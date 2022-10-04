from setuptools import setup

setup(
    name='AutoWSGR',
    version='0.0.2',
    description="All in one Warship Girls python package",
    url="https://github.com/huan-yp/Auto-WSGR",
    # use_scm_version=True,
    setup_requires=['setuptools_scm'],
    include_package_data=True,
    install_requires=[
        "torch",
        "airtest",
        "keyboard",
        "easyocr",
        "opencv-python==4.5.5.64",
    ],
)
