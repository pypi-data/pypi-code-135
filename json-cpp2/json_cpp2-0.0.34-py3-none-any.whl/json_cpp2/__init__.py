#add imports here

from . import core

class _Json_member:
    def __init__(self, json_class, member_name):
        self.member_name = member_name
        setattr(json_class, member_name, property( fget = self._get_, fset = self._set_))

    def _set_( self, o, value):
        if type(value) is bool:
            o.set_bool_member(self.member_name, value)
        elif type(value) is int:
            o.set_int_member(self.member_name, value)
        elif type(value) is float:
            o.set_float_member(self.member_name, value)
        else:
            raise "type not supported"

    def _get_( self, o ):
        t = o.get_member_type(self.member_name)
        if t == "bool":
            return o.get_bool_member(self.member_name)
        elif t == "int":
            return o.get_int_member(self.member_name)
        elif t == "float":
            return o.get_float_member(self.member_name)
        else:
            raise "type not supported"


class JsonObject(core.JsonObject):
    def __init__(self):
        core.JsonObject.__init__(self)
        v = vars(self).copy()
        if hasattr(self.__class__, "_getsets_"):
            _getsets_=getattr(self.__class__, "_getsets_")
        else:
            _getsets_ = dict()
        for k in v:
            if k[0] == "_":
                continue
            if not k in _getsets_:
                _getsets_[k] = _Json_member( self.__class__, k )
            _getsets_[k]._set_(self, v[k])
        setattr(self.__class__, "_getsets_" , _getsets_)
