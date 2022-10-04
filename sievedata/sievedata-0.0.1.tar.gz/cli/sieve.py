#! python3
import click
from cli.commands import projects, model, api

@click.group(
    "sieve",
    help="Sieve CLI"
)
def cli():
    pass


cli.add_command(
    cmd=model.model,
    name="model",
)
cli.add_command(
    projects.main,
    name="projects",
)

@cli.command()
def ls():
    from sieve.api.client import SieveClient
    client = SieveClient()
    for p in client.list_projects():
        print(p)

if __name__ == '__main__':
    cli()