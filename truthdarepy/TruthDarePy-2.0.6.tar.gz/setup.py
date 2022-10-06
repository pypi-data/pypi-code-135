import setuptools


with open("README.md", "r") as txt:
    long_description = txt.read()

setuptools.setup(
    name='TruthDarePy',
    version='2.0.6',
    description='Truth Dare Fun Api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    author='Awesome-Prince',
    author_email='DarlingPrince@protonmail.com',
    url='https://github.com/Awesome-Prince/Tg-Truth-Dare.git',
    packages=setuptools.find_packages(),
    install_requires= ['requests'],
    python_requires='>=3.6'
)
