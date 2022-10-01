from pemap import items as items_
from pemap import value as value_

from collections import defaultdict


class BaseBlock():
    '''Wraps collection of Item objects and associate them with value.'''
    def __init__(self, items, _type=object) -> None:
        self._items = items
        self._type = _type

    def _to_items(self, _items_like):
        # Returns item objects from iterator of objects.
        # Item objects will be returned unchanged.
        # Non item objects will  result in item objects.
        return  [items_.Item.to_item(_item) for _item in _items_like]

    def copy_items(self):
        # Copies current items of block
        return [self._item.copy() for _item in self._items]

    def get_items(self):
        # Returns items stored in block object
        return self._items
    
    def get_objects(self, value_sort=False):
        '''Gets items underlying objects'''
        return self.extract_objects_from_items(self._items)

    @classmethod
    def extract_objects_from_items(cls, items):
        '''Gets underlying object from item object'''
        return [_item.get_value() for _item in items]

    @classmethod
    def sort_items_by_value(cls, items):
        '''Returns items sorted by their values'''
        return sorted(items, key=lambda _item: _item.get_value())

    def filter_items(self, key=None, limit=None):
        '''Filters item objects filtered by key function'''
        filtered_items = list(filter(key, self._items))
        if limit != None:
            filtered_items = filtered_items[:limit]
        return filtered_items


    def to_tuple(self):
        '''Returns tuple form of block with values and objects'''
        # Value will be used as tuple key and object as value.
        # object is the object under reference object of items
        results = []
        for _item in self._items:
            results.append((_item.get_value(), _item.get_object()))
        return tuple(results)

    def to_dict(self):
        '''Returns dict form of block with values and objects'''
        # This will fail if value not hashable.
        return dict(self.to_tuple())

    def _to_multi_dict(self):
        # Returns multi dict from items values and underlying objects
        # Key is value and values are underlying objects.
        result_dict = defaultdict(set)
        for _value, _object in self.to_tuple():
            result_dict[_value].add(_object)
        return result_dict

    def to_multi_dict(self):
        '''Returns multi dict from items values and underlying objects.
        Key is value and values are underlying objects.'''
        return self._to_multi_dict()

    def __iter__(self):
        return iter(self.get_sorted_items())

    def __len__(self):
        return len(self._items)


class Block(BaseBlock):
    '''Wraps collection of Item objects and associate them with value.
    
    Instances of this class first copies each item before performing
    any operation on them. Value for item can influence value
    for block instance if value for block is not provided.
    
    When `strict` is True, block instance will not allow item containing
    another block. This is by default set to True to avoid confusion
    but can be set to True to allow nested block instances.'''
    # Default value when value not provided.
    _default_value = items_.Item.get_default_value()

    def __init__(self, items, _type=object, strict=True):
        '''
        items: Iterator
            Collection of Item objects
        value: Any
            Any object can sorted or support comparison operators.   
            It needs to be compatible with items values unless 
            `update_values` is False.
        _type: Type
            Type of items this block expectes, default: object
        strict: Bool
            Prevents block from containing items containing other blocks.
        value_mode: Str
            Mode for calculating value for block and items, default:
            'median'.
        update_values: Bool
            Enables and disables updating of block and items values.
        '''
        super().__init__(items, _type)
        self._items = items
        self._type = _type
        self._strict = strict
        # Setup items after value have been set from existing items.
        # The method may modify values for items.
        # Value is passed as argument since value argument may
        # have been modified.
        # This are results of calling methods within initialiser.
        self._setup_items(items)
        # Calling method within initializer is hell.
        # The instance is not yet fully created.
        # Warning has been included on the methods called by __init__().

    def _setup_items(self, items):
        # Setup items to ensure they are in correct type.
        # Item objects will be created when neccessary.
        # This could make find bugs hard but it simplifies things.
        # This method is not meant to be overiden(take care)
        new_items = []
        for _item in items:
            new_item = items_.Item.to_item(_item)
            # Gets object underlying item.
            _object = new_item.get_object()
            # Check if strict is respected(Block objects not allowed).
            # Exception is raised if not respected.
            if self._strict and isinstance(_object, Block):
                err_msg = "Nested Block objects not allowed when " +\
                    "'strict' is enabled"
                raise TypeError(err_msg)
            # Check if type for object is correct.
            # Exception is if type of object does not match expected one.
            if not isinstance(_object, self._type):
                err_msg = "Item should have reference of type '{}' not '{}'"
                type_name = _object.__class__.__name__
                err_msg = err_msg.format(self._type.__name__, type_name)
                raise TypeError(err_msg)
            # Appends new item to items list
            new_items.append(new_item)
        self._items = new_items
        #self._items_dict = dict(self._to_multi_dict())

    def get_values(self):
        '''Gets values of block item objects'''
        return [_item.get_value() for _item in self._items]

    def get_items_by_value(self, value):
        '''Gets item objects matching value'''
        def func(_item):
            return _item.get_value() == value
        return self.filter_items(func)

    def get_item_by_value(self, value):
        '''Gets first item matching value'''
        items = self.get_items_by_value(value)
        if items: return items[0]

    def get_items_by_values(self, values):
        '''Gets item objects matching any of values'''
        def func(_item):
            return _item.get_value() in values
        return self.filter_items(func)

    def get_item_by_values(self, values):
        '''Gets first item matching any of values'''
        items = self.get_items_by_values(values)
        if items: return items[0]

    def get_items_by_type(self, _type):
        '''Gets item objects of provided type'''
        # Type is defined as type of object underlying item.
        def func(_item):
            return isinstance(_item.get_value(), _type)
        return self.filter_items(func)   

    def get_item_by_type(self, _type):
        '''Gets first item of provided type'''
        items = self.get_items_by_type(_type)
        if items: return items[0] 


