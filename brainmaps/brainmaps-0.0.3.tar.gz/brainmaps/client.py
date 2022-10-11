from itertools import chain
import click
import requests
import json

API_URL = "https://api.brainmaps.io/graphql"

body = """

"""

@click.group(chain=True)
def cli():
    """BrainMaps command-line client."""
    pass



@cli.command("register")
@click.option("--name", default="John Smith", prompt="Enter your full name", help="Your full name")
@click.option("--username", default="@johnsmith", prompt="Enter your BrainMaps username", help="Your username on BrainMaps")
def register(name, username):
    click.echo(f"Hello, {name}!")
    if username:
        click.echo(f"Your username is {username}")

@cli.command("generate")
@click.option("--apikey", default="12345abc", prompt="Your API key", help="Your API key")
def generate(apikey):
    if apikey: 
        click.echo(f"Your API Key {apikey} has been registered successfully.")

@cli.command("upload")
@click.option("--dataset", default="", prompt="Enter a dataset ID", help="Dataset ID to upload")
def upload(dataset):
    # click.echo(f"Hello, {name}!")
    if dataset:
        click.echo(f"Dataset to upload: {dataset}")
    else:
        click.echo("Please enter a dataset ID.")


@cli.command("download")
@click.option("--dataset", default="", prompt="Enter a dataset ID", help="Dataset ID to download")
def download(dataset):
    # click.echo(f"Hello, {name}!")
    if dataset:
        click.echo(f"Dataset to upload: {dataset}")
    else:
        click.echo(f"Please enter a dataset name")

cli.add_command(register)
cli.add_command(generate)
cli.add_command(upload)
cli.add_command(download)

if __name__ == "__main__":
    cli()
