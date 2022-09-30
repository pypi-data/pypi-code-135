##################### generated by xml-casa (v2) from imcollapse.xml ################
##################### b131fe08644211a85ce28c27c66e74c8 ##############################
from __future__ import absolute_import
from casashell.private.stack_manip import find_local as __sf__
from casashell.private.stack_manip import find_frame as _find_frame
from casatools.typecheck import validator as _pc
from casatools.coercetype import coerce as _coerce
from casatasks import imcollapse as _imcollapse_t
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

class _imcollapse:
    """
    imcollapse ---- Collapse image along one axis, aggregating pixel values along that axis.

    
    This task collapses an image along a specified axis or set of axes of
    N pixels to a single pixel on each specified axis. Both float valued
    and complex valued images are supported. It computes the specified
    aggregate function for pixel values along the specified axes and
    places those values in the single remaining plane of those axes in the
    output image.
    
    The reference pixel of the collapsed axis is set to 0 and its
    reference value is set to the mean of the the first and last values of
    that axis in the specified region of the input image. Convolution to a
    common beam is not performed automatically as part of the
    preprocessing before the collapse operation occurs. Therefore, if the
    input image has per-plane beams, then the user should consider first
    smoothing the data to have the same resolution, and use the resulting
    image as the input for imcollapse.

    --------- parameter descriptions ---------------------------------------------

    imagename Name of the input image
              Default: none
              
                 Example: imagename='ngc5921.im'
    function  Function used to compute aggregation of pixel values
              along the collapsed axis.
              Default: none
              Options: flux, madm, max, mean, median, min,
              npts, rms, stddev, sum, variance, xmadm
              
              Minimum match is supported for the function
              parameter (eg, function="r" will compute the rms
              of the pixel values).
              
              If one specifies function='flux', the following
              constraints must be true:
              1. The image must have a direction coordinate,
              2. The image must have at least one beam,
              3. The specified axes must be exactly the
              direction coordinate axes,
              4. Only one of the non-directional axes may be
              non-degenerate,
              5. The iamge brightness unit must be conformant
              with x*yJy/beam, where x is an optional unit
              (such as km/s for moments images) and y is an
              optional SI prefix.
    axes      Zero-based axis number(s) or minimal match strings to
              collapse.
              Default: [0]
              Axes can be specified as a single integer or
              array of integers indicating the zero-based axes
              along which to collapse the image. Axes may also
              be specified as a single or array of strings
              which minimally and uniquely match (ignoring
              case) world axes names in the image (eg "dec" or
              ["ri, "d"] for collapsing along the declination
              axis or along the right ascension and declination
              axes, respectively).
    outfile   Name of output CASA image. Must be specified.
              Default: none
              
                 Example: outfile='collapsed.im'
    box       Rectangular region to select in direction plane. 
              Default: '' (use the entire direction plane)
              
                 Example: box="100,100,200,200"
    region    Region selection.
              Default: '' (use the full image)
    chans     Channels to use. 
              Default: '' (use all channels)
    stokes    Stokes planes to use.
              Default: '' (use all stokes planes)
    mask      Mask to use.
              Default: none
    overwrite Overwrite output image if it exists?
              Default: False
              Options: False|True
    stretch   Stretch the mask if necessary and possible? 
              Default: False
              Options: False|True
              
              Stretch the input mask if necessary and
              possible. Only used if a mask is specified.
    [1;42mRETURNS[1;m      bool

    --------- examples -----------------------------------------------------------

    
    FOR MORE INFORMATION, SEE THE TASK PAGES OF IMCOLLAPSE IN CASA DOCS:
    https://casa.nrao.edu/casadocs/


    """

    _info_group_ = """analysis"""
    _info_desc_ = """Collapse image along one axis, aggregating pixel values along that axis."""

    __schema = {'imagename': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'function': {'type': 'cStr', 'coerce': _coerce.to_str}, 'axes': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'outfile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'box': {'type': 'cStr', 'coerce': _coerce.to_str}, 'region': {'type': 'cStr', 'coerce': _coerce.to_str}, 'chans': {'type': 'cStr', 'coerce': _coerce.to_str}, 'stokes': {'type': 'cStr', 'coerce': _coerce.to_str}, 'mask': {'type': 'cStr', 'coerce': _coerce.to_str}, 'overwrite': {'type': 'cBool'}, 'stretch': {'type': 'cBool'}}

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

    def __outfile_dflt( self, glb ):
        return ''

    def __outfile( self, glb ):
        if 'outfile' in glb: return glb['outfile']
        return ''

    def __mask_dflt( self, glb ):
        return ''

    def __mask( self, glb ):
        if 'mask' in glb: return glb['mask']
        return ''

    def __axes_dflt( self, glb ):
        return [ ]

    def __axes( self, glb ):
        if 'axes' in glb: return glb['axes']
        return [ ]

    def __stokes_dflt( self, glb ):
        return ''

    def __stokes( self, glb ):
        if 'stokes' in glb: return glb['stokes']
        return ''

    def __region_dflt( self, glb ):
        return ''

    def __region( self, glb ):
        if 'region' in glb: return glb['region']
        return ''

    def __chans_dflt( self, glb ):
        return ''

    def __chans( self, glb ):
        if 'chans' in glb: return glb['chans']
        return ''

    def __imagename_dflt( self, glb ):
        return ''

    def __imagename( self, glb ):
        if 'imagename' in glb: return glb['imagename']
        return ''

    def __function_dflt( self, glb ):
        return ''

    def __function( self, glb ):
        if 'function' in glb: return glb['function']
        return ''

    def __box_dflt( self, glb ):
        return ''

    def __box( self, glb ):
        if 'box' in glb: return glb['box']
        return ''

    #--------- return non subparam/when values ---------------------------------------------
    def __stretch( self, glb ):
        if 'stretch' in glb: return glb['stretch']
        return False

    #--------- return inp/go default --------------------------------------------------
    def __stretch_dflt( self, glb ):
        if self.__mask( glb ) != "": return bool(False)
        return None
    def __overwrite_dflt( self, glb ):
        if self.__outfile( glb ) != "": return bool(False)
        return None

    #--------- return subparam values -------------------------------------------------
    def __overwrite( self, glb ):
        if 'overwrite' in glb: return glb['overwrite']
        dflt = self.__overwrite_dflt( glb )
        if dflt is not None: return dflt
        return False

    #--------- subparam inp output ----------------------------------------------------
    def __imagename_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__imagename_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Name of the input image'
        value = self.__imagename( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'imagename': value},{'imagename': self.__schema['imagename']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-12.12s = %s%-23s%s' % ('imagename',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __function_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__function_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Aggregate function to apply. This can be set one of flux, madm, max, mean, median, min, npts, rms, stddev, sum, variance, xmadm. Must be specified.'
        value = self.__function( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'function': value},{'function': self.__schema['function']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-12.12s = %s%-23s%s' % ('function',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __axes_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__axes_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return [ ]
        description = 'Zero-based axis number(s) or minimal match strings to collapse.'
        value = self.__axes( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'axes': value},{'axes': self.__schema['axes']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-12.12s = %s%-23s%s' % ('axes',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __outfile_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__outfile_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Name of output CASA image. Must be specified.'
        value = self.__outfile( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'outfile': value},{'outfile': self.__schema['outfile']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('\x1B[1m\x1B[47m%-12.12s =\x1B[0m %s%-23s%s' % ('outfile',pre,self.__to_string_(value),post),description,13+len(pre)+len(post))
    def __box_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__box_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Rectangular region to select in direction plane. Default is to use the entire direction plane.'
        value = self.__box( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'box': value},{'box': self.__schema['box']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-12.12s = %s%-23s%s' % ('box',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __region_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__region_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Region selection. Default is to use the full image.'
        value = self.__region( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'region': value},{'region': self.__schema['region']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-12.12s = %s%-23s%s' % ('region',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __chans_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__chans_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Channels to use. Default is to use all channels.'
        value = self.__chans( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'chans': value},{'chans': self.__schema['chans']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-12.12s = %s%-23s%s' % ('chans',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __stokes_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__stokes_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Stokes planes to use. Default is to use all Stokes planes.'
        value = self.__stokes( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'stokes': value},{'stokes': self.__schema['stokes']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-12.12s = %s%-23s%s' % ('stokes',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __mask_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__mask_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Mask to use. Default is none.'
        value = self.__mask( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'mask': value},{'mask': self.__schema['mask']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('\x1B[1m\x1B[47m%-12.12s =\x1B[0m %s%-23s%s' % ('mask',pre,self.__to_string_(value),post),description,13+len(pre)+len(post))
    def __overwrite_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__overwrite_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return False
        if self.__overwrite_dflt( self.__globals_( ) ) is not None:
             description = 'Overwrite output image if it exists?'
             value = self.__overwrite( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'overwrite': value},{'overwrite': self.__schema['overwrite']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-9.9s =\x1B[0m %s%-23s%s' % ('overwrite',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __stretch_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__stretch_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return False
        description = 'Stretch the mask if necessary and possible?'
        value = self.__stretch( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'stretch': value},{'stretch': self.__schema['stretch']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-12.12s = %s%-23s%s' % ('stretch',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))

    #--------- global default implementation-------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def set_global_defaults(self):
        self.set_global_defaults.state['last'] = self
        glb = self.__globals_( )
        if 'stokes' in glb: del glb['stokes']
        if 'outfile' in glb: del glb['outfile']
        if 'mask' in glb: del glb['mask']
        if 'stretch' in glb: del glb['stretch']
        if 'imagename' in glb: del glb['imagename']
        if 'axes' in glb: del glb['axes']
        if 'function' in glb: del glb['function']
        if 'chans' in glb: del glb['chans']
        if 'region' in glb: del glb['region']
        if 'box' in glb: del glb['box']
        if 'overwrite' in glb: del glb['overwrite']


    #--------- inp function -----------------------------------------------------------
    def inp(self):
        print("# imcollapse -- %s" % self._info_desc_)
        self.term_width, self.term_height = shutil.get_terminal_size(fallback=(80, 24))
        self.__imagename_inp( )
        self.__function_inp( )
        self.__axes_inp( )
        self.__outfile_inp( )
        self.__box_inp( )
        self.__region_inp( )
        self.__chans_inp( )
        self.__stokes_inp( )
        self.__mask_inp( )
        self.__overwrite_inp( )
        self.__stretch_inp( )

    #--------- tget function ----------------------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def tget(self,savefile=None):
        from casashell.private.stack_manip import find_frame
        from runpy import run_path
        filename = savefile
        if filename is None:
            filename = "imcollapse.last" if os.path.isfile("imcollapse.last") else "imcollapse.saved"
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

        _postfile = outfile if outfile is not None else os.path.realpath('imcollapse.last')

        _invocation_parameters = OrderedDict( )
        _invocation_parameters['imagename'] = self.__imagename( self.__globals_( ) )
        _invocation_parameters['function'] = self.__function( self.__globals_( ) )
        _invocation_parameters['axes'] = self.__axes( self.__globals_( ) )
        _invocation_parameters['outfile'] = self.__outfile( self.__globals_( ) )
        _invocation_parameters['box'] = self.__box( self.__globals_( ) )
        _invocation_parameters['region'] = self.__region( self.__globals_( ) )
        _invocation_parameters['chans'] = self.__chans( self.__globals_( ) )
        _invocation_parameters['stokes'] = self.__stokes( self.__globals_( ) )
        _invocation_parameters['mask'] = self.__mask( self.__globals_( ) )
        _invocation_parameters['overwrite'] = self.__overwrite( self.__globals_( ) )
        _invocation_parameters['stretch'] = self.__stretch( self.__globals_( ) )

        try:
            with open(_postfile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-9s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#imcollapse( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: return False
        return True

    def __call__( self, imagename=None, function=None, axes=None, outfile=None, box=None, region=None, chans=None, stokes=None, mask=None, overwrite=None, stretch=None ):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s
        _prefile = os.path.realpath('imcollapse.pre')
        _postfile = os.path.realpath('imcollapse.last')
        _return_result_ = None
        _arguments = [imagename,function,axes,outfile,box,region,chans,stokes,mask,overwrite,stretch]
        _invocation_parameters = OrderedDict( )
        if any(map(lambda x: x is not None,_arguments)):
            # invoke python style
            # set the non sub-parameters that are not None
            local_global = { }
            if imagename is not None: local_global['imagename'] = imagename
            if function is not None: local_global['function'] = function
            if axes is not None: local_global['axes'] = axes
            if outfile is not None: local_global['outfile'] = outfile
            if box is not None: local_global['box'] = box
            if region is not None: local_global['region'] = region
            if chans is not None: local_global['chans'] = chans
            if stokes is not None: local_global['stokes'] = stokes
            if mask is not None: local_global['mask'] = mask
            if stretch is not None: local_global['stretch'] = stretch

            # the invocation parameters for the non-subparameters can now be set - this picks up those defaults
            _invocation_parameters['imagename'] = self.__imagename( local_global )
            _invocation_parameters['function'] = self.__function( local_global )
            _invocation_parameters['axes'] = self.__axes( local_global )
            _invocation_parameters['outfile'] = self.__outfile( local_global )
            _invocation_parameters['box'] = self.__box( local_global )
            _invocation_parameters['region'] = self.__region( local_global )
            _invocation_parameters['chans'] = self.__chans( local_global )
            _invocation_parameters['stokes'] = self.__stokes( local_global )
            _invocation_parameters['mask'] = self.__mask( local_global )
            _invocation_parameters['stretch'] = self.__stretch( local_global )

            # the sub-parameters can then be set. Use the supplied value if not None, else the function, which gets the appropriate default
            _invocation_parameters['overwrite'] = self.__overwrite( _invocation_parameters ) if overwrite is None else overwrite

        else:
            # invoke with inp/go semantics
            _invocation_parameters['imagename'] = self.__imagename( self.__globals_( ) )
            _invocation_parameters['function'] = self.__function( self.__globals_( ) )
            _invocation_parameters['axes'] = self.__axes( self.__globals_( ) )
            _invocation_parameters['outfile'] = self.__outfile( self.__globals_( ) )
            _invocation_parameters['box'] = self.__box( self.__globals_( ) )
            _invocation_parameters['region'] = self.__region( self.__globals_( ) )
            _invocation_parameters['chans'] = self.__chans( self.__globals_( ) )
            _invocation_parameters['stokes'] = self.__stokes( self.__globals_( ) )
            _invocation_parameters['mask'] = self.__mask( self.__globals_( ) )
            _invocation_parameters['overwrite'] = self.__overwrite( self.__globals_( ) )
            _invocation_parameters['stretch'] = self.__stretch( self.__globals_( ) )
        try:
            with open(_prefile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-9s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#imcollapse( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: pass
        try:
            _return_result_ = _imcollapse_t( _invocation_parameters['imagename'],_invocation_parameters['function'],_invocation_parameters['axes'],_invocation_parameters['outfile'],_invocation_parameters['box'],_invocation_parameters['region'],_invocation_parameters['chans'],_invocation_parameters['stokes'],_invocation_parameters['mask'],_invocation_parameters['overwrite'],_invocation_parameters['stretch'] )
        except Exception as e:
            from traceback import format_exc
            from casatasks import casalog
            casalog.origin('imcollapse')
            casalog.post("Exception Reported: Error in imcollapse: %s" % str(e),'SEVERE')
            casalog.post(format_exc( ))
            _return_result_ = False
        try:
            os.rename(_prefile,_postfile)
        except: pass
        return _return_result_

imcollapse = _imcollapse( )

