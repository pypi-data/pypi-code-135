import itertools
import multiprocessing
import pathlib
import subprocess

import click
import structlog

from dovi_helpers.helpers import mediainfo_file_generator
from dovi_helpers.initializers import init_system
from dovi_helpers.models.data import AudioData, TrackData, TrackType, VideoData
from dovi_helpers.models.info import Media

INFO_DATA_FILENAME = "mediainfo.data.json"

log = structlog.get_logger(__name__)


@click.command()
@click.argument("file", type=click.Path(exists=True, path_type=pathlib.Path))
def demux(file: pathlib.Path) -> None:
    """Demuxing MKV container into HEVC and AC3 streams."""
    _log = log.bind(file=str(file))
    log.info("demux.started")

    record = get_record(file)

    with multiprocessing.Pool(
        multiprocessing.cpu_count(), initializer=init_system
    ) as pool:
        for track_type, group in itertools.groupby(record.tracks, track_group_key_func):
            if track_type == TrackType.VIDEO:
                for idx, video_stream in enumerate(group):
                    pool.apply_async(demux_video, args=[file, video_stream, idx])
            if track_type == TrackType.AUDIO:
                for idx, audio_stream in enumerate(group):
                    pool.apply_async(demux_audio, args=[file, audio_stream, idx])

        pool.close()
        pool.join()

    log.info("demux.finished")


def demux_video(file: pathlib.Path, video_stream: VideoData, idx: int):
    command = (
        f'ffmpeg -i "{file.absolute()}" -c:v copy -vbsf hevc_mp4toannexb -f hevc - | '
        f'dovi_tool -m 2 convert --discard -o "{file.absolute()}.BL_RPU.hevc" -'
    )

    _log = log.bind(
        command=command, file=str(file), idx=idx, video_stream=video_stream.dict()
    )
    _log.info("demux.video.started")

    result = subprocess.run(command, capture_output=True, shell=True, text=True)

    _log.info(
        "demux.video.finished",
        returncode=result.returncode,
        stdout=result.stdout.strip(),
        stderr=result.stderr.strip(),
    )


def demux_audio(file: pathlib.Path, audio_stream: AudioData, idx: int):
    _log = log.bind(file=str(file), idx=idx, audio_stream=audio_stream.dict())

    if audio_stream.codec_id == "A_TRUEHD":
        return
    elif audio_stream.codec_id == "A_AC3":
        extension = "ac3"
    else:
        _log.error("demux.audio.unknown_codec", codec_id=audio_stream.codec_id)
        return

    output_file = file.parent / f"{file.name}.audio{idx}.{extension}"
    command = (
        f'ffmpeg -y -i "{file.absolute()}" -c:a copy -map 0:a:{idx} '
        f'"{output_file.absolute()}"'
    )
    _log = _log.bind(command=command, file=str(file), output_file=output_file)
    _log.info("demux.audio.started")

    result = subprocess.run(command, capture_output=True, shell=True, text=True)

    _log.info(
        "demux.audio.finished",
        returncode=result.returncode,
        stdout=result.stdout.strip(),
        stderr=result.stderr.strip(),
    )


def track_group_key_func(track: TrackData) -> TrackType:
    return track.type


def get_record(file: pathlib.Path) -> Media:
    for record in mediainfo_file_generator():
        if pathlib.Path(record.media.ref).absolute() == file.absolute():
            return record.media

    log.error("demux.record.not_found", file=str(file))
    raise click.Abort("Record not found. Unable to proceed.")
