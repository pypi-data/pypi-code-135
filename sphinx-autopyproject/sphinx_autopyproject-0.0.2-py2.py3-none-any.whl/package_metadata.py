from email import message_from_bytes
from email.header import Header
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict, List, Literal, Union

from build import PathType, ProjectBuilder
from build.env import IsolatedEnvBuilder


def get_metadata_by_build(
    srcdir: PathType = ".",
    distribution: Union[Literal["wheel"], Literal["sdist"]] = "wheel",
) -> Dict[str, Union[str, List[str]]]:
    # sadly not that straightforward ...
    # create a temporary env and install build requirements
    with IsolatedEnvBuilder() as env:
        builder = ProjectBuilder(srcdir)
        builder.python_executable = env.executable
        builder.scripts_dir = env.scripts_dir

        env.install(builder.build_system_requires)
        env.install(builder.get_requires_for_build(distribution))

        # create temporary directory for metadata
        with TemporaryDirectory() as temp_dir:
            # ... and populate it
            dist_info = builder.metadata_path(temp_dir)
            dist_info_data = (Path(dist_info) / "METADATA").read_bytes()

    # everything is cleaned up now and the data in dist_info_data
    result: Dict[str, Union[str, List[str]]] = {}

    for key, value in message_from_bytes(dist_info_data).items():
        if isinstance(value, Header):
            value_str = value.encode()
        else:
            value_str = str(value)
        key = key.capitalize()

        if key in result:
            current = result[key]
            if isinstance(current, list):
                current.append(value_str)
            else:
                result[key] = [current, str(value_str)]
        else:
            result[key] = value_str

    return result
