##################### generated by xml-casa (v2) from initweights.xml ###############
##################### 908788e72e2a98b7cf740d722da0a74a ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_initweights import initweights as _initweights_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _initweights:
    """
    initweights ---- Initializes weight information in the MS

    --------- parameter descriptions ---------------------------------------------

    vis       Name of input visibility file (MS)
    wtmode    Initialization mode
    tsystable Tsys calibration table to apply on the fly
    gainfield Select a subset of calibrators from Tsys table
    interp    Interpolation type in time[,freq]. default==\'linear,linear\'
    spwmap    Spectral windows combinations to form for gaintable(s)
    dowtsp    Initialize the WEIGHT_SPECTRUM column
    [1;42mRETURNS[1;m      void

    --------- examples -----------------------------------------------------------

    
    
    This task provides for initialization of the weight information
    in the MS.  For ALMA interferometry and EVLA data, it should not
    generally be necessary to use this task, as the per-spectral window
    weight information should have been initialized properly at
    fill time (v4.2.2 and later). To set per-channel weights, use
    initweights(vis=finalvis,wtmode='weight',dowtsp=True)
    
    Several initialization modes are supported via the wtmode parameter.
    
    If wtmode='nyq' (the default), SIGMA and WEIGHT will be
    initialized according to bandwidth and integration time.  This
    is the theoretically correct mode for raw normalized visibilities.
    (e.g., ALMA).  For the EVLA, this is correct if switched-power
    and bandpass calibration will later be applied.
    
    If wtmode='sigma', WEIGHT will be initialized according to the
    existing SIGMA column.
    
    If wtmode='weight', WEIGHT_SPECTRUM will be initialized according
    to the existing WEIGHT column; dowtspec=T must be specified in
    this case.
    
    If wtmode='ones', SIGMA and WEIGHT will be initialized with 1.0,
    globally.  This is a traditional means of initializing weight
    information, and is adequate when the integration time and
    bandwidth are uniform. It is not recommended for modern
    instruments (ALMA, EVLA), where variety in observational setups
    is common, and properly initialized and calibrated weights
    will be used for imaging sensitivity estimates.
    
    There are two EXPERIMENTAL modes, wtmode='tsys' and 'tinttsys'.
    In the modes, SIGMA and WEIGHT will be initialized according to
    Tsys, bandwidth, and integration time (used only in 'tinttsys'),
    i.e.,
    tsys    : weight=bw/Tsys^2
    tinttsys: weight=bw*t_int/Tsys^2
    These modes use Tsys values to calculate weight as is done in
    Tsys calibration. Tsys values are taken from a tsys calibration
    table given as tsystable. Selection of gain field (gainfield),
    interpolation method (interp), and spectral window mapping (spwmap)
    are supported, too.
    Available types of interpolation are,
    Time: 'nearest', 'linear', the variation of those with 'perobs',
    e.g., 'linearperobs' (enforce obsId boundaries in interpolation)
    Freq: 'nearest', 'linear', 'cubic', 'spline', and the variation
    of those with 'flag', e.g., 'linearflag' (with
    channelized flag).
    See the help of applycal for details of interpolations.
    Note if the weight in an MS is initialized with these modes and
    Tsys calibration table is applied with calwt=True after that, the
    weight would be contaminated by being devided by square of Tsys
    twice.
    !!! USERS ARE ADVISED TO USE THESE EXPERIMENTAL MODES WITH CARE !!!
    
    For the above wtmodes, if dowtsp=T (or if the WEIGHT_SPECTRUM
    column already exists), the WEIGHT_SPECTRUM column will be
    initialized (uniformly in channel in wtmode='nyq', 'sigma',
    'weight', and 'ones'), in a manner consistent with the
    disposition of the WEIGHT column.  If the WEIGHT_SPECTRUM
    column does not exist, dowtsp=T will force its creation.
    Use of the WEIGHT_SPECTRUM column is only meaningful
    for ALMA data which will be calibrated with channelized
    Tsys information, or if the weights will become channelized
    after calibration, e.g., via averaging over time- and
    channel-dependent flagging.  (A task for channel-dependent
    weight estimation from the data itself is also currently under
    development).
    In non-channelized modes (wtmode='nyq', 'sigma', 'weight', and
    'ones') or when dowtsp=F, SIGMA_SPECTRUM column will be removed
    from MS. On the other hand, SIGMA_SPECTRUM column is added and
    initialized in channelized modes (wtmode='tsys' and 'tinttsys')
    if dowtsp=T or WEIGHT_SPECTRUM already column exists.
    
    Two additional modes are available for managing the spectral
    weight info columns; these should be used with extreme care: If
    wtmode='delwtsp', the WEIGHT_SPECTRUM column will be deleted (if
    it exists).  If wtmode='delsigsp', the SIGMA_SPECTRUM column
    will be deleted (if it exists).  Note that creation of
    SIGMA_SPECTRUM is not supported via this method.
    
    Note that this task does not support any prior selection.
    Intialization of the weight information must currently be done
    globally or not at all.  This is to maintain consistency.
    
    


    """

    _info_group_ = """calibration"""
    _info_desc_ = """Initializes weight information in the MS"""

    def __call__( self, vis='', wtmode='nyq', tsystable='', gainfield='', interp='', spwmap=[  ], dowtsp=False ):
        schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'wtmode': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'delwtsp', 'nyq', 'ones', 'tsys', 'weight', 'tinttsys', 'sigma', 'delsigsp' ]}, 'tsystable': {'type': 'cPath', 'coerce': _coerce.expand_path}, 'gainfield': {'type': 'cStr', 'coerce': _coerce.to_str}, 'interp': {'type': 'cStr', 'coerce': _coerce.to_str}, 'spwmap': {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}, 'dowtsp': {'type': 'cBool'}}
        doc = {'vis': vis, 'wtmode': wtmode, 'tsystable': tsystable, 'gainfield': gainfield, 'interp': interp, 'spwmap': spwmap, 'dowtsp': dowtsp}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'initweights', [ 'vis=' + repr(_pc.document['vis']), 'wtmode=' + repr(_pc.document['wtmode']), 'tsystable=' + repr(_pc.document['tsystable']), 'gainfield=' + repr(_pc.document['gainfield']), 'interp=' + repr(_pc.document['interp']), 'spwmap=' + repr(_pc.document['spwmap']), 'dowtsp=' + repr(_pc.document['dowtsp']) ] )
        task_result = None
        try:
            task_result = _initweights_t( _pc.document['vis'], _pc.document['wtmode'], _pc.document['tsystable'], _pc.document['gainfield'], _pc.document['interp'], _pc.document['spwmap'], _pc.document['dowtsp'] )
        except Exception as exc:
            _except_log('initweights', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'initweights', task_result )
        return task_result

initweights = _initweights( )

