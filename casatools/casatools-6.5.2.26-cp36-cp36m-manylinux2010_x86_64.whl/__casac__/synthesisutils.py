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
        mname = '.'.join((pkg, '_synthesisutils')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_synthesisutils')
    _synthesisutils = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_synthesisutils', [dirname(__file__)])
        except ImportError:
            import _synthesisutils
            return _synthesisutils
        try:
            _mod = imp.load_module('_synthesisutils', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _synthesisutils = swig_import_helper()
    del swig_import_helper
else:
    import _synthesisutils
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

class synthesisutils(_object):
    """Proxy of C++ casac::synthesisutils class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, synthesisutils, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, synthesisutils, name)
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(self) -> synthesisutils"""
        this = _synthesisutils.new_synthesisutils()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def contdatapartition(self, *args, **kwargs) -> "record *":
        """
        contdatapartition(self, _selpars, _npart) -> record *



        Summary:
            Partition data selection parameters for continuum imaging

        Input Parameters:
            selpars                   All selection parameters for one or more MSs
            npart                     Number of partitions

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_contdatapartition(self, *args, **kwargs)


    def advisechansel(self, *args, **kwargs) -> "record *":
        """
        advisechansel(self, _freqstart, _freqend, _freqstep, _freqframe, _ephemtable, _msname, _fieldid, _getfreqrange, _spwselection) -> record *



        Summary:
            Advise on spw and chan selection optimal for the image frequency range wanted

        Description:


        It is a helper function, for cube imaging, that allows you to
        determine the spectral window data selection you may need to cover a
        given range of frequencies.

        In the mode with getfreqrange=False, the freqstep can be used (i.e., set to the channel width) to achieve the extra padding needed for data selection at the beginning and end of the desired cube range in order to retrieve all channels that will potentially contribute to the edge channels of the cube (to maximize S/N). If freqstep is not specified, it is taken as zero, and the output channel range will typically be slightly smaller.

        The meaning of freqframe parameter is dependent on the value of getfreqrange.
        When getfreqrange=False, frequency parameters are considered as input parameters that are known to be in the frame specified by freqframe; but when getfreqrange=True, the frequency parameters are output parameters that will be determined in the frame specified by freqframe. In the former case, the frequencies will be converted to the frame of the data as a function of time in order to locate which channels match.

        You need to specify the field_id for which this calculation is
        being done.

        If the parameter {tt getfreqrange=True} then the reverse is requested. You set {tt spwselection} to be the range of data selection you want to use and you'll get the range of frequency covered in the frame you set. The freqstart and freqend output values correspond to the frequency of the extreme edges of the requested channel range.
        Inputs
        ----------------
        freqstart
        Begining of frequency range
        allowed:  double, string, quantity
        example: freqstart='1.0GHz'
        Default:
        ----------------
        freqend
        End of frequency range
        allowed:  double, string, quantity
        example: freqend='2.0GHz'
        Default:''
        -----------------
        freqstep
        spectral channel resolution of intended image
        allowed:  double, string, quantity
        example: freqstep='1.0MHz'
        Default:''
        -----------------
        freqframe
        frame in which frequency is being expressed in other parameters. For solar system  moving sources if the frame of the source is intended then this parameter can be 'SOURCE'
        allowed : one of the following strings 'LSRK', 'LSRD', 'BARY', 'GEO', 'TOPO', 'GALACTO', 'LGROUP','CMB', 'SOURCE'
        Default: 'LSRK'
        ----------------
        msname
        name of a valid measurement set.
        allowed: string
        Default: ''
        -----------------
        ephemtable
        when freqframe='SOURCE' this parameter is used
        name of a valid ephemeris table or 'TRACKFIELD' to use the ephemeris table attached to the FIELD subtable of the ms or one of the following solar system object: 'MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 'NEPTUNE', 'PLUTO', 'SUN', 'MOON'
        allowed: string
        Default: ''
        -----------------
        fieldid
        fieldid to use (needed to get the direction on the sky for any spectral frame conversion)
        allowed: integer
        Default: 0
        -------------------
        getfreqrange
        if set then freqrange is returned in the frame requested for the data selected
        allowed: bool
        Default: False
        -----------------
        spwselection
        if getfreqrange=True then this is needed to find the range of frequency in the frame requested. It should have the spectral window selection syntax as defined in the msselection (Casa memo 3)
        allowed: string
        Default: ''

        Input Parameters:
            freqstart                 Begining of frequency range in Hz
            freqend                   End of frequency range in Hz
            freqstep                  spectral channel resolution of intended image in Hz
            freqframe                 frame in which frequency is being expressed in other parameters
            ephemtable                valid ephemeris table name or TRACKFIELD (use ephemeris in FIELD subtable) if freqframe is SOURCE
            msname                    name of an ms, if empty string it will use the ms's used in selectvis
            fieldid                   fieldid to use when msname is not empty otherwise ignored and field selected in selectvis is used
            getfreqrange              if set then freqrange is returned in the frame requested for the data selected
            spwselection              if getfreqrange=True then this is needed to find the range of frequency in the frame requested

        Example:

        Example 1
        In this example, we are interested in an image cube which span 20.0682GHz to 20.1982 in LSRK  which will have a channel resolution of 3.9MHz. The field we are interested the one with fieldid=4

        #############################
        >>> from casatools import synthesisutils
        >>> syut=synthesisutils()
        >>> syut.advisechansel(freqstart='20.0682GHz', freqend='20.1982GHz', freqstep='3.9kHz', freqframe='LSRK', msname='test1.ms')
        {'nchan': array([109,  23], dtype=int32),  'spw': array([4, 5], dtype=int32),
        'start': array([19,  0], dtype=int32)}
        # implies 108 channels of spw 4 starting channel 19 and 23 channels of spw 5 starting at channel 0 would contribute data to the frequency range under consideration
        #############################

        Example 2

        To determine what is the frequency range in a given frame is covered by a given spwselection of the ms

        ##############
        >>> syut.advisechansel(msname='test3.ms', freqframe='LSRK', getfreqrange=True, spwselection='0:20~210')

        {'freqend': {'unit': 'Hz', 'value': 362746224619.3091}, 'freqstart': {'unit': 'Hz', 'value': 362512788988.5036}}

        ##############

        Example 3:

        Same as Example 1 but with a solar system moving source and the frequency range provided is in the frame of the source. We are using the ephemeris table attached to the FIELD subtable of the ms.

        ##########
        >>> syut.advisechansel(msname='uid___A002_Xc05f54_X142a_target.spw31.contsub.ms', freqstart='362.5145206GHz', freqend='362.7476643GHz', freqstep='122.064714kHz', fieldid=3, freqframe='SOURCE', ephemtable='TRACKFIELD')
        ###########
        Now one can do the same with a valid ephemeris table
        ###########
        >>> syut.advisechansel(msname='uid___A002_Xc05f54_X142a_target.spw31.contsub.ms', freqstart='362.5145206GHz', freqend='362.7476643GHz', freqstep='122.064714kHz', fieldid=3, freqframe='SOURCE', ephemtable='EPHEM0_Titan_57889.1.tab')
        ###########

        Or if we want it in the frame of a solar system source known by casa, e.g 'SATURN'
        ############
        >>> syut.advisechansel(msname='uid___A002_Xc05f54_X142a_target.spw31.contsub.ms', freqstart='362.5145206GHz', freqend='362.7476643GHz', freqstep='122.064714kHz', fieldid=3, freqframe='SOURCE', ephemtable='SATURN')
        ############

        Example 4:

        Same as Example 2  but with a solar system moving source and the frequency range we want to find is in the frame of the source.

        ############
        >>> syut.advisechansel(msname='uid___A002_Xc05f54_X142a_target.spw31.contsub.ms', fieldid=3, freqframe='SOURCE', ephemtable='TRACKFIELD', getfreqrange=True, spwselection='31:9~1919')
        #############
        similarly if we want it in the frame of a solar system source known casa e.g saturn
        #############
        >>> syut.advisechansel(msname='uid___A002_Xc05f54_X142a_target.spw31.contsub.ms', fieldid=3, freqframe='SOURCE', ephemtable='SATURN', getfreqrange=True, spwselection='31:9~1919')
        #############

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_advisechansel(self, *args, **kwargs)


    def cubedatapartition(self, *args, **kwargs) -> "record *":
        """
        cubedatapartition(self, _selpars, _npart, _fstart, _fend, _frame) -> record *



        Summary:
            Partition data selection parameters for CUBE imaging

        Description:


        returns a dictionary with data spectral parttiion that maps  data  to  nparts
        of the input range frequency... usually to be used for doing data selection
        when imaging a cube from fstart to fend in npart subcubes

        Input Parameters:
            selpars                   All selection parameters for one or more MSs
            npart                     Number of partitions
            fstart                    start frequency of cube image
            fend                      end frequency of cube image
            frame                     frame of fstart and fend

        Example:

        ##make a synthesisutils tool
        siu=casac.synthesisutils()
        ### define first ms parameters
        msrec={'msname':'ngc5921.ms.contsub', 'field':'0', 'spw':'0'}
        pars={'ms0':msrec}
        ##  can add ms1, ms2 etc for multiple ms  into dictionary pars

        ##now get the data selections for 20 subpart of a cube that
        ## spans from 1.412787GHz to 1.413287GHz
        siu.cubedatapartition(selprs=pars, npart=20, fstart='1.412787GHz', fend='1.413287GHz', frame='LSRK')

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_cubedatapartition(self, *args, **kwargs)


    def cubeimagepartition(self, *args, **kwargs) -> "record *":
        """
        cubeimagepartition(self, _impars, _npart) -> record *



        Summary:
            Partition image cube parameters for CUBE deconvolution

        Input Parameters:
            impars                    All imaging parameters for one or more image fields
            npart                     Number of partitions

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_cubeimagepartition(self, *args, **kwargs)


    def cubedataimagepartition(self, *args, **kwargs) -> "record *":
        """
        cubedataimagepartition(self, _selpars, _incsys, _npart, _nchannel) -> record *



        Summary:
            Partition data/image cube parameters for CUBE deconvolution

        Input Parameters:
            selpars                   All selection parameters for one or more MSs
            incsys                    input coordinate system
            npart                     Number of partitions
            nchannel                  Number of channels

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_cubedataimagepartition(self, *args, **kwargs)


    def checkselectionparams(self, *args, **kwargs) -> "record *":
        """
        checkselectionparams(self, _selpars) -> record *



        Summary:
            Check and Fix Selection Parameters for one MS

        Input Parameters:
            selpars                   All selection parameters for one MS

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_checkselectionparams(self, *args, **kwargs)


    def checkimageparams(self, *args, **kwargs) -> "record *":
        """
        checkimageparams(self, _impars) -> record *



        Summary:
            Check and Fix Imaging Parameters for one field

        Input Parameters:
            impars                    All imaging parameters for one image-field

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_checkimageparams(self, *args, **kwargs)


    def checkgridparams(self, *args, **kwargs) -> "record *":
        """
        checkgridparams(self, _gridpars) -> record *



        Summary:
            Check and Fix Gridding/FTM Parameters for one field

        Input Parameters:
            gridpars                  All gridding/ftm parameters for one image-field

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_checkgridparams(self, *args, **kwargs)


    def updateimpars(self, *args, **kwargs) -> "record *":
        """
        updateimpars(self, _impars) -> record *



        Summary:
            check the consistency between the csys record and other impars and update/modify impars if necessary

        Input Parameters:
            impars                    All image parameters of one image-field

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_updateimpars(self, *args, **kwargs)


    def getOptimumSize(self, *args, **kwargs) -> "long":
        """
        getOptimumSize(self, _size) -> long



        Summary:
            Get Optimum Image size

        Input Parameters:
            size                      Input size

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_getOptimumSize(self, *args, **kwargs)


    def fitPsfBeam(self, *args, **kwargs) -> "bool":
        """
        fitPsfBeam(self, _imagename, _nterms, _psfcutoff) -> bool



        Summary:
            Fit a restoring beam to the PSF, and save it in the PSF image.

        Input Parameters:
            imagename                 Image Prefix name
            nterms                    Single or Multi-Term (to pick namng conventions)
            psfcutoff                 A fractional cut-off level to determine what part of the PSF is sent to the beam fitter

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_fitPsfBeam(self, *args, **kwargs)


    def done(self) -> "bool":
        """
        done(self) -> bool



        Summary:
            Close the tool

        --------------------------------------------------------------------------------

        """
        return _synthesisutils.synthesisutils_done(self)

    __swig_destroy__ = _synthesisutils.delete_synthesisutils
    __del__ = lambda self: None
synthesisutils_swigregister = _synthesisutils.synthesisutils_swigregister
synthesisutils_swigregister(synthesisutils)

# This file is compatible with both classic and new-style classes.


