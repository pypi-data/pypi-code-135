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
        mname = '.'.join((pkg, '_sdm')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_sdm')
    _sdm = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sdm', [dirname(__file__)])
        except ImportError:
            import _sdm
            return _sdm
        try:
            _mod = imp.load_module('_sdm', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _sdm = swig_import_helper()
    del swig_import_helper
else:
    import _sdm
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

class sdm(_object):
    """Proxy of C++ casac::sdm class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sdm, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sdm, name)
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        """__init__(self, _path) -> sdm"""
        this = _sdm.new_sdm(*args, **kwargs)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def summarystr(self) -> "string":
        """
        summarystr(self) -> string



        Summary:
            Returns a summary of the SDM as a string

        --------------------------------------------------------------------------------

        """
        return _sdm.sdm_summarystr(self)


    def fromms(self, *args, **kwargs) -> "bool":
        """
        fromms(self, _mspath, _datacolumn, _archiveid, _rangeid, _subscanduration, _sbduration, _apcorrected, _verbose) -> bool



        Summary:
            convert measurement set into an SDM (stored path)

        Description:


        Create an sdm object with a non-existant path, and then use this function to populate
        the directory (which will be created) with the specified measurement set.


        Input Parameters:
            mspath                    Path to the MS to import
            datacolumn                 specifies which of the MS data columns (DATA, CORRECTED_DATA, or MODEL_DATA) should be used as the visibilities in the ASDM 
            archiveid                  the X0 in uid://X0/X1/X<running> 
            rangeid                    the X1 in uid://X0/X1/X<running> 
            subscanduration            maximum duration of a subscan in the output ASDM 
            sbduration                 maximum duration of a scheduling block in the output ASDM 
            apcorrected                If true, the data in column datacolumn should be regarded as having atmospheric phase correction 
            verbose                   produce log output

        --------------------------------------------------------------------------------

        """
        return _sdm.sdm_fromms(self, *args, **kwargs)


    def toms(self, *args, **kwargs) -> "bool":
        """
        toms(self, _vis, _createmms, _separationaxis, _numsubms, _corr_mode, _srt, _time_sampling, _ocorr_mode, _compression, _lazy, _asis, _wvr_corrected_data, _scans, _ignore_time, _process_syspower, _process_caldevice, _process_pointing, _process_flags, _tbuff, _applyflags, _savecmds, _outfile, _flagbackup, _verbose, _overwrite, _bdfflags, _with_pointing_correction, _convert_ephem2geo, _polyephem_tabtimestep) -> bool



        Summary:
            Convert a Science Data Model observation into a CASA visibility file (MS)

        Input Parameters:
            vis                       Root name of the ms to be created. Note the .ms is NOT added
            createmms                 Create a Multi-MS output
            separationaxis            Axis to do parallelization across(scan, spw, baseline, auto)
            numsubms                  The number of SubMSs to create (auto or any number)
            corr_mode                 specifies the correlation mode to be considered on input. A quoted string containing a sequence of ao, co, ac,or all separated by whitespaces is expected
            srt                       specifies the spectral resolution type to be considered on input. A quoted string containing a sequence of fr, ca, bw, or all separated by whitespaces is expected
            time_sampling             specifies the time sampling (INTEGRATION and/or SUBINTEGRATION)  to be considered on input. A quoted string containing a sequence of i, si, or all separated by whitespaces is expected
            ocorr_mode                output data for correlation mode AUTO_ONLY (ao) or CROSS_ONLY (co) or CROSS_AND_AUTO (ca)
            compression               Flag for turning on data compression
            lazy                      Make the MS DATA column read the ASDM Binary data directly (faster import, smaller MS)
            asis                      Creates verbatim copies of the ASDMtables in the ouput measurement set.  Value given must be a string of table names separated by spaces; A * wildcard is allowed.
            wvr_corrected_data        Specifies which values are considerd in the SDM binary data to fill the DATA column in the MAIN table of the MS. Expected values for this option are: no, for uncorrected data (default), yes, for the corrected data, and both, for for corrected and uncorrected data. Note if both is selected two measurement sets are created, one with uncorrected data and the other with corrected data.
            scans                     processes only the specified scans. This value is a semicolon separated list of scan specifications. A scan specification consists in an exec bock index followed by the : character;  followed by a comma separated list of scan indexes or scan index ranges. A scan index is relative to the exec block it belongs to. Scan indexes are 1-based while exec blocks are 0-based. '0:1' or '2:2~6' or '0:1,1:2~6,8;2:,3:24~30' '1,2' are valid values for the option. '3:' alone will be interpreted as, all the scans of the exec block#3.  An scan index or a scan index range not preceded by an exec block index will be interpreted as, all the scans with such indexes in all the exec blocks.  By default all the scans are considered.
            ignore_time               All the rows of the tables Feed, History, Pointing, Source, SysCal, CalDevice, SysPower, and Weather are processed independently of the time range of the selected exec block / scan.
            process_syspower          The SysPower table is processed if and only if this parameter is set to true.
            process_caldevice         The CalDevice table is processed if and only if this parameter is set to true.
            process_pointing          The Pointing table is processed if and only if this parameter is set to true. If set to false, the POINTING table is empty in the resulting MS
            process_flags             Create online flags in the FLAG_CMD sub-table.
            tbuff                     Time padding buffer (seconds)
            applyflags                Apply the flags to the MS.
            savecmds                  Save flag commands to an ASCII file
            outfile                   Name of ASCII file to save flag commands
            flagbackup                Back up flag column before applying flags.
            verbose                   Output lots of information while the filler is working
            overwrite                 Over write an existing MS(s)
            bdfflags                  Set the MS FLAG column according to the ASDM _binary_ flags
            with_pointing_correction  add (ASDM::Pointing::encoder - ASDM::Pointing::pointingDirection) to the value to be written in MS::Pointing::direction
            convert_ephem2geo         if true, convert any attached ephemerides to the GEO reference frame (time-spacing not changed)
            polyephem_tabtimestep     Timestep (days) for the tabulation of polynomial ephemerides. A value <= 0 disables tabulation.

        --------------------------------------------------------------------------------

        """
        return _sdm.sdm_toms(self, *args, **kwargs)

    __swig_destroy__ = _sdm.delete_sdm
    __del__ = lambda self: None
sdm_swigregister = _sdm.sdm_swigregister
sdm_swigregister(sdm)

# This file is compatible with both classic and new-style classes.


