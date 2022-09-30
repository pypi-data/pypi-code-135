##################### generated by xml-casa (v2) from synthesismaskhandler.xml ######
##################### d2a7cf4f5c511ddd8d3eef3eaff0e84d ##############################
from __future__ import absolute_import 
from .__casac__ import synthesismaskhandler as _synthesismaskhandler

from .platform import str_encode as _str_ec
from .platform import str_decode as _str_dc
from .platform import dict_encode as _dict_ec
from .platform import dict_decode as _dict_dc
from .platform import dict_encode as _quant_ec
from .platform import dict_decode as _quant_dc
from .platform import encode as _any_ec
from .platform import decode as _any_dc
from .errors import create_error_string
from .typecheck import CasaValidator as _validator
_pc = _validator( )
from .coercetype import coerce as _coerce


class synthesismaskhandler:
    _info_group_ = """synthesismaskhandler"""
    _info_desc_ = """tool for mask handling in sysnthesis imaging """
    ### self
    def __init__(self, *args, **kwargs):
        """This is used to construct {tt synthesismaskhandler} tool.
        """
        self._swigobj = kwargs.get('swig_object',None)
        if self._swigobj is None:
            self._swigobj = _synthesismaskhandler()

    def pruneregions(self, inmaskname='', prunesize=float(0.0), chanflag=[  ], outmaskname=''):
        """
        """
        return _dict_dc(self._swigobj.pruneregions(_str_ec(inmaskname), prunesize, chanflag, _str_ec(outmaskname)))

    def done(self):
        """
        """
        return self._swigobj.done()

