import random
import string
from dataclasses import dataclass
from typing import List

import requests
from bs4 import BeautifulSoup

CAPTCHA_URL = "http://revivelink.com/qcap/Qaptcha.jquery.php"


@dataclass
class Link:
    platform: str
    url: str


def _generate_captcha_key() -> str:
    letters_and_digits = string.ascii_letters + string.digits
    return "".join(random.choice(letters_and_digits) for _ in range(32))


def _generate_sessionid() -> str:
    data = {"action": "qaptcha", "qaptcha_key": _generate_captcha_key()}
    response = requests.post(CAPTCHA_URL, data=data)
    return str(response.cookies["PHPSESSID"])


def _get_destination_url(url: str) -> str:
    splitted = url.split("/")
    splitted[-1] = f"slinks.php?R={splitted[-1]}"
    return "/".join(splitted)


def get_links(url: str) -> List[Link]:
    response = requests.get(
        _get_destination_url(url),
        allow_redirects=True,
        timeout=20,
        cookies={"PHPSESSID": _generate_sessionid()},
    )
    response.raise_for_status()

    soup_response = BeautifulSoup(response.content, "html.parser")

    result: List[Link] = []

    for row in soup_response.find_all("tr"):
        link = row.find("a")

        if link:
            tds = row.find_all("td")

            if len(tds) > 2:
                result.append(
                    Link(
                        url=link["href"],
                        platform="".join(tds[1].text.splitlines()).strip(),
                    )
                )

    return result
