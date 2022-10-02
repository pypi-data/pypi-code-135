import click

from oihelper.cli.run_program import run
from oihelper.cli.parse_problem import parse
from oihelper.cli.login import login
from oihelper.cli.submit_program import submit, record


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def unsafe_cli():
    pass


unsafe_cli.add_command(run)
unsafe_cli.add_command(parse)
unsafe_cli.add_command(login)
unsafe_cli.add_command(submit)
unsafe_cli.add_command(record)


def cli():
    try:
        unsafe_cli()
    except Exception as err:
        click.echo(
            f"{click.style('fatal error: ', fg='red', bold=True)}{click.style(err, bold=True)}"
        )
        click.echo(
            f"{click.style('note: ', fg='blue', bold=True)}If you believe this is an internal error caused by OIHelper itself, please file an issue to OIHelper GitHub and include all error messages above."
        )
        click.echo(click.style("Exiting due to an unexpected error."))


if __name__ == "__main__":
    cli()
