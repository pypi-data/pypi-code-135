##################### generated by xml-casa (v2) from listsdm.xml ###################
##################### b97c8caa49b03fa97c3ecc3acb949cc7 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_listsdm import listsdm as _listsdm_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

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

    def __call__( self, sdm='' ):
        schema = {'sdm': {'type': 'cReqPath', 'coerce': _coerce.expand_path}}
        doc = {'sdm': sdm}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'listsdm', [ 'sdm=' + repr(_pc.document['sdm']) ] )
        task_result = None
        try:
            task_result = _listsdm_t( _pc.document['sdm'] )
        except Exception as exc:
            _except_log('listsdm', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'listsdm', task_result )
        return task_result

listsdm = _listsdm( )

