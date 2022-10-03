import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="ruggray", 
    version="0.99.04",
    author="Mark Span (primary developer)",
    author_email="m.m.span@rug.nl",
    description="Opensesame Forms theme for the University of Groningen",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/markspan/ruggray",
    packages=setuptools.find_packages(),
	classifiers=[
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'Environment :: MacOS X',
		'Environment :: Win32 (MS Windows)',
		'Environment :: X11 Applications',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python :: 3',
	],
    python_requires='>=3.6',
	
	data_files=[
		# First target folder.
		('Lib/site-packages/libopensesame/widgets/themes', 
		# Then a list of files that are copied into the target folder. Make sure
		# that these files are also included by MANIFEST.in!
		[
			'src/ruggray.py',
            ]
		)
	])
	
