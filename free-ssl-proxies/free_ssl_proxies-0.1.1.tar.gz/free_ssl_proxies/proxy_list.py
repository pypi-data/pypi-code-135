import json
import logging
import tempfile
import time
import urllib.error
from datetime import date, datetime, timedelta
from random import choice
from typing import List, Optional, Tuple
from urllib import request
from xml.etree import ElementTree

CACHE_FILE = f"{tempfile.gettempdir()}/proxies.tmp.txt"

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class CacheMissError(Exception):
    def __init__(self):
        super(CacheMissError, self).__init__(f"Unable to locate cache file at: {CACHE_FILE}. No cache written.")


def _json_serializer(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Proxy):
        return str(obj)
    elif isinstance(obj, ProxyList):
        return str(obj)


def parse_last_checked_datetime(last_checked: str) -> datetime:
    """
    Given an expression like 15 hours '5 minutes ago', convert the expression into a datetime relative to the
    current datetime.
    :param last_checked: A string conveying the last time a proxy was checked: '5 hours ago'.
    :return: A datetime object
    """
    last_checked_datetime = None
    last_checked_tokens = last_checked.split(" ")
    if len(last_checked_tokens) == 3:
        numeric, unit, _ = last_checked_tokens
        if "hour" in unit:
            last_checked_datetime = datetime.now() - timedelta(hours=int(numeric))
        elif "min" in unit:
            last_checked_datetime = datetime.now() - timedelta(minutes=int(numeric))
        elif "sec" in unit:
            last_checked_datetime = datetime.now() - timedelta(seconds=int(numeric))
    elif len(last_checked_tokens) == 5:
        (
            hours,
            _,
            minutes,
            _,
            _,
        ) = last_checked_tokens
        last_checked_datetime = datetime.now() - timedelta(
            hours=int(hours), minutes=int(minutes)
        )
    return last_checked_datetime


def parse_ssl_proxies_org_table(
    html: str,
) -> List[Tuple[str, int, str, str, bool, datetime]]:
    """
    Given the HTML found on the homepage of https://www.sslproxies.org/ parse the table found there
    :param html: The HTML found on the homepage of sslproxies.org
    :return: A list of tuples where every tuple contains the elements:
             (IP, port, cc, country, google, and last_checked_datetime)
    """
    proxy_list = []
    table_start_idx = html.index("<table")
    table_end_idx = html.index("</table")
    table = html[table_start_idx:table_end_idx]
    for row in table.split("<tr>"):
        row = "<tr>" + row.replace("</tbody>", "")
        if "<td>" not in row:
            continue
        row_element_tree = list(ElementTree.fromstring(row).iter())
        (
            _,
            ip_address,
            port,
            cc,
            country,
            anonymous,
            google,
            https,
            last_checked,
        ) = row_element_tree
        if anonymous.text != "anonymous":
            continue
        if https.text != "yes":
            continue
        parse_last_checked_datetime(last_checked.text)
        proxy_list.append(
            (
                ip_address.text,
                int(port.text),
                cc.text,
                country.text,
                google.text == "yes",
                parse_last_checked_datetime(last_checked.text),
            )
        )
    return proxy_list


def profile_proxy_host(proxy_host: str, timeout: int = 3) -> Optional[float]:
    """
    Given a proxy_host in the form ip:port attempt to connect through that proxy and note the time in seconds it took
    to do so
    :param proxy_host: An ip:port string
    :param timeout: The maximum number of seconds before a proxy is no longer a candidate for selection
    :return: The number of seconds it took to make a request through the proxy
    """
    url = "https://api.ipify.org"
    proxy_support = request.ProxyHandler({"https": proxy_host})
    opener = request.build_opener(proxy_support, request.CacheFTPHandler)
    request.install_opener(opener)
    req = request.Request(
        url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
    )
    try:
        logging.info(f"Profiling {proxy_host}")
        start_time = time.time()
        request.urlopen(req, timeout=timeout)
        end_time = time.time()
        return end_time - start_time
    except urllib.error.URLError as e:
        logger.warning(
            f"Encountered error while profiling: {proxy_host}, likely unacceptable timeout - {e}"
        )
    except TimeoutError as e:
        logger.warning(f"Encountered error while profiling: {proxy_host}, ssl socket timeout - {e}")
    return None


