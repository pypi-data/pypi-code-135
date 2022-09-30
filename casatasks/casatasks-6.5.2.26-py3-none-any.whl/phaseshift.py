##################### generated by xml-casa (v2) from phaseshift.xml ################
##################### 790188cc655c2a2e1e60d0786440bfaa ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_phaseshift import phaseshift as _phaseshift_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _phaseshift:
    """
    phaseshift ---- Rotate a Measurement Set to a new phase-center

    
    This application changes the phase center of a selected subset of an input MS, by taking into
    account the full 3D geometry in the UVW plane (similar to the phasecenter setting in the
    imaging tasks). This function produces an output MS with modified UVW values, visibility
    phases, and a new phase_direction entry in the FIELD sub-table.
    

    --------- parameter descriptions ---------------------------------------------

    vis         Name of input visibility file
                Default: none, must be specified
                
                   Example: vis='ngc5921.ms'
    outputvis   Name of output visibility file
                Default: None, must be specified
                
                   Example: outputvis='ngc5921_out.ms'
    keepmms     Create a Multi-MS as the output if the input is a
                Multi-MS.
                
                Default: True
                Options: True|False
                
                By default it will create a Multi-MS when the
                input is a Multi-MS. The output Multi-MS will
                have the same partition axis of the input
                MMS. See CASA Docs for more information on
                the MMS format.
    field       Select field using field id(s) or field name(s)
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
                   field = '3,4C\*'; field id 3, all names
                   starting with 4C
    spw         Select spectral window/channels
                          Default: ''=all spectral windows and channels
                
                             Examples:
                             spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                             spw='<2';  spectral windows less than 2 (i.e. 0,1)
                             spw='0:5~61'; spw 0, channels 5 to 61
                             spw='0,10,3:3~45'; spw 0,10 all channels, spw
                             3 - chans 3 to 45.
                             spw='0~2:2~6'; spw 0,1,2 with channels 2
                             through 6 in each.
                             spw = '\*:3~64'  channels 3 through 64 for all sp id's
                             spw = ' :3~64' will NOT work.
    scan        Scan number range
                Default: '' = all
    intent      Select observing intent
                Default: '' (no selection by intent)
                
                   Example: intent='*BANDPASS*'  (selects data
                   labelled with BANDPASS intent)
    array       (Sub)array number range
                Default: '' (all)
    observation Select by observation ID(s)
                Default: '' = all
                
                    Example: observation='0~2,4'
    datacolumn  Which data column(s) to process
                (case-insensitive).
                Default: 'all' (= whichever of the options that
                are present)
                Options: 'data', 'model', 'corrected',
                'all','float_data', 'lag_data',
                'float_data,data', 'lag_data,data'
                
                   Example: datacolumn='data'
    phasecenter Direction coordinates of new phase center, specified as absolute
                                    world coordinates including frame, eg 
                
                               phasecenter = 'J2000 19h53m50 40d06m00'
                               phasecenter = 'B1950 292.5deg -40.0deg'
                               phasecenter = 'ICRS 13:05:27.2780 -049.28.04.458'
                               phasecenter = 'GALACTIC 47.5rad -60.22rad'
                
                           Time dependent systems (eg, AZEL) are not supported, nor are ephemeris objects.
                   	
                   		This will change the phase of the baseline visibilities so that the 
                   		final image is centered at the new location. Additionally the uvw 
                   		coordinates and the the PHASE_DIR column from the FIELD sub-table 
                   		will be changed accordingly. 
                   	
                   		This operation will be done for all selected fields, so all fields in the output
                           MS will have as center the new location. The new phase center is not constrained to
                           be located inside any images to be created.

    --------- examples -----------------------------------------------------------

    


    """

    _info_group_ = """manipulation"""
    _info_desc_ = """Rotate a Measurement Set to a new phase-center"""

    def __call__( self, vis='', outputvis='', keepmms=True, field='', spw='', scan='', intent='', array='', observation='', datacolumn='all', phasecenter='' ):
        schema = {'vis': {'type': 'cReqPath', 'coerce': _coerce.expand_path}, 'outputvis': {'type': 'cStr', 'coerce': _coerce.to_str}, 'keepmms': {'type': 'cBool'}, 'field': {'type': 'cStr', 'coerce': _coerce.to_str}, 'spw': {'type': 'cStr', 'coerce': _coerce.to_str}, 'scan': {'type': 'cStr', 'coerce': _coerce.to_str}, 'intent': {'type': 'cStr', 'coerce': _coerce.to_str}, 'array': {'type': 'cStr', 'coerce': _coerce.to_str}, 'observation': {'type': 'cStr', 'coerce': _coerce.to_str}, 'datacolumn': {'type': 'cStr', 'coerce': _coerce.to_str, 'allowed': [ 'DATA', 'model', 'corrected', 'LAG_DATA', 'lag_data', 'FLOAT_DATA,DATA', 'FLOAT_DATA', 'CORRECTED', 'lag_data,data', 'float_data', 'float_data,data', 'DATA,MODEL,CORRECTED', 'ALL', 'MODEL', 'all', 'data,model,corrected', 'LAG_DATA,DATA', 'data' ]}, 'phasecenter': {'type': 'cStr', 'coerce': _coerce.to_str}}
        doc = {'vis': vis, 'outputvis': outputvis, 'keepmms': keepmms, 'field': field, 'spw': spw, 'scan': scan, 'intent': intent, 'array': array, 'observation': observation, 'datacolumn': datacolumn, 'phasecenter': phasecenter}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'phaseshift', [ 'vis=' + repr(_pc.document['vis']), 'outputvis=' + repr(_pc.document['outputvis']), 'keepmms=' + repr(_pc.document['keepmms']), 'field=' + repr(_pc.document['field']), 'spw=' + repr(_pc.document['spw']), 'scan=' + repr(_pc.document['scan']), 'intent=' + repr(_pc.document['intent']), 'array=' + repr(_pc.document['array']), 'observation=' + repr(_pc.document['observation']), 'datacolumn=' + repr(_pc.document['datacolumn']), 'phasecenter=' + repr(_pc.document['phasecenter']) ] )
        task_result = None
        try:
            task_result = _phaseshift_t( _pc.document['vis'], _pc.document['outputvis'], _pc.document['keepmms'], _pc.document['field'], _pc.document['spw'], _pc.document['scan'], _pc.document['intent'], _pc.document['array'], _pc.document['observation'], _pc.document['datacolumn'], _pc.document['phasecenter'] )
        except Exception as exc:
            _except_log('phaseshift', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'phaseshift', task_result )
        return task_result

phaseshift = _phaseshift( )

