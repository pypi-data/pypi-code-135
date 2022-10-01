import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='my_package_devilshorn',  
     version='0.2',
    #  scripts=['add_num'] ,
     author="Indrajeet",
     author_email="inder7171@gmail.com",
     description="Just a test package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Devilshorn999/my_package",
     packages=setuptools.find_packages(),
    #  py_modules=['add_num'],
     install_requires=[
        'numpy>=1.19.0'
    ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )