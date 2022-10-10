def get_stix_type_from_id(stix_id: str) -> str:
    return stix_id.split('--', maxsplit=1)[0]
