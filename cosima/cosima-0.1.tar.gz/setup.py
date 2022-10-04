import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="cosima",
    version="0.1",
    author="Cosima Team",
    author_email="emilie.frost@offis.de",
    description="COmmunication SIMulation with Agents",
    long_description="Integration of the (communication) simulator OMNeT++ into the co-simulation framework mosaik",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/mosaik/examples/cosima.git",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
    ],
    python_requires='>=3.8',
    include_package_data=True,
)
