from concurrent.futures import ThreadPoolExecutor, wait
from dataclasses import dataclass
from typing import Iterable, Optional, cast
import typer
import os
import subprocess
from fnmatch import fnmatch
from pathlib import Path
from PTN import parse
from rich.progress import Progress
from threading import Lock

from tv_audio_extractor.utils import flatten


_video_matchers = '*.mp4', '*.mkv'

@dataclass(frozen=True)
class VideoMetadata:
    show: str
    episode_name: str
    season_num: int
    episode_num: int

    def __str__(self) -> str:
        return f'{self.show} - S{self.season_num}E{self.episode_num} - {self.episode_name}'


class ScanException(Exception):
    def __init__(self, path: str, message: str):
        super().__init__(message)
        self.path = path
        self.message = message


def _is_video_file(filename: str) -> bool:
    for matcher in _video_matchers:
        if fnmatch(filename, matcher):
            return True

    return False


def _find_video_files(path: Path) -> Iterable[str]:
    for root, dirs, files in os.walk(path):
        for file in files:
            if _is_video_file(file):
                yield os.path.join(root, file)


def _scan_video(path: str) -> VideoMetadata:
    filename = Path(path).stem
    filename = filename.replace("'", '') # doesn't seem to like apostrophes
    expected_fields = 'season', 'episode', 'title', 'episodeName'
    result = parse(filename)

    def verify_all_fields() -> None:
        missing = []

        for field in expected_fields:
            if field not in result:
                missing.append(field)

        if missing:
            missing_fields_str = ','.join(missing)
            message = f'Missing metadata fields [{missing_fields_str}]'
            raise ScanException(filename, message)

    def normalize_episode_num() -> int:
        value = result['episode']

        if isinstance(value, int):
            return value
        elif isinstance(value, list):
            # just take the first if it has many
            return cast(int, value[0])
        else:
            raise ValueError(f'episode num has unexpected type: {type(value)}')


    verify_all_fields()

    return VideoMetadata(
        show=result['title'],
        episode_name=result['episodeName'],
        season_num=result['season'],
        episode_num=normalize_episode_num()
    )


@dataclass(frozen=True)
class TranscodeTask:
    source: str
    destination: str
    metadata: VideoMetadata


def _mk_output_path(output: Path, metadata: VideoMetadata) -> Path:
    filename = f'S{str(metadata.season_num).zfill(2)}E{str(metadata.episode_num).zfill(2)} - {metadata.episode_name}.mp3'
    return output / metadata.show / filename


def _mk_transcode_tasks(video_paths: Iterable[str], output: Path) -> Iterable[TranscodeTask]:
   for path in video_paths:
        try:
            metadata = _scan_video(path)
            destination = _mk_output_path(output, metadata)

            # only yield those that exist
            if not destination.exists():
                yield TranscodeTask(path, str(destination), metadata)

        except ScanException as scan_ex:
            print(f'ERROR: Could not parse video filename [{scan_ex.path}]: {scan_ex.message}') 


_create_destination_dir_lock = Lock()

def _ensure_destination_dir(destination: str) -> None:
    destination_path = Path(destination)
    parent_dir = destination_path.parent

    # double checked lock
    if not parent_dir.exists():
        _create_destination_dir_lock.acquire()
        try:
            if not parent_dir.exists():
                parent_dir.mkdir(parents=True)
        finally:
            _create_destination_dir_lock.release()


def _transcode(task: TranscodeTask) -> None:
    _ensure_destination_dir(task.destination)

    # tags taken from https://wiki.multimedia.cx/index.php?title=FFmpeg_Metadata#MP3
    metadata_tags: dict[str, str] = dict(
        album=task.metadata.show,
        artist=task.metadata.show,
        title=task.metadata.episode_name,
        disc=str(task.metadata.season_num),
        track=str(task.metadata.episode_num)
    )

    metadata_args: list[str] = list(flatten(map(lambda item: [ '-metadata', f'{item[0]}={item[1]}'], metadata_tags.items())))

    args = [ 
        'ffmpeg',
        '-hide_banner',
        '-loglevel', 'error',
        '-i', task.source,
        *metadata_args,
        task.destination
    ]

    subprocess.run(args, check=True)


def _lookup_cpu_count() -> int:
    return os.cpu_count() or 1


def _main(
    output: Path, 
    inputs: list[Path], 
    threads:Optional[int] = typer.Option(None, help='Number of concurrent threads to transcode with (defaults to cpu count)')
):
    video_files = set(flatten(map(_find_video_files, inputs)))

    tasks = list(_mk_transcode_tasks(video_files, output))

    max_workers = threads or _lookup_cpu_count()

    print(f'Transcoding {len(tasks)} files using {max_workers} threads')

    with Progress() as progress, ThreadPoolExecutor(max_workers=max_workers) as executor:
        progress_task_id = progress.add_task('Transcoding', total=len(tasks))

        def run(task: TranscodeTask) -> None:
            progress.console.print(str(task.metadata))
            try:
                _transcode(task)
            except Exception as ex:
                progress.console.print(f'[bold red]ERROR[/] Failed to transcode {task.source}')
                progress.console.print(str(ex))
                dest_path = Path(task.destination)
                if dest_path.exists():
                    os.remove(dest_path)

            progress.advance(progress_task_id)

        task_result_futures = list(map(lambda task: executor.submit(run, task), tasks))

        wait(task_result_futures)



def main():
    typer.run(_main)


if __name__ == "__main__":
    typer.run(_main)