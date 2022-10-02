from pemap import reference

    
class Value(reference.Reference):
    '''Defines value to be used with item'''
    # Used for error messages and others.
    _name = "value"
    # Default value when value is not provided.
    # This is taken as if value is not provided(careful).
    # Think of it as None with arguments of function.
    _default_value = ...

    # _value_attr_names = (object attr, object method)
    # Used for getting value for object.
    _default_value_attr_names = ("value", "get_value") 
    _value_attr_names = _default_value_attr_names

    def __init__(self, value) -> None:
        super().__init__(value)

    @classmethod
    def get_name(cls):
        return cls._name

    @classmethod
    def get_default_value(cls):
        return cls._default_value

    @classmethod
    def get_value_attr_names_names(cls):
        return cls._value_attr_names

    @classmethod
    def get_value_attr_name(cls):
        return cls._value_attr_names[0]

    @classmethod
    def get_value_method_name(cls):
        return cls._value_attr_names[1]

    def get_value(self, *args, **kwargs):
        # Gets value behind this object.
        # Object of method or function will result in return value
        # of that callable.
        if self.is_method_func():
            return self._object(*args, **kwargs)
        elif isinstance(self._object, Value):
            return self._object.get_value()
        else:
            return self._object

    def set_value(self, value):
        self._object = value


