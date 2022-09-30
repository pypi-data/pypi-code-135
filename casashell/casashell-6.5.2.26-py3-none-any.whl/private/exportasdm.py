##################### generated by xml-casa (v2) from exportasdm.xml ################
##################### 93407dc85aee418fc32630beafea5dfc ##############################
from __future__ import absolute_import
from casashell.private.stack_manip import find_local as __sf__
from casashell.private.stack_manip import find_frame as _find_frame
from casatools.typecheck import validator as _pc
from casatools.coercetype import coerce as _coerce
from casatasks import exportasdm as _exportasdm_t
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

class _exportasdm:
    """
    exportasdm ---- Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model

    
    Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model

    --------- parameter descriptions ---------------------------------------------

    vis             Name of input visibility file
                    Default: none
                    
                       Example: vis='ngc5921.ms'
    asdm            Name of output ASDM directory (on disk)
                    Default: none
    datacolumn      Which data column(s) to use for processing
                                     (case-insensitive).
                                     Default: 'corrected'
                                     Options: 'data', 'model', 'corrected',
                                     'all','float_data', 'lag_data',
                                     'float_data,data', 'lag_data,data'
                    
                                        Example: datacolumn='data'
                    
                                     NOTE: 'all' = whichever of the above that are
                                     present. If the requested column does not exist,
                                     the task will exit with an error.
    archiveid       The X0 in uid://X0/X1/X2
                    Default: 'S0'
    rangeid         The X1 in uid://X0/X1/X2
                    Default: 'X1'
    subscanduration Maximum duration of a subscan in the output ASDM
                    Default: 24h
    sbduration      Maximum duration of a scheduling block (and therefore
                    exec block) in the output ASDM
                    Default: '2700s'
                    
                    The sbduration parameter controls the number of
                    execution blocks (EBs) into which exportasdm
                    subdivides the visibilities from your input
                    MS. If the total observation time in the MS is
                    shorter than what is given in sbduration, a
                    single EB will be created.
    apcorrected     Data to be marked as having atmospheric phase correction
                    Default: False
                    Options: False|True
    verbose         Produce log output?
                    Default: True
                    Options: True|False
    [1;42mRETURNS[1;m            bool

    --------- examples -----------------------------------------------------------

    
    
    For more information, see the task pages of exportasdm in CASA Docs:
    
    https://casa.nrao.edu/casadocs/
    
    


    """

    _info_group_ = """import/export"""
    _info_desc_ = """Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model"""

    __schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'asdm': {'type': 'cPath', 'coerce': _coerce.expand_path}, 'datacolumn': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'DATA', 'model', 'corrected', 'CORRECTED', 'MODEL', 'data' ]}, 'archiveid': {'type': 'cStr', 'coerce': _coerce.to_str}, 'rangeid': {'type': 'cStr', 'coerce': _coerce.to_str}, 'subscanduration': {'type': 'cStr', 'coerce': _coerce.to_str}, 'sbduration': {'type': 'cStr', 'coerce': _coerce.to_str}, 'apcorrected': {'type': 'cBool'}, 'verbose': {'type': 'cBool'}}

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
        prefix_width = 23 + 15 + 4
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

    def __subscanduration_dflt( self, glb ):
        return '24h'

    def __subscanduration( self, glb ):
        if 'subscanduration' in glb: return glb['subscanduration']
        return '24h'

    def __verbose_dflt( self, glb ):
        return True

    def __verbose( self, glb ):
        if 'verbose' in glb: return glb['verbose']
        return True

    def __vis_dflt( self, glb ):
        return ''

    def __vis( self, glb ):
        if 'vis' in glb: return glb['vis']
        return ''

    def __datacolumn_dflt( self, glb ):
        return 'data'

    def __datacolumn( self, glb ):
        if 'datacolumn' in glb: return glb['datacolumn']
        return 'data'

    def __apcorrected_dflt( self, glb ):
        return False

    def __apcorrected( self, glb ):
        if 'apcorrected' in glb: return glb['apcorrected']
        return False

    def __sbduration_dflt( self, glb ):
        return '2700s'

    def __sbduration( self, glb ):
        if 'sbduration' in glb: return glb['sbduration']
        return '2700s'

    def __asdm_dflt( self, glb ):
        return ''

    def __asdm( self, glb ):
        if 'asdm' in glb: return glb['asdm']
        return ''

    def __rangeid_dflt( self, glb ):
        return 'X1'

    def __rangeid( self, glb ):
        if 'rangeid' in glb: return glb['rangeid']
        return 'X1'

    def __archiveid_dflt( self, glb ):
        return 'S0'

    def __archiveid( self, glb ):
        if 'archiveid' in glb: return glb['archiveid']
        return 'S0'



    #--------- return inp/go default --------------------------------------------------


    #--------- return subparam values -------------------------------------------------


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
        self.__do_inp_output('%-15.15s = %s%-23s%s' % ('vis',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __asdm_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__asdm_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = '>Name of output ASDM directory (on disk)'
        value = self.__asdm( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'asdm': value},{'asdm': self.__schema['asdm']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-15.15s = %s%-23s%s' % ('asdm',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __datacolumn_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__datacolumn_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return 'data'
        description = 'Which data column(s) to process.'
        value = self.__datacolumn( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'datacolumn': value},{'datacolumn': self.__schema['datacolumn']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-15.15s = %s%-23s%s' % ('datacolumn',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __archiveid_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__archiveid_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return 'S0'
        description = 'The X0 in uid://X0/X1/X2'
        value = self.__archiveid( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'archiveid': value},{'archiveid': self.__schema['archiveid']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-15.15s = %s%-23s%s' % ('archiveid',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __rangeid_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__rangeid_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return 'X1'
        description = 'The X1 in uid://X0/X1/X2'
        value = self.__rangeid( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'rangeid': value},{'rangeid': self.__schema['rangeid']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-15.15s = %s%-23s%s' % ('rangeid',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __subscanduration_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__subscanduration_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return '24h'
        description = 'Maximum duration of a subscan in the output ASDM'
        value = self.__subscanduration( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'subscanduration': value},{'subscanduration': self.__schema['subscanduration']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-15.15s = %s%-23s%s' % ('subscanduration',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __sbduration_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__sbduration_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return '2700s'
        description = 'Maximum duration of a scheduling block (and therefore exec block) in the output ASDM'
        value = self.__sbduration( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'sbduration': value},{'sbduration': self.__schema['sbduration']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-15.15s = %s%-23s%s' % ('sbduration',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __apcorrected_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__apcorrected_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return False
        description = 'Data to be marked as having atmospheric phase correction'
        value = self.__apcorrected( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'apcorrected': value},{'apcorrected': self.__schema['apcorrected']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-15.15s = %s%-23s%s' % ('apcorrected',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __verbose_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__verbose_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return True
        description = 'Produce log output'
        value = self.__verbose( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'verbose': value},{'verbose': self.__schema['verbose']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-15.15s = %s%-23s%s' % ('verbose',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))

    #--------- global default implementation-------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def set_global_defaults(self):
        self.set_global_defaults.state['last'] = self
        glb = self.__globals_( )
        if 'rangeid' in glb: del glb['rangeid']
        if 'subscanduration' in glb: del glb['subscanduration']
        if 'apcorrected' in glb: del glb['apcorrected']
        if 'datacolumn' in glb: del glb['datacolumn']
        if 'verbose' in glb: del glb['verbose']
        if 'sbduration' in glb: del glb['sbduration']
        if 'vis' in glb: del glb['vis']
        if 'archiveid' in glb: del glb['archiveid']
        if 'asdm' in glb: del glb['asdm']


    #--------- inp function -----------------------------------------------------------
    def inp(self):
        print("# exportasdm -- %s" % self._info_desc_)
        self.term_width, self.term_height = shutil.get_terminal_size(fallback=(80, 24))
        self.__vis_inp( )
        self.__asdm_inp( )
        self.__datacolumn_inp( )
        self.__archiveid_inp( )
        self.__rangeid_inp( )
        self.__subscanduration_inp( )
        self.__sbduration_inp( )
        self.__apcorrected_inp( )
        self.__verbose_inp( )

    #--------- tget function ----------------------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def tget(self,savefile=None):
        from casashell.private.stack_manip import find_frame
        from runpy import run_path
        filename = savefile
        if filename is None:
            filename = "exportasdm.last" if os.path.isfile("exportasdm.last") else "exportasdm.saved"
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

        _postfile = outfile if outfile is not None else os.path.realpath('exportasdm.last')

        _invocation_parameters = OrderedDict( )
        _invocation_parameters['vis'] = self.__vis( self.__globals_( ) )
        _invocation_parameters['asdm'] = self.__asdm( self.__globals_( ) )
        _invocation_parameters['datacolumn'] = self.__datacolumn( self.__globals_( ) )
        _invocation_parameters['archiveid'] = self.__archiveid( self.__globals_( ) )
        _invocation_parameters['rangeid'] = self.__rangeid( self.__globals_( ) )
        _invocation_parameters['subscanduration'] = self.__subscanduration( self.__globals_( ) )
        _invocation_parameters['sbduration'] = self.__sbduration( self.__globals_( ) )
        _invocation_parameters['apcorrected'] = self.__apcorrected( self.__globals_( ) )
        _invocation_parameters['verbose'] = self.__verbose( self.__globals_( ) )

        try:
            with open(_postfile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-15s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#exportasdm( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: return False
        return True

    def __call__( self, vis=None, asdm=None, datacolumn=None, archiveid=None, rangeid=None, subscanduration=None, sbduration=None, apcorrected=None, verbose=None ):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s
        _prefile = os.path.realpath('exportasdm.pre')
        _postfile = os.path.realpath('exportasdm.last')
        _return_result_ = None
        _arguments = [vis,asdm,datacolumn,archiveid,rangeid,subscanduration,sbduration,apcorrected,verbose]
        _invocation_parameters = OrderedDict( )
        if any(map(lambda x: x is not None,_arguments)):
            # invoke python style
            # set the non sub-parameters that are not None
            local_global = { }
            if vis is not None: local_global['vis'] = vis
            if asdm is not None: local_global['asdm'] = asdm
            if datacolumn is not None: local_global['datacolumn'] = datacolumn
            if archiveid is not None: local_global['archiveid'] = archiveid
            if rangeid is not None: local_global['rangeid'] = rangeid
            if subscanduration is not None: local_global['subscanduration'] = subscanduration
            if sbduration is not None: local_global['sbduration'] = sbduration
            if apcorrected is not None: local_global['apcorrected'] = apcorrected
            if verbose is not None: local_global['verbose'] = verbose

            # the invocation parameters for the non-subparameters can now be set - this picks up those defaults
            _invocation_parameters['vis'] = self.__vis( local_global )
            _invocation_parameters['asdm'] = self.__asdm( local_global )
            _invocation_parameters['datacolumn'] = self.__datacolumn( local_global )
            _invocation_parameters['archiveid'] = self.__archiveid( local_global )
            _invocation_parameters['rangeid'] = self.__rangeid( local_global )
            _invocation_parameters['subscanduration'] = self.__subscanduration( local_global )
            _invocation_parameters['sbduration'] = self.__sbduration( local_global )
            _invocation_parameters['apcorrected'] = self.__apcorrected( local_global )
            _invocation_parameters['verbose'] = self.__verbose( local_global )

            # the sub-parameters can then be set. Use the supplied value if not None, else the function, which gets the appropriate default
            

        else:
            # invoke with inp/go semantics
            _invocation_parameters['vis'] = self.__vis( self.__globals_( ) )
            _invocation_parameters['asdm'] = self.__asdm( self.__globals_( ) )
            _invocation_parameters['datacolumn'] = self.__datacolumn( self.__globals_( ) )
            _invocation_parameters['archiveid'] = self.__archiveid( self.__globals_( ) )
            _invocation_parameters['rangeid'] = self.__rangeid( self.__globals_( ) )
            _invocation_parameters['subscanduration'] = self.__subscanduration( self.__globals_( ) )
            _invocation_parameters['sbduration'] = self.__sbduration( self.__globals_( ) )
            _invocation_parameters['apcorrected'] = self.__apcorrected( self.__globals_( ) )
            _invocation_parameters['verbose'] = self.__verbose( self.__globals_( ) )
        try:
            with open(_prefile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-15s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#exportasdm( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: pass
        try:
            _return_result_ = _exportasdm_t( _invocation_parameters['vis'],_invocation_parameters['asdm'],_invocation_parameters['datacolumn'],_invocation_parameters['archiveid'],_invocation_parameters['rangeid'],_invocation_parameters['subscanduration'],_invocation_parameters['sbduration'],_invocation_parameters['apcorrected'],_invocation_parameters['verbose'] )
        except Exception as e:
            from traceback import format_exc
            from casatasks import casalog
            casalog.origin('exportasdm')
            casalog.post("Exception Reported: Error in exportasdm: %s" % str(e),'SEVERE')
            casalog.post(format_exc( ))
            _return_result_ = False
        try:
            os.rename(_prefile,_postfile)
        except: pass
        return _return_result_

exportasdm = _exportasdm( )

