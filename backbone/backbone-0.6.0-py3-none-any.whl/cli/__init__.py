import typer

from backbone.cli._format import DecoratedFormatter, Format, PlainFormatter
from backbone.cli._models import Context
from backbone.cli._utilities import clear_configuration, config_to_backbone, read_configuration
from backbone.cli.entry import entry_cli
from backbone.cli.namespace import namespace_cli
from backbone.cli.state import state_cli
from backbone.cli.stream import stream_cli
from backbone.cli.user import user_cli
from backbone.cli.workspace import workspace_cli

""" COMMAND LINE INTERFACE ROUTING """
backbone_cli = typer.Typer()
backbone_cli.add_typer(state_cli, name="state")
backbone_cli.add_typer(stream_cli, name="stream")
backbone_cli.add_typer(user_cli, name="user")
backbone_cli.add_typer(workspace_cli, name="workspace")
backbone_cli.add_typer(namespace_cli, name="namespace")
backbone_cli.add_typer(entry_cli, name="entry")


@backbone_cli.callback()
def callback(
    context: typer.Context,
    workspace_name: str = typer.Option(None, "--workspace"),
    fmt: Format = typer.Option(Format.DECORATED, "-f", "--format"),
):
    """
    End-to-end encryption as a service
    """
    configuration = read_configuration()
    client = configuration and config_to_backbone(configuration)
    formatter = PlainFormatter() if fmt == Format.PLAIN else DecoratedFormatter()
    workspace_name = workspace_name or (configuration and configuration.workspace_name)
    context.obj = Context(config=configuration, client=client, workspace_name=workspace_name, fmt=formatter)
