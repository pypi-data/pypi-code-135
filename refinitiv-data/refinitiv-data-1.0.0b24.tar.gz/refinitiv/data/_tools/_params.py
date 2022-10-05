from dataclasses import dataclass
from typing import Callable, List


@dataclass
class ParamItem:
    arg_name: str
    query_param_name: str
    function: Callable = None


class ValueParamItem(ParamItem):
    def __init__(self, arg_name, query_param_name, function):
        super().__init__(arg_name, query_param_name)
        self.function = lambda value, *args, **kwargs: function(value)


def get_params(params_config: List[ParamItem], *args, **kwargs):
    retval = []
    for item in params_config:
        param = kwargs.get(item.arg_name)
        if param is None:
            continue

        if item.function:
            _kwargs = {k: v for k, v in kwargs.items() if k != item.arg_name}
            param = item.function(param, *args, **_kwargs)
        retval.append((item.query_param_name, param))
    return retval
