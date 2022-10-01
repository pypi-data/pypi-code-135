from pemap import reference


class Value(reference.Reference):
    '''Defines value to be used with item'''
    # Used for error messages
    _name = "value"
    # Default value when value is not provided.
    _default_value = ...

    def __init__(self, value) -> None:
        super().__init__(value)

    @classmethod
    def get_name(cls):
        return cls._name

    @classmethod
    def get_default_value(cls):
        return cls._default_value

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
