from ns.application_layer.entities.types import TypeData


PRIMITIVE_TYPES = {
    'str': 'string',
    'int': 'number',
    'float': 'number',
    'Symbol': 'Symbol',
    'bool': 'boolean',
    'list': 'Array',
    'dict': 'Object',
    'Image': 'Image',
}


class JSTranslator:
    def translate_type_name(self, type_data: TypeData) -> str:
        if type_data.is_entity:
            type_name = type_data.name
        else:
            type_name = PRIMITIVE_TYPES[type_data.name]
        if type_data.is_generic:
            generic_names = []
            for generic_type in type_data.generic_args:
                generic_type_name = self.translate_type_name(generic_type)
                generic_names.append(generic_type_name)
            type_name += f'<{", ".join(generic_names)}>'
        return type_name


