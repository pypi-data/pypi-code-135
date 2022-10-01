from pemap import reference as reference_
from pemap import value as value_


class BaseItem():
    '''Associates reference object with any python object/value.
    
    Instances of this class store a reference containing object 
    and associate it with value. If non reference object
    is passed as reference, reference object will be created form it.
    
    Value defines value of reference over other references. Value can
    be anything or any python object.
    
    Remember that this class internally creates reference object if 
    reference argument is not Reference object.'''
    # _value_attrs = (object attr, object method)
    # Used for getting value from object.
    _value_attrs = ("value", "get_value") 
    _default_value_attrs = ("value", "get_value") 
    # Value class/type to use.
    _value_type = value_.Value

    def __init__(self, reference, value=_value_type.get_default_value(), 
    _type=object,  strict=False):
        '''
        reference: Reference
            Instance of Reference type or any python object.
        Value: Any
            Any object to be associated with item.  
        _type: Type
            Type of reference item expectes, default: object.
        strict: Bool
            Forces `reference` argumnet to be strictly Reference instance.
        '''
        self._type = _type
        self._strict = strict
        self._type = _type
        # Calling method within initializer can cause problems.
        # This should be avoided as possible to avoid hard issues.
        # __init__() should be for initialising data not method calls.
        self._setup_reference(reference)
        # Shouldnt super().__init__() be first call of __init__()?
        # Thats because super().__init__() calls another method which
        # is overided by this class(begining of problems).
        self._setup_value(value)

    @classmethod
    def get_value_attr(cls):
        return cls._value_attrs[0]

    @classmethod
    def get_value_method(cls):
        return cls._value_attrs[1]

    @classmethod
    def get_default_value(cls):
        return cls._value_type.get_default_value()

    def _setup_value(self, value):
        # Setup value for item.
        # This method is not meant to be overiden(take care)
        if value == self.get_default_value():
            # Sets up variables to be used to hget value
            _object = self.get_object()
            value_attr = self.get_value_attr()
            value_method = self.get_value_method()
            # Attempt to get value from object.
            if hasattr(_object, value_attr):
                value = getattr(_object, value_attr)
            elif hasattr(_object, value_method):
                value = getattr(_object, value_method)()
            else:
                err_msg = "Cannot get {0} from object of type " +\
                    "'{1}', please provide {0} or define " +\
                    "'{2}()' or '{3}' attributes."
                # Set string format variables
                type_name = _object.__class__.__name__
                value_name = self._value_type.get_name()
                # Format string with those variables.
                err_msg = err_msg.format(value_name, type_name, value_method, 
                value_attr)
                raise AttributeError(err_msg)
        # Now set value attribute using Value type.
        if self.get_default_value() == value:
            type_name = _object.__class__.__name__
            value_name = self._value_type.get_name()
            err_msg = "Item {} cannot of type '{}'"
        self._value = self._value_type(value)

    def _setup_reference(self, reference):
        # Creates reference object when neccessay
        # This method is not meant to be overiden(take care)
        if self._strict and not isinstance(reference, reference_.Reference):
                err_msg = "Reference needs to be instance of '{}' not " +\
                    "'{}' when 'strict' is enabled"
                err_msg = err_msg.format(
                    reference.Reference.__name__,
                    reference.__class__.__name__
                )
                raise TypeError(err_msg)
        else:
            self._reference = reference_.Reference.to_reference(reference)
            if not isinstance(reference, self._type):
                err_msg = "object should be instance of {}, not {}"
                raise TypeError(err_msg.format(reference, self._type))

    @classmethod
    def to_item(cls, _object):
        # Creates item object from if not already item object
        if isinstance(_object, Item):
            _item = _object
        else:
            _item = cls(_object)
        return _item

    def set_value(self, value):
        # Sets value/object behind item.
        return self._value_type(value)
    
    def get_value(self, *args, **kwargs):
        # Gets value behind this item.
        return self._value.get_value(*args, **kwargs)

    def get_reference(self):
        '''Gets underling reference object'''
        return self._reference

    def get_type(self):
        '''Gets type of underlying reference'''
        return self._reference.get_type()

    def get_object(self):
        '''Gets object of underlying reference'''
        return self._reference.get_object()

    def copy(self):
        '''Creates a copy of item'''
        return self.__class__(self._reference, self._value, self._type, 
        self._strict)


class Item(BaseItem):    
    def __init__(self, reference, value=..., *args, **kwargs):
        super().__init__(reference, value, *args, **kwargs) 


if __name__ == "__main__":
    item = Item(10, lambda :34)
    item2 = Item(item)
    item3 = Item(item2)
    print(item.get_object())
    print(item3.get_value())