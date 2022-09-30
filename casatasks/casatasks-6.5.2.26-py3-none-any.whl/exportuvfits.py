##################### generated by xml-casa (v2) from exportuvfits.xml ##############
##################### e9744e7d03285da3e979c183810b8077 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_exportuvfits import exportuvfits as _exportuvfits_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _exportuvfits:
    """
    exportuvfits ---- Convert a CASA visibility data set to a UVFITS file:

    
    This task writes a UVFITS file, a general format data set used to
    transfer data between different software systems. It is written in
    floating point format.  Different programs have different
    restrictions on what forms of UVFITS files they will use, especially
    whether they will accept multiple sources and/or spectral windows in
    the same file.  See the spw, multisource, and combinespw descriptions
    below.
    
    IMPORTANT NOTE: In general, some of the data averaging features of
    this task have never worked properly. In general, users should run
    mstransform to select and average data prior to running
    exportuvfits. The associated input parameters are being slowly
    deprecated and removed.

    --------- parameter descriptions ---------------------------------------------

    vis          Name of input visibility file
                 Default: none
                 
                    Example: vis='ngc5921.ms'
    fitsfile     Name of output UV FITS file
                 Default: none
                 
                    Example: vis='ngc5921XC1.fits'
    datacolumn   Visibility file data column
                 Default: corrected
                 Options: 'data'(raw)|'corrected'|'model'|'weight'
                 
                    Example: datacolumn='model'
    field        Select field using field id(s) or field name(s)
                 Default: '' --> all fields
                 
                 Use 'go listobs' to obtain the list id's or
                 names. If field string is a non-negative integer,
                 it is assumed a field index,  otherwise, it is
                 assumed a field name.
                 
                    Examples:
                    field='0~2'; field ids 0,1,2
                    field='0,4,5~7'; field ids 0,4,5,6,7
                    field='3C286,3C295'; field named 3C286 and
                    3C295
                    field = '3,4C*'; field id 3, all names
                    starting with 4C
    spw          Select spectral window/channels
                 
                 Examples:
                 spw='0~2,4'; spectral windows 0,1,2,4 (all
                 channels)
                 spw='<2';  spectral windows less than 2
                 (i.e. 0,1)
                 spw='0:5~61'; spw 0, channels 5 to 61,
                 INCLUSIVE
                 spw='\*:5~61'; all spw with channels 5 to 61
                 spw='0,10,3:3~45'; spw 0,10 all channels, spw
                 3, channels 3 to 45.
                 spw='0~2:2~6'; spw 0,1,2 with channels 2
                 through 6 in each.
                 spw='0:0~10;15~60'; spectral window 0 with
                 channels 0-10,15-60. (NOTE ';' to separate
                 channel selections)
                 spw='0:0~10^2,1:20~30^5'; spw 0, channels
                 0,2,4,6,8,10, spw 1, channels 20,25,30 
                 type 'help par.selection' for more examples.
    antenna      Select data based on antenna/baseline
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
    timerange    Select data based on time range
                 Subparameter of selectdata=True
                 Default = '' (all)
                 
                    Examples:
                    timerange =
                    'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                    (Note: if YYYY/MM/DD is missing date defaults
                    to first day in data set.)
                    timerange='09:14:0~09:54:0' picks 40 min on
                    first day 
                    timerange= '25:00:00~27:30:00' picks 1 hr to 3
                    hr 30min on NEXT day
                    timerange='09:44:00' pick data within one
                    integration of time
                    timerange='>10:24:00' data after this time
    writesyscal  Write GC and TY tables. Not yet available.
                 Default: False
    multisource  Write in multi-source format? 
                 Default: True
                 
                 Set to False if only one source is selected. 
                 
                 Note: diffmap does not work on multisource uvfits
                 files, so if planning on using diffmap on the
                 resulting uvfits file, select a single source and
                 set multisource = False. Otherwise use True. (If
                 multiple sources are selected, a multi-source
                 file will be written no matter what the setting
                 of this parameter).
    combinespw   Export the spectral windows as IFs?
                 Default: True
                 
                 If True, export the spectral windows as
                 IFs. All spectral windows must have same
                 shape. Otherwise multiple windows will use
                 multiple FREQIDs.
    writestation Write station name instead of antenna name
                 Default: True
    padwithflags Fill in missing data with flags to fit IFs
                 Subparameter of combinespw=True
                 Default: True
                 
                 If True, and combinespw is True, fill in missing
                 data as needed to fit the IF structure. This is
                 appropriate if the MS had a few
                 frequency-dependent flags applied, and was then
                 time-averaged by split, or when exporting for use
                 by difmap. If the spectral windows were observed
                 at different times, padwithflags=True will add a
                 large number of flags, making the output file
                 significantly longer. It does not yet support
                 spectral windows with different widths.
    overwrite    Overwrite output file if it exists?
                 Default: False
                 Options: False|True

    --------- examples -----------------------------------------------------------

    
    
    For more information, see the task pages of exportuvfits in CASA Docs:
    
    https://casa.nrao.edu/casadocs/


    """

    _info_group_ = """import/export"""
    _info_desc_ = """Convert a CASA visibility data set to a UVFITS file:"""

    def __call__( self, vis='', fitsfile='', datacolumn='corrected', field='', spw='', antenna='', timerange='', writesyscal=False, multisource=True, combinespw=True, writestation=True, padwithflags=False, overwrite=False ):
        schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'fitsfile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'datacolumn': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'data', 'corrected', 'model', 'weight' ]}, 'field': {'anyof': [{'type': 'cStr', 'coerce': _coerce.to_str}, {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}, {'type': 'cInt'}, {'type': 'cIntVec', 'coerce': [_coerce.to_list,_coerce.to_intvec]}]}, 'spw': {'type': 'cStr', 'coerce': _coerce.to_str}, 'antenna': {'type': 'cStr', 'coerce': _coerce.to_str}, 'timerange': {'type': 'cStr', 'coerce': _coerce.to_str}, 'writesyscal': {'type': 'cBool'}, 'multisource': {'type': 'cBool'}, 'combinespw': {'type': 'cBool'}, 'writestation': {'type': 'cBool'}, 'padwithflags': {'type': 'cBool'}, 'overwrite': {'type': 'cBool'}}
        doc = {'vis': vis, 'fitsfile': fitsfile, 'datacolumn': datacolumn, 'field': field, 'spw': spw, 'antenna': antenna, 'timerange': timerange, 'writesyscal': writesyscal, 'multisource': multisource, 'combinespw': combinespw, 'writestation': writestation, 'padwithflags': padwithflags, 'overwrite': overwrite}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'exportuvfits', [ 'vis=' + repr(_pc.document['vis']), 'fitsfile=' + repr(_pc.document['fitsfile']), 'datacolumn=' + repr(_pc.document['datacolumn']), 'field=' + repr(_pc.document['field']), 'spw=' + repr(_pc.document['spw']), 'antenna=' + repr(_pc.document['antenna']), 'timerange=' + repr(_pc.document['timerange']), 'writesyscal=' + repr(_pc.document['writesyscal']), 'multisource=' + repr(_pc.document['multisource']), 'combinespw=' + repr(_pc.document['combinespw']), 'writestation=' + repr(_pc.document['writestation']), 'padwithflags=' + repr(_pc.document['padwithflags']), 'overwrite=' + repr(_pc.document['overwrite']) ] )
        task_result = None
        try:
            task_result = _exportuvfits_t( _pc.document['vis'], _pc.document['fitsfile'], _pc.document['datacolumn'], _pc.document['field'], _pc.document['spw'], _pc.document['antenna'], _pc.document['timerange'], _pc.document['writesyscal'], _pc.document['multisource'], _pc.document['combinespw'], _pc.document['writestation'], _pc.document['padwithflags'], _pc.document['overwrite'] )
        except Exception as exc:
            _except_log('exportuvfits', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'exportuvfits', task_result )
        return task_result

exportuvfits = _exportuvfits( )

