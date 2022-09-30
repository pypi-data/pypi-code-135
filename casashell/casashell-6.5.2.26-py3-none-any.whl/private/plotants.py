##################### generated by xml-casa (v2) from plotants.xml ##################
##################### fc14f5bf3c97ff3c18b5ed95c5ba15e6 ##############################
from __future__ import absolute_import
from casashell.private.stack_manip import find_local as __sf__
from casashell.private.stack_manip import find_frame as _find_frame
from casatools.typecheck import validator as _pc
from casatools.coercetype import coerce as _coerce
from casatasks import plotants as _plotants_t
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

class _plotants:
    """
    plotants ---- Plot the antenna distribution in the local reference frame:

    
    The location of the antennas in the MS will be plotted with
    X-toward local east; Y-toward local north.
    

    --------- parameter descriptions ---------------------------------------------

    vis            Name of input visibility file (MS)
    figfile        Save the plotted figure to this file
    antindex       Label antennas with name and antenna ID
    logpos         Whether to plot logarithmic positions
    exclude        Antenna name/id selection to exclude from plot
    checkbaselines Whether to check baselines in the main table.
    title          Title for the plot
    showgui        Show plot on gui.
    [1;42mRETURNS[1;m           void

    --------- examples -----------------------------------------------------------

    
    Plot the antenna distribution in the local reference frame:
    
    The location of the antennas in the MS will be plotted with
    X-toward local east; Y-toward local north. The name of each
    antenna is shown next to its respective location.
    
    Keyword arguments:
    vis -- Name of input visibility file (required)
    Default: none, example: vis='ngc5921.ms'
    
    figfile -- Save the plotted figure in this file
    Default: '', example: figfile='antplot.png'
    
    antindex -- Label antennas with id in addition to name
    Default: False, example: antindex=True
    
    logpos -- Produce a logarithmic position plot
    Default: False, example: logpos=True
    
    exclude -- Antenna selection string to exclude from plotting
    Note: integers are treated as names first then as index
    Default: '', examples: "DV23,DA02" "1,5,7" "0~3"
    
    checkbaselines -- Only plot antennas in the MAIN table
    This can be useful after a split.  WARNING: Setting
    checkbaselines to True will add to runtime in
    proportion to the number of rows in the dataset.
    Default: False, example: checkbaselines=True
    
    title -- Title written along top of plot
    Default: '', example: "ALMA Antenna Positions"
    showgui -- Whether or not to display the plotting GUI
    Default: True; example showgui=False
    
    You can zoom in by pressing the magnifier button (bottom,
    third from right) and making a rectangular region with
    the mouse.  Press the home button (leftmost button) to
    remove zoom.
    
    A hard-copy of this plot can be obtained by pressing the
    button on the right at the bottom of the display. A file
    dialog will allow you to choose the directory, filename,
    and format of the export.
    


    """

    _info_group_ = """visualization, calibration"""
    _info_desc_ = """Plot the antenna distribution in the local reference frame:"""

    __schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'figfile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'antindex': {'type': 'cBool'}, 'logpos': {'type': 'cBool'}, 'exclude': {'type': 'cStr', 'coerce': _coerce.to_str}, 'checkbaselines': {'type': 'cBool'}, 'title': {'type': 'cStr', 'coerce': _coerce.to_str}, 'showgui': {'type': 'cBool'}}

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
        prefix_width = 23 + 14 + 4
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

    def __checkbaselines_dflt( self, glb ):
        return False

    def __checkbaselines( self, glb ):
        if 'checkbaselines' in glb: return glb['checkbaselines']
        return False

    def __exclude_dflt( self, glb ):
        return ''

    def __exclude( self, glb ):
        if 'exclude' in glb: return glb['exclude']
        return ''

    def __vis_dflt( self, glb ):
        return ''

    def __vis( self, glb ):
        if 'vis' in glb: return glb['vis']
        return ''

    def __antindex_dflt( self, glb ):
        return False

    def __antindex( self, glb ):
        if 'antindex' in glb: return glb['antindex']
        return False

    def __figfile_dflt( self, glb ):
        return ''

    def __figfile( self, glb ):
        if 'figfile' in glb: return glb['figfile']
        return ''

    def __logpos_dflt( self, glb ):
        return False

    def __logpos( self, glb ):
        if 'logpos' in glb: return glb['logpos']
        return False

    def __showgui_dflt( self, glb ):
        return True

    def __showgui( self, glb ):
        if 'showgui' in glb: return glb['showgui']
        return True

    def __title_dflt( self, glb ):
        return ''

    def __title( self, glb ):
        if 'title' in glb: return glb['title']
        return ''



    #--------- return inp/go default --------------------------------------------------


    #--------- return subparam values -------------------------------------------------


    #--------- subparam inp output ----------------------------------------------------
    def __vis_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__vis_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Name of input visibility file (MS)'
        value = self.__vis( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'vis': value},{'vis': self.__schema['vis']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('vis',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __figfile_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__figfile_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Save the plotted figure to this file'
        value = self.__figfile( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'figfile': value},{'figfile': self.__schema['figfile']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('figfile',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __antindex_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__antindex_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return False
        description = 'Label antennas with name and antenna ID'
        value = self.__antindex( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'antindex': value},{'antindex': self.__schema['antindex']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('antindex',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __logpos_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__logpos_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return False
        description = 'Whether to plot logarithmic positions'
        value = self.__logpos( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'logpos': value},{'logpos': self.__schema['logpos']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('logpos',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __exclude_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__exclude_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Antenna name/id selection to exclude from plot'
        value = self.__exclude( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'exclude': value},{'exclude': self.__schema['exclude']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('exclude',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __checkbaselines_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__checkbaselines_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return False
        description = 'Whether to check baselines in the main table.'
        value = self.__checkbaselines( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'checkbaselines': value},{'checkbaselines': self.__schema['checkbaselines']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('checkbaselines',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __title_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__title_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return ''
        description = 'Title for the plot'
        value = self.__title( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'title': value},{'title': self.__schema['title']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('title',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))
    def __showgui_inp(self):
        def xml_default( ):
            ## play the crazy subparameter shell game
            dflt = self.__showgui_dflt( self.__globals_( ) )
            if dflt is not None: return dflt
            return True
        description = 'Show plot on gui.'
        value = self.__showgui( self.__globals_( ) )
        (pre,post) = (('','') if value == xml_default( ) else ('\x1B[34m','\x1B[0m')) if self.__validate_({'showgui': value},{'showgui': self.__schema['showgui']}) else ('\x1B[91m','\x1B[0m')
        self.__do_inp_output('%-14.14s = %s%-23s%s' % ('showgui',pre,self.__to_string_(value),post),description,0+len(pre)+len(post))

    #--------- global default implementation-------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def set_global_defaults(self):
        self.set_global_defaults.state['last'] = self
        glb = self.__globals_( )
        if 'showgui' in glb: del glb['showgui']
        if 'logpos' in glb: del glb['logpos']
        if 'vis' in glb: del glb['vis']
        if 'figfile' in glb: del glb['figfile']
        if 'antindex' in glb: del glb['antindex']
        if 'exclude' in glb: del glb['exclude']
        if 'title' in glb: del glb['title']
        if 'checkbaselines' in glb: del glb['checkbaselines']


    #--------- inp function -----------------------------------------------------------
    def inp(self):
        print("# plotants -- %s" % self._info_desc_)
        self.term_width, self.term_height = shutil.get_terminal_size(fallback=(80, 24))
        self.__vis_inp( )
        self.__figfile_inp( )
        self.__antindex_inp( )
        self.__logpos_inp( )
        self.__exclude_inp( )
        self.__checkbaselines_inp( )
        self.__title_inp( )
        self.__showgui_inp( )

    #--------- tget function ----------------------------------------------------------
    @static_var('state', __sf__('casa_inp_go_state'))
    def tget(self,savefile=None):
        from casashell.private.stack_manip import find_frame
        from runpy import run_path
        filename = savefile
        if filename is None:
            filename = "plotants.last" if os.path.isfile("plotants.last") else "plotants.saved"
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

        _postfile = outfile if outfile is not None else os.path.realpath('plotants.last')

        _invocation_parameters = OrderedDict( )
        _invocation_parameters['vis'] = self.__vis( self.__globals_( ) )
        _invocation_parameters['figfile'] = self.__figfile( self.__globals_( ) )
        _invocation_parameters['antindex'] = self.__antindex( self.__globals_( ) )
        _invocation_parameters['logpos'] = self.__logpos( self.__globals_( ) )
        _invocation_parameters['exclude'] = self.__exclude( self.__globals_( ) )
        _invocation_parameters['checkbaselines'] = self.__checkbaselines( self.__globals_( ) )
        _invocation_parameters['title'] = self.__title( self.__globals_( ) )
        _invocation_parameters['showgui'] = self.__showgui( self.__globals_( ) )

        try:
            with open(_postfile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-14s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#plotants( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: return False
        return True

    def __call__( self, vis=None, figfile=None, antindex=None, logpos=None, exclude=None, checkbaselines=None, title=None, showgui=None ):
        def noobj(s):
           if s.startswith('<') and s.endswith('>'):
               return "None"
           else:
               return s
        _prefile = os.path.realpath('plotants.pre')
        _postfile = os.path.realpath('plotants.last')
        _return_result_ = None
        _arguments = [vis,figfile,antindex,logpos,exclude,checkbaselines,title,showgui]
        _invocation_parameters = OrderedDict( )
        if any(map(lambda x: x is not None,_arguments)):
            # invoke python style
            # set the non sub-parameters that are not None
            local_global = { }
            if vis is not None: local_global['vis'] = vis
            if figfile is not None: local_global['figfile'] = figfile
            if antindex is not None: local_global['antindex'] = antindex
            if logpos is not None: local_global['logpos'] = logpos
            if exclude is not None: local_global['exclude'] = exclude
            if checkbaselines is not None: local_global['checkbaselines'] = checkbaselines
            if title is not None: local_global['title'] = title
            if showgui is not None: local_global['showgui'] = showgui

            # the invocation parameters for the non-subparameters can now be set - this picks up those defaults
            _invocation_parameters['vis'] = self.__vis( local_global )
            _invocation_parameters['figfile'] = self.__figfile( local_global )
            _invocation_parameters['antindex'] = self.__antindex( local_global )
            _invocation_parameters['logpos'] = self.__logpos( local_global )
            _invocation_parameters['exclude'] = self.__exclude( local_global )
            _invocation_parameters['checkbaselines'] = self.__checkbaselines( local_global )
            _invocation_parameters['title'] = self.__title( local_global )
            _invocation_parameters['showgui'] = self.__showgui( local_global )

            # the sub-parameters can then be set. Use the supplied value if not None, else the function, which gets the appropriate default
            

        else:
            # invoke with inp/go semantics
            _invocation_parameters['vis'] = self.__vis( self.__globals_( ) )
            _invocation_parameters['figfile'] = self.__figfile( self.__globals_( ) )
            _invocation_parameters['antindex'] = self.__antindex( self.__globals_( ) )
            _invocation_parameters['logpos'] = self.__logpos( self.__globals_( ) )
            _invocation_parameters['exclude'] = self.__exclude( self.__globals_( ) )
            _invocation_parameters['checkbaselines'] = self.__checkbaselines( self.__globals_( ) )
            _invocation_parameters['title'] = self.__title( self.__globals_( ) )
            _invocation_parameters['showgui'] = self.__showgui( self.__globals_( ) )
        try:
            with open(_prefile,'w') as _f:
                for _i in _invocation_parameters:
                    _f.write("%-14s = %s\n" % (_i,noobj(repr(_invocation_parameters[_i]))))
                _f.write("#plotants( ")
                count = 0
                for _i in _invocation_parameters:
                    _f.write("%s=%s" % (_i,noobj(repr(_invocation_parameters[_i]))))
                    count += 1
                    if count < len(_invocation_parameters): _f.write(",")
                _f.write(" )\n")
        except: pass
        try:
            _return_result_ = _plotants_t( _invocation_parameters['vis'],_invocation_parameters['figfile'],_invocation_parameters['antindex'],_invocation_parameters['logpos'],_invocation_parameters['exclude'],_invocation_parameters['checkbaselines'],_invocation_parameters['title'],_invocation_parameters['showgui'] )
        except Exception as e:
            from traceback import format_exc
            from casatasks import casalog
            casalog.origin('plotants')
            casalog.post("Exception Reported: Error in plotants: %s" % str(e),'SEVERE')
            casalog.post(format_exc( ))
            _return_result_ = False
        try:
            os.rename(_prefile,_postfile)
        except: pass
        return _return_result_

plotants = _plotants( )

