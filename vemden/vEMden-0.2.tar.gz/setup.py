import os

from pathlib import Path
from setuptools import find_packages, setup

import vEMden



def AllFiles():
	files = []
	for file_path in Path('./vEMden/').glob('**/*.py'):
		files.append(str(file_path))
	return files



setup(
	name=vEMden.__name__,
	packages=find_packages(),
	version=vEMden.__version__,
	author="Guillaume THIBAULT, Katya GIANNIOS",
	author_email="thibaulg@ohsu.edu",
	maintainer="Guillaume THIBAULT",
	maintainer_email="thibaulg@ohsu.edu",
	url="https://www.thibault.biz/Research/VolumeEM/vEMden/vEMden.html",
	download_url="https://www.thibault.biz/Doc/vEMden/vEMden-" + vEMden.__version__ + ".tar.gz",
	license="MIT",
	plateforms='ALL',
	package_data={'vEMden': AllFiles()},
	keywords=["Denoising", "Electron Microscopy", "Volume EM", "vEM", "FIB-SEM",
			"Focused Ion Beam Scanning Electron Microscop"],
	classifiers=["Development Status :: 4 - Beta",# "Development Status :: 5 - Production/Stable",
					"Environment :: Console",
					"Environment :: GPU",
					"Environment :: GPU :: NVIDIA CUDA :: 10.2",
					"Environment :: Other Environment",
					"Intended Audience :: Developers",
					"Intended Audience :: Healthcare Industry",
					"Intended Audience :: Science/Research",
					"License :: OSI Approved :: MIT License",
					"Operating System :: OS Independent",
					"Programming Language :: Python :: 3",
					"Programming Language :: Python :: 3.8",
					"Programming Language :: Python :: 3.9",
					"Topic :: Scientific/Engineering",
					"Topic :: Scientific/Engineering :: Artificial Intelligence",
					"Topic :: Scientific/Engineering :: Bio-Informatics",
					"Topic :: Scientific/Engineering :: Image Processing"],
	install_requires=["FiReTiTiPyLib>=1.5"],
	python_requires=">=3.8,<3.10",
	entry_points={'console_scripts': ['vEMden=vEMden.vEMden:Denoise']},
	description="Volume Electron Microscopy DENoising (vEMden)",
	long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
	)
