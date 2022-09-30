##################### generated by xml-casa (v2) from predictcomp.xml ###############
##################### 72a05d658fe103e7f240bb1a6f564f30 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_predictcomp import predictcomp as _predictcomp_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _predictcomp:
    """
    predictcomp ---- Make a component list for a known calibrator

    
    Writes a component list named clist to disk and returns a dict of
    {'clist': clist,
    'objname': objname,
    'standard': standard,
    'epoch': epoch,
    'freqs': pl.array of frequencies, in GHz,
    'antennalist': a simdata type configuration file,
    'amps':  pl.array of predicted visibility amplitudes, in Jy,
    'savedfig': False or, if made, the filename of a plot.}
    or False on error.
    

    --------- parameter descriptions ---------------------------------------------

    objname     Object name
    standard    Flux density standard
    epoch       Epoch
    minfreq     Minimum frequency
    maxfreq     Maximum frequency
    nfreqs      Number of frequencies
    prefix      Prefix for the component list directory name.
    antennalist Plot for this configuration
    showplot    Plot S vs \|u\| to the screen?
    savefig     Save a plot of S vs \|u\| to this filename
    symb        A matplotlib plot symbol code
    include0amp Force the amplitude axis to start at 0?
    include0bl  Force the baseline axis to start at 0?
    blunit      unit of the baseline axis
    showbl0flux Print the zero baseline flux ?
    [1;42mRETURNS[1;m        record

    --------- examples -----------------------------------------------------------

    
    
    Writes a component list to disk and returns a dict of
    {'clist': filename of the component list,
    'objname': objname,
    'angdiam': angular diameter in radians (if used in clist),
    'standard': standard,
    'epoch': epoch,
    'freqs': pl.array of frequencies, in GHz,
    'antennalist': pl.array of baseline lengths, in m,
    'amps':  pl.array of predicted visibility amplitudes, in Jy,
    'savedfig': False or, if made, the filename of a plot.}
    or False on error.
    
    objname: An object supported by standard.
    standard: A standard for calculating flux densities, as in setjy.
    Default: 'Butler-JPL-Horizons 2010'
    epoch: The epoch to use for the calculations.   Irrelevant for
    extrasolar standards. (Uses UTC)
    Examples: '2011-12-31/5:34:12', '2011-12-31-5:34:12'
    minfreq: The minimum frequency to use.
    Example: '342.0GHz'
    maxfreq: The maximum frequency to use.
    Default: minfreq
    Example: '346.0GHz'
    Example: '', anything <= 0, or None: use minfreq.
    nfreqs:  The number of frequencies to use.
    Default: 1 if minfreq == maxfreq,
    2 otherwise.
    prefix: The component list will be saved to
    prefix + 'spw0_<objname>_<minfreq><epoch>.cl'
    Default: ''
    Example: "Bands3to7_"
    (which could produce 'Bands3to7_Uranus_spw0_100GHz55877d.cl',
    depending on the other parameters)
    antennalist: 'Observe' and plot the visibility amplitudes for this
    antenna configuration.  The file should be in a format usable
    by simdata.  The search path is:
    .:casa['dirs']['data'] + '/alma/simmos/'
    Default: '' (None, just make clist.)
    Example: 'alma.cycle0.extended.cfg'
    
    Subparameters of antennalist:
    showplot: Whether or not to show a plot of S vs. |u| on screen.
    Subparameter of antennalist.
    Default: Necessarily False if antennalist is not specified.
    True otherwise.
    savefig: Filename for saving a plot of S vs. |u|.
    Subparameter of antennalist.
    Default: ''
    Examples: ''           (do not save the plot)
    'myplot.png' (save to myplot.png)
    symb: One of matplotlib's codes for plot symbols: .:,o^v<>s+xDd234hH|_
    Default: '.'
    include0amp: Force the amplitude axis to start at 0?
    Default: False
    include0bl: Force the baseline axis to start at 0?
    Default: False
    blunit: unit of the baseline axis ('' or 'klambda')
    Default:''=use a unit in the data
    showbl0flux: Print the zero baseline flux?
    Default: False
    
    


    """

    _info_group_ = """imaging, calibration"""
    _info_desc_ = """Make a component list for a known calibrator"""

    def __call__( self, objname='', standard='Butler-JPL-Horizons 2010', epoch='', minfreq='', maxfreq='', nfreqs=int(2), prefix='', antennalist='', showplot=False, savefig='', symb='.', include0amp=False, include0bl=False, blunit='', showbl0flux=False ):
        schema = {'objname': {'type': 'cStr', 'coerce': _coerce.to_str}, 'standard': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'Perley-Taylor 95', 'Butler-JPL-Horizons 2010', 'Perley-Butler 2010', 'Perley-Taylor 99', 'Perley-Butler 2013', 'Perley 90', 'Butler-JPL-Horizons 2012', 'Perley-Butler 2017', 'Baars' ]}, 'epoch': {'type': 'cStr', 'coerce': _coerce.to_str}, 'minfreq': {'type': 'cStr', 'coerce': _coerce.to_str}, 'maxfreq': {'type': 'cStr', 'coerce': _coerce.to_str}, 'nfreqs': {'type': 'cInt'}, 'prefix': {'type': 'cPath', 'coerce': _coerce.expand_path}, 'antennalist': {'type': 'cStr', 'coerce': _coerce.to_str}, 'showplot': {'type': 'cBool'}, 'savefig': {'type': 'cStr', 'coerce': _coerce.to_str}, 'symb': {'type': 'cStr', 'coerce': _coerce.to_str}, 'include0amp': {'type': 'cBool'}, 'include0bl': {'type': 'cBool'}, 'blunit': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ '', 'klambda' ]}, 'showbl0flux': {'type': 'cBool'}}
        doc = {'objname': objname, 'standard': standard, 'epoch': epoch, 'minfreq': minfreq, 'maxfreq': maxfreq, 'nfreqs': nfreqs, 'prefix': prefix, 'antennalist': antennalist, 'showplot': showplot, 'savefig': savefig, 'symb': symb, 'include0amp': include0amp, 'include0bl': include0bl, 'blunit': blunit, 'showbl0flux': showbl0flux}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'predictcomp', [ 'objname=' + repr(_pc.document['objname']), 'standard=' + repr(_pc.document['standard']), 'epoch=' + repr(_pc.document['epoch']), 'minfreq=' + repr(_pc.document['minfreq']), 'maxfreq=' + repr(_pc.document['maxfreq']), 'nfreqs=' + repr(_pc.document['nfreqs']), 'prefix=' + repr(_pc.document['prefix']), 'antennalist=' + repr(_pc.document['antennalist']), 'showplot=' + repr(_pc.document['showplot']), 'savefig=' + repr(_pc.document['savefig']), 'symb=' + repr(_pc.document['symb']), 'include0amp=' + repr(_pc.document['include0amp']), 'include0bl=' + repr(_pc.document['include0bl']), 'blunit=' + repr(_pc.document['blunit']), 'showbl0flux=' + repr(_pc.document['showbl0flux']) ] )
        task_result = None
        try:
            task_result = _predictcomp_t( _pc.document['objname'], _pc.document['standard'], _pc.document['epoch'], _pc.document['minfreq'], _pc.document['maxfreq'], _pc.document['nfreqs'], _pc.document['prefix'], _pc.document['antennalist'], _pc.document['showplot'], _pc.document['savefig'], _pc.document['symb'], _pc.document['include0amp'], _pc.document['include0bl'], _pc.document['blunit'], _pc.document['showbl0flux'] )
        except Exception as exc:
            _except_log('predictcomp', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'predictcomp', task_result )
        return task_result

predictcomp = _predictcomp( )

