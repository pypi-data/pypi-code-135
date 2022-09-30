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
        mname = '.'.join((pkg, '_utils')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_utils')
    _utils = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_utils', [dirname(__file__)])
        except ImportError:
            import _utils
            return _utils
        try:
            _mod = imp.load_module('_utils', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _utils = swig_import_helper()
    del swig_import_helper
else:
    import _utils
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

class utils(_object):
    """Proxy of C++ casac::utils class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, utils, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, utils, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(self) -> utils"""
        this = _utils.new_utils()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def getrc(self, *args, **kwargs) -> "string":
        """
        getrc(self, _rcvar) -> string



        Input Parameters:
            rcvar                     Returns the value of the rc variable given. If no value is give it returns the root directory of CASA.

        --------------------------------------------------------------------------------

        """
        return _utils.utils_getrc(self, *args, **kwargs)


    def removetable(self, *args, **kwargs) -> "bool":
        """
        removetable(self, _tablenames) -> bool



        Input Parameters:
            tablenames                Removes tables safely

        --------------------------------------------------------------------------------

        """
        return _utils.utils_removetable(self, *args, **kwargs)


    def tableinfo(self, *args, **kwargs) -> "record *":
        """
        tableinfo(self, _tablename) -> record *



        Summary:
            Get information about a particular table

        Description:


        Currently this only returns the pid of the process locking the table (lockpid), if the lock
        is permanent (lockperm), and the status (lockstatus) -- 'not in use', 'open', 'read', 'write',
        or 'unknown'. However, the hope is that this will eventually return a complete description of
        the table.


        Input Parameters:
            tablename                 path to table

        --------------------------------------------------------------------------------

        """
        return _utils.utils_tableinfo(self, *args, **kwargs)


    def lockedtables(self) -> "std::vector< std::string >":
        """
        lockedtables(self) -> std::vector< std::string >



        Summary:
            get the tables locked by this process

        --------------------------------------------------------------------------------

        """
        return _utils.utils_lockedtables(self)


    def hostinfo(self) -> "record *":
        """
        hostinfo(self) -> record *



        Summary:
            returns host information

        --------------------------------------------------------------------------------

        """
        return _utils.utils_hostinfo(self)


    def c_exception(self) -> "string":
        """
        c_exception(self) -> string



        Summary:
            Returns detailed information about last C-level exception

        Description:

        Returns detailed information from the last CASA C++ exception (i.e., AipsError).  The
        exception message and the stack trace (mangled; use the shell's c++filt to demangle)
        from the last CASA C++ exception.  The information is from the last one generated
        and may not represent an exception from the last action; c_exception_clear can be
        used to remove stale information.  The information's exception might also
        have been caught in the C++ code and not have been translated into a Python-level
        exception.


        --------------------------------------------------------------------------------

        """
        return _utils.utils_c_exception(self)


    def c_exception_clear(self) -> "void":
        """
        c_exception_clear(self)



        Summary:
            Clears information about last C-level exception

        Description:

        Clears the CASA C++ exception information.  This allows the user to be sure that
        information retrieved using c_exception is not from an exception in the
        distant past.


        --------------------------------------------------------------------------------

        """
        return _utils.utils_c_exception_clear(self)


    def _crash_reporter_initialize(self, *args, **kwargs) -> "string":
        """
        _crash_reporter_initialize(self, _crashDumpDirectory, _crashDumpPosterApplication, _crashPostingUrl, _logFile) -> string



        Summary:
            Initializes the crash reporter.

        Description:


        Initializes the crash reporter which will generate a crash report if casapy
        crashes.  For reporter purposes a crash is the reception of an signal by
        casapy which would normally result in the program being terminated.  This includes
        segfaults, aborts, etc., plus any unhandled C++ exceptions (C++ generates an
        abort signal for unhandled exceptions).  This method is intended for use by the
        casapy infrastructure and should not be called by other code or by users; however,
        the call will only install the crash reporter the first time it is called so any
        subsequent calls should be no-ops.  Returns true if initialization occurred and
        false if the crash reporter was stubbed out (i.e., symbol UseCrashReporter was
        not defined).


        Input Parameters:
            crashDumpDirectory        Directory to write crash dumps into.
            crashDumpPosterApplicatio Application to post crash dumps to http server.
            crashPostingUrl           URL to use when posting crash report.
            logFile                   Full name of initial logfile

        --------------------------------------------------------------------------------

        """
        return _utils.utils__crash_reporter_initialize(self, *args, **kwargs)


    def _trigger_segfault(self, *args, **kwargs) -> "bool":
        """
        _trigger_segfault(self, _faultType) -> bool



        Summary:
            Crashes casa with segfault.

        Description:


        This triggers a segfault for testing the crash reporter.  Obviously you
        shouldn't call this unless that's what you want.  It's in here for
        development/debugging purposes and ought to be removed before you see this.


        Input Parameters:
            faultType                 How to kill the program

        --------------------------------------------------------------------------------

        """
        return _utils.utils__trigger_segfault(self, *args, **kwargs)


    def tryit(self, *args, **kwargs) -> "double":
        """
        tryit(self, _input) -> double



        Description:


        test variant convesion

        Input Parameters:
            input                     testing variant

        --------------------------------------------------------------------------------

        """
        return _utils.utils_tryit(self, *args, **kwargs)


    def maxint(self) -> "long":
        """
        maxint(self) -> long



        Description:

        maximum number an C++ int can hold

        --------------------------------------------------------------------------------

        """
        return _utils.utils_maxint(self)


    def minint(self) -> "long":
        """
        minint(self) -> long



        Description:

        minimum number an C++ int can hold

        --------------------------------------------------------------------------------

        """
        return _utils.utils_minint(self)


    def maxlong(self) -> "long":
        """
        maxlong(self) -> long



        Description:

        maximum number an C++ long can hold

        --------------------------------------------------------------------------------

        """
        return _utils.utils_maxlong(self)


    def minlong(self) -> "long":
        """
        minlong(self) -> long



        Description:

        minimum number an C++ long can hold

        --------------------------------------------------------------------------------

        """
        return _utils.utils_minlong(self)


    def initialize(self, *args, **kwargs) -> "bool":
        """
        initialize(self, _python_path, _distro_data_path, _default_path, _nogui, _agg, _pipeline) -> bool



        Summary:
            initialize CASAtools

        Description:


        returns true if initalization was performed; returns false if initialization was already done

        Input Parameters:
            python_path               path to python executable
            distro_data_path          path to the data provided by the casadata pkg
            default_path              directories that should constitute the default data path
            nogui                     are guis disabled at startup
            agg                       was the graphical backend disabled at startup
            pipeline                  was the pipeline included at startup

        --------------------------------------------------------------------------------

        """
        return _utils.utils_initialize(self, *args, **kwargs)


    def rundata(self) -> "string":
        """
        rundata(self) -> string



        Summary:
            path to the measures data

        Description:

        path to the measures data

        --------------------------------------------------------------------------------

        """
        return _utils.utils_rundata(self)


    def setrundata(self, *args, **kwargs) -> "void":
        """
        setrundata(self, _path)



        Summary:
            set path to the measures data

        Description:


        Set path to the measures data. Must be called during initalization
        before Measures module is initialized.

        Input Parameters:
            path                      path to IERS data

        --------------------------------------------------------------------------------

        """
        return _utils.utils_setrundata(self, *args, **kwargs)


    def defaultpath(self) -> "std::vector< std::string >":
        """
        defaultpath(self) -> std::vector< std::string >



        Summary:
            returns the default data path

        Description:


        Returns the default data path. This path is used unless the user has set the current path to something else using the setpath function.

        --------------------------------------------------------------------------------

        """
        return _utils.utils_defaultpath(self)


    def setpath(self, *args, **kwargs) -> "bool":
        """
        setpath(self, _dirs) -> bool



        Summary:
            sets the data path to the specified list of directories

        Description:


        Sets the data path to the specified list of directories. Returns true if all directories were added
        returns false otherwise.

        Input Parameters:
            dirs                      directories that should constitute the data path

        --------------------------------------------------------------------------------

        """
        return _utils.utils_setpath(self, *args, **kwargs)


    def getpath(self) -> "std::vector< std::string >":
        """
        getpath(self) -> std::vector< std::string >



        Summary:
            retrieves the data path

        Description:


        Returns the list of directories that are currently in the data path.

        --------------------------------------------------------------------------------

        """
        return _utils.utils_getpath(self)


    def clearpath(self) -> "void":
        """
        clearpath(self)



        Summary:
            removes all directories from the data path

        Description:


        Removes all directories from the data path.

        --------------------------------------------------------------------------------

        """
        return _utils.utils_clearpath(self)


    def resolve(self, *args, **kwargs) -> "string":
        """
        resolve(self, _path) -> string



        Summary:
            resolve a complete path from a subdirectory using the data path

        Description:


        If the provided path already represents a file or a directory, it is returned. If it does not,
        this function tries to find a complete path by matching up this partial directory with the
        elements of the data path.

        Input Parameters:
            path                      path to be expanded

        --------------------------------------------------------------------------------

        """
        return _utils.utils_resolve(self, *args, **kwargs)


    def getnogui(self) -> "bool":
        """
        getnogui(self) -> bool



        Summary:
            gets the nogui config value

        Description:


        Returns the value of the nogui parameter used at startup. Defaults to False.


        --------------------------------------------------------------------------------

        """
        return _utils.utils_getnogui(self)


    def getagg(self) -> "bool":
        """
        getagg(self) -> bool



        Summary:
            gets the agg config value

        Description:


        Returns the value of the agg parameter used at startup. Defaults to False.


        --------------------------------------------------------------------------------

        """
        return _utils.utils_getagg(self)


    def getpipeline(self) -> "bool":
        """
        getpipeline(self) -> bool



        Summary:
            gets the pipeline config value

        Description:


        Returns the value of the pipeline parameter used at startup. Defaults to False.


        --------------------------------------------------------------------------------

        """
        return _utils.utils_getpipeline(self)


    def registry(self) -> "record *":
        """
        registry(self) -> record *



        Summary:
            retrieve registry information

        Description:


        returns record containing the URI for the CASAtools registry which can be used by other unix processes to access the registry

        --------------------------------------------------------------------------------

        """
        return _utils.utils_registry(self)


    def services(self) -> "record *":
        """
        services(self) -> record *



        Summary:
            retrieve registered services

        Description:


        returns record containing the information about the services that have been registered with CASAtools

        --------------------------------------------------------------------------------

        """
        return _utils.utils_services(self)


    def remove_service(self, *args, **kwargs) -> "bool":
        """
        remove_service(self, _uri) -> bool



        Summary:
            remove a service using its URI

        Description:


        Remove a service from the registry using the URI for the
        service. The URI should be a string that looks something
        like '0.0.0.0:34101'. This function returns true if the
        removal was successful. Otherwise, it returns false.

        Input Parameters:
            uri                       uri (Address) of the service to remove.

        --------------------------------------------------------------------------------

        """
        return _utils.utils_remove_service(self, *args, **kwargs)


    def shutdown(self) -> "void":
        """
        shutdown(self)



        Summary:
            shutdown signal from python

        Description:


        python is shutting down cleanup anything that is outstanding

        --------------------------------------------------------------------------------

        """
        return _utils.utils_shutdown(self)


    def getpython(self) -> "string":
        """
        getpython(self) -> string



        Summary:
            get path to python executable

        --------------------------------------------------------------------------------

        """
        return _utils.utils_getpython(self)


    def version(self) -> "std::vector< long >":
        """
        version(self) -> std::vector< long >



        Summary:
            returns four element vector for the version

        Description:



        Returns a four element vector representing the version (major, minor, patch and feature).

        --------------------------------------------------------------------------------

        """
        return _utils.utils_version(self)


    def version_variant(self) -> "string":
        """
        version_variant(self) -> string



        Summary:
            returns the target instrument f.e. ALMA or VLA

        Description:



        Returns the target instrument. This helps distinguish versions that otherwise may have the same version number

        --------------------------------------------------------------------------------

        """
        return _utils.utils_version_variant(self)


    def version_desc(self) -> "string":
        """
        version_desc(self) -> string



        Summary:
            returns the descriptive version string, e.g. DEV or REL

        Description:



        The descriptive string describes a particular packaged version. During a development
        cycle there are different sorts of packaged distributions. For example, a development
        version ('DEV') or a release version ('REL').

        --------------------------------------------------------------------------------

        """
        return _utils.utils_version_desc(self)


    def version_info(self) -> "string":
        """
        version_info(self) -> string



        Summary:
            Returns the complete version description as a string.

        Description:



        Returns a description string that includes the version information and the descriptive string..

        --------------------------------------------------------------------------------

        """
        return _utils.utils_version_info(self)


    def version_string(self) -> "string":
        """
        version_string(self) -> string



        Summary:
            Returns the complete version description as a string but without the description (i.e. git hash) string.

        Description:



        Returns a description string that includes the version information and the descriptive string..

        --------------------------------------------------------------------------------

        """
        return _utils.utils_version_string(self)


    def compare_version(self, *args, **kwargs) -> "bool":
        """
        compare_version(self, _comparitor, _vec) -> bool



        Summary:
            Returns the complete version description as a string.

        Description:



        Returns a description string that includes the version information and the descriptive string..

        Input Parameters:
            comparitor                what sort of comparison to do, one of >, <, <=, >=, ==, = !=
            vec                       vector to use to compare current version number against vec

        --------------------------------------------------------------------------------

        """
        return _utils.utils_compare_version(self, *args, **kwargs)


    def toolversion(self) -> "std::vector< long >":
        """
        toolversion(self) -> std::vector< long >



        Summary:
            returns two element vector containing CASA 6 tool version number

        Description:



        Returns a two element vector representing the CASAtools version (year, build). This is only
        returned with CASA 6. With CASA 5, an zero element vector is returned.

        --------------------------------------------------------------------------------

        """
        return _utils.utils_toolversion(self)


    def toolversion_string(self) -> "string":
        """
        toolversion_string(self) -> string



        Summary:
            Returns the complete CASA 6 CASAtools version description as a string

        Description:



        Returns a description string that shows the CASA 6 CASAtools version information as a descriptive string.
        With CASA 5, a zero length string is returned.

        --------------------------------------------------------------------------------

        """
        return _utils.utils_toolversion_string(self)

    __swig_destroy__ = _utils.delete_utils
    __del__ = lambda self: None
utils_swigregister = _utils.utils_swigregister
utils_swigregister(utils)

# This file is compatible with both classic and new-style classes.


