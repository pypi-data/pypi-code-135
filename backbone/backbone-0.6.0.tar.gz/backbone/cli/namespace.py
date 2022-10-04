import re
import subprocess
from typing import List

import typer

from backbone.cli import Context
from backbone.cli._models import KeyspacePermission
from backbone.cli._utilities import expect_client, expect_workspace, find_workspace_user, handle_exceptions
from backbone.common import enums, models
from backbone.sync.workspace import WorkspaceClient

namespace_cli = typer.Typer()


@namespace_cli.callback()
def docs():
    """Keyspace hierarchy operations"""


@namespace_cli.command("tree")
@handle_exceptions
@expect_workspace
@expect_client
def namespace_tree(
    context: typer.Context,
    key: str = typer.Argument(""),
    depth: int = 3,
    all: bool = typer.Option(False, "-a", "--all"),
):
    """Visually display the children of a namespace"""
    ctx: Context = context.obj

    def print_layer(client: WorkspaceClient, layer_key: str, level: int = 1, indent: str = ""):
        if level > depth:
            return

        resources = client.namespace.list_children(layer_key)
        for index, resource in enumerate(resources):
            is_last: bool = index == len(resources) - 1
            is_namespace: bool = isinstance(resource, models.Namespace)
            resource_name = resource.path.split("/", level)[-1]

            # Skip resources prefixed with a '.' if the --all / -a option is not passed
            if not all and resource_name.startswith("."):
                continue

            wire: str = "└──" if is_last else "├──"
            bulb: str = "●" if is_namespace else "○"

            # Display resource
            ctx.fmt.raw(f"{indent}{wire}{bulb} {resource_name}")

            if is_namespace:
                next_indent = indent + ("   " if is_last else "│  ")

                # Display unexplored namespaces
                if level == depth:
                    ctx.fmt.raw(f"{next_indent}└── ...")

                print_layer(client, resource.path, level=level + 1, indent=next_indent)

    with ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        print_layer(workspace_client, key)


@namespace_cli.command("mount")
@handle_exceptions
@expect_workspace
@expect_client
def namespace_mount(context: typer.Context, key: str, command: str):
    """Run a command within a namespace"""
    ctx: Context = context.obj
    env = {}

    with ctx.fmt.begin(f"Mounting namespace '{key}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)

        for resource in workspace_client.namespace.list_children(key):
            if isinstance(resource, models.Entry):
                env_variable = re.sub(r"\w+", "_", resource.path[len(key) :]).upper().strip("_")
                env[env_variable] = workspace_client.entry.get(resource.path).decode("utf-8")

    ctx.fmt.success(f"Launching {command} within {key}")
    process = subprocess.Popen(command, env=env, shell=True)
    process.wait()


@namespace_cli.command("create")
@handle_exceptions
@expect_workspace
@expect_client
def namespace_create(context: typer.Context, key: str):
    """Create a namespace"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Creating namespace '{key}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        workspace_client.namespace.create(key)
        ctx.fmt.success(f"Created namespace '{key}'")


@namespace_cli.command("delete")
@handle_exceptions
@expect_workspace
@expect_client
def namespace_delete(context: typer.Context, key: str):
    """Delete a namespace"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Deleting namespace '{key}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        workspace_client.namespace.delete(key)
        ctx.fmt.success(f"Deleted namespace '{key}'")


@namespace_cli.command("grants")
@handle_exceptions
@expect_workspace
def grants_namespace(context: typer.Context, key: str):
    """List grants on a namespace"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Fetching grants for namespace '{key}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        namespace_grants = workspace_client.namespace.list_grants(key)

        for grant in namespace_grants:
            ctx.fmt.display_grant(grant)

        ctx.fmt.success(f"Fetched grants for namespace '{key}'")


@namespace_cli.command("grant")
@handle_exceptions
@expect_workspace
def grant_namespace(context: typer.Context, key: str, user_name: str, access: List[KeyspacePermission] = None):
    """Grant a user access to a namespace"""
    ctx: Context = context.obj
    access = access and set(enums.KeyspacePermission[level.name] for level in access)
    access_string = ", ".join(sorted(level.name for level in access)) or "inherited access"

    with ctx.fmt.begin(f"Granting '{access_string}' on namespace '{key}' to '{user_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        user_identity = find_workspace_user(workspace_client, user_name)

        if user_identity is None:
            ctx.fmt.failure(f"No such user '{user_name}'")
            raise typer.Exit()

        workspace_client.namespace.grant(key, user_identity, access)
        ctx.fmt.success(f"Granted '{access_string}' on namespace '{key}' to '{user_name}'")


@namespace_cli.command("revoke")
@handle_exceptions
@expect_workspace
def revoke_namespace(context: typer.Context, key: str, user_name: str):
    """Revoke a user's access to a namespace"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Revoking access to namespace '{key}' from '{user_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        user_identity = find_workspace_user(workspace_client, user_name)

        if user_identity is None:
            ctx.fmt.failure(f"No such user '{user_name}'")
            raise typer.Exit()

        workspace_client.namespace.revoke(key, user_identity)
        ctx.fmt.success(f"Revoked access to namespace '{key}' from '{user_name}'")
