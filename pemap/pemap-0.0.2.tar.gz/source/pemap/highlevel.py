from pemap import block
from pemap import items
from pemap import value


__all__ = [
    "create_item",
    "create_block",
    "create_deep_block",
    "create_mapping",

    "items_to_tuple",
    "items_to_dict",

    "flatten_items",
    "extract_objects",
    "sort_items_by_value",

    "find_items_by_values",
    "find_item_by_values",

    "find_items_by_type",
    "find_item_by_type",
]

# Default value to use when value not provided.
default_value = value.Value.get_default_value()

def create_item(_object, value=default_value, **kwargs):
    '''Creates item object containing object and its value.

    _reference: Reference
        Instance of Reference type or any python object.
    value: Any
        Any object can sorted or support comparison operators.   
    _type: Type
        Type of reference item expectes, default: object.
    strict: Bool
        Forces `_reference` argumnet to be strictly Reference instance.
    '''
    return items.Item(_object, value, **kwargs)

def create_block(items, **kwargs):
    '''Creates block object with value from items.

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
    
    If items contains block object consider using `create_deep_block()`
    as it will extract the items of that block. Continue using this
    function if thats what you want.'''
    return block.Block(items, **kwargs)

def create_deep_block(items, **kwargs):
    '''Creates deep block object from items. 

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
    
    Deep block is neccessay when items can contain block object
    which may contain other items. This function results in block object
    that contain other items extracted. Any nested block objects within
    items get removed while retaining non block items.
    
    This is different from `create_block()` as it keeps items containing
    block object. That makes it harder to access deep or low-level items
    within the nested block objects.

    Note that extracted deep/low-level items are only copies of original.
    Block object first copies items before performing anything on them.
    Getting items throuh `.get_items()` will only return the copies.
    '''
    return block.DeepBlock(items, **kwargs)


def create_mapping(items, flatten=False, **kwargs):
    '''Creates corresponding block object based on 'flatten' argument.

    items: Iterator
        Collection of Item objects
    flatten: Bool
        Enables and disables use `create_block()` or `create_deep_block()`.
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

    When 'flatten' is True, `create_deep_block()` will be used to create 
    block object else `create_block()`. Set 'flatten' argument to 
    True to remove any nested block objects and replace them with their 
    items.
    '''
    if flatten:
        return create_deep_block(items, **kwargs)
    else:
        return create_block(items, **kwargs)


######################################################################
# Functions defined after here internally creates block object.
# It may be better to manually create block object for performance.
# These functions are meant to give functional programming flavour.
# Manually creating block object could result in few more advantages.
######################################################################

def items_to_tuple(items, flatten=False):
    '''Convert items into map like tuple'''
    block_object = create_mapping(items, flatten=flatten, strict=False)
    return block_object.to_tuple()

def items_to_dict(items, flatten=False):
    '''Convert items into multi dict'''
    block_object = create_mapping(items, flatten=flatten, strict=False)
    return block_object.to_dict()



def flatten_items(items):
    '''Flattens items by exposing items within nested block objects.
    
    This function removes any block object within items while retaining
    items. The number of resulting items may be larger than items 
    provided on argumnets. This is because this function exposes items
    that were nested deep within block objects.
    
    This function does not affect nested items but items containing
    block. Nested items is something out of scope of this library but block
    and items can be nested.

    Block can contain items containing other blocks and items can contain
    block objects. But items containg other items is something that wasnt
    planned for this library.
    '''
    block_object = create_deep_block(items)
    return block_object.get_items()

def sort_items_by_value(items):
    '''Sorts items based on their values'''
    block_object = create_block(items, strict=False)
    return block_object.get_sorted_items()

def extract_objects(items, flatten=False):
    '''Extracts objects within items'''
    #return [_item.get_object() for _item in items]
    block_object = create_mapping(items, flatten=flatten, strict=False)
    return block_object.get_objects()



def find_items_by_values(items, values, flatten=False):
    '''Finds items with values matching any of values'''
    block_object = create_mapping(items, flatten=flatten, strict=False)
    return block_object.get_items_by_values(values)

def find_item_by_values(items, values, flatten=False):
    '''Finds item with value matching any of values'''
    block_object = create_mapping(items, flatten=flatten, strict=False)
    return block_object.get_item_by_values(values)



def find_items_by_type(items, _type, flatten=False):
    '''Finds items with type matching provided type'''
    block_object = create_mapping(items, flatten=flatten, strict=False)
    return block_object.get_items_by_type(_type)

def find_item_by_type(items, _type, flatten=False):
    '''Finds item with type matching provided type'''
    block_object = create_mapping(items, flatten=flatten, strict=False)
    return block_object.get_item_by_type(_type)