class Proxy:
    def __init__(
        self,
        ip_address: str,
        port: int,
        cc: str,
        country: str,
        google: bool,
        last_checked: datetime,
    ):
        self.ip_address = ip_address
        self.port = port
        self.cc = cc
        self.country = country
        self.google = google
        self.last_checked = last_checked
        self.avg_request_time = None

    def __lt__(self, other):
        return self.last_checked < other.last_checked

    def __gt__(self, other):
        return self.last_checked > other.last_checked

    def __str__(self):
        return json.dumps(self.__dict__, default=_json_serializer, indent=1)

    def profile(self, timeout: int = 3):
        """
        Determine the number of seconds it takes to make a simple HTTP Get request to an external API,
        set the avg_request_time instance variable if request was made under the timeout time
        :param timeout: The maximum number of seconds before a proxy is no longer a candidate for selection
        :return: None
        """
        self.avg_request_time = profile_proxy_host(
            f"{self.ip_address}:{self.port}", timeout=timeout
        )


class ProxyList:
    def __init__(
        self,
        proxy_list: List[Tuple[str, int, str, str, bool, datetime]],
        profile: bool = True,
        timeout: int = 3,
    ):
        self._idx = 0
        self.profile = profile
        self.timeout = timeout
        self.proxies = self._load(proxy_list, profile, timeout)

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.proxies)

    def __next__(self):
        self._idx += 1
        try:
            return self.proxies[self._idx - 1]
        except IndexError:
            raise StopIteration()

    def __str__(self):
        return json.dumps([json.loads(str(p)) for p in self.proxies], indent=1)

    @staticmethod
    def _load(
        proxy_list: List[Tuple[str, int, str, str, bool, datetime]],
        profile: bool = True,
        timeout: int = 3,
    ):
        proxies = []
        for proxy_item in proxy_list:
            ip_address, port, cc, country, google, last_checked = proxy_item
            proxy_obj = Proxy(ip_address, port, cc, country, google, last_checked)
            if profile:
                proxy_obj.profile(timeout=timeout)
                if proxy_obj.avg_request_time:
                    logger.info(f"Found fast proxy {proxy_obj.ip_address}:{port}")
            proxies.append(proxy_obj)
        return proxies

    @classmethod
    def from_ssl_proxies_org(cls, profile: bool = True, timeout: int = 3):
        url = "https://www.sslproxies.org"
        req = request.Request(
            url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
        )
        try:
            response = request.urlopen(req)
            proxy_list = parse_ssl_proxies_org_table(response.read().decode("ascii"))
            return cls(proxy_list, profile, timeout)

        except urllib.error.URLError as e:
            logger.warning(
                f"Encountered error while pulling: {url} - {e}"
            )
        except TimeoutError as e:
            logger.warning(f"Encountered error while pulling: {url}, ssl socket timeout - {e}")
        time.sleep(5)

    @classmethod
    def from_cache(cls, profile: bool = False, timeout: int = 3):
        proxy_obj_list = cls([], profile, timeout)
        try:
            with open(CACHE_FILE, "r") as cache_fin:
                proxy_list = json.load(cache_fin)
                for p in proxy_list:
                    ip_address = p.get("ip_address")
                    port = p.get("port")
                    cc = p.get("cc")
                    country = p.get("country")
                    google = p.get("google")
                    last_checked = datetime.fromisoformat(p.get("last_checked"))
                    avg_request_time = p.get("avg_request_time")
                    proxy = Proxy(ip_address, port, cc, country, google, last_checked)
                    proxy.avg_request_time = avg_request_time
                    proxy_obj_list.append(proxy)
        except FileNotFoundError:
            raise CacheMissError()
        return proxy_obj_list

    def append(self, proxy: Proxy):
        self.proxies.append(proxy)

    def get(self, ip: str) -> Optional[Proxy]:
        for proxy in self.proxies:
            if proxy.ip_address == ip:
                return proxy
        return None

    def get_by_country(self, cc: str) -> List[Proxy]:
        matches = []
        for proxy in self.proxies:
            if cc.lower() == proxy.cc.lower() or cc.lower() == proxy.country.lower():
                matches.append(proxy)
        return matches

    def get_fastest(self) -> List[Proxy]:
        matches = []
        for proxy in self.proxies:
            if not proxy.avg_request_time:
                continue
            matches.append(proxy)
        return sorted(matches, key=lambda x: x.avg_request_time)

    def random(self) -> Proxy:
        if self.get_fastest():
            return choice(self.get_fastest())
        return choice(self.proxies)


def write_proxy_list_to_cache(proxy_list: ProxyList):
    with open(CACHE_FILE, "w") as proxy_list_fo:
        proxy_list_fo.write(str(proxy_list))
