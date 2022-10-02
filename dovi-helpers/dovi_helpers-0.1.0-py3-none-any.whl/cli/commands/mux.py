import pathlib
import subprocess

import click
import structlog

INFO_DATA_FILENAME = "mediainfo.data.json"

log = structlog.get_logger(__name__)


@click.command()
@click.argument("file", type=click.Path(exists=True, path_type=pathlib.Path))
def mux(file: pathlib.Path) -> None:
    """Muxing HEVC and AC3 streams into compatible MP4 container."""

    _log = log.bind(file=str(file))
    log.info("mux.started")

    sources = " ".join(
        [f'-i "{source}"' for source in file.parent.glob(f"{file.name}.*")]
    )

    command = (
        f"mp4muxer --dv-profile 8 --dv-bl-compatible-id 1 {sources} "
        "--hvc1flag 0 --mpeg4-comp-brand mp42,iso6,isom,msdh,dby1 "
        f'--overwrite -o "{file.absolute()}.dovi81.mp4"'
    )

    result = subprocess.run(command, capture_output=True, shell=True, text=True)

    _log.info(
        "mux.video.finished",
        returncode=result.returncode,
        stdout=result.stdout.strip(),
        stderr=result.stderr.strip(),
    )
