from pathlib import Path

import click
import uvicorn
from click.core import Group
from dynamic_imports import class_instances_from_package

from . import pages
from .utils import static_dir
from .core.compiler import WebPage, compile_web_pages

cli = Group("pyui")


@cli.command()
def compile():
    web_pages = class_instances_from_package(
        class_type=WebPage,
        package=pages,
    )
    click.echo(
        click.style(
            f"Compiling {len(web_pages)} pages:\n{[p.html.title for p in web_pages]}",
            fg="cyan",
        )
    )
    compile_web_pages(
        pages=web_pages,
        output_dir=Path(__file__).parent.joinpath("static"),
    )


@cli.command()
@click.option("-p", "--port", default=8000)
@click.option("-h", "--host", default="0.0.0.0")
@click.option("-l", "--log-level", default="info")
@click.option("-r", "--reload", is_flag=True)
def serve(port, host, log_level, reload):
    uvicorn.run(
        "danklabs.ui.server:app",
        port=port,
        host=host,
        log_level=log_level,
        reload=reload,
    )
