##################### generated by xml-casa (v2) from fixplanets.xml ################
##################### 9e77d5f648d8c3e845548de6053a7d00 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_fixplanets import fixplanets as _fixplanets_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _fixplanets:
    """
    fixplanets ---- Changes FIELD and SOURCE table entries based on user-provided direction or POINTING table, optionally fixes the UVW coordinates

    
    This task's main purpose is to correct observations which were
    performed with correct pointing and correlation but for which
    incorrect direction information was entered in the FIELD and SOURCE
    table of the MS. If you actually want to change the phase center of
    the visibilties in an MS, you should use task fixvis.

    --------- parameter descriptions ---------------------------------------------

    vis       Name of input visibility file
              Default: none
              
                 Example: vis='ngc5921.ms'
    field     Select field using field id(s) or field name(s)
              Default: '' (all fields)
              
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
    fixuvw    Recalculate Fourier-plane u,v,w coordinates?
              Default: False
              Options: False|True
    direction If set, do not use pointing table but set direction to
              this value
              Default: '' (use pointing table)
              
                 Example: 'J2000 19h30m00 -40d00m00'
              
              The direction can either be given explicitly or
              as the path to a JPL Horizons
              ephemeris. Alternatively, the ephemeris table can
              also be provided as mime format file. For more
              information, see the task pages of fixplanets in
              CASA Docs (https://casa.nrao.edu/casadocs/).
    refant    Reference antenna name(s); a prioritized list may be
              specified
              Default: 0 (antenna ID 0)
              
                 Examples: 
                 refant='4' (antenna with index 4)
                 refant='VA04' (VLA antenna #4)
                 refant='EA02,EA23,EA13' (EVLA antenna EA02,
                 use EA23 and EA13 as alternates if/when EA02
                 drops out)
              
              Use taskname=listobs for antenna listing
    reftime   If using pointing table information, use it from this
              timestamp
              Default: 'first'
              
                 Examples: 
                 * 'median' will use the median timestamp for
                   the given field using only the unflagged
                   maintable rows
                 * '2012/07/11/08:41:32' will use the given
                   timestamp (must be within the observaton
                   time)

    --------- examples -----------------------------------------------------------

    
    
    For more information, see the task pages of fixplanets in CASA Docs:
    
    https://casa.nrao.edu/casadocs/


    """

    _info_group_ = """manipulation, calibration"""
    _info_desc_ = """Changes FIELD and SOURCE table entries based on user-provided direction or POINTING table, optionally fixes the UVW coordinates"""

    def __call__( self, vis='', field=[ ], fixuvw=False, direction='', refant=int(0), reftime='first' ):
        schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'field': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'fixuvw': {'type': 'cBool'}, 'direction': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'refant': {'type': 'cVariant', 'coerce': [_coerce.to_variant]}, 'reftime': {'type': 'cStr', 'coerce': _coerce.to_str}}
        doc = {'vis': vis, 'field': field, 'fixuvw': fixuvw, 'direction': direction, 'refant': refant, 'reftime': reftime}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'fixplanets', [ 'vis=' + repr(_pc.document['vis']), 'field=' + repr(_pc.document['field']), 'fixuvw=' + repr(_pc.document['fixuvw']), 'direction=' + repr(_pc.document['direction']), 'refant=' + repr(_pc.document['refant']), 'reftime=' + repr(_pc.document['reftime']) ] )
        task_result = None
        try:
            task_result = _fixplanets_t( _pc.document['vis'], _pc.document['field'], _pc.document['fixuvw'], _pc.document['direction'], _pc.document['refant'], _pc.document['reftime'] )
        except Exception as exc:
            _except_log('fixplanets', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'fixplanets', task_result )
        return task_result

fixplanets = _fixplanets( )

