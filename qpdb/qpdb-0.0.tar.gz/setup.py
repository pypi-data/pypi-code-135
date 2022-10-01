import re
from pathlib import Path

from setuptools import find_packages, setup

########################################################################################

NAME = "qpdb"
PROJECT_URLS = {
    "Bug Tracker": "https://github.com/qu-arx/qp/issues",
    "Source Code": "https://github.com/qu-arx/qp",
}
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Intended Audience :: Developers",
    "Topic :: Education",
]
INSTALL_REQUIRES = Path("requirements.txt").read_text().splitlines()
EXTRAS_REQUIRE = {
    "tests": ["coverage[toml]>=5.5", "pytest"],
}
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + ["pre-commit"]
)
PYTHON_REQUIRES = ">=3.10"
LONG_DESCRIPTION = Path("README.md").read_text()
PACKAGE_DATA = {"qp": ["py.typed"]}

########################################################################################


def local_scheme(version):
    return ""


def version_scheme(version):
    return version.tag.base_version


########################################################################################


META_PATH = Path(__file__).parent.absolute() / "src" / NAME / "__init__.py"
META_FILE = META_PATH.read_text()


def find_meta(meta):
    "Extract __*meta*__ from META_FILE."
    meta_match = re.search(rf"^__{meta}__ = ['\"]([^'\"]*)['\"]", META_FILE, re.M)
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


if __name__ == "__main__":
    setup(
        name=NAME,
        description=find_meta("description"),
        license=find_meta("license"),
        url=find_meta("url"),
        project_urls=PROJECT_URLS,
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        packages=find_packages("src"),
        package_dir={"": "src"},
        package_data=PACKAGE_DATA,
        include_package_data=True,
        zip_safe=False,
        classifiers=CLASSIFIERS,
        use_scm_version={
            "write_to": "version.py",
            "version_scheme": version_scheme,
            "local_scheme": local_scheme,
        },
        setup_requires=["setuptools_scm"],
        install_requires=INSTALL_REQUIRES,
        extras_require=EXTRAS_REQUIRE,
        python_requires=PYTHON_REQUIRES,
    )
