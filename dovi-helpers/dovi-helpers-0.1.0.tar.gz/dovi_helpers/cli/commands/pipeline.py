import pathlib
from typing import List

import click
import structlog

from dovi_helpers.cli.commands import demux, info, mux
from dovi_helpers.models.info import MediaInfoData

INFO_DATA_FILENAME = "mediainfo.data.json"

log = structlog.get_logger(__name__)


@click.command()
@click.pass_context
@click.argument("path", type=click.Path(exists=True, path_type=pathlib.Path))
def pipeline(ctx: click.Context, path: pathlib.Path) -> None:
    """Command to chain info, demux and mux operations."""
    records: List[MediaInfoData] = ctx.invoke(info, path=path, force=True)

    for record in records:
        ctx.invoke(demux, file=record.media.ref)
        ctx.invoke(mux, file=record.media.ref)
