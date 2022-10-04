import typer

from backbone import sync as backbone
from backbone.cli import Context
from backbone.cli._config import LocalConfiguration
from backbone.cli._utilities import (
    clear_configuration,
    expect_client,
    handle_exceptions,
    request_master_secret,
    write_configuration,
)
from backbone.common import service

user_cli = typer.Typer()


@user_cli.callback()
def docs():
    """User and local trust operations"""


@user_cli.command("create")
@handle_exceptions
def create_user(context: typer.Context, user_name: str = typer.Argument(...)):
    """Create a user"""
    ctx: Context = context.obj
    master_secret = request_master_secret(context, associated_data=[user_name], setup=True)

    with ctx.fmt.begin(f"Creating user '{user_name}'"):
        client = backbone.from_master_secret(user_name=user_name, master_secret=master_secret)
        client.user.create()

        ctx.fmt.success(f"Created user '{user_name}'")
        configuration = LocalConfiguration.from_master_secret(user_name=user_name, master_secret=master_secret)
        write_configuration(configuration)


@user_cli.command("login")
@handle_exceptions
def login_user(context: typer.Context, user_name: str = typer.Argument(...)):
    """Login as a user"""
    ctx: Context = context.obj
    master_secret = request_master_secret(context)

    with ctx.fmt.begin(f"Authenticating user '{user_name}'"):
        client = backbone.from_master_secret(user_name=user_name, master_secret=master_secret)
        try:
            client.user.fetch_self()
        except service.Error as e:
            if e.code == "unauthenticated":
                raise ValueError("Invalid credentials")
            raise e

        ctx.fmt.success(f"Authenticated user '{user_name}'")
        configuration = LocalConfiguration.from_master_secret(user_name=user_name, master_secret=master_secret)
        write_configuration(configuration)


@user_cli.command("trust")
@handle_exceptions
@expect_client
def trust(context: typer.Context, identity_token: str):
    """Trust a workspace"""
    ctx: Context = context.obj
    workspace = backbone.WorkspaceClient.load_identity(identity_token)

    trust_identity_token = typer.confirm(
        f"Are you sure you want to trust a workspace named '{workspace.name}' with public key"
        f" '{bytes(workspace.public_key).hex()}' and verify key '{bytes(workspace.verify_key).hex()}'?"
    )

    if not trust_identity_token:
        ctx.fmt.failure("Operation cancelled")
        raise typer.Exit()

    with ctx.fmt.begin(
        f"Trusting workspace '{workspace.name}' for user '{ctx.config.user_name}'"
    ), ctx.client as client:
        client.user.trust(workspace)
        ctx.fmt.success(f"Workspace '{workspace.name}' is now trusted for user '{ctx.config.user_name}'")


@user_cli.command("untrust")
@handle_exceptions
@expect_client
def untrust(context: typer.Context, identity_token: str):
    """Untrust a workspace"""
    ctx: Context = context.obj
    workspace = backbone.WorkspaceClient.load_identity(identity_token)

    untrust_identity_token = typer.confirm(
        f"Are you sure you want to untrust a workspace named '{workspace.name}' with public key"
        f" '{bytes(workspace.public_key).hex()}' and verify key '{bytes(workspace.verify_key).hex()}'?"
    )

    if not untrust_identity_token:
        ctx.fmt.failure("Operation cancelled")
        raise typer.Exit()

    with ctx.fmt.begin(
        f"Untrusting workspace '{workspace.name}' for user '{ctx.config.user_name}'"
    ), ctx.client as client:
        client.user.untrust(workspace)
        ctx.fmt.success(f"Workspace '{workspace.name}' is now untrusted for user '{ctx.config.user_name}'")


@user_cli.command("share")
@expect_client
def share(context: typer.Context):
    """Generate a share key for the current user"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Sharing key for user '{ctx.config.user_name}'"), ctx.client as client:
        identity_token = client.user.share_identity()
        ctx.fmt.info(f"Share this key: {identity_token}")


@user_cli.command("delete")
@expect_client
def delete_user(context: typer.Context):
    """Delete the current user"""
    ctx: Context = context.obj

    with ctx.fmt.begin(f"Deleting user '{ctx.config.user_name}'"), ctx.client as client:
        client.user.delete()
        clear_configuration()
        ctx.fmt.success(f"Deleted user '{ctx.config.user_name}'")
