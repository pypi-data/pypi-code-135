# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2022 Michał Góral.

import requests

from repotea.args import ArgumentParser, cli
from repotea.api import is_success, send_delete
from repotea.utils import die
from ._helpers import eprint_message


@cli.arg("--force", action="store_true", help="force removal without confirmation")
@cli.arg("name", help="full path to repository (owner/repo)")
@cli.subcommand("delete")
def delete(args: ArgumentParser) -> bool:
    """Create new repository"""

    owner, _, repo = args.name.partition("/")
    if not owner:
        die("missing owner in the path of repository to delete")
    if not repo:
        die("missing repository in the path of repository to delete")

    path = f"{owner}/{repo}"
    method = f"repos/{path}"

    if not args.force:
        confirmation = input(
            "To IRREVOCABLY DELETE REPOSITORY, please retype it's full path: "
        )
        if confirmation != path:
            die("Paths mismatch, aborting")

    resp = send_delete(args, method)

    if not is_success(resp.status_code):
        eprint_message(resp)

    return is_success(resp.status_code)
