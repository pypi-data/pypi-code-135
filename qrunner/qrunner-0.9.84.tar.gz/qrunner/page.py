import time
from qrunner.utils.log import logger
from qrunner import AndroidDriver, IosDriver, WebDriver, H5Driver
from typing import Union


class Page(object):

    def __init__(self, driver: Union[AndroidDriver, IosDriver, WebDriver, H5Driver]):
        self.driver = driver

    @staticmethod
    def sleep(n):
        logger.info(f'休眠 {n} 秒')
        time.sleep(n)


