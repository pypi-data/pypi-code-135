import yaml

def command_parser(file:str) -> dict[str, str]:
    """A helper function that parses YAML file to a dictionary

    Structure of YAML:
    commands:
        1:
            name: Test command
            description: Test description
            command: /test
            action: Hi jordan
        2:
            name: Test command
            description: Test description
            command: /test1
            action: Hi jordan1

    Args:
        file (str): YAML file with the above syntax

    Returns:
        dict[str, str]: Parsed dictionary
    """
    
    with open(file, 'r') as f:
        data = yaml.safe_load(f)
    
    parsed = {}

    for val in data['commands'].values():
        cmd = val.get('command')
        action = val.get('action')
        parsed[cmd] = action

    return parsed