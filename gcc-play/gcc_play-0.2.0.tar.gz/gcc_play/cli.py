from sys import is_finalizing
import click
from pathlib import Path
from random import randint
import subprocess as sp


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option("-c", "--compile", is_flag=True)
@click.option("-S", "--silent", is_flag=True)
@click.option("-D", "--debug", is_flag=True)
@click.option("-f", "--force", is_flag=True)
def gcc_play(compile, silent, debug, force, filename):
    p = Path()
    cwd = p.cwd()
    filename = Path(filename)
    filepath = cwd / Path(filename)

    if compile:
        out_filepath = cwd / filename.parent / Path(filename.stem)

        # * conflict check
        if (out_filepath.is_file()) and (not force):
            is_confirm = click.confirm(
                "A compiled file already exists. Do you want to overwrite it?",
                abort=False,
                default=True,
            )
            if not is_confirm:
                return 0

        # * compile
        sp.run(f"gcc {filepath} -o {out_filepath}", shell=True)
        if not silent:
            click.echo(f"compiled {filename} as {out_filepath}.")

    else:
        out_filepath = (
            cwd
            / filename.parent
            / Path(
                f"{filename.stem}.{''.join([str(randint(0, 9)) for _ in range(16)])}.out"
            )
        )

        # * compile
        sp.run(f"gcc {filepath} -o {out_filepath}", shell=True)

        # * exec compiled file
        sp.run(f"{out_filepath}", shell=True)
        sp.run(f"rm {out_filepath}", shell=True)

    if debug:
        click.echo(f"\n---DEBUG MESSAGES---")
        click.echo(f"cwd: {cwd}")
        click.echo(f"filename: {filename}")
        click.echo(f"filename_stem: {filename.stem}")
        click.echo(f"filepath: {filepath}")
        click.echo(f"out_filepath: {out_filepath}")

    return 0
