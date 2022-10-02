import pathlib
import subprocess
from collections import Counter
from typing import List

import click
import structlog

from dovi_helpers.helpers import INFO_DATA_FILENAME, mediainfo_file_generator
from dovi_helpers.models.info import MediaInfoData

log = structlog.get_logger(__name__)


@click.command()
@click.argument("path", type=click.Path(exists=True, path_type=pathlib.Path))
@click.option("--force", "-f", is_flag=True, type=bool, default=False)
def info(path: pathlib.Path, *, force: bool) -> List[MediaInfoData]:
    """Gathering mediainfo data into cached file. It is required to demux/mux later."""
    need_to_analyze = force
    data_file = pathlib.Path(INFO_DATA_FILENAME)

    if data_file.exists() and not force:
        need_to_analyze: bool = click.prompt(
            f"{INFO_DATA_FILENAME} already exists, "
            f"do you want to force analyzing again (yes/no)",
            type=bool,
        )

    if need_to_analyze:
        subprocess.run(
            ["mediainfo", "--Output=JSON", f"--LogFile={INFO_DATA_FILENAME}", path],
            capture_output=True,
        )
    else:
        log.info("info.loading_data_file", file=INFO_DATA_FILENAME)

    counter = Counter()
    records: List[MediaInfoData] = []
    for data_record in mediainfo_file_generator():
        records.append(data_record)
        counter["files"] += 1
        _log = log.bind(file=data_record.media.ref)

        for track in data_record.media.tracks:
            counter[track.type] += 1
            _log.info(f"info.{track.type.lower()}.detected", **track.dict())

    files_count = counter.pop("files")
    log.info(
        "info.summary",
        files_count=files_count,
        streams_count=sum(counter.values()),
        **counter,
    )
    return records
