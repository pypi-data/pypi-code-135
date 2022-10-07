# -*- coding: utf-8 -*-
from setuptools import setup
import atexit
# from distutils import sysconfig
# import os
import sys 
import platform
import pathlib
import subprocess
# from distutils.command.build_ext import build_ext
from distutils.core import Distribution
try:
    from importlib.resources import files
except ImportError:
    import importlib.resources
    import zipfile 
    def fallback_resources(spec):
        package_directory = pathlib.Path(spec.origin).parent
        try:
            archive_path = spec.loader.archive
            rel_path = package_directory.relative_to(archive_path)
            return zipfile.Path(archive_path, str(rel_path) + '/')
        except Exception:
            pass
        return package_directory
    def _resolve(name) -> importlib.resources.ModuleType:
        """If name is a string, resolve to a module."""
        if hasattr(name, '__spec__'):
            return name
        return importlib.resources.import_module(name)
    def _get_package(package) -> importlib.resources.ModuleType:
        """Take a package name or module object and return the module.
        If a name, the module is imported.  If the resolved module
        object is not a package, raise an exception.
        """
        module = _resolve(package)
        if module.__spec__.submodule_search_locations is None:
            raise TypeError('{!r} is not a package'.format(package))
        return module
    def _from_package(package):
        return fallback_resources(package.__spec__)
    def files(package: importlib.resources.Package):
        return _from_package(_get_package(package))

def get_command_class(name):
    # in case pip loads with setuptools this returns the extended commands
    return Distribution({}).get_command_class(name)

du_install = get_command_class("install")

def _post_install():
    py_ver = sys.version_info
    py_ver_str = f"{py_ver[0]}{py_ver[1]}"
    py_ver_str_end = py_ver_str + "m" if py_ver[1] == 7 else py_ver_str
    arch = "win32" if platform.architecture()[0] == "32bit" else "win_amd64"
    # install pycairo
    pycairo = files('pygobject_prebuilt_deps').joinpath(f"wheels/pycairo-1.21.0-cp{py_ver_str}-cp{py_ver_str_end}-{arch}.whl")
    subprocess.run(f"pip install -v --force-reinstall --no-deps {pycairo}", shell=True)
    # install pygobject
    pygobject = files("pygobject_prebuilt_deps").joinpath(f"wheels/PyGObject-3.42.2-cp{py_ver_str}-cp{py_ver_str_end}-{arch}.whl")
    subprocess.run(f"pip install -v --force-reinstall --no-deps {pygobject}", shell=True)

class install(du_install):
    def run(self, *args, **kwargs):
        atexit.register(_post_install)
        du_install.run(self, *args, **kwargs)

def build(setup_kwargs):

    cmdclass = {
        "install": install, 
    }

    setup_kwargs.update({
        "cmdclass": cmdclass,
    })

package_dir = {
    # '': 'pygobject_prebuilt_deps',
}

packages = [
    'pygobject_prebuilt_deps',
    'pygobject_prebuilt_deps.wheels',
    'pygobject_prebuilt_deps.x86_vs16',
    'pygobject_prebuilt_deps.x86_vs16.bin',
    'pygobject_prebuilt_deps.x86_vs16.gi_typelib',
    'pygobject_prebuilt_deps.x86_vs16.gi_typelib.girepository-1_0',
    'pygobject_prebuilt_deps.x64_vs16',
    'pygobject_prebuilt_deps.x64_vs16.bin',
    'pygobject_prebuilt_deps.x64_vs16.gi_typelib',
    'pygobject_prebuilt_deps.x64_vs16.gi_typelib.girepository-1_0',
]

package_data = {
    '': ['*.py', '*.dll', '*.whl', '*.typelib'],
    'pygobject_prebuilt_deps': ['*.py', '*.dll', '*.whl', '*.typelib'],
}

modules = [  ]
setup_kwargs = {
    'name': 'pygobject-pycairo-prebuilt-libraries-vs2019',
    'version': '0.1.1a6',
    'description': 'PyGBject PyCairo prebuilt libraries on vs2019',
    'long_description': '',
    'author': 'dzhsurf',
    'author_email': 'dzhsurf@gmail.com',
    'maintainer': 'dzhsurf',
    'maintainer_email': 'dzhsurf@gmail.com',
    'url': 'https://github.com/dzhsurf/pygobject-pycairo-prebuilt-libraries-vs2019',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'python_requires': '>=3.7',
}

build(setup_kwargs)
setup(**setup_kwargs)