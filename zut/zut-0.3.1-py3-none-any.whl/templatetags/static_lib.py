"""
Usage example in Django base template:

    {% load static %}
    {% load static_lib %}
    ...
    <head>
    ...
    {% style_lib  'bootstrap' 'dist/css/bootstrap.min.css' 'sha256-7ZWbZUAi97rkirk4DcEp4GWDPkWpRMcNaEyXGsNXjLg=' %}
    {% script_lib 'bootstrap' 'dist/js/bootstrap.bundle.min.js' 'sha256-wMCQIK229gKxbUg3QWa544ypI4OoFlC2qQl8Q8xD8x8=' %}
    ...
    </head>
"""
import json, re, logging
from django import template
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from django.conf import settings

logger = logging.getLogger(__name__)

register = template.Library()

_package_versions: dict[str,str] = None

def _get_package_version(name: str):
    global _package_versions

    # retrieve package versions from package.json
    if not _package_versions:
        _package_versions = {}
        with open(settings.BASE_DIR.joinpath("package.json"), "r", encoding="utf-8") as fp:
            package_json = json.load(fp)
            _package_versions = package_json["dependencies"]

    # get version of given package
    version = _package_versions.get(name, None)
    if not version:
        logger.error(f"version not found for package {name}")
        return None

    if not re.match(r"^\d+\.\d+\.\d+$", version):
        logger.error(f"invalid version for package {name}: {version}")
        return None
    
    return version


def _get_lib_url(package, file, version=None):
    if not version:
        version = _get_package_version(package)
    LOCAL_STATIC_LIB = getattr(settings, "LOCAL_STATIC_LIB", False)
    if LOCAL_STATIC_LIB:
        return f"{static('lib')}/{package}/{file}"
    else:
        if version:
            return f"https://cdn.jsdelivr.net/npm/{package}@{version}/{file}"
        else:
            return f"https://cdn.jsdelivr.net/npm/{package}/{file}"


@register.simple_tag
def style_lib(package, file, integrity=None, version=None):
    url = _get_lib_url(package, file, version)
    html = f"<link rel=\"stylesheet\" href=\"{url}\""
    if integrity:
        html += f" integrity=\"{integrity}\" crossorigin=\"anonymous\""
    else:
        logger.error(f"missing integrity hash for {url}")
    html += f" />"
    return mark_safe(html)


@register.simple_tag
def script_lib(package, file, integrity=None, version=None):
    url = _get_lib_url(package, file, version)
    html = f"<script defer src=\"{url}\""
    if integrity:
        html += f" integrity=\"{integrity}\" crossorigin=\"anonymous\""
    else:
        logger.error(f"missing integrity hash for {url}")
    html += f"></script>"
    return mark_safe(html)
