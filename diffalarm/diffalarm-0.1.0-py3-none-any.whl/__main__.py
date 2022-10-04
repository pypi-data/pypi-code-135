"""
DiffAlarm - 웹페이지 변화 감지기

Usage:
    diffalarm <path-to-config>
    diffalarm -h | --help

Options:
    -h --help    이 도움말을 보여줍니다.
"""

import re
import time
from dataclasses import dataclass
from pathlib import Path
from re import Pattern

import docopt
import requests
import yaml
from bs4 import BeautifulSoup as Soup
from typing_extensions import Self

from .beep import beep


@dataclass
class Page:
    url: str
    selector: str
    regex: Pattern[str]
    criteria: int
    interval: int

    @classmethod
    def from_path(cls, path: str | Path) -> "Page":
        data = yaml.safe_load(Path(path).read_text())
        data["regex"] = re.compile(data["regex"])
        return cls(**data)

    def run(self):
        while True:
            html = requests.get(self.url)
            soup = Soup(html.text, "html.parser")
            self.check(soup)
            time.sleep(self.interval)

    def check(self, soup: Soup):
        match soup.select_one(self.selector):
            case None:
                print(
                    f"CSS Selector 규칙 {self.selector}가 잘못되었거나,"
                    "해당 페이지에는 해당 요소가 없습니다."
                )
                exit(1)
            case _ as tag:
                data = "".join(re.findall(self.regex, tag.text.strip()))
                number = int(data)
                if number >= self.criteria:
                    print(f"{number}이 {self.criteria} 이상입니다.")
                    beep(sound="ping")


def main():
    assert __doc__ is not None

    path = Path(docopt.docopt(__doc__).get("<path-to-config>"))  # type: ignore
    if not path.exists():
        print(f"{path.absolute()}가 존재하지 않는 경로입니다.")
        exit(1)

    page = Page.from_path(path)
    page.run()


if __name__ == "__main__":
    main()
