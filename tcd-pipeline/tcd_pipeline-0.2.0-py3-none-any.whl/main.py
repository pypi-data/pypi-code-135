"""
Main CLI application.
"""
import click

from tcd_pipeline.commands import generate_workflows


@click.group(help="TCD Pipeline tools")
def cli():
    """Main cli function"""


cli.add_command(generate_workflows.generate_workflows)

if __name__ == '__main__':
    cli()
