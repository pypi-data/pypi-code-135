from typing import List

import typer

from backbone.cli import Context
from backbone.cli._models import WorkspacePermission
from backbone.cli._utilities import expect_client, expect_workspace, handle_exceptions, write_configuration
from backbone.common import enums
from backbone.sync import UserClient

workspace_cli = typer.Typer()


@workspace_cli.callback()
def docs():
    """Workspace administrative operations"""


@workspace_cli.command("create")
@handle_exceptions
@expect_client
def create_workspace(context: typer.Context, workspace_name=typer.Argument(...)):
    """Create a new workspace"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Creating workspace '{workspace_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(workspace_name)
        workspace_client.create()
        ctx.fmt.success(f"Created workspace '{workspace_name}'")
        ctx.config.workspace_name = workspace_name
        write_configuration(ctx.config)


@workspace_cli.command("status")
@handle_exceptions
@expect_workspace
@expect_client
def status_workspace(context: typer.Context):
    """Display the current workspace"""
    ctx: Context = context.obj
    ctx.fmt.info(ctx.workspace_name)


@workspace_cli.command("share")
@handle_exceptions
@expect_workspace
@expect_client
def share(context: typer.Context):
    """Generate a share key for the current workspace"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Sharing key for workspace '{ctx.workspace_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        identity_token = workspace_client.share_identity()
        ctx.fmt.success(f"Share this key: {identity_token}")


@workspace_cli.command("trust")
@handle_exceptions
@expect_workspace
@expect_client
def trust(context: typer.Context, identity_token: str, access: List[WorkspacePermission] = None):
    """Grant a user access to the current workspace"""
    ctx: Context = context.obj
    user = UserClient.load_identity(identity_token)
    access = access and list(enums.WorkspacePermission[level.name] for level in access)
    access_string = ", ".join(sorted(level.name for level in access)) or "workspace access"

    trust_identity_token = typer.confirm(
        f"Are you sure you want to grant {access_string} to"
        f" user '{user.name}' with public key '{bytes(user.public_key).hex()}' and verify key"
        f" '{bytes(user.verify_key).hex()}'?"
    )

    if not trust_identity_token:
        ctx.fmt.failure("Operation cancelled")
        raise typer.Exit()

    with ctx.fmt.begin(f"Trusting user in workspace '{ctx.workspace_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        workspace_client.trust(user=user, access=access)
        ctx.fmt.success(f"User '{user.name}' is now trusted in workspace '{ctx.workspace_name}'")


@workspace_cli.command("untrust")
@handle_exceptions
@expect_workspace
@expect_client
def untrust(context: typer.Context, user_name: str):
    """Revoke a user's access to the current workspace"""
    ctx: Context = context.obj
    untrust_identity_token = typer.confirm(f"Are you sure you want to revoke workspace access to user '{user_name}'?")

    if not untrust_identity_token:
        ctx.fmt.failure("Operation cancelled")
        raise typer.Exit()

    with ctx.fmt.begin(f"Untrusting user '{user_name}' in workspace '{ctx.workspace_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        workspace_client.untrust(user_name=user_name)
        ctx.fmt.success(f"User '{user_name}' is now untrusted in workspace '{ctx.workspace_name}'")


@workspace_cli.command("list")
@handle_exceptions
@expect_client
def list_workspace(context: typer.Context):
    """List trusted workspaces"""
    ctx: Context = context.obj

    with ctx.fmt.begin("Listing trusted workspaces"), ctx.client as client:
        user = client.user.fetch_self()

        for workspace_identity in user.trusted_workspaces:
            ctx.fmt.info(workspace_identity.name)


@workspace_cli.command("switch")
@handle_exceptions
@expect_client
def switch_workspace(context: typer.Context, workspace_name=typer.Argument(...)):
    """Modify the current workspace"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Entering workspace '{workspace_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(workspace_name)
        workspace_client.fetch()
        ctx.fmt.success(f"Entered workspace '{workspace_name}'")
        ctx.config.workspace_name = workspace_name
        write_configuration(ctx.config)


@workspace_cli.command("delete")
@handle_exceptions
@expect_workspace
@expect_client
def delete_workspace(context: typer.Context):
    """Delete the current workspace"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Deleting workspace '{ctx.workspace_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        workspace_client.delete()
        ctx.fmt.success(f"Deleted workspace '{ctx.workspace_name}'")
        ctx.config.workspace_name = None
        write_configuration(ctx.config)


@workspace_cli.command("members")
@handle_exceptions
@expect_workspace
@expect_client
def list_members(context: typer.Context):
    """List the members of the current workspace"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Listing members of workspace '{ctx.workspace_name}'"), ctx.client as client:
        workspace_client = client.with_workspace(ctx.workspace_name)
        grants = workspace_client.list_grants()

        for grant in grants:
            ctx.fmt.display_grant(grant.plain)
