import urllib.request
import tarfile
import io
import json
import pathlib
import shutil
import tempfile

__package_name__ = "deephaven_plugin_plotly_js"
__version__ = "0.1.0.dev6"  # needs to be static

__npm_org__ = "@deephaven"
__npm_package__ = "js-plugin-plotly"
__npm_version__ = "0.1.0"

__plugin_dist__ = "dist"


def _npm_url():
    return f"https://registry.npmjs.org/{__npm_org__}/{__npm_package__}/-/{__npm_package__}-{__npm_version__}.tgz"


def _dist_path(dst):
    return pathlib.Path(dst) / __package_name__ / __plugin_dist__


def _info_path(dst):
    return pathlib.Path(dst) / __package_name__ / "__info__.py"


# https://pdm.fming.dev/latest/pyproject/build/#custom-file-generation
def build(src, dst):
    with tempfile.TemporaryDirectory() as tmp_dir:

        # Extract to temporary directory - easier to manipulate after extracting from tar
        tmp_dir_path = pathlib.Path(tmp_dir)
        with urllib.request.urlopen(_npm_url()) as tgz:
            with tarfile.open(fileobj=io.BytesIO(tgz.read()), mode="r") as tar:
                tar.extractall(tmp_dir_path)

        # Extracting package/dist/ into __plugin_dist__, and ensuring we strip the appropriate prefix from main
        with open(tmp_dir_path / "package" / "package.json") as json_file:
            package_json = json.load(json_file)
            name = package_json["name"]
            version = package_json["version"]
            main = package_json["main"].removeprefix("dist/")
        dist_path = _dist_path(dst)
        if dist_path.is_dir():
            shutil.rmtree(dist_path)
        shutil.move(tmp_dir_path / "package" / "dist", dist_path)

    with open(_info_path(dst), "w") as version_file:
        version_file.writelines(
            [
                f'__version__ = "{__version__}"\n',
                f'__npm_org__ = "{__npm_org__}"\n',
                f'__npm_package__ = "{__npm_package__}"\n',
                f'__npm_version__ = "{__npm_version__}"\n',
                f'__plugin_name__ = "{name}"\n',
                f'__plugin_version__ = "{version}"\n',
                f'__plugin_main__ = "{main}"\n',
                f'__plugin_dist__ = "{__plugin_dist__}"\n',
            ]
        )
