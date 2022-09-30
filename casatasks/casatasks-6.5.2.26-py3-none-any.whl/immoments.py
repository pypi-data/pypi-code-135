##################### generated by xml-casa (v2) from immoments.xml #################
##################### 71135811d8080ad40de603edf0247328 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_immoments import immoments as _immoments_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _immoments:
    """
    immoments ---- Compute moments from an image

    --------- parameter descriptions ---------------------------------------------

    imagename  Name of the input image
    moments    List of moments you would like to compute
    axis       The momement axis: ra, dec, lat, long, spectral, or stokes
    region     Region selection. Default is to use the full image.
    box        Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
    chans      Channels to use. Default is to use all channels.
    stokes     Stokes planes to use. Default is to use all Stokes planes.
    mask       Mask to use. Default is none.
    includepix Range of pixel values to include
    excludepix Range of pixel values to exclude
    outfile    Output image file name (or root for multiple moments)
    stretch    Stretch the mask if necessary and possible?
    [1;42mRETURNS[1;m       bool

    --------- examples -----------------------------------------------------------

    
    The spectral moment distributions at each pixel are
    determined.  See the cookbook and User Reference Manual for
    mathematical details.
    
    The main control of the calculation is given by parameter
    moments:
    
    moments=-1  - mean value of the spectrum
    moments=0   - integrated value of the spectrum
    moments=1   - intensity weighted coordinate;traditionally used to get
    'velocity fields'
    moments=2   - intensity weighted dispersion of the coordinate; traditionally
    used to get "velocity dispersion"
    moments=3   - median of I
    moments=4   - median coordinate
    moments=5   - standard deviation about the mean of the spectrum
    moments=6   - root mean square of the spectrum
    moments=7   - absolute mean deviation of the spectrum
    moments=8   - maximum value of the spectrum
    moments=9   - coordinate of the maximum value of the spectrum
    moments=10  - minimum value of the spectrum
    moments=11  - coordinate of the minimum value of the spectrum
    
    Keyword arguments:
    imagename    Name of input image
    default: none; example: imagename="ngc5921_task.image"
    moments      List of moments you would like to compute
    default: 0 (integrated spectrum);example: moments=[0,1]
    see list above
    axis         The moment axis
    default: (spectral axis); example: axis=spec
    options: ra, dec, lattitude, longitude, spectral, stokes
    mask         Mask to use. Default is none.
    stretch      Stretch the input mask if necessary and possible. See below.
    region       Region selection. Default
    is to use the full image.
    box         Rectangular region to select in direction plane. See
    Default is to use the entire direction plane.
    Example: box="10,10,50,50"
    box = "10,10,30,30,35,35,50,50" (two boxes)
    chans       Channels to use. Default is to use
    all channels.
    
    stokes      Stokes planes to use. Default is to
    use all Stokes planes.
    Example: stokes="IQUV";
    Example:stokes="I,Q"
    includepix  Range of pixel values to include
    default: [-1] (all pixels); example=[0.02,100.0]
    excludepix  Range of pixel values to exclude
    default: [-1] (don"t exclude pixels); example=[100.,200.]
    outfile     Output image file name (or root for multiple moments)
    default: "" (input+auto-determined suffix);example: outfile="source_moment"
    
    If stretch is true and if the number of mask dimensions is less than
    or equal to the number of image dimensions and some axes in the
    mask are degenerate while the corresponding axes in the image are not,
    the mask will be stetched in the degenerate axis dimensions. For example,
    if the input image has shape [100, 200, 10] and the input
    mask has shape [100, 200, 1] and stretch is true, the mask will be
    stretched along the third dimension to shape [100, 200, 10]. However if
    the mask is shape [100, 200, 2], stretching is not possible and an
    error will result.
    
    Example for finding the 1-momment, intensity-weighted
    coordinate, often used for finding velocity fields.
    immoments( axis="spec", imagename="myimage", moment=1, outfile="velocityfields" )
    
    Example finding the spectral mean, -1 moment, on a specified region
    of the image as defined by the box and stokes parameters
    taskname="immoments"
    default()
    imagename = "myimage"
    moment    =  -1
    
    axis      = "spec"
    stokes     = "I"
    box       = [55,12,97,32]
    go
    
    Example using a mask created with a second file to select the
    data used to calculate the 0-moments, integrated values.  In
    this case the mask is from the calibrated.im file and all values
    that have a value greater than 0.5 will be positive in the mask..
    immoments( "clean.image", axis="spec", mask="calibrated.im>0.5", outfile="mom_withmask.im" )
    
    If an image has multiple (per-channel beams) and the moment axis is equal to the
    spectral axis, each channel will be convolved with a beam that is equal to the beam
    having the largest area in the beamset prior to moment determination.


    """

    _info_group_ = """analysis"""
    _info_desc_ = """Compute moments from an image"""

    def __call__( self, imagename='', moments=[ int(0) ], axis='spectral', region='', box='', chans='', stokes='', mask='', includepix=int(-1), excludepix=int(-1), outfile='', stretch=False ):
        schema = {'imagename': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'moments': {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}, 'axis': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cInt'}]}, 'region': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}]}, 'box': {'type': 'cStr', 'coerce': _coerce.to_str}, 'chans': {'type': 'cStr', 'coerce': _coerce.to_str}, 'stokes': {'type': 'cStr', 'coerce': _coerce.to_str}, 'mask': {'type': 'cStr', 'coerce': _coerce.to_str}, 'includepix': {'anyof': [{'type': 'cInt'}, {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}]}, 'excludepix': {'anyof': [{'type': 'cInt'}, {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}]}, 'outfile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'stretch': {'type': 'cBool'}}
        doc = {'imagename': imagename, 'moments': moments, 'axis': axis, 'region': region, 'box': box, 'chans': chans, 'stokes': stokes, 'mask': mask, 'includepix': includepix, 'excludepix': excludepix, 'outfile': outfile, 'stretch': stretch}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'immoments', [ 'imagename=' + repr(_pc.document['imagename']), 'moments=' + repr(_pc.document['moments']), 'axis=' + repr(_pc.document['axis']), 'region=' + repr(_pc.document['region']), 'box=' + repr(_pc.document['box']), 'chans=' + repr(_pc.document['chans']), 'stokes=' + repr(_pc.document['stokes']), 'mask=' + repr(_pc.document['mask']), 'includepix=' + repr(_pc.document['includepix']), 'excludepix=' + repr(_pc.document['excludepix']), 'outfile=' + repr(_pc.document['outfile']), 'stretch=' + repr(_pc.document['stretch']) ] )
        task_result = None
        try:
            task_result = _immoments_t( _pc.document['imagename'], _pc.document['moments'], _pc.document['axis'], _pc.document['region'], _pc.document['box'], _pc.document['chans'], _pc.document['stokes'], _pc.document['mask'], _pc.document['includepix'], _pc.document['excludepix'], _pc.document['outfile'], _pc.document['stretch'] )
        except Exception as exc:
            _except_log('immoments', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'immoments', task_result )
        return task_result

immoments = _immoments( )