class DeepBlock(Block):
    ''' Varient of Block that allows extracting of deep/low-level items.

    This block class differs from its parent in that it eliminates
    nested block instances by extracting their items and then removing
    any item that contain block instances.
    
    At end of day, items with block instances are removed while retaining
    their items. This class gurantees that its items wont have any block
    object. That makes it easy to access items that were deep into nested
    block objects.
    
    `strict` is now set to False as this block type is based on nested 
    block objects. One should now not fear to nest block objects together
    within item objects that will be used on another block object.
    
    values for block and items will be updated accordinly as similar
    to its parent class.'''
    def __init__(self, items, _type=object, strict=False):
        super().__init__(items, _type, strict)
    
    @classmethod
    def _extract_deep_items(cls, _block):
        # Extracts low level(deep) items from block object.
        # This include item objects not containing block object.
        # This method is called by _setup_items().
        # Take care when extensing it on sub classes.
        deep_items = []
        # Gets item objects of block(not sorted by value)
        items = _block.get_items()
        for _item in items: 
            # Gets value for item.
            _object = _item.get_value() 
            # Checks if object of reference is block object.
            # Uses recursion if the object is block object.
            # Recursion continues until non block item is found.
            if isinstance(_object, Block):
                # Extract non block items from the block object.
                block_deep_items = cls._extract_deep_items(_object)
                deep_items.extend(block_deep_items)
            else:
                # This item does not contain block object
                deep_items.append(_item)
        return deep_items

    def _setup_items(self, items,):
        # Setup deep items overiding existing item objects.
        # Ensures all items are really item objects.
        # _extract_deep_items() expectes item objects.
        self._items = self._to_items(self._items)
        _items = self._extract_deep_items(self)
        # Now asks super class to setup items as usual.
        # Items values will be updated as expected.
        super()._setup_items(_items)


if __name__ == "__main__":
    from pemap import reference

    item_object = items_.Item(reference.Reference("Ruth"), "b")
    item_object2 = items_.Item("Marry", "a")
    item_object3 = items_.Item("John", "c")

    items = [item_object, item_object2, item_object3]

    block_object = Block(items)
    block_item = items_.Item(block_object, "we")
    deep_object = DeepBlock([block_item])

    print("block value: ", block_object.get_values())
    print("deep_block value: ", deep_object.get_values())