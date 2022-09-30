##################### generated by xml-casa (v2) from delmod.xml ####################
##################### 2f0bbe58ff0653115c12b5dc327582ae ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_delmod import delmod as _delmod_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _delmod:
    """
    delmod ---- Deletes model representations in the MS

    
    This utility task is to be used to delete the model visibility data
    representations in the MS.

    --------- parameter descriptions ---------------------------------------------

    vis     Name of input visibility file (MS)
    otf     Delete the on-the-fly model data keywords
            Default=True
            
            The 'otf' representation is the 'scratch-less'
            model data, stored as keywords in the MS header
            containing model data formation instructions.  It
            is generated by the setjy, ft, and tclean tasks
            (usescratch=False), and if present, overrides the
            MODEL_DATA column (if present). If a user wishes
            to use the MODEL_DATA column _after_ having
            operated with the 'otf' representation, this task
            can be used to delete the 'otf' represenatation
            to make the MODEL_DATA column visible.  (Create
            the MODEL_DATA column by using usescratch=True in
            setjy, ft, or clean; or by running the clearcal
            task with addmodel=True.)
    field   Select field using field id(s) or field name(s)
            Subparameter of otf
            Default: '' (all fields' models will be deleted)
    scr     Delete the MODEL_DATA scr col (if it exists)
            Default: False
            
            Note: it is not possible to delete the MODEL_DATA
            column per field.
            
            If otf=F and scr=F, delmod will provide a listing
            of the header field records.
    [1;42mRETURNS[1;m    void

    --------- examples -----------------------------------------------------------

    
    
    
    For more information, see the task pages of delmod in CASA Docs:
    
    https://casa.nrao.edu/casadocs/
    
    


    """

    _info_group_ = """imaging, calibration"""
    _info_desc_ = """Deletes model representations in the MS"""

    def __call__( self, vis='', otf=True, field='', scr=False ):
        schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'otf': {'type': 'cBool'}, 'field': {'type': 'cStr', 'coerce': _coerce.to_str}, 'scr': {'type': 'cBool'}}
        doc = {'vis': vis, 'otf': otf, 'field': field, 'scr': scr}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'delmod', [ 'vis=' + repr(_pc.document['vis']), 'otf=' + repr(_pc.document['otf']), 'field=' + repr(_pc.document['field']), 'scr=' + repr(_pc.document['scr']) ] )
        task_result = None
        try:
            task_result = _delmod_t( _pc.document['vis'], _pc.document['otf'], _pc.document['field'], _pc.document['scr'] )
        except Exception as exc:
            _except_log('delmod', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'delmod', task_result )
        return task_result

delmod = _delmod( )

