##################### generated by xml-casa (v2) from sdsmooth.xml ##################
##################### 1faefec8c7f2376940dc98c5d1f95d26 ##############################
from __future__ import absolute_import
from casashell.private.stack_manip import find_local as __sf__
from casashell.private.stack_manip import find_frame as _find_frame
from casatools.typecheck import validator as _pc
from casatools.coercetype import coerce as _coerce
from casatasks import sdsmooth as _sdsmooth_t
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

class _sdsmooth:
    """
    sdsmooth ---- Smooth spectral data

    
    Task sdsmooth performs smoothing along spectral axis using user-specified
    smoothing kernel. Currently gaussian and boxcar kernels are supported.
    

    --------- parameter descriptions ---------------------------------------------

    infile     name of input SD dataset
    datacolumn name of data column to be used ["data", "float_data", or "corrected"]
    antenna    select data by antenna name or ID, e.g. "PM03"
    field      select data by field IDs and names, e.g. "3C2*" (""=all)
    spw        select data by spectral window IDs, e.g. "3,5,7" (""=all)
    timerange  select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
    scan       select data by scan numbers, e.g. "21~23" (""=all)
    pol        select data by polarization IDs, e.g. "0,1" (""=all)
    intent     select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
    reindex    Re-index indices in subtables based on data selection
    kernel     spectral smoothing kernel type
    kwidth     smoothing kernel width in channel
    outfile    name of output file
    overwrite  overwrite the output file if already exists
    [1;42mRETURNS[1;m       void

    --------- examples -----------------------------------------------------------

    
    -----------------
    Keyword arguments
    -----------------
    infile -- name of input SD dataset
    datacolumn -- name of data column to be used
    options: 'data', 'float_data', or 'corrected'
    default: 'data'
    antenna -- select data by antenna name or ID
    default: '' (use all antennas)
    example: 'PM03'
    field -- select data by field IDs and names
    default: '' (use all fields)
    example: field='3C2*' (all names starting with 3C2)
    field='0,4,5~7' (field IDs 0,4,5,6,7)
    field='0,3C273' (field ID 0 or field named 3C273)
    this selection is in addition to the other selections to data
    spw -- select data by spectral window IDs/channels
    default: '' (use all spws and channels)
    example: spw='3,5,7' (spw IDs 3,5,7; all channels)
    spw='<2' (spw IDs less than 2, i.e., 0,1; all channels)
    spw='30~45GHz' (spw IDs with the center frequencies in range 30-45GHz; all channels)
    spw='0:5~61' (spw ID 0; channels 5 to 61; all channels)
    spw='3:10~20;50~60' (select multiple channel ranges within spw ID 3)
    spw='3:10~20,4:0~30' (select different channel ranges for spw IDs 3 and 4)
    spw='1~4;6:15~48' (for channels 15 through 48 for spw IDs 1,2,3,4 and 6)
    this selection is in addition to the other selections to data
    timerange -- select data by time range
    default: '' (use all)
    example: timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
    Note: YYYY/MM/DD can be dropped as needed:
    timerange='09:14:00~09:54:00' # this time range
    timerange='09:44:00' # data within one integration of time
    timerange='>10:24:00' # data after this time
    timerange='09:44:00+00:13:00' #data 13 minutes after time
    this selection is in addition to the other selections to data
    scan -- select data by scan numbers
    default: '' (use all scans)
    example: scan='21~23' (scan IDs 21,22,23)
    this selection is in addition to the other selections to data
    pol -- select data by polarization IDs
    default: '' (use all polarizations)
    example: pol='0,1' (polarization IDs 0,1)
    this selection is in addition to the other selections to data
    intent -- select data by observational intent, also referred to as 'scan intent'
    default: '' (use all scan intents)
    example: intent='*ON_SOURCE*' (any valid scan-intent expression accepted by the MSSelection module can be specified)
    this selection is in addition to the other selections to data
    reindex -- Re-index indices in subtables based on data selection.
    If True, DATA_DESCRIPTION, FEED, SPECTRAL_WINDOW, STATE, and SOURCE
    subtables are filtered based on data selection and re-indexed in output MS.
    default: True
    kernel -- type of spectral smoothing kernel
    options: 'gaussian', 'boxcar'
    default: 'gaussian' (no smoothing)
    
    >>>kernel expandable parameter
    kwidth -- width of spectral smoothing kernel
    options: (int) in channels
    default: 5
    outfile -- name of output file
    default: '' (<infile>_bs)
    overwrite -- overwrite the output file if already exists
    options: (bool) True, False
    default: False
    NOTE this parameter is ignored when outform='ASCII'
    
    
    -----------
    DESCRIPTION
    -----------
    Task sdsmooth performs smoothing along spectral axis using user-specified
    smoothing kernel. Currently gaussian and boxcar kernels are supported.
    
    
    


    """

    _info_group_ = """single dish"""
    _info_desc_ = """Smooth spectral data """

    __schema = {'infile': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'datacolumn': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'DATA', 'corrected', 'FLOAT_DATA', 'CORRECTED', 'float_data', 'data' ]}, 'antenna': {'type': 'cStr', 'coerce': _coerce.to_str}, 'field': {'type': 'cStr', 'coerce': _coerce.to_str}, 'spw': {'type': 'cStr', 'coerce': _coerce.to_str}, 'timerange': {'type': 'cStr', 'coerce': _coerce.to_str}, 'scan': {'type': 'cStr', 'coerce': _coerce.to_str}, 'pol': {'type': 'cStr', 'coerce': _coerce.to_str}, 'intent': {'type': 'cStr', 'coerce': _coerce.to_str}, 'reindex': {'type': 'cBool'}, 'kernel': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'gaussian', 'boxcar' ]}, 'kwidth': {'type': 'cInt'}, 'outfile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'overwrite': {'type': 'cBool'}}

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

    def __kernel_dflt( self, glb ):
        return 'gaussian'

    def __kernel( self, glb ):
        if 'kernel' in glb: return glb['kernel']
        return 'gaussian'

    def __spw_dflt( self, glb ):
        return ''

    def __spw( self, glb ):
        if 'spw' in glb: return glb['spw']
        return ''

    def __datacolumn_dflt( self, glb ):
        return 'data'

    def __datacolumn( self, glb ):
        if 'datacolumn' in glb: return glb['datacolumn']
        return 'data'

    def __outfile_dflt( self, glb ):
        return ''

    def __outfile( self, glb ):
        if 'outfile' in glb: return glb['outfile']
        return ''

    def __scan_dflt( self, glb ):
        return ''

    def __scan( self, glb ):
        if 'scan' in glb: return glb['scan']
        return ''

    def __timerange_dflt( self, glb ):
        return ''

    def __timerange( self, glb ):
        if 'timerange' in glb: return glb['timerange']
        return ''

    def __field_dflt( self, glb ):
        return ''

    def __field( self, glb ):
        if 'field' in glb: return glb['field']
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

    def __intent_dflt( self, glb ):
        return ''

    def __intent( self, glb ):
        if 'intent' in glb: return glb['intent']
        return ''

    def __reindex_dflt( self, glb ):
        return True

    def __reindex( self, glb ):
        if 'reindex' in glb: return glb['reindex']
        return True

    def __infile_dflt( self, glb ):
        return ''

    def __infile( self, glb ):
        if 'infile' in glb: return glb['infile']
        return ''

    def __overwrite_dflt( self, glb ):
        return False

    def __overwrite( self, glb ):
        if 'overwrite' in glb: return glb['overwrite']
        return False



    #--------- return inp/go default --------------------------------------------------
    def __kwidth_dflt( self, glb ):
        if self.__kernel( glb ) == "gaussian": return int(5)
        if self.__kernel( glb ) == "boxcar": return int(5)
        return None

    #--------- return subparam values -------------------------------------------------
    def __kwidth( self, glb ):
        if 'kwidth' in glb: return glb['kwidth']
        dflt = self.__kwidth_dflt( glb )
        if dflt is not None: return dflt
        return int(5)

    #--------- subparam inp output ----------------------------------------------------
    def __infile_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__infile_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'name of input SD dataset'
        value = self.__infile( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'infile': value},{'infile': self.__schema['infile']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('infile',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __datacolumn_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__datacolumn_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return 'data'
        description = 'name of data column to be used ["data", "float_data", or "corrected"]'
        value = self.__datacolumn( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'datacolumn': value},{'datacolumn': self.__schema['datacolumn']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('datacolumn',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __antenna_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__antenna_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'select data by antenna name or ID, e.g. "PM03"'
        value = self.__antenna( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'antenna': value},{'antenna': self.__schema['antenna']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('antenna',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __field_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__field_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'select data by field IDs and names, e.g. "3C2*" (""=all)'
        value = self.__field( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'field': value},{'field': self.__schema['field']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('field',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __spw_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__spw_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'select data by spectral window IDs, e.g. "3,5,7" (""=all)'
        value = self.__spw( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'spw': value},{'spw': self.__schema['spw']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('spw',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __timerange_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__timerange_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)'
        value = self.__timerange( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'timerange': value},{'timerange': self.__schema['timerange']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('timerange',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __scan_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__scan_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'select data by scan numbers, e.g. "21~23" (""=all)'
        value = self.__scan( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'scan': value},{'scan': self.__schema['scan']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('scan',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __pol_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__pol_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'select data by polarization IDs, e.g. "0,1" (""=all)'
        value = self.__pol( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'pol': value},{'pol': self.__schema['pol']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('pol',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __intent_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__intent_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'select data by observational intent, e.g. "*ON_SOURCE*" (""=all)'
        value = self.__intent( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'intent': value},{'intent': self.__schema['intent']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('intent',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __reindex_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__reindex_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return True
        description = 'Re-index indices in subtables based on data selection'
        value = self.__reindex( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'reindex': value},{'reindex': self.__schema['reindex']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('reindex',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __kernel_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__kernel_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return 'gaussian'
        description = 'spectral smoothing kernel type'
        value = self.__kernel( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'kernel': value},{'kernel': self.__schema['kernel']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('\x1B[1m\x1B[47m%-10.10s =\x1B[0m %s%-23s%s' % ('kernel',pre,self.__to_string_(value),post),description,13+len(pre)+len(post))
    def __kwidth_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__kwidth_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return int(5)
        if self.__kwidth_dflt( self.__globals_( ) ) is not None:
             description = 'smoothing kernel width in channel'
             value = self.__kwidth( self.__globals_( ) )
             (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'kwidth': value},{'kwidth': self.__schema['kwidth']}) else ('\x1B[91m','\x1B[0m')
             self.__do_inp_output('   \x1B[92m%-7.7s =\x1B[0m %s%-23s%s' % ('kwidth',pre,self.__to_string_(value),post),description,9+len(pre)+len(post))
    def __outfile_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__outfile_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'name of output file'
        value = self.__outfile( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'outfile': value},{'outfile': self.__schema['outfile']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('outfile',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __overwrite_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__overwrite_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return False
        description = 'overwrite the output file if already exists [True, False]'
        value = self.__overwrite( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'overwrite': value},{'overwrite': self.__schema['overwrite']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-10.10s = %s%-23s%s' % ('overwrite',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))

    #--------- global default implementation-------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def set_global_defaults(self):
        self.set_global_defaults.state['last'] = self
        glb = self.__globals_( )
        if 'antenna' in glb: del glb['antenna']
        if 'kwidth' in glb: del glb['kwidth']
        if 'infile' in glb: del glb['infile']
        if 'kernel' in glb: del glb['kernel']
        if 'outfile' in glb: del glb['outfile']
        if 'field' in glb: del glb['field']
        if 'datacolumn' in glb: del glb['datacolumn']
        if 'intent' in glb: del glb['intent']
        if 'scan' in glb: del glb['scan']
        if 'reindex' in glb: del glb['reindex']
        if 'overwrite' in glb: del glb['overwrite']
        if 'pol' in glb: del glb['pol']
        if 'spw' in glb: del glb['spw']
        if 'timerange' in glb: del glb['timerange']


    #--------- inp function -----------------------------------------------------------
    def inp(self):
        print("# sdsmooth -- %s" % self._info_desc_)
        self.term_width, self.term_height = shutil.get_terminal_size(fallback=(80, 24))
        self.__infile_inp( )
        self.__datacolumn_inp( )
        self.__antenna_inp( )
        self.__field_inp( )
        self.__spw_inp( )
        self.__timerange_inp( )
        self.__scan_inp( )
        self.__pol_inp( )
        self.__intent_inp( )
        self.__reindex_inp( )
        self.__kernel_inp( )
        self.__kwidth_inp( )
        self.__outfile_inp( )
        self.__overwrite_inp( )

    #--------- tget function ----------------------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def tget(self,savefile=None):
        from casashell.private.stack_manip import find_frame
        from runpy import run_path
        filename = savefile
        if filename is None:
            filename = "sdsmooth.last" if os.path.isfile("sdsmooth.last") else "sdsmooth.saved"
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

        _postfile = outfile if outfile is not None else os.path.realpath('sdsmooth.last')

        _invocation_parameters = OrderedDict( )
        _invocation_parameters['infile'] = self.__infile( self.__globals_( ) )
        _invocation_parameters['datacolumn'] = self.__datacolumn( self.__globals_( ) )
        _invocation_parameters['antenna'] = self.__antenna( self.__globals_( ) )
        _invocation_parameters['field'] = self.__field( self.__globals_( ) )
        _invocation_parameters['spw'] = self.__spw( self.__globals_( ) )
        _invocation_parameters['timerange'] = self.__timerange( self.__globals_( ) )
        _invocation_parameters['scan'] = self.__scan( self.__globals_( ) )
        _invocation_parameters['pol'] = self.__pol( self.__globals_( ) )
        _invocation_parameters['intent'] = self.__intent( self.__globals_( ) )
        _invocation_parameters['reindex'] = self.__reindex( self.__globals_( ) )
        _invocation_parameters['kernel'] = self.__kernel( self.__globals_( ) )
        _invocation_parameters['kwidth'] = self.__kwidth( self.__globals_( ) )
        _invocation_parameters['outfile'] = self.__outfile( self.__globals_( ) )
        _invocation_parameters['overwrite'] = self.__overwrite( self.__globals_( ) )

        try:
            with open(_postfile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-10s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#sdsmooth( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: return False
        return True

    def __call__( self, infile=None, datacolumn=None, antenna=None, field=None, spw=None, timerange=None, scan=None, pol=None, intent=None, reindex=None, kernel=None, kwidth=None, outfile=None, overwrite=None ):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s
        _prefile = os.path.realpath('sdsmooth.pre')
        _postfile = os.path.realpath('sdsmooth.last')
        _return_result_ = None
        _arguments = [infile,datacolumn,antenna,field,spw,timerange,scan,pol,intent,reindex,kernel,kwidth,outfile,overwrite]
        _invocation_parameters = OrderedDict( )
        if any(map(lambda x: x is not None,_arguments)):
            # invoke python style
            # set the non sub-parameters that are not None
            local_global = { }
            if infile is not None: local_global['infile'] = infile
            if datacolumn is not None: local_global['datacolumn'] = datacolumn
            if antenna is not None: local_global['antenna'] = antenna
            if field is not None: local_global['field'] = field
            if spw is not None: local_global['spw'] = spw
            if timerange is not None: local_global['timerange'] = timerange
            if scan is not None: local_global['scan'] = scan
            if pol is not None: local_global['pol'] = pol
            if intent is not None: local_global['intent'] = intent
            if reindex is not None: local_global['reindex'] = reindex
            if kernel is not None: local_global['kernel'] = kernel
            if outfile is not None: local_global['outfile'] = outfile
            if overwrite is not None: local_global['overwrite'] = overwrite

            # the invocation parameters for the non-subparameters can now be set - this picks up those defaults
            _invocation_parameters['infile'] = self.__infile( local_global )
            _invocation_parameters['datacolumn'] = self.__datacolumn( local_global )
            _invocation_parameters['antenna'] = self.__antenna( local_global )
            _invocation_parameters['field'] = self.__field( local_global )
            _invocation_parameters['spw'] = self.__spw( local_global )
            _invocation_parameters['timerange'] = self.__timerange( local_global )
            _invocation_parameters['scan'] = self.__scan( local_global )
            _invocation_parameters['pol'] = self.__pol( local_global )
            _invocation_parameters['intent'] = self.__intent( local_global )
            _invocation_parameters['reindex'] = self.__reindex( local_global )
            _invocation_parameters['kernel'] = self.__kernel( local_global )
            _invocation_parameters['outfile'] = self.__outfile( local_global )
            _invocation_parameters['overwrite'] = self.__overwrite( local_global )

            # the sub-parameters can then be set. Use the supplied value if not None, else the function, which gets the appropriate default
            _invocation_parameters['kwidth'] = self.__kwidth( _invocation_parameters ) if kwidth is None else kwidth

        else:
            # invoke with inp/go semantics
            _invocation_parameters['infile'] = self.__infile( self.__globals_( ) )
            _invocation_parameters['datacolumn'] = self.__datacolumn( self.__globals_( ) )
            _invocation_parameters['antenna'] = self.__antenna( self.__globals_( ) )
            _invocation_parameters['field'] = self.__field( self.__globals_( ) )
            _invocation_parameters['spw'] = self.__spw( self.__globals_( ) )
            _invocation_parameters['timerange'] = self.__timerange( self.__globals_( ) )
            _invocation_parameters['scan'] = self.__scan( self.__globals_( ) )
            _invocation_parameters['pol'] = self.__pol( self.__globals_( ) )
            _invocation_parameters['intent'] = self.__intent( self.__globals_( ) )
            _invocation_parameters['reindex'] = self.__reindex( self.__globals_( ) )
            _invocation_parameters['kernel'] = self.__kernel( self.__globals_( ) )
            _invocation_parameters['kwidth'] = self.__kwidth( self.__globals_( ) )
            _invocation_parameters['outfile'] = self.__outfile( self.__globals_( ) )
            _invocation_parameters['overwrite'] = self.__overwrite( self.__globals_( ) )
        try:
            with open(_prefile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-10s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#sdsmooth( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: pass
        try:
            _return_result_ = _sdsmooth_t( _invocation_parameters['infile'],_invocation_parameters['datacolumn'],_invocation_parameters['antenna'],_invocation_parameters['field'],_invocation_parameters['spw'],_invocation_parameters['timerange'],_invocation_parameters['scan'],_invocation_parameters['pol'],_invocation_parameters['intent'],_invocation_parameters['reindex'],_invocation_parameters['kernel'],_invocation_parameters['kwidth'],_invocation_parameters['outfile'],_invocation_parameters['overwrite'] )
        except Exception as e:
            from traceback import format_exc
            from casatasks import casalog
            casalog.origin('sdsmooth')
            casalog.post("Exception Reported: Error in sdsmooth: %s" % str(e),'SEVERE')
            casalog.post(format_exc( ))
            _return_result_ = False
        try:
            os.rename(_prefile,_postfile)
        except: pass
        return _return_result_

sdsmooth = _sdsmooth( )

