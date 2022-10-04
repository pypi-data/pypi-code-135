from typing import List, Tuple, Union

from . import formulator
from . import utils


class BinanceWsRequestParamsGenerator:

    @staticmethod
    def trade(**kwargs):
        base_token: str = kwargs["base_token"]
        quote_token: str = kwargs["quote_token"]
        return f"{base_token.lower()}{quote_token.lower()}@<channel>"

    @staticmethod
    def book_ticker(**kwargs):
        return BinanceWsRequestParamsGenerator.trade(**kwargs)


class BinanceWsFormulator(formulator.WsFormulator):
    method = utils.WsMethod(
        subscribe="SUBSCRIBE",
        unsubscribe="UNSUBSCRIB"
    )
    channel = utils.WsChannel(
        trade="trade",
        book_ticker="bookTicker"
    )

    @property
    def template(self):
        return {
            "method": "",
            "params": None,
            "id": self.id
        }

    @formulator.WsFormulator.if_json_decorator
    def formulate_request(self, method: utils.WsMethodEnum, channel: utils.WsChannelEnum, **kwargs):
        self_method, self_channel = super().formulate_request(method, channel, **kwargs)
        params_ori: str = getattr(BinanceWsRequestParamsGenerator, channel.name.lower())(**kwargs)
        params = params_ori.replace("<channel>", self_channel)
        template = self.template
        template["method"] = self_method
        template["params"] = [params]
        return template

    @formulator.WsFormulator.if_json_decorator
    def formulate_requests(self, method: utils.WsMethodEnum, channel_kwargs_list: List[Tuple[utils.WsChannelEnum, Union[dict, None]]], **kwargs):
        res_list = super().formulate_requests(method, channel_kwargs_list)
        params = []
        for res in res_list:
            params.append(res["params"][0])
        final_res = res_list[-1]
        final_res["params"] = params
        return final_res
