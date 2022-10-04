import os
from setuptools import find_packages, setup

requirements = [
    "numpy>=1.21.0",
]

setup(
    name="my-test-fibonacci",
    version=os.environ.get("PACKAGE_VERSION", "1.0.0"),
    description="implementation of fibonacci function",
    maintainer="Ru Zhang",
    maintainer_email="heavenmarshal@gmail.com",
    packages=find_packages(),
	install_requires=requirements,
    python_requires=">=3.7",
	setup_requires=['pytest-runner'],
    tests_require=["pytest"],
	test_suite="unittests",
)
