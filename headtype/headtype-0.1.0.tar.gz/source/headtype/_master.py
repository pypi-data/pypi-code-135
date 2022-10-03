from headtype._types import Type
from headtype._types import Types


class Master():
    '''Finds types matching object'''
    def __init__(self, object_, types_):
        self._types = types_
        self._object = object_
        # Ensures self.items_ is always Items instance.
        if not isinstance(types_, Types):
            self._types = Types(types_)
    
    def get_types(self):
        return self._types

    def get_object(self):
        return self._object

    def match_exists(self):
        # Checks if there was a match(returns type on match)
        type_ = self.get_matching_type()
        if type_: return type_
        else: return False

    def _type_matched(self, type_):
        # Checks if type is matched by object.
        return type_.is_supported(self._object)

    def _get_types_filtered(self):
        # Gets types but in their filtered form.
        object_type = type(self._object)
        return self._types.filter_by_object_types([object_type])

    def get_matching_types(self, limit=None):
        # Gets types matching object
        types = self._get_types_filtered()
        if limit != None:
            types = types[:limit]
        return filter(self._type_matched, types)

    def get_matching_type(self):
        # Gets first types matching object.
        for type_ in self.get_matching_types():
            return type_


if __name__ == "__main__":
    # Creates type instances to use with master
    type1 = Type(list, lambda obj: isinstance(obj, str))
    type2 = Type(set, lambda obj: isinstance(obj, int))

    # Creates types from the defined type instances.
    types_list = [type1, type2]
    types = Types(types_list)

    master = Master(400, types_list, True)

    print(list(master.get_matching_types()))