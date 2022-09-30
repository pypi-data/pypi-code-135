##################### generated by xml-casa (v2) from sdfixscan.xml #################
##################### 6a1de0fd6bb62ca1dace38fc285b49d9 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_sdfixscan import sdfixscan as _sdfixscan_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _sdfixscan:
    """
    sdfixscan ---- Task for single-dish image processing

    
    Task sdfixscan is used to remove a scanning noise that appears
    as a striped noise pattern along the scan direction in a raster
    scan data.
    
    By default, the scanning noise is removed by using the
    FFT-based 'Basket-Weaving' method (Emerson & Grave 1988) that
    requires multiple images that observed exactly the same area with
    different scanning direction. If only one image is available, the
    'Pressed-out' method (Sofue & Reich 1979) can be used to remove
    the scanning effect.
    

    --------- parameter descriptions ---------------------------------------------

    infiles    list of name of input SD images (FITS or CASA image)
    mode       image processing mode
    numpoly    order of polynomial fit for Pressed-out method
    beamsize   beam size for Pressed-out method
    smoothsize size of smoothing beam for Pressed-out method
    direction  scan direction (p.a.) counterclockwise from the horizontal axis in unit of degree
    maskwidth  mask width for Basket-Weaving (on percentage)
    tmax       maximum threshold value for processing
    tmin       minimum threshold value for processing
    outfile    name of output file
    overwrite  overwrite the output file if already exists
    [1;42mRETURNS[1;m       void

    --------- examples -----------------------------------------------------------

    
    -----------------
    Keyword arguments
    -----------------
    infiles -- name or list of names of input SD (FITS or CASA) image(s)
    mode -- image processing mode
    options: 'fft_mask' (FFT-based Basket-Weaving),
    'model' (Pressed-out method)
    default: 'fft_mask'
    >>>mode expandable parameter
    direction -- scan direction (p.a.) counterclockwise from the
    horizontal axis in unit of degree.
    default: []
    example: direction=[0.0, 90.0] means that the first image
    has scan direction along longitude axis while the
    second image is along latitude axis.
    maskwidth -- mask width for Basket-Weaving on percentage
    default: 1.0 (1.0% of map size)
    numpoly -- order of polynomial fit in Presssed-out method
    default: 2
    beamsize -- beam size for Pressed-out method
    default: 0.0
    example: beamsize=10.0 is interpreted as '10arcsec'.
    beamsize='1arcmin' specifies beam size as
    quantity.
    smoothsize -- smoothing beam size in Pressed-out method.
    if numeric value is given, it is interpreted in unit
    of beam size specified by the parameter beamsize
    default: 2.0
    example: smoothsize=2.0 means that smoothing beam size is
    2.0 * beamsize.
    smoothsize='1arcmin' sets smoothsize directly.
    tmax -- maximum threshold value for processing
    default: 0.0 (no threshold in maximum)
    example: 10.0 (mask data larger value than 10.0)
    tmin -- minimum threshold value for processing
    default: 0.0 (no threshold in minimum)
    example: -10.0 (mask data smaller value than -10.0)
    outfile -- name of output file. output file is in CASA image format.
    default: '' (use default name 'sdfixscan.out.im')
    example: 'output.im'
    overwrite -- overwrite the output file if already exists
    options: (bool) True, False
    default: False
    
    -----------
    DESCRIPTION
    -----------
    Task sdfixscan is used to remove a scanning noise that appears
    as a striped noise pattern along the scan direction in a raster
    scan data.
    
    By default, the scanning noise is removed by using the FFT-based
    'Basket-Weaving' method (Emerson & Grave 1988) that requires
    multiple images that observed exactly the same area with different
    scanning direction. If only one image is available, the 'Pressed-out'
    method (Sofue & Reich 1979) can be used to remove the scanning
    effect.
    
    For 'Basket-Weaving', scanning directions must have at least two
    different values. Normally, the scanning direction should be
    specified for each input image. Otherwise, specified scanning
    directions will be used iteratively. The maskwidth is a width of
    masking region in the Fourier plane. It is specified as a fraction
    (percentage) of the image size.
    
    For 'Pressed-out', the scanning direction must be unique. There are
    two ways to specify a size of smoothing beam used for process. One
    is to specify smoothing size directly. To do this, smoothsize should
    be specified as string that consists of a numerical value and an unit
    (e.g. '10.0arcsec'). A value of beamsize will be ignored in this case.
    Another way to specify smoothing size is to set an observed beam size
    and indicate smoothing size as a scale factor of the observed beam
    size. In this case, the beamsize is interpreted as the observed beam
    size, and the smoothsize is the scale factor. If the beamsize is
    provided as float value, its unit is assumed to 'arcsec'. It is also
    possible to set the beamsize as string consisting of the numerical
    value and the unit. The smoothsize must be float value.
    
    The infiles only allows an image data (CASA or FITS), and does not
    work with MS or Scantable. The direction is an angle with respect to
    the horizontal direction, and its unit is degree. Any value may be
    interpreted properly, but the value ranging from 0.0 to 180.0 will
    be secure. The tmax and the tmin is used to specify a threshold that
    defines a range of spectral values used for processing. The data point
    that has the value larger than tmax or smaller than tmin will be
    excluded from the processing. The default (0.0) is no threshold.
    The outfile specifies an output CASA image name. If the outfile is
    empty, the default name ('sdfixscan.out.im') will be used.
    


    """

    _info_group_ = """single dish"""
    _info_desc_ = """Task for single-dish image processing"""

    def __call__( self, infiles=[  ], mode='fft_mask', numpoly=int(2), beamsize=float(0.0), smoothsize=float(2.0), direction=[  ], maskwidth=float(1.0), tmax=float(0.0), tmin=float(0.0), outfile='', overwrite=False ):
        schema = {'infiles': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'mode': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'fft_mask', 'model' ]}, 'numpoly': {'type': 'cInt'}, 'beamsize': {'type': 'cFloat', 'coerce': _coerce.to_float}, 'smoothsize': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'direction': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'maskwidth': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'tmax': {'type': 'cFloat', 'coerce': _coerce.to_float}, 'tmin': {'type': 'cFloat', 'coerce': _coerce.to_float}, 'outfile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'overwrite': {'type': 'cBool'}}
        doc = {'infiles': infiles, 'mode': mode, 'numpoly': numpoly, 'beamsize': beamsize, 'smoothsize': smoothsize, 'direction': direction, 'maskwidth': maskwidth, 'tmax': tmax, 'tmin': tmin, 'outfile': outfile, 'overwrite': overwrite}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'sdfixscan', [ 'infiles=' + repr(_pc.document['infiles']), 'mode=' + repr(_pc.document['mode']), 'numpoly=' + repr(_pc.document['numpoly']), 'beamsize=' + repr(_pc.document['beamsize']), 'smoothsize=' + repr(_pc.document['smoothsize']), 'direction=' + repr(_pc.document['direction']), 'maskwidth=' + repr(_pc.document['maskwidth']), 'tmax=' + repr(_pc.document['tmax']), 'tmin=' + repr(_pc.document['tmin']), 'outfile=' + repr(_pc.document['outfile']), 'overwrite=' + repr(_pc.document['overwrite']) ] )
        task_result = None
        try:
            task_result = _sdfixscan_t( _pc.document['infiles'], _pc.document['mode'], _pc.document['numpoly'], _pc.document['beamsize'], _pc.document['smoothsize'], _pc.document['direction'], _pc.document['maskwidth'], _pc.document['tmax'], _pc.document['tmin'], _pc.document['outfile'], _pc.document['overwrite'] )
        except Exception as exc:
            _except_log('sdfixscan', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'sdfixscan', task_result )
        return task_result

sdfixscan = _sdfixscan( )

