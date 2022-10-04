import os
from pathlib import Path

import click

from h2cow.create_project.new_project import new
from h2cow.data_collection.data_collection import capture_frames

@click.group()
def main():
    click.echo("h2cow started.")

###########################################################################################################################

@click.option("-p", "--path", prompt="Project path", help="Where to create project.")
@click.option("-a", "--address", prompt="Server IP-address", help="IP-address of rtsp server.")
@main.command()
def create_project(path, address):
    """Creates a new default project for h2cow."""
    path = os.path.abspath(path)
    try:
        proj = new(path, address)
    except FileExistsError:
        click.echo(f"Project already exists at '{path}': Exitting.")
        exit()
    click.echo(f"Created project at '{path}'. Please edit config.yaml there before continuing.")



###########################################################################################################################

@main.command()
@click.argument("config")
def capture(config):
    """Starting capturing data from ip cameras."""
    if not os.path.isdir(config):
        click.echo(f"Invalid configuration file '{Path(config, 'config.yaml')}'.\n Have you created a project yet?")
        exit()
    capture_frames(Path(config, "config.yaml"))
    


###########################################################################################################################