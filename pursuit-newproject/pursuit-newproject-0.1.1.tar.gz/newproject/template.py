from typing import Dict

from jinja2 import Template


def template_string(template: str, variables: Dict) -> str:
    template_obj = Template(template)
    return template_obj.render(**variables)


def template_file(path: str, variables: Dict):
    with open(path, "r") as source_file:
        source = source_file.read()
    result = template_string(source, variables)
    with open(path, "w") as dest_file:
        dest_file.write(result)
