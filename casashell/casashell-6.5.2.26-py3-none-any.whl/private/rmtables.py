##################### generated by xml-casa (v2) from rmtables.xml ##################
##################### 9c9e8a04e66b72709cb57b410e3e40a4 ##############################
from __future__ import absolute_import
from casashell.private.stack_manip import find_local as __sf__
from casashell.private.stack_manip import find_frame as _find_frame
from casatools.typecheck import validator as _pc
from casatools.coercetype import coerce as _coerce
from casatasks import rmtables as _rmtables_t
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

class _rmtables:
    """
    rmtables ---- Remove tables cleanly, use this instead of rm -rf

    
    This task removes tables if they are not being currently accessed via
    the casapy process. Note: if you have multiple sessions running bad things
    could happen if you remove a table being accessed by another process.
    

    --------- parameter descriptions ---------------------------------------------

    tablenames Name of the tables

    --------- examples -----------------------------------------------------------

    
    Removes tables cleanly.
    Arguments may contain * or ?. Ranges [] are support but
    not ~ expansion.
    


    """

    _info_group_ = """manipulation"""
    _info_desc_ = """Remove tables cleanly, use this instead of rm -rf"""

    __schema = {'tablenames': {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}}

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
        prefix_width = 23 + 10 + 4
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

    def __tablenames_dflt( self, glb ):
        return [  ]

    def __tablenames( self, glb ):
        if 'tablenames' in glb: return glb['tablenames']
        return [  ]



    #--------- return inp/go default --------------------------------------------------


    #--------- return subparam values -------------------------------------------------


    #--------- subparam inp output ----------------------------------------------------
    def __tablenames_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__tablenames_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return [  ]
        description = 'Name of the tables'
        value = self.__tablenames( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'tablenames': value},{'tablenames': self.__schema['tablenames']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('tablenames',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))

    #--------- global default implementation-------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def set_global_defaults(self):
        self.set_global_defaults.state['last'] = self
        glb = self.__globals_( )
        if 'tablenames' in glb: del glb['tablenames']


    #--------- inp function -----------------------------------------------------------
    def inp(self):
        print("# rmtables -- %s" % self._info_desc_)
        self.term_width, self.term_height = shutil.get_terminal_size(fallback=(80, 24))
        self.__tablenames_inp( )

    #--------- tget function ----------------------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def tget(self,savefile=None):
        from casashell.private.stack_manip import find_frame
        from runpy import run_path
        filename = savefile
        if filename is None:
            filename = "rmtables.last" if os.path.isfile("rmtables.last") else "rmtables.saved"
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

        _postfile = outfile if outfile is not None else os.path.realpath('rmtables.last')

        _invocation_parameters = OrderedDict( )
        _invocation_parameters['tablenames'] = self.__tablenames( self.__globals_( ) )

        try:
            with open(_postfile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-10s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#rmtables( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: return False
        return True

    def __call__( self, tablenames=None ):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s
        _prefile = os.path.realpath('rmtables.pre')
        _postfile = os.path.realpath('rmtables.last')
        _return_result_ = None
        _arguments = [tablenames]
        _invocation_parameters = OrderedDict( )
        if any(map(lambda x: x is not None,_arguments)):
            # invoke python style
            # set the non sub-parameters that are not None
            local_global = { }
            if tablenames is not None: local_global['tablenames'] = tablenames

            # the invocation parameters for the non-subparameters can now be set - this picks up those defaults
            _invocation_parameters['tablenames'] = self.__tablenames( local_global )

            # the sub-parameters can then be set. Use the supplied value if not None, else the function, which gets the appropriate default
            

        else:
            # invoke with inp/go semantics
            _invocation_parameters['tablenames'] = self.__tablenames( self.__globals_( ) )
        try:
            with open(_prefile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-10s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#rmtables( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: pass
        try:
            _return_result_ = _rmtables_t( _invocation_parameters['tablenames'] )
        except Exception as e:
            from traceback import format_exc
            from casatasks import casalog
            casalog.origin('rmtables')
            casalog.post("Exception Reported: Error in rmtables: %s" % str(e),'SEVERE')
            casalog.post(format_exc( ))
            _return_result_ = False
        try:
            os.rename(_prefile,_postfile)
        except: pass
        return _return_result_

rmtables = _rmtables( )

