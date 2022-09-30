##################### generated by xml-casa (v2) from slsearch.xml ##################
##################### 0e3591a3f62455e598c37cb372657674 ##############################
from __future__ import absolute_import
import numpy
from casatools.typecheck import CasaValidator as _val_ctor
_pc = _val_ctor( )
from casatools.coercetype import coerce as _coerce
from casatools.errors import create_error_string
from .private.task_slsearch import slsearch as _slsearch_t
from casatasks.private.task_logging import start_log as _start_log
from casatasks.private.task_logging import end_log as _end_log
from casatasks.private.task_logging import except_log as _except_log

class _slsearch:
    """
    slsearch ---- Search a spectral line table.

    --------- parameter descriptions ---------------------------------------------

    tablename  Input spectral line table name to search. If not specified, use the default table in the system.
    outfile    Results table name. Blank means do not write the table to disk.
    freqrange  Frequency range in GHz.
    species    Species to search for.
    reconly    List only NRAO recommended frequencies.
    chemnames  Chemical names to search for.
    qns        Resolved quantum numbers to search for.
    intensity  CDMS/JPL intensity range. -1 -> do not use an intensity range.
    smu2       Quantum mechanical line strength. -1 -> do not use a smu2 range.
    loga       log(A) (Einstein coefficient) range. -1 -> do not use a loga range.
    el         Lower energy state range in Kelvin. -1 -> do not use an el range.
    eu         Upper energy state range in Kelvin. -1 -> do not use an eu range.
    rrlinclude Include RRLs in the result set?
    rrlonly    Include only RRLs in the result set?
    verbose    List result set to logger (and optionally logfile)?
    logfile    List result set to this logfile (only used if verbose=True).
    append     If true, append to logfile if it already exists, if false overwrite logfile it it exists. Only used if verbose=True and logfile not blank.
    [1;42mRETURNS[1;m       bool

    --------- examples -----------------------------------------------------------

    
    
    PARAMETER SUMMARY
    
    tablename      Input spectral line table name to search. If not specified, use the default table in the system.
    outfile        Results table name. Blank means do not write the table to disk.
    freqrange      Frequency range in GHz.
    species        Species to search for.
    reconly        List only NRAO recommended frequencies.
    chemnames      Chemical names to search for.
    qns            Resolved quantum numbers to search for.
    intensity      CDMS/JPL intensity range. -1 -> do not use an intensity range.
    smu2           S*mu*mu range in Debye**2. -1 -> do not use an S*mu*mu range.
    loga           log(A) (Einstein coefficient) range. -1 -> do not use a loga range.
    el             Lower energy state range in Kelvin. -1 -> do not use an el range.
    eu             Upper energy state range in Kelvin. -1 -> do not use an eu range.
    rrlinclude     Include RRLs in the result set?
    rrlonly        Include only RRLs in the result set?
    verbose        List result set to logger (and optionally logfile)?
    logfile        List result set to this logfile (only used if verbose=True).
    append         If true, append to logfile if it already exists, if false overwrite logfile it it exists. Only used if verbose=True and logfile not blank.
    
    Search the specfied spectral line table. The results table can be written to disk by specifying its name in the outfile parameter.
    If outfile is not specified (ie outfile=""), no table is created. Because Splatalogue does not have values for intensity, smu2,
    loga, eu, and el for radio recombination lines (rrls), one must specify to include RRLs in the specified frequency range in the
    output. In this case, RRLs will be included ignoring any filters on intensity, smu2, loga, eu, and el. One can also specify to
    list only RRLs. One can specify to list the search results to the logger via the verbose parameter. If verbose is False, no
    logger output is listed. If verbose=True, one can also specify that the results be listed to a logfile and if this file already
    exists, one can specify that the results be appended to it or to overwrite it with the results.
    
    # put search results in a table but do not list to the logger
    slsearch("myspectrallines.tbl", verbose=False)


    """

    _info_group_ = """information"""
    _info_desc_ = """Search a spectral line table."""

    def __call__( self, tablename='', outfile='', freqrange=[ float(84),float(90) ], species=[  ], reconly=False, chemnames=[  ], qns=[  ], intensity=[ float(-1) ], smu2=[ float(-1) ], loga=[ float(-1) ], el=[ float(-1) ], eu=[ float(-1) ], rrlinclude=True, rrlonly=False, verbose=False, logfile='""', append=False ):
        schema = {'tablename': {'type': 'cPath', 'coerce': _coerce.expand_path}, 'outfile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'freqrange': {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, 'species': {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}, 'reconly': {'type': 'cBool'}, 'chemnames': {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}, 'qns': {'type': 'cStrVec', 'coerce': [_coerce.to_list,_coerce.to_strvec]}, 'intensity': {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, 'smu2': {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, 'loga': {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, 'el': {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, 'eu': {'type': 'cFloatVec', 'coerce': [_coerce.to_list,_coerce.to_floatvec]}, 'rrlinclude': {'type': 'cBool'}, 'rrlonly': {'type': 'cBool'}, 'verbose': {'type': 'cBool'}, 'logfile': {'type': 'cStr', 'coerce': _coerce.to_str}, 'append': {'type': 'cBool'}}
        doc = {'tablename': tablename, 'outfile': outfile, 'freqrange': freqrange, 'species': species, 'reconly': reconly, 'chemnames': chemnames, 'qns': qns, 'intensity': intensity, 'smu2': smu2, 'loga': loga, 'el': el, 'eu': eu, 'rrlinclude': rrlinclude, 'rrlonly': rrlonly, 'verbose': verbose, 'logfile': logfile, 'append': append}
        assert _pc.validate(doc,schema), create_error_string(_pc.errors)
        _logging_state_ = _start_log( 'slsearch', [ 'tablename=' + repr(_pc.document['tablename']), 'outfile=' + repr(_pc.document['outfile']), 'freqrange=' + repr(_pc.document['freqrange']), 'species=' + repr(_pc.document['species']), 'reconly=' + repr(_pc.document['reconly']), 'chemnames=' + repr(_pc.document['chemnames']), 'qns=' + repr(_pc.document['qns']), 'intensity=' + repr(_pc.document['intensity']), 'smu2=' + repr(_pc.document['smu2']), 'loga=' + repr(_pc.document['loga']), 'el=' + repr(_pc.document['el']), 'eu=' + repr(_pc.document['eu']), 'rrlinclude=' + repr(_pc.document['rrlinclude']), 'rrlonly=' + repr(_pc.document['rrlonly']), 'verbose=' + repr(_pc.document['verbose']), 'logfile=' + repr(_pc.document['logfile']), 'append=' + repr(_pc.document['append']) ] )
        task_result = None
        try:
            task_result = _slsearch_t( _pc.document['tablename'], _pc.document['outfile'], _pc.document['freqrange'], _pc.document['species'], _pc.document['reconly'], _pc.document['chemnames'], _pc.document['qns'], _pc.document['intensity'], _pc.document['smu2'], _pc.document['loga'], _pc.document['el'], _pc.document['eu'], _pc.document['rrlinclude'], _pc.document['rrlonly'], _pc.document['verbose'], _pc.document['logfile'], _pc.document['append'] )
        except Exception as exc:
            _except_log('slsearch', exc)
            raise
        finally:
            task_result = _end_log( _logging_state_, 'slsearch', task_result )
        return task_result

slsearch = _slsearch( )

