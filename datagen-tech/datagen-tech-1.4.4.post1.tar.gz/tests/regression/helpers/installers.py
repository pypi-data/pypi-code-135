import subprocess
import sys


def install_sdk(from_test_pypi: bool) -> None:
    if from_test_pypi:
        subprocess.check_call(
            [
                sys.executable, "-m", "pip", "install", "-q", "--index-url=https://test.pypi.org/simple/",
                "--extra-index-url=https://pypi.org/simple", "datagen-tech", "--upgrade"
            ]
        )
    else:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-q", "datagen-tech", "--upgrade"]
        )
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "ipython", "--upgrade"])
    subprocess.check_call([sys.executable, "-m", "pip", "show", "datagen-tech"])


def install_prettyprinter() -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "prettyprinter==0.17.0"])
