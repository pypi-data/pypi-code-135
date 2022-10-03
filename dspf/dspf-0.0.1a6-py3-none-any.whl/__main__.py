"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Start the Data Science Portfolio CLI."""


if __name__ == "__main__":
    main(prog_name="data-science-portfolio")  # pragma: no cover
