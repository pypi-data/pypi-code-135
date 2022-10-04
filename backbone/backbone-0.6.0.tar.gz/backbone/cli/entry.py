from typing import List, Optional

import typer

from backbone.cli import Context
from backbone.cli._models import KeyspacePermission
from backbone.cli._utilities import expect_client, expect_workspace, find_workspace_user, handle_exceptions
from backbone.common import enums

entry_cli = typer.Typer()


@entry_cli.callback()
def docs():
    """Keyspace value operations"""


@entry_cli.command("set")
@handle_exceptions
@expect_workspace
@expect_client
def entry_set(context: typer.Context, key: str, value: str, duration_ms: Optional[int] = None):
    """Set an entry's value"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Setting entry '{key}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        workspace_client.entry.set(key, value, duration_ms=duration_ms)
        ctx.fmt.success(f"Set entry '{key}' to '{value}'{f' for {duration_ms}ms' if duration_ms else ''}")


@entry_cli.command("get")
@handle_exceptions
@expect_workspace
@expect_client
def entry_get(context: typer.Context, key: str):
    """Get an entry's value"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Reading entry '{key}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        value = workspace_client.entry.get(key)
        ctx.fmt.success(value)


@entry_cli.command("delete")
@handle_exceptions
@expect_workspace
@expect_client
def entry_delete(context: typer.Context, key: str):
    """Delete an entry"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Deleting entry '{key}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        workspace_client.entry.delete(key)
        ctx.fmt.success(f"Deleted entry '{key}'")


@entry_cli.command("grants")
@handle_exceptions
@expect_workspace
@expect_client
def entry_grants(context: typer.Context, key: str):
    """List grants on an entry"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Fetching grants for entry '{key}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        entry_grants = workspace_client.entry.list_grants(key)

        for grant in entry_grants:
            ctx.fmt.display_grant(grant)

        ctx.fmt.success(f"Fetched grants for entry '{key}'")


@entry_cli.command("grant")
@handle_exceptions
@expect_workspace
@expect_client
def grant_entry(context: typer.Context, key: str, user_name: str, access: List[KeyspacePermission] = None):
    """Grant a user access to an entry"""
    ctx: Context = context.obj
    access = access and set(enums.KeyspacePermission[level.name] for level in access)
    access_string = ", ".join(sorted(level.name for level in access))

    with ctx.fmt.begin(f"Granting '{access_string}' on entry '{key}' to '{user_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        user_identity = find_workspace_user(workspace_client, user_name)

        if user_identity is None:
            ctx.fmt.failure(f"No such user '{user_name}'")
            raise typer.Exit()

        workspace_client.entry.grant(key, user_identity, access)
        ctx.fmt.success(f"Granted '{access_string}' on entry '{key}' to '{user_name}'")


@entry_cli.command("revoke")
@handle_exceptions
@expect_workspace
@expect_client
def revoke_entry(context: typer.Context, key: str, user_name: str):
    """Revoke a user's access to an entry"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Revoking access to entry '{key}' from '{user_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        user_identity = find_workspace_user(workspace_client, user_name)

        if user_identity is None:
            ctx.fmt.failure(f"No such user '{user_name}'")
            raise typer.Exit()

        workspace_client.entry.revoke(key, user_identity)
        ctx.fmt.success(f"Revoked access to entry '{key}' from '{user_name}'")
