##################### generated by xml-casa (v2) from synthesisimager.xml ###########
##################### 7650622d99a3bacd5e07f2addadffb21 ##############################
from __future__ import absolute_import 
from .__casac__ import synthesisimager as _synthesisimager

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
from .synthesisimstore import synthesisimstore as _wrap_synthesisimstore

class synthesisimager:
    _info_group_ = """synthesisimager"""
    _info_desc_ = """tool for synthesis imaging"""
    ### self
    def __init__(self, *args, **kwargs):
        """This is used to construct {tt synthesisimager} tool.
        """
        self._swigobj = kwargs.get('swig_object',None)
        if self._swigobj is None:
            self._swigobj = _synthesisimager()

    def selectdata(self, selpars={ }):
        """
        """
        return self._swigobj.selectdata(_dict_ec(selpars))

    def tuneselectdata(self):
        """
        """
        return _dict_dc(self._swigobj.tuneselectdata())

    def defineimage(self, impars={ }, gridpars={ }):
        """
        """
        return self._swigobj.defineimage(_dict_ec(impars), _dict_ec(gridpars))

    def normalizerinfo(self, normpars={ }):
        """
        """
        return self._swigobj.normalizerinfo(_dict_ec(normpars))

    def setdata(self, msname='', spw='', freqbeg='', freqend='', freqframe='LSRK', field='', antenna='', timestr='', scan='', obs='', state='', uvdist='', taql='', usescratch=False, readonly=False, incrmodel=False):
        """Select data from one MS. Call this function in succession if there are
        multiple MSs.
        """
        return self._swigobj.setdata(_str_ec(msname), _str_ec(spw), _str_ec(freqbeg), _str_ec(freqend), _str_ec(freqframe), _str_ec(field), _str_ec(antenna), _str_ec(timestr), _str_ec(scan), _str_ec(obs), _str_ec(state), _str_ec(uvdist), _str_ec(taql), usescratch, readonly, incrmodel)

    def setimage(self, imagename='', nx=int(128), ny=int(-1), cellx=[ ], celly=[ ], stokes='I', phasecenter=[ ], nchan=int(-1), freqstart=[ ], freqstep=[ ], restfreq=[ ], facets=int(1), ftmachine='gridft', ntaylorterms=int(1), reffreq=[ ], projection='SIN', distance=[ ], freqframe='LSRK', tracksource=False, trackdir=[ ], overwrite=True, padding=float(1.0), useautocorr=False, usedoubleprec=True, wprojplanes=int(1), convfunc='SF', startmodel='', aterm=True, psterm=True, mterm=False, wbawp=True, cfcache='', usepointing=False, pointingoffsetsigdev=[ ], dopbcorr=True, conjbeams=False, computepastep=float(360.0), rotatepastep=float(5.0)):
        """Define the image coordinate systems and shapes.
        """
        return self._swigobj.setimage(_str_ec(imagename), nx, ny, _any_ec(cellx), _any_ec(celly), _str_ec(stokes), _any_ec(phasecenter), nchan, _any_ec(freqstart), _any_ec(freqstep), _any_ec(restfreq), facets, _str_ec(ftmachine), ntaylorterms, _any_ec(reffreq), _str_ec(projection), _any_ec(distance), _str_ec(freqframe), tracksource, _any_ec(trackdir), overwrite, padding, useautocorr, usedoubleprec, wprojplanes, _str_ec(convfunc), _str_ec(startmodel), aterm, psterm, mterm, wbawp, _str_ec(cfcache), usepointing, _any_ec(pointingoffsetsigdev), dopbcorr, conjbeams, computepastep, rotatepastep)

    def setweighting(self, type='natural', rmode='norm', noise=[ ], robust=float(0.0), fieldofview=[ ], npixels=int(0), multifield=False, usecubebriggs=False, uvtaper=[  ]):
        """
        """
        return self._swigobj.setweighting(_str_ec(type), _str_ec(rmode), _any_ec(noise), robust, _any_ec(fieldofview), npixels, multifield, usecubebriggs, _str_ec(uvtaper))

    def makepsf(self):
        """
        """
        return self._swigobj.makepsf()

    def apparentsens(self):
        """
        """
        return _dict_dc(self._swigobj.apparentsens())

    def predictmodel(self):
        """
        """
        return self._swigobj.predictmodel()

    def drygridding(self, cflist=[ '' ]):
        """
        """
        return self._swigobj.drygridding(_str_ec(cflist))

    def fillcfcache(self, cflist=[ '' ], ftmname='', cfcpath='', pstermon=False, atermon=True, conjbeams=False):
        """
        """
        return self._swigobj.fillcfcache(_str_ec(cflist), _str_ec(ftmname), _str_ec(cfcpath), pstermon, atermon, conjbeams)

    def reloadcfcache(self):
        """
        """
        return self._swigobj.reloadcfcache()

    def executemajorcycle(self, controls={ }):
        """
        """
        return self._swigobj.executemajorcycle(_dict_ec(controls))

    def makepb(self):
        """
        """
        return self._swigobj.makepb()

    def makesdimage(self):
        """
        """
        return self._swigobj.makesdimage()

    def makesdpsf(self):
        """
        """
        return self._swigobj.makesdpsf()

    def makeimage(self, type='observed', image='', compleximage='', model=int(0)):
        """This tool function actually does gridding (and Fourier inversion if
        needed) of visibility data to make an image. It allows calculation of
        various types of image:
        begin{description}
        item[observed] Make the dirty image from the DATA column ({em default})
        item[model] Make the dirty image from the MODEL_DATA column
        item[corrected] Make the dirty image from the CORRECTED_DATA column
        item[residual] Make the dirty image from the difference of the
        CORRECTED_DATA and MODEL_DATA columns
        item[psf] Make the point spread function
        item[singledish] Make a single dish image
        item[coverage] Make a single dish or mosaic coverage image
        item[holography] Make a complex holography image (experimental)
        
        end{description}
        """
        return self._swigobj.makeimage(_str_ec(type), _str_ec(image), _str_ec(compleximage), model)

    def unlockimages(self, imagefieldid=int(0)):
        """Try to unlock images if the need arise
        """
        return self._swigobj.unlockimages(imagefieldid)

    def estimatememory(self):
        """This function returns an estimate of the memory (RAM) to be used by sythesisimager tool. Need to be run after functions setdata and defineimage are done
        """
        return _any_dc(self._swigobj.estimatememory())

    def getimstore(self, id=int(0)):
        """
        """
        return _wrap_synthesisimstore(swig_object=self._swigobj.getimstore(id))

    def getImageName(self, facetId=int(0), imageId='IMAGE', taylorTerm=int(0)):
        """Get the image name for the given type of image (eg "PB"), the facet index, and the taylor term.
        
        """
        return _str_dc(self._swigobj.getImageName(facetId, _str_ec(imageId), taylorTerm))

    def getcsys(self):
        """
        """
        return _dict_dc(self._swigobj.getcsys())

    def updatenchan(self):
        """
        """
        return self._swigobj.updatenchan()

    def getweightdensity(self):
        """
        """
        return _str_dc(self._swigobj.getweightdensity())

    def setweightdensity(self, type=''):
        """Load the gridded weight density into image weighting; useful in parallel when weight density is combined into one image and loaded in each process. if no imagename is passed the imagename.weight is loaded
        
        """
        return self._swigobj.setweightdensity(_str_ec(type))

    def initmpi(self):
        """
        """
        return self._swigobj.initmpi()

    def releasempi(self):
        """
        """
        return self._swigobj.releasempi()

    def done(self):
        """
        """
        return self._swigobj.done()

