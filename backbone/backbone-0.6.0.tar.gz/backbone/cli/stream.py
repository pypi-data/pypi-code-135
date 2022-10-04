from typing import List

import typer

from backbone.cli import Context
from backbone.cli._models import KeyspacePermission
from backbone.cli._utilities import expect_client, expect_workspace, find_workspace_user, handle_exceptions
from backbone.common import enums

stream_cli = typer.Typer()


@stream_cli.callback()
def stream():
    """Streaming operations"""


@stream_cli.command("create")
@handle_exceptions
@expect_workspace
@expect_client
def stream_create(context: typer.Context, name: str):
    """Create a stream"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Creating stream '{name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        workspace_client.stream.create(name)
        ctx.fmt.success(f"Created stream '{name}'")


@stream_cli.command("delete")
@handle_exceptions
@expect_workspace
@expect_client
def stream_delete(context: typer.Context, name: str):
    """Delete a stream"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Deleting stream '{name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        workspace_client.stream.delete(name)
        ctx.fmt.success(f"Deleted stream '{name}'")


@stream_cli.command("publish")
@handle_exceptions
@expect_workspace
@expect_client
def stream_publish(context: typer.Context, name: str, messages: List[str]):
    """Publish messages to a stream"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Publishing {len(messages)} messages to stream '{name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        workspace_client.stream.publish(name, *map(lambda s: s.encode(), messages))
        ctx.fmt.success(f"Published {len(messages)} messages to stream '{name}'")


@stream_cli.command("consume")
@handle_exceptions
@expect_workspace
@expect_client
def stream_consume(context: typer.Context, name: str, messages: int, shared: bool = False):
    """Consume messages to a stream"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Consuming {messages} messages from stream '{name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        for message in workspace_client.stream.consume(name, messages, shared=shared):
            try:
                message = message.decode()
            except:
                pass

            ctx.fmt.info(message)
        ctx.fmt.success(f"Consumed {messages} messages from stream '{name}'")


@stream_cli.command("grants")
@handle_exceptions
@expect_workspace
def grants_stream(context: typer.Context, name: str):
    """List grants on a stream"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Fetching grants for stream '{name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        stream_grants = workspace_client.stream.list_grants(name)

        for grant in stream_grants:
            ctx.fmt.display_grant(grant)

        ctx.fmt.success(f"Fetched grants for stream '{name}'")


@stream_cli.command("grant")
@handle_exceptions
@expect_workspace
def grant_stream(context: typer.Context, name: str, user_name: str, access: List[KeyspacePermission] = None):
    """Grant a user access to a stream"""
    ctx: Context = context.obj
    access = access and set(enums.KeyspacePermission[level.name] for level in access)
    access_string = ", ".join(sorted(level.name for level in access)) or "inherited access"

    with ctx.fmt.begin(f"Granting '{access_string}' on stream '{name}' to '{user_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        user_identity = find_workspace_user(workspace_client, user_name)

        if user_identity is None:
            ctx.fmt.failure(f"No such user '{user_name}'")
            raise typer.Exit()

        workspace_client.stream.grant(name, user_identity, access)
        ctx.fmt.success(f"Granted '{access_string}' on stream '{name}' to '{user_name}'")


@stream_cli.command("revoke")
@handle_exceptions
@expect_workspace
def revoke_stream(context: typer.Context, name: str, user_name: str):
    """Revoke a user's access to a stream"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Revoking access to stream '{name}' from '{user_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        user_identity = find_workspace_user(workspace_client, user_name)

        if user_identity is None:
            ctx.fmt.failure(f"No such user '{user_name}'")
            raise typer.Exit()

        workspace_client.stream.revoke(name, user_identity)
        ctx.fmt.success(f"Revoked access to stream '{name}' from '{user_name}'")
