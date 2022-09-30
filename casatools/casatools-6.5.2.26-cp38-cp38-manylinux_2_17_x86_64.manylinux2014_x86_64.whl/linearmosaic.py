##################### generated by xml-casa (v2) from linearmosaic.xml ##############
##################### d7d8ecd70c999ac89b3abe88fb91689c ##############################
from __future__ import absolute_import 
from .__casac__ import linearmosaic as _linearmosaic

from .platform import str_encode as _str_ec
from .platform import str_decode as _str_dc
from .platform import dict_encode as _dict_ec
from .platform import dict_decode as _dict_dc
from .platform import dict_encode as _quant_ec
from .platform import dict_decode as _quant_dc
from .platform import encode as _any_ec
from .platform import decode as _any_dc
from .errors import create_error_string
from .typecheck import CasaValidator as _validator
_pc = _validator( )
from .coercetype import coerce as _coerce


class linearmosaic:
    _info_group_ = """linearmosaic"""
    _info_desc_ = """combining images in a weighted fashion"""
    ### self
    def __init__(self, *args, **kwargs):
        """Create a {tt linearmosaic} tool.
        """
        self._swigobj = kwargs.get('swig_object',None)
        if self._swigobj is None:
            self._swigobj = _linearmosaic()

    def defineoutputimage(self, nx=int(128), ny=int(-1), cellx=[ ], celly=[ ], imagecenter=[ ], outputimage='', outputweight=''):
        """Define the direction axes output image parameters.
        The output image will get the same number of spectral and polarization planes as the input images. This function create a fresh new output image. If an image of the same name exist on disk it will be erased. The spectral and polarization part of the image will be identical to the images that are being mosaiced.
        
        The output image will by default be flux correct and the weight image will be ${sum_p A_p^2(theta)}$ where the primary beam is $  A_p(theta)$
        """
        return self._swigobj.defineoutputimage(nx, ny, _any_ec(cellx), _any_ec(celly), _any_ec(imagecenter), _str_ec(outputimage), _str_ec(outputweight))

    def setoutputimage(self, outputimage='', outputweight='', imageweighttype=int(1), weighttype=int(1)):
        """Use this function if the mosaicing is to be done onto a previous mosaic or image. For now the stokes and spectral characteristic of the images to be mosaic and the output image has to be similar (i.e the user has to regrid them prior to linearmosaic if necessary).
        The weightimage represents the sensitivity image of the image (for example the weighted primary beam coverage of a mosaic)
        
        {tt imageweighttype} parameter:
        
        If the image is of the type that has been normalized to be flux correct then the imageweighttype should 0.
        If the image has been  apodized by a primary beam then imageweighttype should be 1
        and if the image is multiplied by $PB^2$ then it should be 2.
        
        {tt weighttype} parameter:
        This should be 1 if the weight image is the sum of Primary beams or equivalent
        and it should be 2 if it is the sum of of $PB^2$
        """
        return self._swigobj.setoutputimage(_str_ec(outputimage), _str_ec(outputweight), imageweighttype, weighttype)

    def saultweightimage(self, outputimage='', fracpeak=float(0.1)):
        """"Sault weighted" image is one which is more pleasant to view (without high noise at the edges of mosaic images), it is flux correct upto a where the beam coverage becomes low and is tapered off onwards just to keep the noise from rising in the overall image(see  Eq[2] from Sault, Staveley-Smith and Brouw (1996), Astron. Astrophys. Suppl, 120, 375)
        """
        return self._swigobj.saultweightimage(_str_ec(outputimage), fracpeak)

    def setlinmostype(self, linmostype='optimal'):
        """Use this function if the mosaicing is to be done using a non optimal weighting mode.
        
        
        For now {tt optimal} (which is the default) follows this equation
        begin{equation}
        I^{lm}(theta)={{sum_p A_p(theta)(I_p(theta)A_p(theta))w_p}over{sum_p A_p^2(theta)w_p}}
        end{equation}
        
        And {tt pbweight} follows this one
        begin{equation}
        I^{lm}(theta)={{sum_p (I_p(theta)A_p(theta))w_p}over{sum_p A_p(theta)w_p}}
        end{equation}
        
        where $A_p(theta)$ is the primary beam (PB) of a given pointing $p$, $w_p$ is a sensitivity weight and the image of that pointing is $I_p(theta)$; the linear mosaic being $I^{lm}(theta)$
        For now  $w_p=1$
        """
        return self._swigobj.setlinmostype(_str_ec(linmostype))

    def makemosaic(self, images=[ ], weightimages=[ ], imageweighttype=int(1), weighttype=int(1)):
        """Put the list of images onto the mosaic image using the weight images
        """
        return self._swigobj.makemosaic(_any_ec(images), _any_ec(weightimages), imageweighttype, weighttype)

