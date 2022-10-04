import typer

from backbone.cli import Context
from backbone.cli._utilities import clear_configuration, handle_exceptions

state_cli = typer.Typer()


@state_cli.callback()
def docs():
    """Local state operations"""


@state_cli.command("get")
@handle_exceptions
def get(context: typer.Context):
    """View local state"""
    ctx: Context = context.obj

    if ctx.client:
        ctx.fmt.info(f"User name: {ctx.config.user_name}")
    else:
        ctx.fmt.failure("User name: N/A")

    if ctx.workspace_name:
        ctx.fmt.info(f"Workspace name: {ctx.workspace_name}")
    else:
        ctx.fmt.failure("Workspace name: N/A")


@state_cli.command("clear")
@handle_exceptions
def clear(context: typer.Context):
    """Clear local state"""
    ctx: Context = context.obj
    should_proceed: bool = typer.confirm("Are you sure you wish to clear your machine-local configuration?")

    if not should_proceed:
        ctx.fmt.failure("Operation cancelled")
        raise typer.Exit()

    with ctx.fmt.begin("Clearing machine-local configuration"):
        clear_configuration()
        ctx.fmt.success("Cleared machine-local configuration")
