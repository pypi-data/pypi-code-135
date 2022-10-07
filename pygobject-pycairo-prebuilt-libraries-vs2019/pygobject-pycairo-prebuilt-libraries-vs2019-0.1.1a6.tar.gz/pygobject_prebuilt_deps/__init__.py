# -*- coding: utf-8 -*-
import pathlib
import platform
import sys
import os 
from setuptools.dist import Distribution

def import_pygobject_dll_module():
    if platform.system() != "Windows":
        return 
    module_path = pathlib.Path(__file__).parent
    arch = "x86_vs16" if platform.architecture()[0] == "32bit" else "x64_vs16"
    dll_path = str(module_path.joinpath(f"{arch}/bin/"))
    py_ver = sys.version_info
    try:
        if py_ver[1] >= 8:
            os.add_dll_directory(dll_path)
    except:
        pass 
    os.environ['PATH'] = dll_path + os.pathsep + os.environ['PATH']

    gi_typelib = str(module_path.joinpath(f"{arch}/gi_typelib/girepository-1_0"))
    if 'GI_TYPELIB_PATH' not in os.environ:
        os.environ['GI_TYPELIB_PATH'] = gi_typelib
    else:
        os.environ['GI_TYPELIB_PATH'] = gi_typelib + os.pathsep + os.environ['GI_TYPELIB_PATH']

    
   
        