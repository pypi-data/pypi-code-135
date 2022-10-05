from setuptools import setup, find_packages

setup(
    name='inspector-python',
    version='0.1.0',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://inspector.dev/',
    license='MIT',
    author='Antonio Bruno',
    author_email='antoniobruno82@gmail.com',
    description='Connect your Python application to Inspector'
)
