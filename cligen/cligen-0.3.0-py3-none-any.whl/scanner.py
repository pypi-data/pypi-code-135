import datetime
from pathlib import Path


class Scanner:
    """scans for files to update"""

    def __init__(self, patterns):
        self._patterns = patterns

    def __call__(self):
        base_path = Path('.')
        for pattern in self._patterns:
            for fn in base_path.glob(pattern):
                if fn.is_dir():
                    continue
                upd = Updater(fn)
                if upd.todo:
                    yield upd


class Updater:
    def __init__(self, path):
        self._todo = True
        self._path = path
        text = path.read_text()
        if path.name == '__init__.py':
            if '_cligen_data' not in text:
                self._todo = False
                return
        self._text = text.splitlines()
        self._start_line = 0
        self._end_line = len(self._text)

    @property
    def todo(self):
        return self._todo

    def replace(self, frm, to, backup=None):
        changed = False
        for idx, line in enumerate(self._text):
            if idx < self._start_line:
                continue
            if idx > self._end_line:
                break
            if frm in line:
                if not changed:
                    changed = True
                    print('fn', self._path)
                print(' <', line)
                newline = line.replace(frm, to)
                print(' >', newline)
                self._text[idx] = newline
        if not changed:
            return
        backup_path = (
            self._path.parent / f'{self._path.name}.{datetime.datetime.now():%Y%m%d-%H%M%S}'
        )
        self._path.rename(backup_path)
        self._path.write_text('\n'.join(self._text) + '\n')
