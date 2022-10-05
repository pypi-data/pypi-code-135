import setuptools

with open('src/intelinair_utils/__version__.py') as version_file:
    exec(version_file.read())

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read().splitlines()

required = []

# Do not add to required lines pointing to Git repositories
EGG_MARK = '#egg='
for line in requirements:
    if line.startswith('-e git:') or line.startswith('-e git+') or line.startswith('git:') or line.startswith('git+'):
        if EGG_MARK in line:
            package_name = line[line.find(EGG_MARK) + len(EGG_MARK):]
            required.append(f'{package_name} @ {line}')
        else:
            print('Dependency to a git repository should have the format:')
            print('git+ssh://git@github.com/xxxxx/xxxxxx#egg=package_name')
    else:
        required.append(line)

setuptools.setup(
    name='intelinair_utils',
    version=globals()['__version__'],
    package_dir={'': 'src'},
    packages=setuptools.find_namespace_packages(where='src'),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=required
)


