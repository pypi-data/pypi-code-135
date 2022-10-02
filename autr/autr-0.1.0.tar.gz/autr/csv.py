import pandas as pd

from .base import Reader


class CSVReader(Reader, extensions=(".csv",)):
    def _read(self, filename: str, *args, **kwargs) -> pd.DataFrame:
        return pd.read_csv(filename, *args, **kwargs)

    def _write(self, filename: str, *args, **kwargs):
        if not isinstance(self.data, pd.DataFrame):
            self._data = pd.DataFrame(self.data)

        self.data.to_csv(filename, *args, **kwargs)
