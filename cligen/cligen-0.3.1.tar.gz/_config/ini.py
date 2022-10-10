import configparser
import typing

from ._base import ConfigBase


class ConfigINI(ConfigBase):
    suffix = '.ini'

    def load(self) -> typing.Any:
        config = configparser.ConfigParser()
        config.read(self._path)
        data = {}
        for section in config.sections():
            sl = section.lower().split('.')
            if not sl[0] == 'defaults':
                continue
            if len(sl) == 1:
                data['global'] = dict(config.items(section))
            elif len(sl) == 2:
                data[sl[1]] = dict(config.items(section))
            else:
                raise NotImplementedError
        return data
