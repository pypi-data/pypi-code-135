import click


def print_cmd_step__(cmd):
    print_step__(cmd, 'blue')


def print_step__(step, color):
    click.echo(click.style('>> ' + step, fg=color))
