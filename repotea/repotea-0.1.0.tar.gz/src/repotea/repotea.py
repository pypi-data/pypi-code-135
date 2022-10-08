# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2022 Michał Góral.

from typing import Optional

import sys
import argparse
import requests
from urllib.parse import urlsplit, urljoin

from repotea.args import cli
from repotea.utils import getenv, eprint, die

# importing commands enables them in ArgumentParser
from repotea.cmds import *


def prepare_global_args():
    cli.parser.add_argument(
        "--url",
        nargs="?",
        default=getenv("REPOTEA_URL"),
        help="Gitea's URL. Can be set by REPOTEA_URL environment variable",
    )
    cli.parser.add_argument(
        "--token",
        nargs="?",
        default=getenv("REPOTEA_TOKEN"),
        help="Access token for Gitea's API. Can be set by REPOTEA_TOKEN environment variable",
    )


@cli.empty_subcommand_handler
def no_command(args):
    eprint("No subcommand selected. See: repotea --help.")
    return 1


def cmd_new(args):
    data = {
        "name": args.name,
        "auto_init": true,
        "default_branch": "master",
        "private": False,
        "template": False,
        "trust_model": "default",
    }
    resp = requests.post(
        get_api_url(args.repository, "repos"), headers=get_headers(args), json=data
    )

    return resp.status_code == 200


def main():
    prepare_global_args()
    args = cli.parse_args()

    if not args.url:
        die("No repository configured via package --repository")
    if not args.token:
        die("No API token configured via package --token")

    return int(not args.func(args))


sys.exit(main())
