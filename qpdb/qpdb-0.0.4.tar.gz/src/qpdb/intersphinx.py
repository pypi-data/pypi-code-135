from __future__ import annotations

from sphobjinv import Inventory

__all__ = ["fetch_inv"]


# Could set versions with {major}.{minor} if more generality desired
package_urls = {"pandas": "https://pandas.pydata.org/pandas-docs/version/{version}/"}


def fetch_inv(package: str, version: str) -> dict[str,dict[str, dict[str, str]]]:
    """
    For reference, see the explanation of the Sphinx objects.inv format given in
    https://buildmedia.readthedocs.org/media/pdf/sphobjinv/v.doc/sphobjinv.pdf
    """
    if package not in package_urls:
        raise ValueError("No known URL for this package")
    else:
        url = package_urls[package].format(version=version) + "objects.inv"
    inv = Inventory(url=url)
    return {url: inv}
