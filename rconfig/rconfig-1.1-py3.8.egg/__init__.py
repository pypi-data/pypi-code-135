from pathlib import Path
import yaml, json, copy
from addict import Dict
from .utils import more_yaml

__version__ = '1.1'


class Config(object):
    def __init__(self, cfg=None, filename=None):
        super().__setattr__('_cfg', Dict(cfg))
        super().__setattr__('_cfg_filename', filename)

    @staticmethod
    def from_file(file_path):
        file_path = Path(file_path).resolve()

        if not file_path.exists():
            log_info = '{} not exist'.format(file_path.as_posix())
            raise IOError(log_info)

        # Yaml
        if file_path.suffix == '.yaml':
            with file_path.open('r', encoding='utf-8') as f:
                cfg_dict = yaml.load(f, Loader=yaml.FullLoader)
            return Config(cfg=cfg_dict, filename=file_path.name)
        # Json
        elif file_path.suffix == '.json':
            with file_path.open('r', encoding='utf-8') as f:
                cfg_dict = json.load(f)
            return Config(cfg=cfg_dict, filename=file_path.name)
        else:
            raise IOError('Not support file suffix yet.')

    def to_json(self, file_path):
        file_path = Path(file_path).resolve()
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open('w') as f:
            json.dump(self._cfg, f, indent=4 ,ensure_ascii=True)

    def __getitem__(self, name):
        return self._cfg.get(name)

    def __setitem__(self, name, value):
        self._cfg[name] = value

    def __getattr__(self, name):
        return self._cfg.get(name)

    def __setattr__(self, name, value):
        self._cfg[name] = value

    def __iter__(self):
        return iter(self._cfg)

    def __repr__(self):
        return self._cfg.__repr__()

    def __deepcopy__(self, memo):
        cls = self.__class__
        other = cls.__new__(cls)
        memo[id(self)] = other
        super(Config, other).__setattr__('_cfg', Dict())
        for key, value in self._cfg.items():
            other._cfg[key] = copy.deepcopy(value, memo)
            # setattr(other, key, copy.deepcopy(value, memo))
            # print(other[key])
    #     #     # super(Config, other).__setattr__(key, copy.deepcopy(value, memo))
    #     #     pass
        return other

