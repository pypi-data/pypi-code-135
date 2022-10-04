"""
This file holds all of the CLI commands for the "anyscale logs" path. Note that
most of the implementation for this command is in the controller to make the controller
accessible to the SDK in the future.

TODO (shomilj): Bring the controller to feature parity with the CLI.
"""
from datetime import timedelta
import math
from typing import Optional

import click
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table

from anyscale.cli_logger import BlockLogger
from anyscale.client.openapi_client.models import LogFilter
from anyscale.client.openapi_client.models.node_type import NodeType
from anyscale.controllers.logs_controller import LogsController


log = BlockLogger()

# Options to configure core functionality. These are mutually exclusive.
option_download = click.option(
    "-d",
    "--download",
    is_flag=True,
    default=False,
    help="Download logs to the current working directory, or a specified path.",
)
option_tail = click.option(
    "-t", "--tail", type=int, default=-1, help="Read the last N lines of logs."
)
option_follow = click.option(
    "-f",
    "--follow",
    is_flag=True,
    default=False,
    help="Stream logs from a Ray cluster.",
)

# The "glob" is an optional argument.
# e.g. anyscale logs cluster --cluster-id <cluster-id> [GLOB]
argument_glob = click.argument("glob", type=str, default=None, required=False)

# Options to filter beyond what the subcommand already filters to.
option_node_ip = click.option(
    "-ip", "--node-ip", type=str, default=None, help="Filter logs by a node IP."
)
option_instance_id = click.option(
    "--instance-id", type=str, default=None, help="Filter logs by an instance ID."
)
option_worker_only = click.option(
    "--worker-only", is_flag=True, help="Download logs of only the worker nodes."
)
option_head_only = click.option(
    "--head-only", is_flag=True, help="Download logs of only the head node."
)

option_timeout = click.option(
    "--timeout", type=int, default=30, help="Timeout in seconds for the API requests.",
)
option_page_size = click.option(
    "--page-size",
    type=int,
    default=None,
    hidden=True,
    help="Results to get in a single network API call.",
)
option_ttl = click.option(
    "--ttl",
    type=int,
    default=1800,
    hidden=True,
    help="TTL in seconds to pass to the service that generates presigned URL's.",
)
option_parallelism = click.option(
    "--parallelism",
    type=int,
    default=10,
    hidden=True,
    help="Number of files to download in parallel at a time.",
)
option_read_timeout = click.option(
    "--read-timeout",
    type=int,
    default=30,
    hidden=True,
    help="Timeout in seconds for the HTTP call while downloading files.",
)

# ADVANCED: Configure the download behavior, only useful if --download enabled.
option_download_dir = click.option(
    "--download-dir", type=str, default=None, help="Directory to download logs into."
)


@click.group(
    "logs",
    help="Print or download Ray logs for an Anyscale job, service, or cluster.",
    hidden=True,
)
def log_cli() -> None:
    pass


# TODO (shomilj): Support environment variable for cluster ID here.
@log_cli.command(name="cluster", help="Access log files of a cluster.")
@click.option("--id", type=str, required=True, help="Provide a cluster ID.")
@option_download
@option_tail
@option_follow
@argument_glob
@option_node_ip
@option_instance_id
@option_worker_only
@option_head_only
@option_timeout
@option_download_dir
@option_page_size
@option_ttl
@option_parallelism
@option_read_timeout
def anyscale_logs_cluster(
    id: str,
    download: bool,
    follow: bool,
    tail: int,
    # filters
    glob: Optional[str],
    node_ip: Optional[str],
    instance_id: Optional[str],
    worker_only: bool,
    head_only: bool,
    # list files config
    page_size: Optional[int],
    ttl: Optional[int],
    # download files config
    download_dir: Optional[str],
    parallelism: int,
    timeout: int,
    read_timeout: int,
) -> None:
    logs_controller = LogsController()

    node_type: Optional[NodeType] = None
    if worker_only and head_only:
        raise click.ClickException("Cannot specify both --worker-only and --head-only.")
    if worker_only:
        node_type = NodeType.WORKER_NODES
    elif head_only:
        node_type = NodeType.HEAD_NODE

    filter = LogFilter(
        cluster_id=id,
        glob=glob,
        node_ip=node_ip,
        instance_id=instance_id,
        node_type=node_type,
    )

    if download:
        logs_controller.download_logs(
            filter=filter,
            page_size=page_size,
            timeout=timedelta(seconds=timeout),
            read_timeout=timedelta(seconds=read_timeout),
            ttl_seconds=ttl,
            download_dir=download_dir,
            parallelism=parallelism,
        )

    elif follow:
        raise click.ClickException("This feature has not been implemented.")

    else:
        # This is for both tailing logs AND for the default behavior (no -t/-d/-f => rendering them in UI).
        console = Console()
        log_group = logs_controller.get_logs_for_tail(
            filter=filter,
            page_size=page_size,
            timeout=timedelta(seconds=timeout),
            ttl_seconds=ttl,
        )
        if len(log_group.get_files()) == 0:
            console.log("No results found.")
        elif len(log_group.get_files()) > 1:
            console.log(
                "These are the available log files. To download all files, use --download. To render a specific file, just paste the filename after this command."
            )
            click.echo()
            for session in log_group.get_sessions():
                click.echo()
                renderables = []

                for node in session.get_nodes():
                    table = Table()
                    table.add_column("Node Type", style="magenta")
                    table.add_column("File Name", justify="left", style="green")
                    table.add_column("Chunks")
                    table.add_column("Size")
                    for log_file in node.get_files():
                        table.add_row(
                            node.node_type,
                            log_file.file_name,
                            str(len(log_file.get_chunks())),
                            convert_size(log_file.get_size()),
                        )

                    renderables.append(
                        Panel(
                            Group(table),
                            title=f"Node: {node.node_ip} ({node.instance_id})",
                            title_align="left",
                        )
                    )
                group = Group(*renderables)
                console.print(
                    Panel(
                        group,
                        title=f"Session: {session.session_id}",
                        title_align="left",
                        padding=(1, 1),
                    )
                )

        else:
            logs_controller.render_logs(
                log_group=log_group,
                parallelism=parallelism,
                read_timeout=timedelta(seconds=read_timeout),
                tail=tail,
            )

        click.echo()


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
