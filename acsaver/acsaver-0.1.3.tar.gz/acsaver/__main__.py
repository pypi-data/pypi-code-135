# coding=utf-8
import click
from acfunsdk import Acer
from acsaver import AcSaver, live_recorder

__author__ = 'dolacmeo'


@click.command()
@click.argument('cmd_name')
@click.option("-url", type=str)
@click.option("-root", type=str)
@click.option("--args", nargs=3)
def cli(cmd_name, url, root, args):
    if cmd_name == 'live_recorder':
        acer = Acer()
        live_obj = acer.get(args[0]).live
        return live_recorder(live_obj, *args[1:])
    elif cmd_name == "download":
        obj = AcSaver(Acer(), root).get(url)
        return obj.save_all()
    return True


if __name__ == '__main__':
    cli()
