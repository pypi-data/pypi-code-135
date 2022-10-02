from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme_text = readme_file.read()


setup_args = dict(
    entry_points = {
        'console_scripts': ['image-cli-convert=image_cli.command_line_convert:main'],
    },
    name='image-cli',
    version='0.0.0.2',
    description="",
    keywords=[],
    long_description=readme_text,
    long_description_content_type="text/markdown",
    license='Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License',
    packages=find_packages(),
    author="Leo Ertuna",
    author_email="leo.ertuna@gmail.com",
    url="https://github.com/jpleorx/image-cli",
    download_url='https://pypi.org/project/image-cli/'
)


install_requires = [
    'argparse',
    'colorama',
    'tekleo-common-utils'
]


if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
