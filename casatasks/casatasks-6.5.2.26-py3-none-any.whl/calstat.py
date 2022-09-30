##################### generated by xml-casa (v2) from calstat.xml ###################
##################### 7de4c369496e80b365bdc878532eca46 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_calstat import calstat as _calstat_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _calstat:
    """
    calstat ---- Displays statistical information on a calibration table

    
    This task returns statistical information about a column in a
    calibration table. The following values are computed: mean value, sum
    of values, sum of squared values, median, median absolute deviation,
    quartile, minimum, maximum, variance, standard deviation, root mean
    square.

    --------- parameter descriptions ---------------------------------------------

    caltable   Name of input calibration table
               Default: ''
               
                  Example: vis='ggtau.1mm.amp.gcal'
    axis       Which data to analyze.
               Default: 'amplitude'
               Options: 'amp', 'amplitude', 'phase', 'real',
               'imag', 'imaginary'. Also, the name of any real
               valued MS column can be given, e.g. TIME,
               POLY_COEFF_AMP, REF_ANT, ANTENNA1, FLAG, ...
               
               Note: the phase of a complex number is in
               radians in the range [-pi; pi].
    datacolumn Which data column to use if axis is 'amp', 'amplitude', 'phase', 'real', 'imag' or 'imaginary'.
               Default: 'gain'

    --------- examples -----------------------------------------------------------

    
    
    
    For more information, see the task pages of calstat in CASA Docs:
    
    https://casa.nrao.edu/casadocs/


    """

    _info_group_ = """information, calibration"""
    _info_desc_ = """Displays statistical information on a calibration table"""

    def __call__( self, caltable='', axis='amplitude', datacolumn='gain' ):
        schema = {'caltable': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'axis': {'type': 'cStr', 'coerce': _coerce.to_str}, 'datacolumn': {'type': 'cStr', 'coerce': _coerce.to_str}}
        doc = {'caltable': caltable, 'axis': axis, 'datacolumn': datacolumn}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'calstat', [ 'caltable=' + repr(_pc.document['caltable']), 'axis=' + repr(_pc.document['axis']), 'datacolumn=' + repr(_pc.document['datacolumn']) ] )
        task_result = None
        try:
            task_result = _calstat_t( _pc.document['caltable'], _pc.document['axis'], _pc.document['datacolumn'] )
        except Exception as exc:
            _except_log('calstat', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'calstat', task_result )
        return task_result

calstat = _calstat( )

