"""
Validate a dictionary against a schema
"""
from flatten_dictionary import FlattenDictionary

FLATTEN_DICTIONARY = FlattenDictionary()

TYPES = {
    "string": str,
    "boolean": bool,
    "float": float,
    "list": list,
    "integer": int,
}


def validate_json(schema: dict, json_object: dict) -> dict:
    """
    params:
        1. schema -> dictionary used to campare json_object against
        2. json_object -> dictionary
    """
    if type(schema) is not dict or type(json_object) is not dict:
        invalid_types = [type(schema), type(json_object)]
        return {
            "valid": False,
            "error": (
                f"invalid type {str(invalid_types)} as arguments"
                f" instead of [<class 'dict'>, <class 'dict'>]"
            ),
        }

    flattened_schema = FLATTEN_DICTIONARY.flatten_dictionary(dictionary=schema)
    flattened_json_obj = FLATTEN_DICTIONARY.flatten_dictionary(dictionary=json_object)

    # schema validation
    for key, value in flattened_schema.items():
        if type(value) != list or len(value) == 0 or len(value) > 2:
            return {
                "valid": False,
                "error": (
                    f"invalid format for key {key}: "
                    f"values in schema should use format: key: ['required', 'type'] "
                    f"or key: ['type'] only eg {key}: ['required', 'string']"
                ),
            }

        value = [item.lower() for item in value]
        types_supported = [key for key in TYPES.keys()]
        if "required" in value and len(value) != 2 or not TYPES.get(value[1], False):
            return {
                "valid": False,
                "error": (
                    f"{key} is a required key but type is missing or invalid"
                    f"\n please use any of the supported types: {str(types_supported)}"
                    f"\n eg {key}: ['required', 'string']"
                ),
            }

    if len(flattened_json_obj) != len(flattened_schema):
        keys = [
            key
            for key in flattened_schema.keys()
            if key not in flattened_json_obj.keys()
        ]

        if len(keys):
            return {
                "valid": False,
                "error": f"key(s) : {str(keys)} missing in json_object",
            }
        else:
            keys = [
                key
                for key in flattened_json_obj.keys()
                if key not in flattened_schema.keys()
            ]

        return {
            "valid": False,
            "error": (
                f"json_object has the following extra key(s)"
                f" that are not in the schema: {str(keys)}"
            ),
        }

    # key value validation for json_object
    required_keys = []
    key_types_errored_fields = []
    for key, value in flattened_schema.items():
        json_obj_value = flattened_json_obj.get(key, False)
        value = [item.lower() for item in value]

        if "required" in value and not flattened_json_obj:
            required_keys.append(key)

        if (
            json_obj_value
            and len(value) > 1
            and value[1]
            and type(json_obj_value) != TYPES.get(value[1], False)
        ):
            key_types_errored_fields.append(key)

    error_messages = []
    if len(required_keys):
        error_messages.append(
            f"required key(s) : {str(required_keys)} are missing values"
        )
    if len(key_types_errored_fields):
        error_messages.append(
            f"The following value(s) received wrong"
            f" data type: {str(key_types_errored_fields)}"
        )
    if len(error_messages):
        return {
            "valid": False,
            "error": f"{str(error_messages)}",
        }

    return {
        "valid": True,
        "error": "",
    }
