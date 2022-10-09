from __future__ import annotations

from sphobjinv import Inventory

__all__ = ["pkg_urls_and_versions", "fetch_inv"]


# Could set versions with {major}.{minor} if more generality desired
pkg_urls_and_versions = {
    "numpy": ("https://numpy.org/doc/{version}/", "1.23"),
    "pandas": ("https://pandas.pydata.org/pandas-docs/version/{version}/", "1.5"),
    "torch": ("https://pytorch.org/docs/{version}/", "1.12"),
}


def fetch_inv(package: str, version: str) -> tuple[str, dict[str, dict[str, str]]]:
    """
    For reference, see the explanation of the Sphinx objects.inv format given in
    https://buildmedia.readthedocs.org/media/pdf/sphobjinv/v.doc/sphobjinv.pdf
    """
    if package not in pkg_urls_and_versions:
        raise ValueError("No known URL for this package")
    else:
        url_base_template, default_v = pkg_urls_and_versions[package]
        url_base = url_base_template.format(version=version if version else default_v)
        url = url_base + "objects.inv"
    inv = Inventory(url=url)
    return url_base, inv
