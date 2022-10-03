from typing import Any, Dict, List, Tuple, Union

from dataclasses import dataclass, field

from .schemas import Template as TemplateSchema


@dataclass
class Template:

    name: str
    path_prefix: str = "{}-{}-{}"
    path_patterns: list[str] = field(default_factory=list)


@dataclass
class Manifest:

    name: str
    template: Template
    args: tuple[str, ...] = field(default_factory=tuple)
    path_patterns: list[str] = field(default_factory=list)


@dataclass
class LocalComparisonResult:

    manifest: Manifest
    local_dir: str
    resolved_paths: list[tuple[str, list[str]]] = field(default_factory=list)
    found: list[str] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)


template_schema = TemplateSchema()


def dict_to_template(data: dict[str, Any]) -> Any:
    loaded = template_schema.load(data)  # validation
    return Template(**loaded)


def alt_dict_to_template(data: dict[str, Any]) -> Template:
    """
    Note
    ----
    alternative template syntax from Ben
    """
    path_patterns = []
    for key, value in data["files"].items():
        filename = value.get("filename")
        directory_name = value.get("directory_name")
        if filename:
            path_patterns.append(filename.lstrip("%"))
        elif directory_name:
            path_patterns.append(directory_name.lstrip("%"))
        else:
            raise Exception("Invalid format for: %s" % value)

    return Template(
        name=data["name"],
        path_prefix="{}-{}-{}",
        path_patterns=path_patterns,
    )


def is_alt_format(data: dict[str, Any]) -> bool:
    return data.get("files") is not None


def dump_Template(template: Template) -> Any:
    return template_schema.dump(template)
