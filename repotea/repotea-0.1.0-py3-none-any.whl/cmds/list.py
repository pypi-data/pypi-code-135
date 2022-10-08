# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2022 Michał Góral.

import requests

from repotea.args import ArgumentParser, cli
from repotea.api import scoped, is_success, send_get


@cli.arg("--org", nargs="?", help="list repositories of organization instead of user's")
@cli.arg("--full-name", nargs="?", help="use repository full name")
@cli.subcommand("list")
def list_(args: ArgumentParser):
    """List repositories"""
    method = scoped("repos", args.org)

    resp = send_get(args, method)
    if not is_success(resp.status_code):
        return False

    for repo in resp.json():
        key = "full_name" if args.full_name else "name"
        print(repo[key])

    return True
