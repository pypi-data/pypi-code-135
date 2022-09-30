##################### generated by xml-casa (v2) from gencal.xml ####################
##################### 4843ffba5f020a7c5dddda65c4d10f82 ##############################
from __future__ import absolute_import
from casashell.private.stack_manip import find_local as __sf__
from casashell.private.stack_manip import find_frame as _find_frame
from casatools.typecheck import validator as _pc
from casatools.coercetype import coerce as _coerce
from casatasks import gencal as _gencal_t
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

class _gencal:
    """
    gencal ---- Specify Calibration Values of Various Types

    
    The gencal task provides a means of specifying antenna-based
    calibration values manually.  The values are put in designated tables
    and applied to the data using applycal. Several specialized
    calibrations are also generated with gencal.
    
    Current antenna-based gencal options (caltype) are:
    
    - 'amp'= amplitude correction
    - 'ph' = phase correction
    - 'sbd'= single-band delay (phase-frequency slope for each spw)
    - 'mbd'= multi-band delay (phase-frequency slope over all spw)
    - 'antpos' = ITRF antenna position corrections
    - 'antposvla' = VLA-centric antenna position corrections
    - 'tsys' = Tsys from the SYSCAL table (ALMA)
    - 'swpow' = EVLA switched-power gains (experimental)
    - 'evlagain' (='swpow') (this syntax will deprecate)
    - 'rq' = EVLA requantizer gains _only_
    - 'swp/rq' = EVLA switched-power gains divided by requantizer gain
    - 'opac' = Tropospheric opacity
    - 'gc' = Gain curve (zenith-angle-dependent gain) (VLA only)
    - 'eff' = Antenna efficiency (sqrt(K/Jy)) (VLA only)
    - 'gceff' = Gain curve and efficiency (VLA only)
    - 'tecim' = Time-dep TEC image specified in infile
    - 'jyperk'= Jy/K factor via Jy/K DB Web API

    --------- parameter descriptions ---------------------------------------------

    vis             Name of input visibility file
                                         Default: none
                    
                                            Example: vis='ngc5921.ms'
    caltable        Name of input calibration table
                    
                                         Default: none
                    
                                         If a calibration table does not exist, it will be
                                         created. Specifying an existing table will result
                                         in the parameters being applied
                                         cumulatively. Only a single time-stamp for all
                                         calibrations are supported, currently.  Do not
                                         use a caltable created by gaincal, bandpass,
                                         etc. 
                    
                                            Example: caltable='test.G'
    caltype         The calibration parameter type being specified
                                         Default: none
                                         Options: 'amp', 'ph', 'sbd', 'mbd', 'antpos',
                                         'antposvla', 'tsys', 'evlagain', 'opac', 'gc',
                                         'gceff', 'eff', 'tecim', 'jyperk'
                    
                                         - 'amp' = gain (G) amplitude (1 real parameter
                                            per pol, antenna, spw)
                                         - 'ph'  = gain (G) phase (deg) (1 real parameter
                                            per pol, antenna, spw)
                                         - 'sbd' = single-band delays (nsec) (1 real
                                            parameter per pol, antenna, spw)
                                         - 'mbd' = multi-band delay (nsec) (1 real
                                            parameter per pol, antenna, spw)
                                         - 'antpos' = antenna position corrections (m) (3
                                            real ITRF offset parameters per antenna; spw,
                                            pol selection will be ignored)
                                            With antenna='', this triggers an automated
                                            lookup of antenna positions for EVLA and ALMA.
                                         - 'antposvla' = antenna position corrections (m)
                                            specified in the old VLA-centric coordinate
                                            system
                                         - 'tsys' = Tsys from the SYSCAL table (ALMA)
                                         - 'evlagain' = EVLA switched-power gains
                                            (experimental)
                                         - 'opac' = Tropospheric opacity (1 real parameter
                                            per antenna, spw)
                                         - 'gc' = Antenna zenith-angle dependent gain
                                            curve (auto-lookup)
                                         - 'gceff' = Gain curve and efficiency
                                            (auto-lookup)
                                         - 'eff' = Antenna efficiency (auto-lookup)
                                         - 'jyperk' = Jy/K factor via Jy/K DB Web API
                    
                                            Example: caltype='ph'
    infile          Input ancilliary file
                    Subparameter of caltype='gc|gceff|tecim|jyperk'
                    Default: none
    endpoint        Input endpoint of the Jy/K DB Web API.
                    Subparameter of caltype='jyperk'
                    Default: 'asdm'
                    Options: 'asdm', 'model-fit', 'interpolation'
                    
                    The 'interpolation' option may not work for the data after 2019.
    timeout         Maximum waiting time [sec] for the Web API access.
                    Subparameter of caltype='jyperk'
                    Default: 180
    retry           Number of retry when the Web API access fails.
                    Subparameter of caltype='jyperk'
                    Default: 3
    retry_wait_time Waiting time [sec] until next query, when the Web API access fails.
                    Subparameter of caltype='jyperk'
                    Default: 5
    spw             Select spectral window/channels
                             Default: '' (all spectral windows and channels)
                    
                                Examples: spw='0~2,4'; spectral windows 0,1,2,4 (all channels) spw='<2';  spectral windows less than 2 (i.e. 0,1) spw='0:5~61'; spw 0, channels 5 to 61 spw='0,10,3:3~45'; spw 0,10 all channels, spw
                                3 - chans 3 to 45. spw='0~2:2~6'; spw 0,1,2 with channels 2
                                through 6 in each.
                                spw = '\*:3~64'  channels 3 through 64 for all sp id's
                                spw = ' :3~64' will NOT work.
    antenna         Select data based on antenna/baseline
                                         Subparameter of selectdata=True
                                         Default: '' (all)
                    
                                         If antenna string is a non-negative integer, it
                                         is assumed an antenna index, otherwise, it is
                                         assumed as an antenna name
                      
                                             Examples: 
                                             antenna='5&6'; baseline between antenna
                                             index 5 and index 6.
                                             antenna='VA05&VA06'; baseline between VLA
                                             antenna 5 and 6.
                                             antenna='5&6;7&8'; baselines with
                                             indices 5-6 and 7-8
                                             antenna='5'; all baselines with antenna index
                                             5
                                             antenna='05'; all baselines with antenna
                                             number 05 (VLA old name)
                                             antenna='5,6,10'; all baselines with antennas
                                             5,6,10 index numbers
    pol             Polarization selection for specified parameters
                                         Default: pol='' (specified parameters apply to
                                         all polarizations)
                    
                                            Example: pol='R' (specified parameters to
                                            apply to R only)
    parameter       The calibration values
                    
                                         The calibration parameters, specified as a list,
                                         to store in the caltable for the spw, antenna,
                                         and pol selection.  The required length of the
                                         list is determined by the caltype and the spw,
                                         antenna, pol selection.  One "set" of parameters
                                         (e.g., one value for 'amp', 'ph', etc., three
                                         values for 'antpos') specified the same value for
                                         all indicated spw, antenna, and pol.
                                         OR, 
                                         When specifying a long list of calibration
                                         parameter values, these should be ordered first
                                         (fastest) by pol (if pol!=''), then by antenna
                                         (if antenna!=''), and finally (sloweset) by spw
                                         (if spw!='').  Unspecified selection axes must
                                         not be enumerated in the parameter list
    uniform         Assume uniform calibration values across the array
                    Subparameter of caltype='tsys'
                     Default: True
                     Options: True|False
    [1;42mRETURNS[1;m            void

    --------- examples -----------------------------------------------------------

    
    FOR MORE INFORMATION, SEE THE TASK PAGES OF GENCAL IN CASA DOCS:
    https://casa.nrao.edu/casadocs/


    """

    _info_group_ = """calibration"""
    _info_desc_ = """Specify Calibration Values of Various Types"""

    __schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'caltable': {'type': 'cStr', 'coerce': _coerce.to_str}, 'caltype': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'eff', 'antposvla', 'mbd', 'opac', 'gc', 'antpos', 'tsys', 'swp/rq', 'swpow', 'amp', 'tecim', 'gceff', 'jyperk', 'ph', 'rq', 'evlagain', 'sbd' ]}, 'infile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'endpoint': {'type': 'cStr', 'coerce': _coerce.to_str}, 'timeout': {'type': 'cInt'}, 'retry': {'type': 'cInt'}, 'retry_wait_time': {'type': 'cInt'}, 'spw': {'type': 'cStr', 'coerce': _coerce.to_str}, 'antenna': {'type': 'cStr', 'coerce': _coerce.to_str}, 'pol': {'type': 'cStr', 'coerce': _coerce.to_str}, 'parameter': {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, 'uniform': {'type': 'cBool'}}

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
        prefix_width = 23 + 18 + 4
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

    def __parameter_dflt( self, glb ):
        return [  ]

    def __parameter( self, glb ):
        if 'parameter' in glb: return glb['parameter']
        return [  ]

    def __vis_dflt( self, glb ):
        return ''

    def __vis( self, glb ):
        if 'vis' in glb: return glb['vis']
        return ''

    def __caltable_dflt( self, glb ):
        return ''

    def __caltable( self, glb ):
        if 'caltable' in glb: return glb['caltable']
        return ''

    def __spw_dflt( self, glb ):
        return ''

    def __spw( self, glb ):
        if 'spw' in glb: return glb['spw']
        return ''

    def __pol_dflt( self, glb ):
        return ''

    def __pol( self, glb ):
        if 'pol' in glb: return glb['pol']
        return ''

    def __antenna_dflt( self, glb ):
        return ''

    def __antenna( self, glb ):
        if 'antenna' in glb: return glb['antenna']
        return ''

    def __caltype_dflt( self, glb ):
        return ''

    def __caltype( self, glb ):
        if 'caltype' in glb: return glb['caltype']
        return ''



    #--------- return inp/go default --------------------------------------------------
    def __infile_dflt( self, glb ):
        if self.__caltype( glb ) == "tecim": return ""
        if self.__caltype( glb ) == "gc": return ""
        if self.__caltype( glb ) == "gceff": return ""
        if self.__caltype( glb ) == "jyperk": return ""
        return None
    def __uniform_dflt( self, glb ):
        if self.__caltype( glb ) == "tsys": return bool(True)
        return None
    def __retry_wait_time_dflt( self, glb ):
        if self.__caltype( glb ) == "jyperk": return int(5)
        return None
    def __endpoint_dflt( self, glb ):
        if self.__caltype( glb ) == "jyperk": return "asdm"
        return None
    def __timeout_dflt( self, glb ):
        if self.__caltype( glb ) == "jyperk": return int(180)
        return None
    def __retry_dflt( self, glb ):
        if self.__caltype( glb ) == "jyperk": return int(3)
        return None

    #--------- return subparam values -------------------------------------------------
    def __infile( self, glb ):
        if 'infile' in glb: return glb['infile']
        dflt = self.__infile_dflt( glb )
        if dflt is not None: return dflt
        return ''
    def __endpoint( self, glb ):
        if 'endpoint' in glb: return glb['endpoint']
        dflt = self.__endpoint_dflt( glb )
        if dflt is not None: return dflt
        return 'asdm'
    def __timeout( self, glb ):
        if 'timeout' in glb: return glb['timeout']
        dflt = self.__timeout_dflt( glb )
        if dflt is not None: return dflt
        return int(180)
    def __retry( self, glb ):
        if 'retry' in glb: return glb['retry']
        dflt = self.__retry_dflt( glb )
        if dflt is not None: return dflt
        return int(3)
    def __retry_wait_time( self, glb ):
        if 'retry_wait_time' in glb: return glb['retry_wait_time']
        dflt = self.__retry_wait_time_dflt( glb )
        if dflt is not None: return dflt
        return int(5)
    def __uniform( self, glb ):
        if 'uniform' in glb: return glb['uniform']
        dflt = self.__uniform_dflt( glb )
        if dflt is not None: return dflt
        return True

    #--------- subparam inp output ----------------------------------------------------
    def __vis_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__vis_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Name of input visibility file'
        value = self.__vis( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'vis': value},{'vis': self.__schema['vis']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-18.18s = %s%-23s%s' % ('vis',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __caltable_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__caltable_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Name of input calibration table'
        value = self.__caltable( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'caltable': value},{'caltable': self.__schema['caltable']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-18.18s = %s%-23s%s' % ('caltable',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __caltype_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__caltype_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'The calibration type: (amp, ph, sbd, mbd, antpos, antposvla, tsys, evlagain, opac, gc, gceff, eff, tecim, jyperk)'
        value = self.__caltype( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'caltype': value},{'caltype': self.__schema['caltype']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('\x1B[1m\x1B[47m%-18.18s =\x1B[0m %s%-23s%s' % ('caltype',pre,self.__to_string_(value),post),description,13+len(pre)+len(post))
    def __infile_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__infile_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        if self.__infile_dflt( self.__globals_( ) ) is not None:
             description = 'Input ancilliary file'
             value = self.__infile( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'infile': value},{'infile': self.__schema['infile']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-15.15s =\x1B[0m %s%-23s%s' % ('infile',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __endpoint_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__endpoint_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return 'asdm'
        if self.__endpoint_dflt( self.__globals_( ) ) is not None:
             description = 'Input endpoint of the Jy/K DB Web API: (asdm, model-fit, interpolation)'
             value = self.__endpoint( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'endpoint': value},{'endpoint': self.__schema['endpoint']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-15.15s =\x1B[0m %s%-23s%s' % ('endpoint',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __timeout_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__timeout_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return int(180)
        if self.__timeout_dflt( self.__globals_( ) ) is not None:
             description = 'Maximum waiting time [sec] for the Web API access'
             value = self.__timeout( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'timeout': value},{'timeout': self.__schema['timeout']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-15.15s =\x1B[0m %s%-23s%s' % ('timeout',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __retry_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__retry_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return int(3)
        if self.__retry_dflt( self.__globals_( ) ) is not None:
             description = 'Number of retry when the Web API access fails'
             value = self.__retry( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'retry': value},{'retry': self.__schema['retry']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-15.15s =\x1B[0m %s%-23s%s' % ('retry',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __retry_wait_time_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__retry_wait_time_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return int(5)
        if self.__retry_wait_time_dflt( self.__globals_( ) ) is not None:
             description = 'Waiting time [sec] until next query'
             value = self.__retry_wait_time( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'retry_wait_time': value},{'retry_wait_time': self.__schema['retry_wait_time']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-15.15s =\x1B[0m %s%-23s%s' % ('retry_wait_time',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __spw_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__spw_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Select spectral window/channels'
        value = self.__spw( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'spw': value},{'spw': self.__schema['spw']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-18.18s = %s%-23s%s' % ('spw',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __antenna_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__antenna_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Select data based on antenna/baseline'
        value = self.__antenna( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'antenna': value},{'antenna': self.__schema['antenna']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-18.18s = %s%-23s%s' % ('antenna',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __pol_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__pol_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Calibration polarizations(s) selection'
        value = self.__pol( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'pol': value},{'pol': self.__schema['pol']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-18.18s = %s%-23s%s' % ('pol',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __parameter_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__parameter_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return [  ]
        description = 'The calibration values'
        value = self.__parameter( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'parameter': value},{'parameter': self.__schema['parameter']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-18.18s = %s%-23s%s' % ('parameter',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __uniform_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__uniform_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return True
        if self.__uniform_dflt( self.__globals_( ) ) is not None:
             description = 'Assume uniform calibration values across the array'
             value = self.__uniform( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'uniform': value},{'uniform': self.__schema['uniform']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-15.15s =\x1B[0m %s%-23s%s' % ('uniform',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))

    #--------- global default implementation-------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def set_global_defaults(self):
        self.set_global_defaults.state['last'] = self
        glb = self.__globals_( )
        if 'antenna' in glb: del glb['antenna']
        if 'infile' in glb: del glb['infile']
        if 'parameter' in glb: del glb['parameter']
        if 'vis' in glb: del glb['vis']
        if 'uniform' in glb: del glb['uniform']
        if 'caltype' in glb: del glb['caltype']
        if 'retry_wait_time' in glb: del glb['retry_wait_time']
        if 'endpoint' in glb: del glb['endpoint']
        if 'caltable' in glb: del glb['caltable']
        if 'pol' in glb: del glb['pol']
        if 'timeout' in glb: del glb['timeout']
        if 'retry' in glb: del glb['retry']
        if 'spw' in glb: del glb['spw']


    #--------- inp function -----------------------------------------------------------
    def inp(self):
        print("# gencal -- %s" % self._info_desc_)
        self.term_width, self.term_height = shutil.get_terminal_size(fallback=(80, 24))
        self.__vis_inp( )
        self.__caltable_inp( )
        self.__caltype_inp( )
        self.__infile_inp( )
        self.__endpoint_inp( )
        self.__timeout_inp( )
        self.__retry_inp( )
        self.__retry_wait_time_inp( )
        self.__spw_inp( )
        self.__antenna_inp( )
        self.__pol_inp( )
        self.__parameter_inp( )
        self.__uniform_inp( )

    #--------- tget function ----------------------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def tget(self,savefile=None):
        from casashell.private.stack_manip import find_frame
        from runpy import run_path
        filename = savefile
        if filename is None:
            filename = "gencal.last" if os.path.isfile("gencal.last") else "gencal.saved"
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

        _postfile = outfile if outfile is not None else os.path.realpath('gencal.last')

        _invocation_parameters = OrderedDict( )
        _invocation_parameters['vis'] = self.__vis( self.__globals_( ) )
        _invocation_parameters['caltable'] = self.__caltable( self.__globals_( ) )
        _invocation_parameters['caltype'] = self.__caltype( self.__globals_( ) )
        _invocation_parameters['infile'] = self.__infile( self.__globals_( ) )
        _invocation_parameters['endpoint'] = self.__endpoint( self.__globals_( ) )
        _invocation_parameters['timeout'] = self.__timeout( self.__globals_( ) )
        _invocation_parameters['retry'] = self.__retry( self.__globals_( ) )
        _invocation_parameters['retry_wait_time'] = self.__retry_wait_time( self.__globals_( ) )
        _invocation_parameters['spw'] = self.__spw( self.__globals_( ) )
        _invocation_parameters['antenna'] = self.__antenna( self.__globals_( ) )
        _invocation_parameters['pol'] = self.__pol( self.__globals_( ) )
        _invocation_parameters['parameter'] = self.__parameter( self.__globals_( ) )
        _invocation_parameters['uniform'] = self.__uniform( self.__globals_( ) )

        try:
            with open(_postfile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-15s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#gencal( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: return False
        return True

    def __call__( self, vis=None, caltable=None, caltype=None, infile=None, endpoint=None, timeout=None, retry=None, retry_wait_time=None, spw=None, antenna=None, pol=None, parameter=None, uniform=None ):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s
        _prefile = os.path.realpath('gencal.pre')
        _postfile = os.path.realpath('gencal.last')
        _return_result_ = None
        _arguments = [vis,caltable,caltype,infile,endpoint,timeout,retry,retry_wait_time,spw,antenna,pol,parameter,uniform]
        _invocation_parameters = OrderedDict( )
        if any(map(lambda x: x is not None,_arguments)):
            # invoke python style
            # set the non sub-parameters that are not None
            local_global = { }
            if vis is not None: local_global['vis'] = vis
            if caltable is not None: local_global['caltable'] = caltable
            if caltype is not None: local_global['caltype'] = caltype
            if spw is not None: local_global['spw'] = spw
            if antenna is not None: local_global['antenna'] = antenna
            if pol is not None: local_global['pol'] = pol
            if parameter is not None: local_global['parameter'] = parameter

            # the invocation parameters for the non-subparameters can now be set - this picks up those defaults
            _invocation_parameters['vis'] = self.__vis( local_global )
            _invocation_parameters['caltable'] = self.__caltable( local_global )
            _invocation_parameters['caltype'] = self.__caltype( local_global )
            _invocation_parameters['spw'] = self.__spw( local_global )
            _invocation_parameters['antenna'] = self.__antenna( local_global )
            _invocation_parameters['pol'] = self.__pol( local_global )
            _invocation_parameters['parameter'] = self.__parameter( local_global )

            # the sub-parameters can then be set. Use the supplied value if not None, else the function, which gets the appropriate default
            _invocation_parameters['infile'] = self.__infile( _invocation_parameters ) if infile is None else infile
            _invocation_parameters['endpoint'] = self.__endpoint( _invocation_parameters ) if endpoint is None else endpoint
            _invocation_parameters['timeout'] = self.__timeout( _invocation_parameters ) if timeout is None else timeout
            _invocation_parameters['retry'] = self.__retry( _invocation_parameters ) if retry is None else retry
            _invocation_parameters['retry_wait_time'] = self.__retry_wait_time( _invocation_parameters ) if retry_wait_time is None else retry_wait_time
            _invocation_parameters['uniform'] = self.__uniform( _invocation_parameters ) if uniform is None else uniform

        else:
            # invoke with inp/go semantics
            _invocation_parameters['vis'] = self.__vis( self.__globals_( ) )
            _invocation_parameters['caltable'] = self.__caltable( self.__globals_( ) )
            _invocation_parameters['caltype'] = self.__caltype( self.__globals_( ) )
            _invocation_parameters['infile'] = self.__infile( self.__globals_( ) )
            _invocation_parameters['endpoint'] = self.__endpoint( self.__globals_( ) )
            _invocation_parameters['timeout'] = self.__timeout( self.__globals_( ) )
            _invocation_parameters['retry'] = self.__retry( self.__globals_( ) )
            _invocation_parameters['retry_wait_time'] = self.__retry_wait_time( self.__globals_( ) )
            _invocation_parameters['spw'] = self.__spw( self.__globals_( ) )
            _invocation_parameters['antenna'] = self.__antenna( self.__globals_( ) )
            _invocation_parameters['pol'] = self.__pol( self.__globals_( ) )
            _invocation_parameters['parameter'] = self.__parameter( self.__globals_( ) )
            _invocation_parameters['uniform'] = self.__uniform( self.__globals_( ) )
        try:
            with open(_prefile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-15s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#gencal( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: pass
        try:
            _return_result_ = _gencal_t( _invocation_parameters['vis'],_invocation_parameters['caltable'],_invocation_parameters['caltype'],_invocation_parameters['infile'],_invocation_parameters['endpoint'],_invocation_parameters['timeout'],_invocation_parameters['retry'],_invocation_parameters['retry_wait_time'],_invocation_parameters['spw'],_invocation_parameters['antenna'],_invocation_parameters['pol'],_invocation_parameters['parameter'],_invocation_parameters['uniform'] )
        except Exception as e:
            from traceback import format_exc
            from casatasks import casalog
            casalog.origin('gencal')
            casalog.post("Exception Reported: Error in gencal: %s" % str(e),'SEVERE')
            casalog.post(format_exc( ))
            _return_result_ = False
        try:
            os.rename(_prefile,_postfile)
        except: pass
        return _return_result_

gencal = _gencal( )

