# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2022 Michał Góral.

from typing import Optional, Any, Iterable

from urllib.parse import urljoin
import requests

from repotea.args import ArgumentParser


def get_headers(token: str):
    return {
        "Authorization": f"token {token}",
        "accept": "application/json",
    }


def get_api_url(url: str, method: str, api: str = "api/v1") -> str:
    path = f"{api}/{method}"
    return urljoin(url, path)


def scoped(method: str, org: Optional[str] = None) -> str:
    scope = f"orgs/{org}" if org else "user"
    return f"{scope}/{method}"


def is_success(sc: int) -> bool:
    return 200 <= sc < 300


def send_get(
    args: ArgumentParser, method: str, api: str = "api/v1"
) -> requests.Response:
    url = get_api_url(args.url, method, api)
    resp = requests.get(url, headers=get_headers(args.token))
    return resp


def send_post(
    args: ArgumentParser, method: str, json: Optional[Any] = None, api: str = "api/v1"
) -> requests.Response:
    url = get_api_url(args.url, method, api)
    resp = requests.post(url, json=json, headers=get_headers(args.token))
    return resp


def send_delete(
    args: ArgumentParser, method: str, api: str = "api/v1"
) -> requests.Response:
    url = get_api_url(args.url, method, api)
    resp = requests.delete(url, headers=get_headers(args.token))
    return resp
