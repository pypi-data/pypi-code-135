import os
from pathlib import Path
from typing import Optional

import pooch
import typer

__all__ = ["app"]

app = typer.Typer()

url_doc = """
The URL to the file that is to be downloaded. Ideally, the URL should
end in a file name.
"""

hash_doc = """
A known hash (checksum) of the file. Will be used to verify the
download or check if an existing file needs to be updated. By default,
will assume it's a SHA256 hash. To specify a different hashing method,
prepend the hash with ``algorithm:``, for example
``md5:pw9co2iun29juoh`` or ``sha1:092odwhi2ujdp2du2od2odh2wod2``. If
None, will NOT check the hash of the downloaded file or check if an
existing file needs to be updated.
"""

filename_doc = """
The name that will be used to save the file. Should NOT include the
full the path, just the file name (it will be appended to *path*). If
None, will create a unique file name using a combination of the last
part of the URL (assuming it's the file name) and the MD5 hash of the
URL. For example, ``81whdo2d2e928yd1wi22-data-file.csv``. This ensures
that files from different URLs never overwrite each other, even if they
have the same name.
"""

cachedir_doc = """
The location of the cache folder on disk. This is where the file will
be saved. If None, will save to a ``pooch`` folder in the default cache
location for your operating system (see :func:`pooch.os_cache`).
"""

progress_doc = """
If True, will print a progress bar of the download to standard error
(stderr).
"""


@app.callback()
def dl(
    url: str = typer.Argument(url_doc),
    hash: Optional[str] = typer.Option(None, help=hash_doc),
    filename: Optional[str] = typer.Option(None, help=filename_doc),
    cachedir: Optional[str] = typer.Option(None, help=cachedir_doc),
    progress: bool = typer.Option(False, help=progress_doc),
):
    if filename is not None:
        filename = os.path.basename(filename)
    typer.echo(f"Download: {url}")
    typer.echo(f"known_hash: {hash}")
    typer.echo(f"fname: {filename}")
    typer.echo(f"path: {cachedir}")
    typer.echo(f"progressbar: {progress}")
    filepath = pooch.retrieve(
        url=url, known_hash=hash, fname=filename, path=cachedir, progressbar=progress
    )
    typer.echo(f"filepath: {filepath}")
    if filename is None:
        filename = os.path.basename(filepath).split("-", 1)[1]

    assert filename is not None
    target_path = Path(os.getcwd()) / filename
    os.link(filepath, target_path)
