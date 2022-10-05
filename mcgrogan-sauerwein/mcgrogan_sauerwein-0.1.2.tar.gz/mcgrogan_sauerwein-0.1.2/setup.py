from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='mcgrogan_sauerwein',
    version='0.1.2',
    description='Useful tools to work in TDA Python',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Neil McGrogan',
    author_email='mcgrognp@mail.uc.edu',
    keywords=['Tech'],
    url='https://github.com/neilmcgrogan',
    download_url='https://pypi.org/project/neilmcgrogan/'
)

install_requires = [
    'elasticsearch>=6.0.0,<7.0.0',
    'jinja2'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
