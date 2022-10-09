from __future__ import annotations

from bs4 import BeautifulSoup as BS

__all__ = ["slurp"]


def slurp(content: bytes, doc_id: str, print_target=True):
    soup = BS(content, "html5lib")
    target = soup.find(id=doc_id)
    if target.name == "dt":
        target = target.parent.find(name="dd")
    if print_target:
        print("```html")
        print(target)
        print("```", end="")
    # breakpoint()
    input()
