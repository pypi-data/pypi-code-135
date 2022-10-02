from .base import Reader


class TextReader(Reader, extensions=(".txt", ".md")):
    def _read(self, filename: str, *args, split_lines: bool = False, **kwargs) -> str:
        with open(filename, "r", *args, **kwargs) as f:
            if split_lines:
                return f.readlines()
            return f.read()

    def _write(self, filename: str, *args, **kwargs):
        with open(filename, "w", *args, **kwargs) as f:
            if isinstance(self.data, str):
                f.write(self.data)
            else:
                f.writelines(self.data)
