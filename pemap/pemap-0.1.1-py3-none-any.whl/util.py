

def rename_attribute(object_, old_attr_name, new_attr_name):
    # Renames attribute by replacing it with new name.
    setattr(object_, new_attr_name, getattr(object_, old_attr_name))
    delattr(object_, old_attr_name)

def copy_attribute(object_, old_attr_name, new_attr_name):
    # Creates copy of attribute with new name.
    setattr(object_, new_attr_name, getattr(object_, old_attr_name))

