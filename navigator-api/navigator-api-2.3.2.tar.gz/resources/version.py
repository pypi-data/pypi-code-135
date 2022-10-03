"""version.

Extract the version of all required packages and showed in a response.
"""
import importlib
from aiohttp import web
from navigator.types import HTTPRequest
from navigator.responses import JSONResponse

package_list = ('asyncdb', 'notify', 'datamodel', 'navconfig', 'navigator', )


async def get_versions(request: HTTPRequest):
    """
    ---
    summary: Return version of all required packages
    tags:
    - version
    produces:
    - application/json
    responses:
        "200":
            description: list of packages and versions.
    """
    versions = {}
    for package in package_list:
        mdl = importlib.import_module(f'{package}.version', package='version')
        obj = getattr(mdl, '__version__')
        versions[package] = obj
    return JSONResponse(versions, status=200)
