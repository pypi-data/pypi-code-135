# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2022 Michał Góral.

import requests

from repotea.args import ArgumentParser, cli
from repotea.api import scoped, is_success, send_get


@cli.arg("--user", action="store_true", help="list only user organizations")
@cli.subcommand("orgs")
def orgs(args: ArgumentParser):
    """List organizations"""
    method = "user/orgs" if args.user else "orgs"

    resp = send_get(args, method)
    if not is_success(resp.status_code):
        return False

    for org in resp.json():
        print(org["username"])

    return True
