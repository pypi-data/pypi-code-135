from pathlib import Path
from rich import print
import magic
import re


class GrepBinary(object):
    r"""
    Usage Example:

    gb = GrepBinary()
    gb.extract(src="SecureW2_JoinNow.run", keyword="#ARCHIVE#\n")
    gb.export(file_name="SecureW2_JoinNow.tar")
    """

    def __init__(self, **kwargs):
        """Init"""
        self.src = kwargs.get("src")
        self.keyword = kwargs.get("keyword")
        self.inclusive = kwargs.get("inclusive")
        self.file_name = kwargs.get("file_name")
        self.binary = b""

    def extract(self, src=b"", keyword="", inclusive=False):
        """Extract Hidden Binary From File"""
        # -- setup arguments
        src = src if src else self.src
        keyword = keyword if keyword else self.keyword
        inclusive = inclusive if inclusive else self.inclusive

        # -- read entire file or string
        if Path(src).is_file():
            with open(src, "rb") as f:
                raw_data = f.read()
        elif isinstance(src, str):
            raw_data = src.encode()
        else:
            raw_data = src

        # -- using regex to search keyword and extract contents that follow
        # -- note: '.' matches any character except newline.
        # --       '.*' will repeatingly match any character except newline
        # --       re.DOTALL flag includes newline character to '.*' matches
        if inclusive:
            regex = rf"(?P<binary>{keyword}.*)".encode()
        else:
            regex = rf"{keyword}(?P<binary>.*)".encode()
        r = re.compile(regex, re.DOTALL)
        m = r.search(raw_data)

        # -- return binary
        binary = m.group("binary") if m else False
        if binary:
            self.binary = binary
            print("[green]binary extracted successfully[/]")
            return
        print("[red]FAILED TO FIND BINARY[/]")

    def guessFileName(self, binary=b''):
        """Guess the File Name from binary"""
        mime = magic.detect_from_content(binary)
        regex = r'"(?P<file_name>.*)"'
        r = re.compile(regex)

        # -- try from mime.name
        if r.search(mime.name):
            self.file_name = r.search(mime.name).group('file_name')
            print(f'[cyan]detected filename[/]: "[yellow]{self.file_name}[/]"')
            return self.file_name

        # -- stich from mime detection
        self.file_name = Path(self.src).with_suffix(mime.mime_type.split('/')[1]).name
        return self.file_name

    def export(self, file_name="", binary=b""):
        """Export Binary to File"""
        # -- setup arguments
        binary = binary if binary else self.binary
        file_name = file_name if file_name else self.guessFileName(binary)

        # -- save binary byte-string to file
        with open(file_name, "wb") as f:
            f.write(binary)
