from setuptools import setup, find_packages
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setup(
    name="vetl",
    version="0.0.0-beta2",
    author="Asyraf N. Adianto",
    author_email="asyraf.adianto@gmail.com",
    package_dir={'': '.'},
    packages=find_packages('.'),
    description="Virtual ETL Tools",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/asyraf-adianto/vetl",
    license='MIT',
    python_requires='>=3.0',
    install_requires=[
        'pandas>=1.0.3',
        'petl>=1.7.0',
        'redshift-connector>=2.0.908',
        'psycopg2-binary>=2.9.3',
        'paramiko>=2.11.0',
        'sshtunnel>=0.4.0'
    ]
)