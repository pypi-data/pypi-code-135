# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2022 Michał Góral.

import requests

from repotea.args import ArgumentParser, cli
from repotea.api import scoped, is_success, send_post
from ._helpers import get_data_from_keys, eprint_message


@cli.arg("--private", action="store_true", help="repository should be private")
@cli.arg("--license", nargs="?", help="license")
@cli.arg("--default-branch", nargs="?", default="master", help="name of default branch")
@cli.arg(
    "--init",
    dest="auto_init",
    action="store_true",
    help="create repository with initial commit",
)
@cli.arg("--description", nargs="?", help="repository description")
@cli.arg("--org", nargs="?", help="create repository under organization")
@cli.arg("name", help="name of new repository")
@cli.subcommand("new")
def new(args: ArgumentParser) -> bool:
    """Create new repository"""
    method = scoped("repos", args.org)

    keys = ("name", "private", "default_branch", "license", "description", "auto_init")
    data = get_data_from_keys(keys, args)
    resp = send_post(args, method, json=data)

    if not is_success(resp.status_code):
        eprint_message(resp)

    return is_success(resp.status_code)
