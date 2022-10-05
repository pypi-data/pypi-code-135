## This file is just to let Python recognize this folder is a package.

# Ref: Package vs. Module  https://tinyurl.com/y8nlao8p
# Any Python file is a module, its name being the file's base name without the .py extension. A package is a collection of Python modules: while a module is a single Python file, a package is a directory of Python modules containing an additional __init__.py file, to distinguish a package from a directory that just happens to contain a bunch of Python scripts. Packages can be nested to any depth, provided that the corresponding directories contain their own __init__.py file.

# * Organize Code: https://tinyurl.com/ygprtegj

# * Import Module From Subdirectory in Python: https://tinyurl.com/yzjqs4tm
# * Import subfolder as module: https://www.tutorialsteacher.com/python/python-package
# * NOTEs: to use subfolder-name as module-name, in the __init__.py must import all module in that subfolder
#         from . import file1
#         from . import file2
#         from .file3 import function-in-file3

"""
Thang's Tool is an object-oriented Python package for pre-processing and post-processing data from MD simulations.

This package is developed and maintained by [thangckt](https://thangckt.github.io)
```
      thatool_package  
      │__ README.md
      │__ LICENSE.md
      │__ setup.py   
      | 
      |__ thatool
          │__ __init__.py
          │__ data.py  
          │
          |__ io
          │   │__ __init__.py
          │   │__ define_script.py
          |   |__ LmpFrame.py
          │   │__ ...
          │ 
          |__ model
          |   |__ __init__.py
          |   |__ box_orientation.py
          |   |__ crystal3D.py
          |   |__  ...
          |
          |__ colvar
          |   |__ __init__.py
          |   |__ cv_fccCUBIC.py
          |   |__ cv_localCRYSTALLINITY.py
          |   |__ ...
          │   
          |__ free_energy
          |   |__ __init__.py
          |   |__ Helmholtz_excess_UF.py
          |   |__ replica_logPD_intergration.py
          |   |__ ...
          |
          |__ utils
          |   |__ __init__.py
          |   |__ coord_rotation.py
          |   |__ unit_convert.py
          |   |__ compute_distance.py
          |   |__ fitting.py
          |   |__ ...
          |   
```

"""
__description__ = "Python package"
__long_description__ = "ThangTool is an object-oriented Python package for pre-processing and post-processing data from MD simulations. This package is developed and maintained by [[https://thangckt.github.io|thangckt]]"
__author__  = "thangckt"
__version__ = "1.1.3"

from .io                import  *
from .free_energy       import  *
from .model             import  *
from .colvar            import  *
from .utils             import  *
