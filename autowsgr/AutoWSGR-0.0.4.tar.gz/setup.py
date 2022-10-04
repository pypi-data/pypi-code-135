from setuptools import setup

setup(
    name='AutoWSGR',
    version='0.0.4',
    description="All in one Warship Girls python package",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/huan-yp/Auto-WSGR",
    setup_requires=['setuptools_scm'],
    use_scm_version=False,
    include_package_data=True,
    packages=['AutoWSGR'],
    install_requires=[
        "torch",
        "airtest",
        "keyboard",
        "easyocr",
        "opencv-python==4.5.5.64",
    ],
)
