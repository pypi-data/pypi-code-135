from ensure import ensure_annotations
from pyGeckoCrypto.custom_exception import (
    InvalidRequestException,
    InvalidCoinIDException,
    InvalidCurrencyException,
)
from pyGeckoCrypto.logger import logger
import requests
import json

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


@ensure_annotations
def request(URL: str):
    try:
        session = requests.Session()
        retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[502, 503, 504])
        session.mount("https://", HTTPAdapter(max_retries=retries))
        response = session.get(URL, timeout=5)
        content = json.loads(response.content.decode("utf-8"))
        return content
    except Exception:
        logger.exception("Request Incorrect")
        raise InvalidRequestException("Request Incorrect")


@ensure_annotations
def check_coinID(coinID: str) -> bool:
    try:
        coinID = coinID.lower()
        coinIDS = request("https://api.coingecko.com/api/v3/coins/list")
        for i in coinIDS:
            if i["id"] == coinID:
                return True
        else:
            return False
    except Exception as e:
        logger.exception(e)
        return False


@ensure_annotations
def check_currency(currency: str) -> bool:
    try:
        currency = currency.lower()
        currencies = request(
            "https://api.coingecko.com/api/v3/simple/supported_vs_currencies"
        )
        if currency in currencies:
            return True
        else:
            return False
    except Exception as e:
        logger.exception(e)
        return False


@ensure_annotations
def get_current_price(coinID: str, currency: str) -> float:
    try:
        coinID = coinID.lower()
        currency = currency.lower()
        if coinID is None:
            logger.exception("Coin ID cannot be None")
            raise InvalidCoinIDException("Coin ID cannot be None")
        if currency is None:
            logger.exception("Currency cannot be None")
            raise InvalidCurrencyException("Currency cannot be None")
        if not check_coinID(coinID):
            logger.exception("Coin ID Incorrect")
            raise InvalidCoinIDException("Coin ID Incorrect")
        if not check_currency(currency):
            logger.exception("Currency Incorrect")
            raise InvalidCurrencyException("Currency Incorrect")
        API_URL = f"https://api.coingecko.com/api/v3/simple/price?ids={coinID}&vs_currencies={currency}"
        price = request(API_URL)
        return float(price[coinID][currency])
    except Exception as e:
        logger.exception("Could not get current price %s" % e)
        raise e
