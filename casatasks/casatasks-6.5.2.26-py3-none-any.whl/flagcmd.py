##################### generated by xml-casa (v2) from flagcmd.xml ###################
##################### b8a2611ec7c82cf7a20bc5e22bf736d2 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_flagcmd import flagcmd as _flagcmd_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _flagcmd:
    """
    flagcmd ---- Flagging task based on batches of flag-commands

    
    The flagcmd task will flag the visibility data or calibration
    table based on several batch-operations using flag commands.
    
    Flag commands follow the mode and parameter names from the
    flagdata task.
    
    The flagcmd task will flag data based on the commands input on
    inpmode:
    table = input from FLAG_CMD table in MS
    list  = input from text file or list of strings from inpfile
    xml   = input from Flag.xml in the MS given by vis
    
    Batch operations include : apply/unapply/list/plot/clear/extract
    
    IMPORTANT: If you use other ways to flag such as interactive
    flagging in plotms, the FLAG_CMD will NOT be updated!
    
    NOTE on flagging calibration tables.
    -----------------------------------
    We recommend using the flagdata task for flagging cal tabels. When
    using flagcmd to flag cal tables, only the 'apply' and 'list'
    actions are supported. Because cal tables do not have a FLAG_CMD
    sub-table, the default inpmode='table' can only be used if an MS
    is given in the 'inpfile' parameter so that flags from the MS are
    applied to the cal table. Otherwise, the flag commands must be
    given using inpmode='list', either from a file(s) or from a list
    of strings. Data selection for calibration tables is limited to
    field, scan, antenna, time, spw and observation.
    
    

    --------- parameter descriptions ---------------------------------------------

    vis        Name of input visibility file or calibration table.
               default: '' (none) 
               
                  example: vis='uid___A002_X2a5c2f_X54.ms'
    inpmode    Input mode for flag commands(table/list/xml)
               options: 'table','list','xml'
               default: 'table' (the input commands from
               FLAG_CMD table of the MS)
               
               inpmode='xml' inputs online flags from Flag.xml
               file in the MS. This mode has become largely
               obsolete with the deprecation of the importevla
               task (see the flagcmd task pages in CASA Docs for
               more information). This mode will not work for
               ALMA MS or cal tables.
               
               NOTE: You can only apply the flags from a list or
               xml; you will not be able to unapply
               them. Transfer the flag commands to the FLAG_CMD
               table if you want to unapply the flags (see
               'inpfile' description below).
    inpfile    Source of flag commands. Subparameter of
               inpmode='table/list'.
               Path to MS containing FLAG_CMD (table), or name
               of an ASCII file, list of files or a list of
               Python strings to apply to MS or cal table
               (list). 
               options: [] with flag commands or [] with
               filenames or '' with a filename. (String values
               must contain quotes around them or the parser
               will not work.)
               default: '' (read from FLAG_CMD table in the MS
               specified via 'vis')
               
               Main use is to read flags from internal FLAG_CMD,
               but one use case is to read the flag commands
               from an MS given in inpfile and apply them to
               another MS or cal table given in vis.
    tablerows  List of rows of the FLAG_CMD table to read. Subparameter
               of inpmode='table/list'.
               default: [] (read all rows)
               
                  example: [0,1,2,10]
               
               NOTE: currently only takes integer lists, not
               parseable strings with ranges.  Use the Python
               range function to generate ranges, e.g. tablerows
               = range(0,30) + range(50,55) instead of
               '0~29,50~54' for now.
    reason     Select flag commands based on REASON(s). Subparameter of
               inpmode.
               default: 'any' (all flags regardless of reason)
               
                  Examples: 
                  reason='FOCUS_ERROR'
                  reason=['FOCUS_ERROR','SUBREFLECTOR_ERROR']
               
               If inpfile is a list of files, the reasons given
               in this parameter will apply to all the files.
               
               NOTE: what is within the string is literally
               matched, e.g. reason='' matches only blank
               reasons, and reason
               ='FOCUS_ERROR,SUBREFLECTOR_ERROR' matches this
               compound reason string only
    useapplied Select commands whose rows have APPLIED column set to
               True. Subparameter of inpmode='table'.
               options: True,False
               default: False   
               
               If useapplied=True it will read in both applied
               and unapplied flags.
               
               IMPORTANT: The APPLIED column is set to True
               after a flag command is applied to the MS. In
               order to re-apply the same flag command, this
               parameter should be set to True.
    tbuff      Time buffer (sec) to pad flags. Subparameter of
               inpmode='xml'.
               default: 0.0
    ants       Allowed flag antenna names to select by. Subparameter of
               inpmode='xml'.
    action     Action to perform in MS and/or in inpfile
                 options: apply/unapply/list/plot/clear/extract
                 default: 'apply'
               
                    Examples:
                    -- action='apply': This operation will apply
                    the commands chosen by inpmode. If
                    inpmode='table' and inpfile='' then the
                    APPLIED column in FLAG_CMD will be set to
                    True.
                    -- action='unapply': unapply flags in MS. (Not
                    available for cal tables). This operation will
                    unapply the commands chosen by inpmode='table'
                    ONLY. After unapplying the commands, the task
                    will update the APPLIED column to False.
                    -- action='list': list and/or save flag
                    commands. This operation will list the
                    commands chosen by inpmode on the screen and
                    save them to the MS or to a file without
                    applying. It will save the commands to outfile
                    if the parameter savepars is set to True. If
                    outfile is None, it will save the commands to
                    the MS given in 'vis'.
                    -- action='plot': plot flags (ant
                    vs. time). (Not available for cal
                    tables). This operation will plot the flags
                    chosen by inpmode to a matplotlib gui or to a
                    file.  These will be sorted by antenna
                    vs. time.  Most useful for showing the online
                    flags.
                    -- action='clear': clear flags from FLAG_CMD
                    in the MS. (Not available for cal tables) This
                    operation will delete the selected flag rows
                    from the internal FLAG_CMD table of the MS.
                    -- action='extract': extract internal flag
                    dictionary. (Not available for cal tables)
                    This option will return the internal flagging
                    dictionary to python. There is no extant
                    description of the format of this dictionary,
                    as it is an internal device used by the
                    flagcmd task. This action is provided for the
                    convenience of advanced users.
               
                WARNING: choosing this action='clear' will
                disregard anything you set in inpmode and will
                always work on the FLAG_CMD table in vis. This can
                be used to totally delete rows from the FLAG_CMD
                table, when setting clearall=True.
    flagbackup Automatically backup the FLAG column before
               execution. Subparameter of action='apply/unapply'.
               options: True,False
               default: True
    clearall   Delete all rows from FLAG_CMD. Subparameter of
               action='clear'.
               default: False (will not clear)
    rowlist    FLAG_CMD rows to clear. Subparameter of action='clear'.
                     default: [] (all flags in table)
               
                        example: [0,1,2,10]
               
                     WARNING: this can be dangerous, and you must set
                     clearall=True  to use this!!! This will delete
                     the specified rows from the internal FLAG_CMD
                     table for vis regardless of what mode is set to
                     (useful for when you import from xml or file),
                     and decide to redo it). This action will NOT
                     unapply the commands.
               
                     NOTE: currently only takes integer lists, not
                     parseable strings with ranges.  Use the Python
                     range function to generate ranges, e.g. rowlist =
                     range(0,30) + range(50,55) instead of
                     '0~29,50~54' for now.
    plotfile   Name of output file to save plot
               default: '' (plot to matplotlib window)
               
               WARNING: will only reliably plot individual flags
               per antenna and timerange (e.g. direct from xml)
    savepars   Save the flag commands to the FLAG_CMD table of the MS or
               to an output text file.
               options: True/False     
               default: False
    outfile    Name of output file to save commands. Subparameter of
               savepars=True.
               default: ' '; it will save the commands in the
               FLAG_CMD table of the MS.
               
                  example: outfile='flags.txt' will save the
                  parameters in a text file.
    overwrite  Overwrite an existing file given in 'outfile' to save the
               flag commands. Subparameter of savepars=True.
               options: True/False
               default: True; it will remove the existing file
               given in 'outfile' and save the current flag
               commands to a new file with the same name. When
               set to False, the task will exit with an error
               message if the file exist.
    [1;42mRETURNS[1;m       void

    --------- examples -----------------------------------------------------------

    
    
    For more information, see the task pages of flagcmd in CASA Docs:
    
    https://casa.nrao.edu/casadocs/


    """

    _info_group_ = """flagging"""
    _info_desc_ = """Flagging task based on batches of flag-commands"""

    def __call__( self, vis='', inpmode='table', inpfile='', tablerows=[  ], reason='any', useapplied=False, tbuff=float(0.0), ants='', action='apply', flagbackup=True, clearall=False, rowlist=[  ], plotfile='', savepars=False, outfile='', overwrite=True ):
        schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'inpmode': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'table', 'list', 'xml' ]}, 'inpfile': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}]}, 'tablerows': {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}, 'reason': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}]}, 'useapplied': {'type': 'cBool'}, 'tbuff': {'type': 'cFloat', 'coerce': _coerce.to_float}, 'ants': {'type': 'cStr', 'coerce': _coerce.to_str}, 'action': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'apply', 'clear', 'plot', 'list', 'extract', 'unapply' ]}, 'flagbackup': {'type': 'cBool'}, 'clearall': {'type': 'cBool'}, 'rowlist': {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}, 'plotfile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'savepars': {'type': 'cBool'}, 'outfile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'overwrite': {'type': 'cBool'}}
        doc = {'vis': vis, 'inpmode': inpmode, 'inpfile': inpfile, 'tablerows': tablerows, 'reason': reason, 'useapplied': useapplied, 'tbuff': tbuff, 'ants': ants, 'action': action, 'flagbackup': flagbackup, 'clearall': clearall, 'rowlist': rowlist, 'plotfile': plotfile, 'savepars': savepars, 'outfile': outfile, 'overwrite': overwrite}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'flagcmd', [ 'vis=' + repr(_pc.document['vis']), 'inpmode=' + repr(_pc.document['inpmode']), 'inpfile=' + repr(_pc.document['inpfile']), 'tablerows=' + repr(_pc.document['tablerows']), 'reason=' + repr(_pc.document['reason']), 'useapplied=' + repr(_pc.document['useapplied']), 'tbuff=' + repr(_pc.document['tbuff']), 'ants=' + repr(_pc.document['ants']), 'action=' + repr(_pc.document['action']), 'flagbackup=' + repr(_pc.document['flagbackup']), 'clearall=' + repr(_pc.document['clearall']), 'rowlist=' + repr(_pc.document['rowlist']), 'plotfile=' + repr(_pc.document['plotfile']), 'savepars=' + repr(_pc.document['savepars']), 'outfile=' + repr(_pc.document['outfile']), 'overwrite=' + repr(_pc.document['overwrite']) ] )
        task_result = None
        try:
            task_result = _flagcmd_t( _pc.document['vis'], _pc.document['inpmode'], _pc.document['inpfile'], _pc.document['tablerows'], _pc.document['reason'], _pc.document['useapplied'], _pc.document['tbuff'], _pc.document['ants'], _pc.document['action'], _pc.document['flagbackup'], _pc.document['clearall'], _pc.document['rowlist'], _pc.document['plotfile'], _pc.document['savepars'], _pc.document['outfile'], _pc.document['overwrite'] )
        except Exception as exc:
            _except_log('flagcmd', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'flagcmd', task_result )
        return task_result

flagcmd = _flagcmd( )

