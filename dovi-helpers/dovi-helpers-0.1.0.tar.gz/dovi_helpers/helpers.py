import multiprocessing
import subprocess
from typing import Iterator, List

import structlog
from pydantic import ValidationError, parse_file_as

from dovi_helpers.initializers import init_system
from dovi_helpers.models.info import MediaInfoData

REQUIRED_COMMANDS = [
    "mediainfo",
    "mp4muxer",
    "dovi_tool",
]

log = structlog.get_logger(__name__)


def check_command_missing(name: str) -> bool:
    result = subprocess.run(["which", name], capture_output=True, text=True)
    log.debug(
        "check_command_missing.result",
        name=name,
        returncode=result.returncode,
        stdout=result.stdout.strip(),
        stderr=result.stderr.strip(),
    )

    if is_missing := result.returncode != 0:
        log.warning("check_command_missing.command.not_found", name=name)

    return is_missing


def check_prerequisites_ok() -> bool:
    have_missing_requirement = False

    with multiprocessing.Pool(
        min(len(REQUIRED_COMMANDS), multiprocessing.cpu_count()),
        initializer=init_system,
    ) as pool:
        for is_missing in pool.imap_unordered(check_command_missing, REQUIRED_COMMANDS):
            if is_missing:
                have_missing_requirement = True

    return not have_missing_requirement


INFO_DATA_FILENAME = "mediainfo.data.json"


def mediainfo_file_generator() -> Iterator[MediaInfoData]:
    try:
        mediainfo_data: List[MediaInfoData] = parse_file_as(
            List[MediaInfoData], INFO_DATA_FILENAME
        )
    except ValidationError as err:
        if "value is not a valid list" not in str(err):
            raise RuntimeError(
                f"Unable to load data from {INFO_DATA_FILENAME}"
            ) from err

        try:
            mediainfo_data = [MediaInfoData.parse_file(INFO_DATA_FILENAME)]
        except ValidationError as err:
            raise RuntimeError(
                f"Unable to load data from {INFO_DATA_FILENAME}"
            ) from err

    yield from mediainfo_data
