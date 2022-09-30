##################### generated by xml-casa (v2) from fringefit.xml #################
##################### 2b50148f2384a4dfbb898078766534f4 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_fringefit import fringefit as _fringefit_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _fringefit:
    """
    fringefit ---- Fringe fit delay and rates

    
    Phase offsets, groups delays and delay rates are calculated with
    respect to a specified referance antenna by a two-dimensional FFT and
    subsequent least-squares optimisation.
    
    Previous calibrations should be applied on the fly.

    --------- parameter descriptions ---------------------------------------------

    vis          Name of input visibility file
    caltable     Name of output gain calibration table
    field        Select field using field id(s) or field name(s)
    spw          Select spectral window/channels
    intent       Select observing intent
    selectdata   Other data selection parameters
    timerange    Select data based on time range
    uvrange      Select data by baseline length.
                 Default = '' (all)
                 
                    Examples:
                    uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                    uvrange='>4klambda';uvranges greater than 4 kilo-lambda
                    uvrange='0~1000km'; uvrange in kilometers
    antenna      Select data based on antenna/baseline
    scan         Scan number range
    observation  Select by observation ID(s)
    msselect     Optional complex data selection (ignore for now)
    solint       Solution interval: egs. \'inf\', \'60s\' (see help)
    combine      Data axes which to combine for solve (obs, scan, spw, and/or field)
    refant       Reference antenna name(s)
    minsnr       Reject solutions below this signal-to-noise ratio (at the FFT stage)
    zerorates    Zero delay-rates in solution table
                 
                     Write a solution table with delay-rates zeroed, for the case of
                 "manual phase calibration", so that the calibration table can be
                 applied to the full dataset without the extrapolation of a non-zero delay-rate term
                 affecting the data
    globalsolve  Refine estimates of delay and rate with global least-squares solver
    niter        Maximum number of iterations for least-squares solver
    delaywindow  Constrain FFT delay search to a window specified as a two-element list with units of nanoseconds
                 Default: [None, None]
                 Examples: [-10, 10]
    ratewindow   Constrain FFT rate search to a window specified as a two-element list with units of seconds per second
                 Default: [None, None]
                 Examples: [-1e-13, 1e-13]
    append       Append solutions to the (existing) table
                 Default: False (overwrite existing table or make
                 new table)
                 
                 Appended solutions must be derived from the same
                 MS as the existing caltable, and solution spws
                 must have the same meta-info (according to spw
                 selection and solint) or be non-overlapping.
    corrdepflags f False (default), if any correlation is flagged, treat all correlations in
                       the visibility vector as flagged when solving (per channel, per baseline).
                       If True, use unflagged correlations in a visibility vector, even if one or more
                       other correlations are flagged.
                             
                       Default: False (treat correlation vectors with one or more correlations flagged as entirely flagged)
                 
                       Traditionally, CASA has observed a strict interpretation of 
                       correlation-dependent flags: if one or more correlations 
                       (for any baseline and channel) is flagged, then all available 
                       correlations for the same baseline and channel are 
                       treated as flagged.  However, it is desirable in some 
                       circumstances to relax this stricture, e.g., to preserve use
                       of data from antennas with only one good polarization (e.g., one polarization
                       is bad or entirely absent).  Solutions for the bad or missing polarization 
                       will be rendered as flagged.
    docallib     Control means of specifying the caltables
                 Default: False (Use gaintable, gainfield, interp,
                 spwmap, calwt)
                 Options: False|True
                 
                 If True, specify a file containing cal library in
                 callib
    callib       Specify a file containing cal library directives
                 Subparameter of docallib=True
    gaintable    Gain calibration table(s) to apply on the fly
                 Default: '' (none)
                 Subparameter of docallib=False
                 Examples: 
                 gaintable='ngc5921.gcal'
                 gaintable=['ngc5921.ampcal','ngc5921.phcal']
    gainfield    Select a subset of calibrators from gaintable(s)
                 Default: '' (all sources on the sky)
                 
                 'nearest' ==> nearest (on sky) available field in
                 table otherwise, same syntax as field
                 
                 Examples: 
                 gainfield='0~2,5' means use fields 0,1,2,5
                 from gaintable
                 gainfield=['0~3','4~6'] means use field 0
                 through 3
    interp       Interpolation parameters (in time[,freq]) for each gaintable, as a list of strings.
                 Default: '' --> 'linear,linear' for all gaintable(s)
                 Options: Time: 'nearest', 'linear'
                 Freq: 'nearest', 'linear', 'cubic',
                 'spline'
                 Specify a list of strings, aligned with the list of caltable specified
                 in gaintable, that contain the required interpolation parameters
                 for each caltable.
                 * When frequency interpolation is relevant (B, Df,
                 Xf), separate time-dependent and freq-dependent
                 interp types with a comma (freq after the
                 comma). 
                 * Specifications for frequency are ignored when the
                 calibration table has no channel-dependence. 
                 * Time-dependent interp options ending in 'PD'
                 enable a "phase delay" correction per spw for
                 non-channel-dependent calibration types.
                 * For multi-obsId datasets, 'perobs' can be
                 appended to the time-dependent interpolation
                 specification to enforce obsId boundaries when
                 interpolating in time. 
                 * Freq-dependent interp options can have 'flag' appended
                 to enforce channel-dependent flagging, and/or 'rel' 
                 appended to invoke relative frequency interpolation
                 
                 Examples: 
                 interp='nearest' (in time, freq-dep will be
                 linear, if relevant)
                 interp='linear,cubic'  (linear in time, cubic
                 in freq)
                 interp='linearperobs,splineflag' (linear in
                 time per obsId, spline in freq with
                 channelized flagging)
                 interp='nearest,linearflagrel' (nearest in
                 time, linear in freq with with channelized 
                 flagging and relative-frequency interpolation)
                 interp=',spline'  (spline in freq; linear in
                 time by default)
                 interp=['nearest,spline','linear']  (for
                 multiple gaintables)
    spwmap       Spectral window mappings to form for gaintable(s)
                 Only used if callib=False
                 default: [] (apply solutions from each calibration spw to
                 the same MS spw only)
                 Any available calibration spw can be mechanically mapped to any 
                  MS spw. 
                 Examples:
                    spwmap=[0,0,1,1] means apply calibration 
                      from cal spw = 0 to MS spw 0,1 and cal spw 1 to MS spws 2,3.
                    spwmap=[[0,0,1,1],[0,1,0,1]] (use a list of lists for multiple
                      gaintables)
    paramactive  Control which parameters are solved for; a vector of (exactly) three booleans for delay, delay-rate and dispersive delay (in that order)
    parang       Apply parallactic angle correction on the fly.

    --------- examples -----------------------------------------------------------

    
    For more information, see the task pages of gaincal in CASA Docs:
    
    https://casa.nrao.edu/casadocs/
    minsnr -- Reject solutions below this SNR
    default: 3.0


    """

    _info_group_ = """calibration"""
    _info_desc_ = """Fringe fit delay and rates"""

    def __call__( self, vis='', caltable='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='', refant='', minsnr=float(3.0), zerorates=False, globalsolve=True, niter=int(100), delaywindow=[  ], ratewindow=[  ], append=False, corrdepflags=False, docallib=False, callib='', gaintable=[  ], gainfield=[  ], interp=[  ], spwmap=[ ], paramactive=[  ], parang=False ):
        schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'caltable': {'type': 'cStr', 'coerce': _coerce.to_str}, 'field': {'type': 'cStr', 'coerce': _coerce.to_str}, 'spw': {'type': 'cStr', 'coerce': _coerce.to_str}, 'intent': {'type': 'cStr', 'coerce': _coerce.to_str}, 'selectdata': {'type': 'cBool'}, 'timerange': {'type': 'cStr', 'coerce': _coerce.to_str}, 'uvrange': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'antenna': {'type': 'cStr', 'coerce': _coerce.to_str}, 'scan': {'type': 'cStr', 'coerce': _coerce.to_str}, 'observation': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cInt'}]}, 'msselect': {'type': 'cStr', 'coerce': _coerce.to_str}, 'solint': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'combine': {'type': 'cStr', 'coerce': _coerce.to_str}, 'refant': {'type': 'cStr', 'coerce': _coerce.to_str}, 'minsnr': {'type': 'cFloat', 'coerce': _coerce.to_float}, 'zerorates': {'type': 'cBool'}, 'globalsolve': {'type': 'cBool'}, 'niter': {'type': 'cInt'}, 'delaywindow': {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, 'ratewindow': {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, 'append': {'type': 'cBool'}, 'corrdepflags': {'type': 'cBool'}, 'docallib': {'type': 'cBool'}, 'callib': {'type': 'cStr', 'coerce': _coerce.to_str}, 'gaintable': {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}, 'gainfield': {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}, 'interp': {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}, 'spwmap': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'paramactive': {'type': 'cBoolVec', 'coerce': [_coerce.to_list,_coerce.to_boolvec]}, 'parang': {'type': 'cBool'}}
        doc = {'vis': vis, 'caltable': caltable, 'field': field, 'spw': spw, 'intent': intent, 'selectdata': selectdata, 'timerange': timerange, 'uvrange': uvrange, 'antenna': antenna, 'scan': scan, 'observation': observation, 'msselect': msselect, 'solint': solint, 'combine': combine, 'refant': refant, 'minsnr': minsnr, 'zerorates': zerorates, 'globalsolve': globalsolve, 'niter': niter, 'delaywindow': delaywindow, 'ratewindow': ratewindow, 'append': append, 'corrdepflags': corrdepflags, 'docallib': docallib, 'callib': callib, 'gaintable': gaintable, 'gainfield': gainfield, 'interp': interp, 'spwmap': spwmap, 'paramactive': paramactive, 'parang': parang}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'fringefit', [ 'vis=' + repr(_pc.document['vis']), 'caltable=' + repr(_pc.document['caltable']), 'field=' + repr(_pc.document['field']), 'spw=' + repr(_pc.document['spw']), 'intent=' + repr(_pc.document['intent']), 'selectdata=' + repr(_pc.document['selectdata']), 'timerange=' + repr(_pc.document['timerange']), 'uvrange=' + repr(_pc.document['uvrange']), 'antenna=' + repr(_pc.document['antenna']), 'scan=' + repr(_pc.document['scan']), 'observation=' + repr(_pc.document['observation']), 'msselect=' + repr(_pc.document['msselect']), 'solint=' + repr(_pc.document['solint']), 'combine=' + repr(_pc.document['combine']), 'refant=' + repr(_pc.document['refant']), 'minsnr=' + repr(_pc.document['minsnr']), 'zerorates=' + repr(_pc.document['zerorates']), 'globalsolve=' + repr(_pc.document['globalsolve']), 'niter=' + repr(_pc.document['niter']), 'delaywindow=' + repr(_pc.document['delaywindow']), 'ratewindow=' + repr(_pc.document['ratewindow']), 'append=' + repr(_pc.document['append']), 'corrdepflags=' + repr(_pc.document['corrdepflags']), 'docallib=' + repr(_pc.document['docallib']), 'callib=' + repr(_pc.document['callib']), 'gaintable=' + repr(_pc.document['gaintable']), 'gainfield=' + repr(_pc.document['gainfield']), 'interp=' + repr(_pc.document['interp']), 'spwmap=' + repr(_pc.document['spwmap']), 'paramactive=' + repr(_pc.document['paramactive']), 'parang=' + repr(_pc.document['parang']) ] )
        task_result = None
        try:
            task_result = _fringefit_t( _pc.document['vis'], _pc.document['caltable'], _pc.document['field'], _pc.document['spw'], _pc.document['intent'], _pc.document['selectdata'], _pc.document['timerange'], _pc.document['uvrange'], _pc.document['antenna'], _pc.document['scan'], _pc.document['observation'], _pc.document['msselect'], _pc.document['solint'], _pc.document['combine'], _pc.document['refant'], _pc.document['minsnr'], _pc.document['zerorates'], _pc.document['globalsolve'], _pc.document['niter'], _pc.document['delaywindow'], _pc.document['ratewindow'], _pc.document['append'], _pc.document['corrdepflags'], _pc.document['docallib'], _pc.document['callib'], _pc.document['gaintable'], _pc.document['gainfield'], _pc.document['interp'], _pc.document['spwmap'], _pc.document['paramactive'], _pc.document['parang'] )
        except Exception as exc:
            _except_log('fringefit', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'fringefit', task_result )
        return task_result

fringefit = _fringefit( )

