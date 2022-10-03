"""通达信实时行情"""


from enum import Enum
import json
import pathlib
import time
import contextlib

from multiprocessing.dummy import Process
from queue import PriorityQueue

from pytdx.hq import TdxHq_API, TDXParams
from pytdx.config.hosts import hq_hosts
from vxutils import logger
from vxquant.model.tools.tdxData import (
    tdxETFLOFTickConvter,
    tdxStockTickConvter,
    tdxConBondTickConvter,
)
from vxquant.model.preset import vxMarketPreset
from vxquant.model.contants import SecType


class vxTdxAPI:
    def __init__(self, host_file="etc/tdxhosts.json") -> None:
        self._tdxapi = None
        self._connect_time = 0
        self._host_file = host_file
        self._hosts = PriorityQueue()
        self._process = None
        if pathlib.Path(host_file).is_file():
            with open(host_file, "r", encoding="utf-8") as fp:
                hosts = json.load(fp)
                for host in hosts:
                    self._hosts.put_nowait(host)

        if self._hosts.empty():
            self._reflash_servers()

    def _reflash_servers(self, hosts=None) -> None:
        if hosts is None:
            hosts = hq_hosts
        tdxapi = TdxHq_API()
        cnt = 0
        for server_name, host, port in hosts:
            start = time.perf_counter()
            if tdxapi.connect(host, port, time_out=0.5):
                cnt += 1
                cost = (time.perf_counter() - start) * 1000
                self._hosts.put_nowait((cost, host, port))
                logger.info(f"测试链接: {server_name}({host}:{port} 成功{cnt}个: {cost:.4f}ms")
                if cnt > 0:
                    tdxapi.close()
                    break
            else:
                logger.debug(f"测试链接: {server_name}({host}:{port} 超时")

        try:
            with open(self._host_file, "w", encoding="utf-8") as fp:
                json.dump(self._hosts.queue, fp, indent=4)
        except OSError as err:
            logger.warning(f"{self._host_file}不存在，没有保存hosts信息: {err}")

    @contextlib.contextmanager
    def get_fastest_api(self):
        while self._tdxapi is None:
            if self._hosts.qsize() <= 5 and (
                self._process is None or self._process.is_alive
            ):
                self._process = Process(target=self._reflash_servers)
                self._process.start()
                self._process

            self._tdxapi = TdxHq_API(raise_exception=True)
            _, host, port = self._hosts.get()

            if self._tdxapi.connect(host, port, time_out=0.5):
                logger.warning(f"连接: {host} {port} 成功...")
                break
            self._tdxapi = None

        try:
            if self._tdxapi:
                yield self._tdxapi
            else:
                logger.error("没有找到可连接的tdx服务器...")
        except Exception as e:
            logger.error(f"发生错误: {e}", exc_info=True)
            self._tdxapi = None

        # *if self._process and self._process.is_alive:
        # *    self._process.join()
        # *    self._process = None


vxtdx = vxTdxAPI()


class TDXExchange(Enum):
    SHSE = TDXParams.MARKET_SH
    SZSE = TDXParams.MARKET_SZ


def to_tdx_symbol(symbol):
    """转成tdx的symbol格式: (market,code)

    Arguments:
        symbol {_type_} -- symbol
    """
    market, code = symbol.split(".")
    return (TDXExchange[market].value, code)


def parser_tdx_symbol(market, code):
    """将tdx的symbol格式转化成symbol："SHSE.0000001"

    Arguments:
        market {_type_} -- tdx 的market代码
        code {_type_} -- 证券代码
    """
    return f"{TDXExchange(market).name}.{code}"


def parser_tdx_tick(tdxtick, key=""):
    """转化为vxtick格式

    Arguments:
        tdxtick {_type_} -- tdx tick格式
    """
    try:
        symbol = parser_tdx_symbol(tdxtick["market"], tdxtick["code"])
        _preset = vxMarketPreset(symbol)

        if _preset.security_type in (
            SecType.BOND_CONVERTIBLE,
            SecType.BOND,
            SecType.REPO,
        ):
            return tdxConBondTickConvter(tdxtick, key="symbol")
        elif _preset.security_type in (SecType.ETFLOF, SecType.CASH):
            return tdxETFLOFTickConvter(tdxtick, key="symbol")
        else:
            return tdxStockTickConvter(tdxtick, key="symbol")
    except Exception as e:
        logger.error(e)


class vxTdxHQ:
    def __init__(self) -> None:
        self._vxtdx = vxTdxAPI()

    def __call__(self, *symbols):
        if len(symbols) == 1 and isinstance(symbols[0], (tuple, list)):
            symbols = symbols[0]

        tdx_codes = list(map(to_tdx_symbol, symbols))

        vxticks = {}
        with self._vxtdx.get_fastest_api() as api:
            for i in range(0, len(symbols), 50):
                tdxticks = api.get_security_quotes(tdx_codes[i: i + 50])
                if tdxticks:
                    vxticks.update(dict(map(parser_tdx_tick, tdxticks)))
                else:
                    logger.warning(f"查询结果失败: {tdx_codes[i : i + 50]}")
        return vxticks
