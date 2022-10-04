import click

import simplejson

import functools
import logging

from tabulate import tabulate
from datonius import *
import datonius.util as util
from peewee import DoesNotExist

@click.group()
@click.option('-d', '--db', 'database', default=None, metavar='PATH', help='path to a Datonius database in SQLite format.')
@click.option('-v', '--verbose', count=True)
@click.pass_context
def cli(ctx, database, verbose):
    ctx.ensure_object(dict)
    ctx.obj['database'] = database
    log_level = {0:60, 1:30, 2:20, 3:10}[verbose]
    logging.basicConfig(level=log_level,
                        format='[%(asctime)s][%(name)-12s][%(levelname)-8s] %(message)s',
                        datefmt='%m-%d %H:%M')

@cli.command()
@click.argument('names', nargs=-1, metavar="NAME")
@click.option('-o', '--output', type=click.File('wt'), default=click.get_text_stream('stdout'))
@click.option('-h', '--human-readable', 'output_format', flag_value=util.TABLE, help='Output in a human-readable table.', default=util.TABLE)
@click.option('-j', '--json', 'output_format', flag_value=util.JSON, help='Output in JSON.')
@click.option('-t', '--tsv', 'output_format', flag_value=util.TSV, help='output in TSV format.')
@click.option('-a', '--all-fields', flag_value=True, default=False)
@click.pass_context
def lookup(ctx, names, output, output_format, all_fields=False):
    "Lookup a name and retreive isolate information."
    if output_format is util.TABLE and output is not click.get_text_stream('stdout'):
        output_format = util.TSV # coerce to TSV if we're going to a file
    try:
        with make_connection(ctx.obj['database']):
            click.echo(util.lookup(names, output_format, all_fields) or f"{names} not found.", file=output)
    except Exception as e:
        click.echo(str(e), err=True)
        exit(1)

@cli.command()
@click.argument('names', nargs=-1, metavar="TAXON")
@click.option('-o', '--output', type=click.File('wt'), default=click.get_text_stream('stdout'))
@click.option('-h', '--human-readable', 'output_format', flag_value=util.TABLE, help='Output in a human-readable table.', default=util.TABLE)
@click.option('-j', '--json', 'output_format', flag_value=util.JSON, help='Output in JSON.')
@click.option('-t', '--tsv', 'output_format', flag_value=util.TSV, help='output in TSV format.')
@click.option('-a', '--all-fields', flag_value=True, default=False)
@click.pass_context
def tax(ctx, names, output, output_format, all_fields=False):
    "Lookup a taxon and retreive information for its isolates."
    if output_format is util.TABLE and output is not click.get_text_stream('stdout'):
        output_format = util.TSV # coerce to TSV if we're going to a file
    with make_connection(ctx.obj['database']):
        try:
            click.echo(util.tax(names, output_format, all_fields), file=output)
        except DoesNotExist:
            click.echo(f"{' '.join(names)} isn't a taxon in the database.", err=True)
            exit(1)
        except Exception as e:
            click.echo(str(e), err=True)
            exit(1)

if __name__ == '__main__':
    cli(obj={})