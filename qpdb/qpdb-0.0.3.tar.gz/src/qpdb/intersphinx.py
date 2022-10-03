from __future__ import annotations

from sys import stderr

from sphinx.ext.intersphinx import fetch_inventory

__all__ = ["get_intersphinx_inv"]


class MockConfig:
    intersphinx_timeout: int | None = None
    tls_verify = False
    user_agent = None


class MockApp:
    srcdir = ""
    config = MockConfig()

    def warn(self, msg: str) -> None:
        print(msg, file=stderr)


# Could set versions with {major}.{minor} if more generality desired
package_urls = {"pandas": "https://pandas.pydata.org/pandas-docs/version/{version}/"}


def get_intersphinx_inv(package: str, version: str) -> dict[str, dict[str, str]]:
    """
    Unwrapped version of the routine that runs when :mod:`sphinx.ext.intersphinx` is
    called as ``__main__``.
    """
    if package not in package_urls:
        raise ValueError("No known URL for this package")
    else:
        url = package_urls[package].format(version=version) + "objects.inv"
    invdata = fetch_inventory(MockApp(), "", url)  # type: ignore
    for entity_type in sorted(invdata or {}):
        print(entity_type)
        for key, einfo in sorted(invdata[entity_type].items()):
            extra_info = einfo[3] if einfo[3] != "-" else ""
            doc_path = einfo[2]
            if entity_type not in ["std:doc", "std:label"]:
                qualname, title = key, extra_info
                print(f"  {qualname=}, {title=}, {doc_path=}")
            else:
                # Not clear why, but std:label doc_ref has "/" prefix
                # Maybe instead 'detect' if qualname or title by "." or " "
                doc_ref, qualname_or_title = key, extra_info
                print(f"  {doc_ref=}, {qualname_or_title=}, {doc_path=}")
