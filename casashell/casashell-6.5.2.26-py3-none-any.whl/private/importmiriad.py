##################### generated by xml-casa (v2) from importmiriad.xml ##############
##################### 816bce2ce9c34258335e566cc652c17b ##############################
from __future__ import absolute_import
from casashell.private.stack_manip import find_local as __sf__
from casashell.private.stack_manip import find_frame as _find_frame
from casatools.typecheck import validator as _pc
from casatools.coercetype import coerce as _coerce
from casatasks import importmiriad as _importmiriad_t
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

class _importmiriad:
    """
    importmiriad ---- Convert a Miriad visibility file into a CASA MeasurementSet

    
    Convert a Miriad visibility file into a CASA MeasurementSet with
    optional selection of spectral windows and weighting scheme
    

    --------- parameter descriptions ---------------------------------------------

    mirfile Name of input Miriad visibility file
            Default: none
            
               Example: mirfile='mydata.uv'
    vis     Name of output MeasurementSet
            Default: none
            
               Example: vis='mydata.ms'
    tsys    Use the Tsys to set the visibility weights
            Default: False
            Options: False|True
    spw     Select spectral window/channels
                      Default: '' (all spectral windows and channels)
            
                         Examples:
                         spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                         spw='<2';  spectral windows less than 2 (i.e. 0,1)
                         spw='0:5~61'; spw 0, channels 5 to 61
                         spw='0,10,3:3~45'; spw 0,10 all channels, spw
                         3 - chans 3 to 45.
                         spw='0~2:2~6'; spw 0,1,2 with channels 2
                         through 6 in each.
                         spw = '\*:3~64'  channels 3 through 64 for all sp id's
                         spw = ' :3~64' will NOT work.
    vel     Select velocity reference
            Default: telescope dependent, ATCA -> TOPO, CARMA
            -> LSRK
            Options: TOPO|LSRK|LSRD
            
               Example: vel='LSRK'
    linecal (CARMA) Apply line calibration
                                Default: False
                                Options: False|True
            
                                Only useful for CARMA data
    wide    (CARMA) Select wide window averages
            
            Select which of the wide-band channels should be loaded 
            Only useful for CARMA data
    debug   Display increasingly verbose debug messages
            Default: 0
            
               Example: debug=1
    [1;42mRETURNS[1;m    void

    --------- examples -----------------------------------------------------------

    
    FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTMIRIAD IN CASA DOCS:
    https://casa.nrao.edu/casadocs/
    


    """

    _info_group_ = """import/export"""
    _info_desc_ = """Convert a Miriad visibility file into a CASA MeasurementSet"""

    __schema = {'mirfile': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'vis': {'type': 'cStr', 'coerce': _coerce.to_str}, 'tsys': {'type': 'cBool'}, 'spw': {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}, 'vel': {'type': 'cStr', 'coerce': _coerce.to_str}, 'linecal': {'type': 'cBool'}, 'wide': {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}, 'debug': {'type': 'cInt'}}

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
        prefix_width = 23 + 7 + 4
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

    def __vis_dflt( self, glb ):
        return ''

    def __vis( self, glb ):
        if 'vis' in glb: return glb['vis']
        return ''

    def __vel_dflt( self, glb ):
        return ''

    def __vel( self, glb ):
        if 'vel' in glb: return glb['vel']
        return ''

    def __mirfile_dflt( self, glb ):
        return ''

    def __mirfile( self, glb ):
        if 'mirfile' in glb: return glb['mirfile']
        return ''

    def __debug_dflt( self, glb ):
        return int(0)

    def __debug( self, glb ):
        if 'debug' in glb: return glb['debug']
        return int(0)

    def __spw_dflt( self, glb ):
        return [ int(-1) ]

    def __spw( self, glb ):
        if 'spw' in glb: return glb['spw']
        return [ int(-1) ]

    def __wide_dflt( self, glb ):
        return [  ]

    def __wide( self, glb ):
        if 'wide' in glb: return glb['wide']
        return [  ]

    def __linecal_dflt( self, glb ):
        return False

    def __linecal( self, glb ):
        if 'linecal' in glb: return glb['linecal']
        return False

    def __tsys_dflt( self, glb ):
        return False

    def __tsys( self, glb ):
        if 'tsys' in glb: return glb['tsys']
        return False



    #--------- return inp/go default --------------------------------------------------


    #--------- return subparam values -------------------------------------------------


    #--------- subparam inp output ----------------------------------------------------
    def __mirfile_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__mirfile_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Name of input Miriad visibility file'
        value = self.__mirfile( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'mirfile': value},{'mirfile': self.__schema['mirfile']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-7.7s = %s%-23s%s' % ('mirfile',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __vis_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__vis_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Name of output MeasurementSet'
        value = self.__vis( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'vis': value},{'vis': self.__schema['vis']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-7.7s = %s%-23s%s' % ('vis',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __tsys_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__tsys_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return False
        description = 'Use the Tsys to set the visibility weights'
        value = self.__tsys( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'tsys': value},{'tsys': self.__schema['tsys']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-7.7s = %s%-23s%s' % ('tsys',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __spw_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__spw_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return [ int(-1) ]
        description = 'Select spectral window/channels'
        value = self.__spw( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'spw': value},{'spw': self.__schema['spw']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-7.7s = %s%-23s%s' % ('spw',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __vel_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__vel_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Select velocity reference (TOPO,LSRK,LSRD)'
        value = self.__vel( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'vel': value},{'vel': self.__schema['vel']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-7.7s = %s%-23s%s' % ('vel',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __linecal_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__linecal_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return False
        description = '(CARMA) Apply line calibration'
        value = self.__linecal( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'linecal': value},{'linecal': self.__schema['linecal']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-7.7s = %s%-23s%s' % ('linecal',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __wide_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__wide_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return [  ]
        description = '(CARMA) Select wide window averages'
        value = self.__wide( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'wide': value},{'wide': self.__schema['wide']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-7.7s = %s%-23s%s' % ('wide',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __debug_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__debug_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return int(0)
        description = 'Display increasingly verbose debug messages'
        value = self.__debug( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'debug': value},{'debug': self.__schema['debug']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-7.7s = %s%-23s%s' % ('debug',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))

    #--------- global default implementation-------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def set_global_defaults(self):
        self.set_global_defaults.state['last'] = self
        glb = self.__globals_( )
        if 'linecal' in glb: del glb['linecal']
        if 'mirfile' in glb: del glb['mirfile']
        if 'vel' in glb: del glb['vel']
        if 'vis' in glb: del glb['vis']
        if 'tsys' in glb: del glb['tsys']
        if 'debug' in glb: del glb['debug']
        if 'wide' in glb: del glb['wide']
        if 'spw' in glb: del glb['spw']


    #--------- inp function -----------------------------------------------------------
    def inp(self):
        print("# importmiriad -- %s" % self._info_desc_)
        self.term_width, self.term_height = shutil.get_terminal_size(fallback=(80, 24))
        self.__mirfile_inp( )
        self.__vis_inp( )
        self.__tsys_inp( )
        self.__spw_inp( )
        self.__vel_inp( )
        self.__linecal_inp( )
        self.__wide_inp( )
        self.__debug_inp( )

    #--------- tget function ----------------------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def tget(self,savefile=None):
        from casashell.private.stack_manip import find_frame
        from runpy import run_path
        filename = savefile
        if filename is None:
            filename = "importmiriad.last" if os.path.isfile("importmiriad.last") else "importmiriad.saved"
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

        _postfile = outfile if outfile is not None else os.path.realpath('importmiriad.last')

        _invocation_parameters = OrderedDict( )
        _invocation_parameters['mirfile'] = self.__mirfile( self.__globals_( ) )
        _invocation_parameters['vis'] = self.__vis( self.__globals_( ) )
        _invocation_parameters['tsys'] = self.__tsys( self.__globals_( ) )
        _invocation_parameters['spw'] = self.__spw( self.__globals_( ) )
        _invocation_parameters['vel'] = self.__vel( self.__globals_( ) )
        _invocation_parameters['linecal'] = self.__linecal( self.__globals_( ) )
        _invocation_parameters['wide'] = self.__wide( self.__globals_( ) )
        _invocation_parameters['debug'] = self.__debug( self.__globals_( ) )

        try:
            with open(_postfile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-7s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#importmiriad( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: return False
        return True

    def __call__( self, mirfile=None, vis=None, tsys=None, spw=None, vel=None, linecal=None, wide=None, debug=None ):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s
        _prefile = os.path.realpath('importmiriad.pre')
        _postfile = os.path.realpath('importmiriad.last')
        _return_result_ = None
        _arguments = [mirfile,vis,tsys,spw,vel,linecal,wide,debug]
        _invocation_parameters = OrderedDict( )
        if any(map(lambda x: x is not None,_arguments)):
            # invoke python style
            # set the non sub-parameters that are not None
            local_global = { }
            if mirfile is not None: local_global['mirfile'] = mirfile
            if vis is not None: local_global['vis'] = vis
            if tsys is not None: local_global['tsys'] = tsys
            if spw is not None: local_global['spw'] = spw
            if vel is not None: local_global['vel'] = vel
            if linecal is not None: local_global['linecal'] = linecal
            if wide is not None: local_global['wide'] = wide
            if debug is not None: local_global['debug'] = debug

            # the invocation parameters for the non-subparameters can now be set - this picks up those defaults
            _invocation_parameters['mirfile'] = self.__mirfile( local_global )
            _invocation_parameters['vis'] = self.__vis( local_global )
            _invocation_parameters['tsys'] = self.__tsys( local_global )
            _invocation_parameters['spw'] = self.__spw( local_global )
            _invocation_parameters['vel'] = self.__vel( local_global )
            _invocation_parameters['linecal'] = self.__linecal( local_global )
            _invocation_parameters['wide'] = self.__wide( local_global )
            _invocation_parameters['debug'] = self.__debug( local_global )

            # the sub-parameters can then be set. Use the supplied value if not None, else the function, which gets the appropriate default
            

        else:
            # invoke with inp/go semantics
            _invocation_parameters['mirfile'] = self.__mirfile( self.__globals_( ) )
            _invocation_parameters['vis'] = self.__vis( self.__globals_( ) )
            _invocation_parameters['tsys'] = self.__tsys( self.__globals_( ) )
            _invocation_parameters['spw'] = self.__spw( self.__globals_( ) )
            _invocation_parameters['vel'] = self.__vel( self.__globals_( ) )
            _invocation_parameters['linecal'] = self.__linecal( self.__globals_( ) )
            _invocation_parameters['wide'] = self.__wide( self.__globals_( ) )
            _invocation_parameters['debug'] = self.__debug( self.__globals_( ) )
        try:
            with open(_prefile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-7s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#importmiriad( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: pass
        try:
            _return_result_ = _importmiriad_t( _invocation_parameters['mirfile'],_invocation_parameters['vis'],_invocation_parameters['tsys'],_invocation_parameters['spw'],_invocation_parameters['vel'],_invocation_parameters['linecal'],_invocation_parameters['wide'],_invocation_parameters['debug'] )
        except Exception as e:
            from traceback import format_exc
            from casatasks import casalog
            casalog.origin('importmiriad')
            casalog.post("Exception Reported: Error in importmiriad: %s" % str(e),'SEVERE')
            casalog.post(format_exc( ))
            _return_result_ = False
        try:
            os.rename(_prefile,_postfile)
        except: pass
        return _return_result_

importmiriad = _importmiriad( )

