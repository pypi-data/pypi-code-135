# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_vlafiller')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_vlafiller')
    _vlafiller = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_vlafiller', [dirname(__file__)])
        except ImportError:
            import _vlafiller
            return _vlafiller
        try:
            _mod = imp.load_module('_vlafiller', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _vlafiller = swig_import_helper()
    del swig_import_helper
else:
    import _vlafiller
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class vlafiller(_object):
    """Proxy of C++ casac::vlafiller class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vlafiller, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vlafiller, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(self) -> vlafiller"""
        this = _vlafiller.new_vlafiller()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def fill(self, *args, **kwargs) -> "void":
        """
        fill(self, _msname, _inputfile, _project, _start, _stop, _centerfreq, _bandwidth, _bandname, _source, _subarray, _qualifier, _calcode, _overwrite, _freqtol, _applytsys, _keepautocorr, _antnamescheme, _useday, _keepblanks, _evlabands)



        Summary:
            Perform fill operations

        Input Parameters:
            msname                    name of output ms
            inputfile                 name of vla archive
            project                   name of project to extract, defaults to all projects in input
            start                     start time to extract
            stop                      end time of extracted data
            centerfreq                frequency of data to extract (used along with bandwidth param)
            bandwidth                 data around centerfreq to get out
            bandname                  name of band to extract
            source                    name of source
            subarray                  subarray - 0 means all subarrays
            qualifier                 qualifier for source
            calcode                   Calibrator code, 1 character only
            overwrite                 overwrite or append
            freqtol                   Frequency tolerance, the default tolerance for frequency is set to be 6 times of the channel width. You may have to tweak the tolerance depending on the dataset, just depends.
            applytsys                 scale data and weights by Tsys info
            keepautocorr              Fill autocorrelations along with cross correlation data. If False data that have same ANTENNA1 and ANTENNA2 are ignored 
            antnamescheme             If 'new', VLA antenna name is prepended by EVLA or VLA to distinguish between the refurbished and non-refubished antennas. 'old' will just put the VLA antenna identifier as is in the NAME column of the ANTENNA table. 
            useday                     This option is only available at the AOC in Socorro! When filling at the AOC, select the online day file to use < 0 means any previous day up to 14 0 means from the start of the current day > 0 means starting now 
            keepblanks                Scans with blank (empty) source names (i.e. tipping scans) will be filled. The default is to not fill.
            evlabands                 Use the EVLA frequencies and bandwith tolerances when specifying band codes or wavelengths.

        --------------------------------------------------------------------------------

        """
        return _vlafiller.vlafiller_fill(self, *args, **kwargs)

    __swig_destroy__ = _vlafiller.delete_vlafiller
    __del__ = lambda self: None
vlafiller_swigregister = _vlafiller.vlafiller_swigregister
vlafiller_swigregister(vlafiller)

# This file is compatible with both classic and new-style classes.


