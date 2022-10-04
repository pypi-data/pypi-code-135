from abc import ABC, abstractmethod
from typing import List, Tuple, Union
import json

from . import utils


class WsFormulator(ABC):
    method: utils.WsMethod
    channel: utils.WsChannel

    id: int = 1

    @property
    @abstractmethod
    def template(self):
        pass

    def if_json_decorator(func):
        def wrapper(self, *args, **kwargs):
            res = func(self, *args, **kwargs)
            is_json = kwargs.get("json_str", False)
            if is_json:
                return json.dumps(res)
            return res
        return wrapper

    @abstractmethod
    def formulate_request(self, method: utils.WsMethodEnum, channel: utils.WsChannelEnum, **kwargs):
        self_method: str = getattr(self.method, method.value)
        self_channel: str = getattr(self.channel, channel.value)
        return self_method, self_channel

    @abstractmethod
    def formulate_requests(self, method: utils.WsMethodEnum, channel_kwargs_list: List[Tuple[utils.WsChannelEnum, Union[dict, None]]], **kwargs):
        res_list = []
        for channel_kwargs in channel_kwargs_list:
            kwargs = channel_kwargs[1] if channel_kwargs[1] != None else {}
            res_list.append(
                self.formulate_request(
                    method,
                    channel_kwargs[0],
                    **kwargs
                )
            )
        return res_list