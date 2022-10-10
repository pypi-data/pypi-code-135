import sys
import os
import pathlib
import typing

# subclasses need to provide suffix / load


class ConfigBase:
    suffix = ""

    def __init__(self, path: typing.Optional[typing.Union[pathlib.Path, str]]=None):
        self._data = None
        tmp_path = self.get_config_parm()
        if tmp_path:
            self._path = tmp_path
        elif isinstance(path, pathlib.Path):
            self._path = path
        elif path is not None:
            if path[0] in '~/':
                self._path = pathlib.Path(path).expanduser()
            elif '/' in path:  # assume '!Config config_dir/config_name'
                self._path = self.config_dir / path
            else:
                self._path = self.config_dir / path / (path.rsplit('.')[-1] + self.suffix)
        else:
            # could use sys.argv[0]
            raise NotImplementedError

    @property
    def data(self) -> typing.Any:
        if self._data is None:
            self._data = self.load()  # NOQA
        return self._data

    def get(self, *args: typing.Any, pd: typing.Optional[typing.Any]=None) -> typing.Any:
        data = self.data
        try:
            for arg in args:
                if arg in data:
                    data = data[arg]
                else:
                    break
            else:
                return data
        except Exception as e:
            print(f'exception getting "{arg}" from "{args}" ({self.data})') 
            return {}
        if args[0] != 'global':
            return self.get(*(['global'] + list(args[1:])), pd=pd)
        return pd

    def get_config_parm(self) -> typing.Union[pathlib.Path, None]:
        # check if --config was given on commandline
        for idx, arg in enumerate(sys.argv[1:]):
            if arg.startswith('--config'):
                if len(arg) > 8 and arg[8] == '=':
                    return pathlib.Path(arg[9:])
                else:
                    try:
                        return pathlib.Path(sys.argv[idx + 2])
                    except IndexError:
                        print('--config needs an argument')
                        sys.exit(1)
        return None

    @property
    def config_dir(self) -> pathlib.Path:
        # https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
        attr = '_' + sys._getframe().f_code.co_name
        if not hasattr(self, attr):
            if sys.platform.startswith('win32'):
                d = os.environ['APPDATA']
            else:
                d = os.environ.get(
                    'XDG_CONFIG_HOME', os.path.join(os.environ['HOME'], '.config')
                )
            pd = pathlib.Path(d)
            setattr(self, attr, pd)
            return pd
        return getattr(self, attr)  # type: ignore

    def load(self) -> typing.Any:
        raise NotImplementedError
