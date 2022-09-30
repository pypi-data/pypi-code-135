##################### generated by xml-casa (v2) from listsdm.xml ###################
##################### b97c8caa49b03fa97c3ecc3acb949cc7 ##############################
from __future__ import absolute_import
from casashell.private.stack_manip import find_local as __sf__
from casashell.private.stack_manip import find_frame as _find_frame
from casatools.typecheck import validator as _pc
from casatools.coercetype import coerce as _coerce
from casatasks import listsdm as _listsdm_t
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

class _listsdm:
    """
    listsdm ---- Lists observation information present in an SDM directory.

    Given an SDM directory, this task will print observation information to the logger and return a dictionary keyed by scan.

    --------- parameter descriptions ---------------------------------------------

    sdm     Name of input SDM directory
    [1;42mRETURNS[1;m    void

    --------- examples -----------------------------------------------------------

    
    
    The listsdm task reads SDM XML tables, processes the
    observation information contained therein, and prints this
    information to the CASA log.  It will also return a dictionary
    keyed on scan number.  The dictionary contains the following
    information:
    
    'baseband'   list of baseband name(s)
    'chanwidth'  list of channel widths (Hz)
    'end'        observation end time (UTC)
    'field'      field ID
    'intent'     scan intent(s)
    'nchan'      list of number of channels
    'nsubs'      number of subscans
    'reffreq'    list of reference frequencies (Hz)
    'source'     source name
    'spws'       list of spectral windows
    'start'      observation start time (UTC)
    'timerange'  start time - end time range (UTC)
    
    Example:
    
    myscans = listsdm(sdm='AS1039_sb1382796_2_000.55368.51883247685')
    
    Prints information about the requested SDM to the CASA logger
    and returns a dictionary with scan information in 'myscans'.
    
    Keyword argument:
    
    sdm -- Name of input SDM directory.
    example: sdm='AG836_sb1377811_1.55345.300883159725'
    
    


    """

    _info_group_ = """information"""
    _info_desc_ = """Lists observation information present in an SDM directory."""

    __schema = {'sdm': {'type': 'cReqPath', 'coerce': _coerce.expand_path}}

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
        prefix_width = 23 + 3 + 4
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

    def __sdm_dflt( self, glb ):
        return ''

    def __sdm( self, glb ):
        if 'sdm' in glb: return glb['sdm']
        return ''



    #--------- return inp/go default --------------------------------------------------


    #--------- return subparam values -------------------------------------------------


    #--------- subparam inp output ----------------------------------------------------
    def __sdm_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__sdm_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Name of input SDM directory'
        value = self.__sdm( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'sdm': value},{'sdm': self.__schema['sdm']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-3.3s = %s%-23s%s' % ('sdm',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))

    #--------- global default implementation-------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def set_global_defaults(self):
        self.set_global_defaults.state['last'] = self
        glb = self.__globals_( )
        if 'sdm' in glb: del glb['sdm']


    #--------- inp function -----------------------------------------------------------
    def inp(self):
        print("# listsdm -- %s" % self._info_desc_)
        self.term_width, self.term_height = shutil.get_terminal_size(fallback=(80, 24))
        self.__sdm_inp( )

    #--------- tget function ----------------------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def tget(self,savefile=None):
        from casashell.private.stack_manip import find_frame
        from runpy import run_path
        filename = savefile
        if filename is None:
            filename = "listsdm.last" if os.path.isfile("listsdm.last") else "listsdm.saved"
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

        _postfile = outfile if outfile is not None else os.path.realpath('listsdm.last')

        _invocation_parameters = OrderedDict( )
        _invocation_parameters['sdm'] = self.__sdm( self.__globals_( ) )

        try:
            with open(_postfile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-3s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#listsdm( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: return False
        return True

    def __call__( self, sdm=None ):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s
        _prefile = os.path.realpath('listsdm.pre')
        _postfile = os.path.realpath('listsdm.last')
        _return_result_ = None
        _arguments = [sdm]
        _invocation_parameters = OrderedDict( )
        if any(map(lambda x: x is not None,_arguments)):
            # invoke python style
            # set the non sub-parameters that are not None
            local_global = { }
            if sdm is not None: local_global['sdm'] = sdm

            # the invocation parameters for the non-subparameters can now be set - this picks up those defaults
            _invocation_parameters['sdm'] = self.__sdm( local_global )

            # the sub-parameters can then be set. Use the supplied value if not None, else the function, which gets the appropriate default
            

        else:
            # invoke with inp/go semantics
            _invocation_parameters['sdm'] = self.__sdm( self.__globals_( ) )
        try:
            with open(_prefile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-3s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#listsdm( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: pass
        try:
            _return_result_ = _listsdm_t( _invocation_parameters['sdm'] )
        except Exception as e:
            from traceback import format_exc
            from casatasks import casalog
            casalog.origin('listsdm')
            casalog.post("Exception Reported: Error in listsdm: %s" % str(e),'SEVERE')
            casalog.post(format_exc( ))
            _return_result_ = False
        try:
            os.rename(_prefile,_postfile)
        except: pass
        return _return_result_

listsdm = _listsdm( )

