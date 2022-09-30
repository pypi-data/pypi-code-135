##################### generated by xml-casa (v2) from asdmsummary.xml ###############
##################### f80868a97288f171678257692e450452 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_asdmsummary import asdmsummary as _asdmsummary_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _asdmsummary:
    """
    asdmsummary ---- Summarized description of an ASDM dataset.

    
    Given an ASDM directory, this task will print, to the CASA log,
    information about the content of the dataset contained in that
    directory (down to the level of a subscan).

    --------- parameter descriptions ---------------------------------------------

    asdm    Name of input ASDM directory
            The asdmsummary task prints a description of the
            content of an SDM dataset to the CASA logger.
            
               Example:
               asdm='10C-119_sb3070258_1.55628.42186299768'
    [1;42mRETURNS[1;m    void

    --------- examples -----------------------------------------------------------

    
    For more information, see the task pages of asdmsummary in CASA Docs:
    
    https://casa.nrao.edu/casadocs/
    


    """

    _info_group_ = """information"""
    _info_desc_ = """Summarized description of an ASDM dataset."""

    def __call__( self, asdm='' ):
        schema = {'asdm': {'type': 'cReqPath', 'coerce': _coerce.expand_path}}
        doc = {'asdm': asdm}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'asdmsummary', [ 'asdm=' + repr(_pc.document['asdm']) ] )
        task_result = None
        try:
            task_result = _asdmsummary_t( _pc.document['asdm'] )
        except Exception as exc:
            _except_log('asdmsummary', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'asdmsummary', task_result )
        return task_result

asdmsummary = _asdmsummary( )

