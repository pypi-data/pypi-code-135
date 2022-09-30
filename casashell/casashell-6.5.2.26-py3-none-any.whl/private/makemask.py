##################### generated by xml-casa (v2) from makemask.xml ##################
##################### 8eacce9c9cbe61ce734b2e6da8ec5f9c ##############################
from __future__ import absolute_import
from casashell.private.stack_manip import find_local as __sf__
from casashell.private.stack_manip import find_frame as _find_frame
from casatools.typecheck import validator as _pc
from casatools.coercetype import coerce as _coerce
from casatasks import makemask as _makemask_t
from collections import OrderedDict
import numpy
import sys
import os

import shutil

def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate

class _makemask:
    """
    makemask ---- Makes and manipulates image masks

    Construct masks based on various criteria, convert between mask-types, and generate a mask for clean

    --------- parameter descriptions ---------------------------------------------

    mode      Mask method (list, copy,expand,delete,setdefaultmask)
    inpimage  Name of input image.
    inpmask   mask(s) to be processed: image masks,T/F internal masks(Need to include parent image names),regions(for copy mode)
    output    Name of output mask (imagename or imagename:internal_maskname)
    overwrite overwrite output if exists?
    inpfreqs  List of chans/freqs (in inpmask) to read masks from
    outfreqs  List of chans/freqs (in output) on which to expand the mask
    [1;42mRETURNS[1;m      void

    --------- examples -----------------------------------------------------------

    
    
    Modes :
    -------------
    
    list : list internal masks in inpimage to the log
    copy :  Copy/merge masks and regrid if necessary to a new or existing mask
    expand : Expand a mask from one range of freqs to another range
    delete : delete an internal mask from an image (if the deleted mask was a default mask,
    the task chooses the first one in the remaining internal mask list (as appears
    in the log when do listing with mode='list')
    setdefaultmask : set a specified internal mask as a default internal mask
    
    
    
    
    In all cases (for output mask is expected), if the output image has a different coordinate system from the
    result of input and processing, the mask will be re-gridded to the output
    coordinate system.
    
    
    Parameter Descriptions and rules:
    ------------------------------
    inpimage : Name of input image to use as a reference for the output coordinates (if output does not exist).
    Also used as a reference image when regions are specified in inpmask for copy mode
    If output is a new image specified with an internal T/F mask, the pixel values in the input image
    are copied to the output image and the regions specified in inpmask are merged (if mutliple regions
    specified) and treated as a valid region therefore will be UNMASKED in output.
    default: none (must specify for list, copy, expand modes)
    
    Expandable parameters for mode='copy','expand','delete' and 'setdefaultmask':
    inpmask : Name(s) of input mask(s)
    default: none
    To specify an image (zero/non-zero) mask, just give a image name (e.g. myimage1.im)
    To specify an internal (T/F) mask, you must give a parent image name and the internal mask name
    separated by a colon. (e.g. myimage1.im:mask0). The internal mask names can be found by running
    the makemask task in mode='list'.
    
    (expand mode)
    'myimage:mask0' : use(true/false) internal mask
    'myimage'  : use the inpimage values to make a mask (zero/non-zero).
    Non-zero values are normalized to one in the process.
    (copy mode)
    Specify the image mask(s), T/F mask(s), and region(s) to be merged in a list of strings.
    The regions can be specified directly in the CASA region format or in the text file(s) contains
    the regions.
    
    (delete and setdefaultmask mode)
    Specify the internal mask with the format, image:mask
    
    
    output : Name of output image.
    default: none
    *The resultant mask is written as an image (zero/one) mask if the output is a plain image name
    *The resultant mask is written as an internal (T/F) mask if the output name is the form of 'imagename:maskname'
    The created mask is set as a default internal mask.
    *To re-grid a mask to a different coordinate system,
    give an image with the target coordinate system in inpimage. Or make a copy an image
    with the target coordinate system and specified the name of the copy in output.
    
    
    - If output is specified as a plain image, if it exists, it will regrid the mask to
    the new coordinate system  and modify output (if overwrite=True).
    - If output is specified as an image with an internal mask, if the internal mask exists,
    it will regrid the mask to the new coordinate system  and modify the internal mask only (if overwrite=True).
    - If output does not exist, it will only copy inpimage.
    - If output == inpimage, do not regrid. Only modify in-place.
    
    *** Please note that the term 'mask' is used in the image analysis and clean tasks in opposite
    sense. In the image analysis, the masked region in general a region to be excluded while
    clean's input mask defines the region to be used as a clean box/region.
    In the makemask task, since the most common use case of output image mask is to use as
    an input mask in clean, when it converts an internal mask to the image mask,
    the 'masked' region (where the pixels are masked and have the Boolean values 'False')
    of the internal mask is translated to the pixels with value of 0 in output image mask.
    
    overwrite : overwrite the mask specified in output? (see also the output rules above)
    default: False
    * Note that for a cube mask, overwrite=True generally overwrites in the specified channel planes only and
    so any pre-existed masks in other channels  will be remain untouched.
    
    Additional expandable parameters for mode='expand':
    inpfreqs : input channel/frequency/velocity range
    Specify channels in a list of integers. for frequency/velocity,
    a range is specified in a string with '~', e.g. '1.5MHz~1.6MHz', '-8km/s~-14km/s'
    (for the cube with ascending frequencies)
    default: []  - all channels
    * Note that the range in frequency or velocity needs to be specified as the same order
    as in the template cube specified in inpimage. E.g., if a template cube has descending
    frequencies, then the range will be, for example,'1.6MHz~1.5MHz' or '-14km/s~-8km/s'
    
    outfreqs : output channel/frequency/velocity range
    Specify same way as inpfreqs
    default: []  - all channels
    
    
    Usage examples :
    ---------------------------
    (1) (list mode):
    makemask(mode='list', inpimage='mymask.im')
    it prints out a list of the internal mask(s) exist in mymask.im to the log
    
    (2) (copy mode):
    Regrid a Boolean mask from one coordinate system to another and save as Boolean mask
    in the output image.
    
    makemask(mode='copy', inpimage='oldmask.im', inpmask='oldmask.im:mask0', output='newmask.im:mask0')
    
    (3) (copy mode):
    Same as (1), but save as integer mask in the output image.
    
    makemask(mode='copy', inpimage='oldmask.im', inpmask='oldmask.im:mask0', output='newmask.im')
    
    * mask0 is translated so that pixels in oldmask.im that appears as 'masked' in the viewer or
    has the pixel mask value = 'False' when extracted in imval, are to have pixel value of 1 in
    the output image, newmask.im.
    
    (4) (copy mode):
    Convert a Boolean(true/false) mask to an integer(one/zero) mask in the same image
    
    makemask(mode='copy', inpimage='oldmask.im', inpmask='oldmask.im:mask0', output='', overwrite=True)
    
    
    (5) (copy mode):
    Convert an integer(one/zero) mask to a Boolean(true/false) mask in the same image
    
    makemask(mode='copy', inpimage='oldmask.im', inpmask='oldmask.im', output='oldmask.im:mask0')
    
    (6) (copy mode):
    Copy a CRTF mask defined in mybox.txt to a Boolean(true/false) mask in a new image
    
    makemask(mode='copy', inpimage='image1.im', inpmask='mybox.txt', output='image2.im:mask0')
    
    The pixel values of image1.im will be copied to image2.im and the region outside mybox.txt
    will be masked.
    
    (7) (copy mode):
    Apply a region defined in a CRTF file to mask part of an image
    
    makemask(mode='copy', inpimage='image1.im', inpmask='myregion.crtf', output='image1.im:mask0')
    
    The region is copied as a T/F mask (mask0) inside the image, image1.im. The region outside myregion.crtf
    will be masked.
    
    
    (8) (copy mode):
    
    Merge a (one/zero) mask and  T/F masks, using the input coordinate-sys of inpimage and
    saving in a new output file. Remember, if the image specified in output already exist and
    has a different coordinate system from inpimage, the mask will be regridded to it.
    All masks to be merged are specified in a list in inpmask.
    The name of internal masks must be given in the format, 'parent_image_name:internal_mask_name',
    as shown the example below.
    
    In the example below, image1.im (the 1/0 mask), the internal masks, mask0 from image1.im
    and mask1 from image2.im, and a region (on image1.im as defined in inpimage)  are combined.
    The output, newmask.im is a new mask name which has not
    yet exist so image specified in inpimage, image1.im's coordinates are used as a target
    image coordinates. If image1.im and image2.im has different coordinates, image2.im:mask1 is
    regridded before it is combined to the other two masks.
    
    makemask(mode='copy',
    inpimage='image1.im',
    inpmask=['image1.im', image1.im:mask0','image2.mask:mask1', 'circle[[15pix , 15pix] ,8pix ]'],
    output='newmask.im);
    
    (9) (expand mode):
    Expand a (one/zero) mask from continuum imaging to use as an input mask image for
    spectral line imaging. Use an existing spectral line clean image as a template by
    specified in inpimage.
    The inpfreqs is left out as it uses a default (=[], means all channels).
    
    makemask(mode='expand', inpimage='spec.clean.image', inpmask='cont.clean.mask'
    outfreqs=[4,5,6,7], output='spec.clean.mask')
    
    (10) (expand mode):
    Expand a Boolean mask from one range of channels to another range
    in the same image.
    
    makemask(mode='expand', inpimage='oldmask.im', inpmask='oldmask.im:mask0', inpfreqs=[5,6], outfreqs=[4,5,6,7],
    output='oldmask.im:mask0', overwrite=True)
    
    
    (11) (expand mode):
    Expand a Boolean mask from a range of channels in the input image to another range
    of channels in a different image with a different spectral-coordinate system.
    Save the mask as ones/zeros so that it can be used as an input mask in the clean task.
    As the inpimage is used as a template for the CoordinateSystem of the output cube, it is
    a prerequisite to have the cube image (a dirty image, etc). In this particular example,
    it is assumed that bigmask.im is a working copy made from the cube image of a previous clean
    execution. It is used as an input template and the resultant mask is overwritten to the same image.
    
    Specify the infreqs and outfreqs in frequency (assuming here bigmask.im has frequencies in ascending order)
    makemask(mode='expand', inpimage='bigmask.im', inpmask='smallmask.im:mask0',
    inpfreqs='1.5MHz~1.6MHz', outfreqs='1.2MHz~1.8MHz', output='bigmask.im', overwrite=True)
    
    or to specify the ranges in velocities,
    makemask(mode='expand', inpimage='bigmask.im', inpmask='smallmask.im:mask0',
    inpfreqs=4.0km/s~0.5km/s', outfreqs='6.5km/s~-2.4km/s', output='bigmask.im', overwrite=True)
    
    
    (12) (delete mode)
    Delete an internal mask from an image.
    
    makemask(mode='delete', inpmask='newmask.im:mask0')
    
    (13) (setdefaultmask mode)
    Set an internal mask as a default internal mask.
    
    makemask(mode='setdefaultmask', inpmask='newmask.im:mask1')
    
    
    
    
    
    


    """

    _info_group_ = """imaging"""
    _info_desc_ = """Makes and manipulates image masks"""

    __schema = {'mode': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'delete', 'copy', 'expand', 'list', 'setdefaultmask' ]}, 'inpimage': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}]}, 'inpmask': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}]}, 'output': {'type': 'cStr', 'coerce': _coerce.to_str}, 'overwrite': {'type': 'cBool'}, 'inpfreqs': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}]}, 'outfreqs': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}]}}

    def __init__(self):
        self.__stdout = None
        self.__stderr = None
        self.__root_frame_ = None

    def __globals_(self):
        if self.__root_frame_ is None:
            self.__root_frame_ = _find_frame( )
            assert self.__root_frame_ is not None, "could not find CASAshell global frame"
        return self.__root_frame_

    def __to_string_(self,value):
        if type(value) is str:
            return "'%s'" % value
        else:
            return str(value)

    def __validate_(self,doc,schema):
        return _pc.validate(doc,schema)

    def __do_inp_output(self,param_prefix,description_str,formatting_chars):
        out = self.__stdout or sys.stdout
        description = description_str.split( )
        prefix_width = 23 + 12 + 4
        output = [ ]
        addon = ''
        first_addon = True
        if len(description) == 0:
            out.write(param_prefix + " #\n")
            return
        while len(description) > 0:
            ## starting a new line.....................................................................
            if len(output) == 0:
                ## for first line add parameter information............................................
                if len(param_prefix)-formatting_chars > prefix_width - 1:
                    output.append(param_prefix)
                    continue
                addon = param_prefix + ' #'
                first_addon = True
                addon_formatting = formatting_chars
            else:
                ## for subsequent lines space over prefix width........................................
                addon = (' ' * prefix_width) + '#'
                first_addon = False
                addon_formatting = 0
            ## if first word of description puts us over the screen width, bail........................
            if len(addon + description[0]) - addon_formatting + 1 > self.term_width:
                ## if we're doing the first line make sure it's output.................................
                if first_addon: output.append(addon)
                break
            while len(description) > 0:
                ## if the next description word puts us over break for the next line...................
                if len(addon + description[0]) - addon_formatting + 1 > self.term_width: break
                addon = addon + ' ' + description[0]
                description.pop(0)
            output.append(addon)
        out.write('\n'.join(output) + '\n')

    #--------- return nonsubparam values ----------------------------------------------

    def __mode_dflt( self, glb ):
        return 'list'

    def __mode( self, glb ):
        if 'mode' in glb: return glb['mode']
        return 'list'



    #--------- return inp/go default --------------------------------------------------
    def __inpimage_dflt( self, glb ):
        if self.__mode( glb ) == "list": return ""
        if self.__mode( glb ) == "copy": return ""
        if self.__mode( glb ) == "expand": return ""
        return None
    def __inpfreqs_dflt( self, glb ):
        if self.__mode( glb ) == "expand": return []
        return None
    def __outfreqs_dflt( self, glb ):
        if self.__mode( glb ) == "expand": return []
        return None
    def __output_dflt( self, glb ):
        if self.__mode( glb ) == "copy": return ""
        if self.__mode( glb ) == "expand": return ""
        return None
    def __overwrite_dflt( self, glb ):
        if self.__mode( glb ) == "copy": return bool(False)
        if self.__mode( glb ) == "expand": return bool(False)
        return None
    def __inpmask_dflt( self, glb ):
        if self.__mode( glb ) == "copy": return ""
        if self.__mode( glb ) == "expand": return ""
        if self.__mode( glb ) == "delete": return ""
        if self.__mode( glb ) == "setdefaultmask": return ""
        return None

    #--------- return subparam values -------------------------------------------------
    def __inpimage( self, glb ):
        if 'inpimage' in glb: return glb['inpimage']
        dflt = self.__inpimage_dflt( glb )
        if dflt is not None: return dflt
        return ''
    def __inpmask( self, glb ):
        if 'inpmask' in glb: return glb['inpmask']
        dflt = self.__inpmask_dflt( glb )
        if dflt is not None: return dflt
        return ''
    def __output( self, glb ):
        if 'output' in glb: return glb['output']
        dflt = self.__output_dflt( glb )
        if dflt is not None: return dflt
        return ''
    def __overwrite( self, glb ):
        if 'overwrite' in glb: return glb['overwrite']
        dflt = self.__overwrite_dflt( glb )
        if dflt is not None: return dflt
        return False
    def __inpfreqs( self, glb ):
        if 'inpfreqs' in glb: return glb['inpfreqs']
        dflt = self.__inpfreqs_dflt( glb )
        if dflt is not None: return dflt
        return [  ]
    def __outfreqs( self, glb ):
        if 'outfreqs' in glb: return glb['outfreqs']
        dflt = self.__outfreqs_dflt( glb )
        if dflt is not None: return dflt
        return [  ]

    #--------- subparam inp output ----------------------------------------------------
    def __mode_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__mode_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return 'list'
        description = 'Mask method (list, copy,expand,delete,setdefaultmask)'
        value = self.__mode( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'mode': value},{'mode': self.__schema['mode']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('\x1B[1m\x1B[47m%-12.12s =\x1B[0m %s%-23s%s' % ('mode',pre,self.__to_string_(value),post),description,13+len(pre)+len(post))
    def __inpimage_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__inpimage_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        if self.__inpimage_dflt( self.__globals_( ) ) is not None:
             description = 'Name of input image.'
             value = self.__inpimage( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'inpimage': value},{'inpimage': self.__schema['inpimage']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-9.9s =\x1B[0m %s%-23s%s' % ('inpimage',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __inpmask_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__inpmask_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        if self.__inpmask_dflt( self.__globals_( ) ) is not None:
             description = 'mask(s) to be processed: image masks,T/F internal masks(Need to include parent image names),regions(for copy mode)'
             value = self.__inpmask( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'inpmask': value},{'inpmask': self.__schema['inpmask']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-9.9s =\x1B[0m %s%-23s%s' % ('inpmask',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __output_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__output_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        if self.__output_dflt( self.__globals_( ) ) is not None:
             description = 'Name of output mask (imagename or imagename:internal_maskname)'
             value = self.__output( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'output': value},{'output': self.__schema['output']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-9.9s =\x1B[0m %s%-23s%s' % ('output',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __overwrite_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__overwrite_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return False
        if self.__overwrite_dflt( self.__globals_( ) ) is not None:
             description = 'overwrite output if exists?'
             value = self.__overwrite( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'overwrite': value},{'overwrite': self.__schema['overwrite']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-9.9s =\x1B[0m %s%-23s%s' % ('overwrite',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __inpfreqs_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__inpfreqs_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return [  ]
        if self.__inpfreqs_dflt( self.__globals_( ) ) is not None:
             description = 'List of chans/freqs (in inpmask) to read masks from'
             value = self.__inpfreqs( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'inpfreqs': value},{'inpfreqs': self.__schema['inpfreqs']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-9.9s =\x1B[0m %s%-23s%s' % ('inpfreqs',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __outfreqs_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__outfreqs_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return [  ]
        if self.__outfreqs_dflt( self.__globals_( ) ) is not None:
             description = 'List of chans/freqs (in output) on which to expand the mask'
             value = self.__outfreqs( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'outfreqs': value},{'outfreqs': self.__schema['outfreqs']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-9.9s =\x1B[0m %s%-23s%s' % ('outfreqs',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))

    #--------- global default implementation-------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def set_global_defaults(self):
        self.set_global_defaults.state['last'] = self
        glb = self.__globals_( )
        if 'inpimage' in glb: del glb['inpimage']
        if 'inpfreqs' in glb: del glb['inpfreqs']
        if 'outfreqs' in glb: del glb['outfreqs']
        if 'mode' in glb: del glb['mode']
        if 'output' in glb: del glb['output']
        if 'overwrite' in glb: del glb['overwrite']
        if 'inpmask' in glb: del glb['inpmask']


    #--------- inp function -----------------------------------------------------------
    def inp(self):
        print("# makemask -- %s" % self._info_desc_)
        self.term_width, self.term_height = shutil.get_terminal_size(fallback=(80, 24))
        self.__mode_inp( )
        self.__inpimage_inp( )
        self.__inpmask_inp( )
        self.__output_inp( )
        self.__overwrite_inp( )
        self.__inpfreqs_inp( )
        self.__outfreqs_inp( )

    #--------- tget function ----------------------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def tget(self,savefile=None):
        from casashell.private.stack_manip import find_frame
        from runpy import run_path
        filename = savefile
        if filename is None:
            filename = "makemask.last" if os.path.isfile("makemask.last") else "makemask.saved"
        if os.path.isfile(filename):
            glob = find_frame( )
            newglob = run_path( filename, init_globals={ } )
            for i in newglob:
                glob[i] = newglob[i]
            self.tget.state['last'] = self
        else:
            print("could not find last file: %s\nsetting defaults instead..." % filename)
            self.set_global_defaults( )

    #--------- tput function ----------------------------------------------------------
    def tput(self,outfile=None):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s

        _postfile = outfile if outfile is not None else os.path.realpath('makemask.last')

        _invocation_parameters = OrderedDict( )
        _invocation_parameters['mode'] = self.__mode( self.__globals_( ) )
        _invocation_parameters['inpimage'] = self.__inpimage( self.__globals_( ) )
        _invocation_parameters['inpmask'] = self.__inpmask( self.__globals_( ) )
        _invocation_parameters['output'] = self.__output( self.__globals_( ) )
        _invocation_parameters['overwrite'] = self.__overwrite( self.__globals_( ) )
        _invocation_parameters['inpfreqs'] = self.__inpfreqs( self.__globals_( ) )
        _invocation_parameters['outfreqs'] = self.__outfreqs( self.__globals_( ) )

        try:
            with open(_postfile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-9s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#makemask( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: return False
        return True

    def __call__( self, mode=None, inpimage=None, inpmask=None, output=None, overwrite=None, inpfreqs=None, outfreqs=None ):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s
        _prefile = os.path.realpath('makemask.pre')
        _postfile = os.path.realpath('makemask.last')
        _return_result_ = None
        _arguments = [mode,inpimage,inpmask,output,overwrite,inpfreqs,outfreqs]
        _invocation_parameters = OrderedDict( )
        if any(map(lambda x: x is not None,_arguments)):
            # invoke python style
            # set the non sub-parameters that are not None
            local_global = { }
            if mode is not None: local_global['mode'] = mode

            # the invocation parameters for the non-subparameters can now be set - this picks up those defaults
            _invocation_parameters['mode'] = self.__mode( local_global )

            # the sub-parameters can then be set. Use the supplied value if not None, else the function, which gets the appropriate default
            _invocation_parameters['inpimage'] = self.__inpimage( _invocation_parameters ) if inpimage is None else inpimage
            _invocation_parameters['inpmask'] = self.__inpmask( _invocation_parameters ) if inpmask is None else inpmask
            _invocation_parameters['output'] = self.__output( _invocation_parameters ) if output is None else output
            _invocation_parameters['overwrite'] = self.__overwrite( _invocation_parameters ) if overwrite is None else overwrite
            _invocation_parameters['inpfreqs'] = self.__inpfreqs( _invocation_parameters ) if inpfreqs is None else inpfreqs
            _invocation_parameters['outfreqs'] = self.__outfreqs( _invocation_parameters ) if outfreqs is None else outfreqs

        else:
            # invoke with inp/go semantics
            _invocation_parameters['mode'] = self.__mode( self.__globals_( ) )
            _invocation_parameters['inpimage'] = self.__inpimage( self.__globals_( ) )
            _invocation_parameters['inpmask'] = self.__inpmask( self.__globals_( ) )
            _invocation_parameters['output'] = self.__output( self.__globals_( ) )
            _invocation_parameters['overwrite'] = self.__overwrite( self.__globals_( ) )
            _invocation_parameters['inpfreqs'] = self.__inpfreqs( self.__globals_( ) )
            _invocation_parameters['outfreqs'] = self.__outfreqs( self.__globals_( ) )
        try:
            with open(_prefile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-9s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#makemask( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: pass
        try:
            _return_result_ = _makemask_t( _invocation_parameters['mode'],_invocation_parameters['inpimage'],_invocation_parameters['inpmask'],_invocation_parameters['output'],_invocation_parameters['overwrite'],_invocation_parameters['inpfreqs'],_invocation_parameters['outfreqs'] )
        except Exception as e:
            from traceback import format_exc
            from casatasks import casalog
            casalog.origin('makemask')
            casalog.post("Exception Reported: Error in makemask: %s" % str(e),'SEVERE')
            casalog.post(format_exc( ))
            _return_result_ = False
        try:
            os.rename(_prefile,_postfile)
        except: pass
        return _return_result_

makemask = _makemask( )

