from . import hsl


def get_proof(type, data):
    if type == "hsl":
        return hsl.get_proof(data)
    raise Exception(f"Unrecognized proof type '{type}'")