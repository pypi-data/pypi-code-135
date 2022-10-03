
class Type():
    '''Contains type/class with associated callback for matching objects'''
    def __init__(self, type_, callback, fast_callaback=None, 
    object_types=[]):
        self._type = type_
        self._callback = callback
        self._fast_callaback = fast_callaback
        self._object_types = object_types

    def get_type(self):
        return self._type

    def get_object_types(self):
        return self._object_types

    def is_fully_supported(self, object_):
        # Checks if object is fully supported by type.
        return self._callback(object_)

    def is_fast_supported(self, object_):
        # Checks if object is is supported but using fast technique.
        if not self._fast_callaback:
            #err_msg = "fast callback is needed to check fast support, " +\
            #    "please provide 'fast_callaback'."
            #raise ValueError(err_msg)
            return False
        return self._fast_callaback(object_)

    def is_supported(self, object_, ):
        # Checks if object is supported by type.
        if self._fast_callaback:
            fast_support = self.is_fast_supported(object_)
            if fast_support: 
                return fast_support
        return self.is_fully_supported(object_)



class Types():
    '''Performs operations on top Type instances'''
    def __init__(self, types) -> None:
        self._types = types

    def get_types(self):
        return self._types

    def get_raw_types(self):
        # Gets underlying types/classes within Type instances.
        return [type_.get_type() for type_ in self._types]

    def get_object_types(self):
        # Gets supported object types from Type instances.
        object_types = []
        for type_ in self._types:
            object_types.extend(type_.get_object_types())
        return object_types

    def get_object_types_map(self):
        # Gets supported object types into map(dict).
        # Key: object_type, Value: Set[Type]
        types_map = {}
        for type_ in self.types_:
            for support_type in type_.get_object_types():
                types_map[support_type] = types_map.get(support_type, set())
                types_map[support_type].add(support_type)
        return types_map

    def filter_by_object_types(self, object_types):
        # Filters types(Types) by supported object types.
        # Types without supported object types wont be filtered out.
        object_types = set(object_types)
        def func(type_): 
            object_types_ = type_.get_object_types()
            if not object_types_: 
                # Those without object types atleast should be allowed.
                return True
            return object_types.intersection(object_types_)
        return list(filter(func, self._types))

    def __len__(self):
        return len(self._types)

    def __iter__(self):
        return iter(self._types)
