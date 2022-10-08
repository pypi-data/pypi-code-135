from utils.common_tools import *
from utils.alert import message_alert

from datetime import datetime

import yfinance as yf
import platform

system_os = platform.system()
print(system_os)

try:
    if system_os == 'Linux' or 'MAC':
        logging.basicConfig(level=logging.INFO, filename='../price_alert/log/main.log',
                            format='%(asctime)s :: %(levelname)s :: %(lineno)d :: '
                                   '%(funcName)s :: %(message)s :: %(filename)s',
                            datefmt='%d-%b%y %H:%M:%S')
    else:
        logging.basicConfig(level=logging.INFO, filename='..\price_alert\log\main.log',
                            format='%(asctime)s :: %(levelname)s :: %(lineno)d :: '
                                   '%(funcName)s :: %(message)s :: %(filename)s',
                            datefmt='%d-%b%y %H:%M:%S')

except Exception as e:
    print(e)


class PriceAlert:
    def __init__(self, asset: str, waiting_time: float):
        self.waiting_time = waiting_time
        self.asset = asset
        self.price_above = []
        self.price_below = []

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"

    def getting_price(self):
        time_now = datetime.now()
        ticker_price = yf.Ticker(self.asset).history(interval="1m", period="1d")
        print(f'\nConsult at: {time_now}')
        print(f"Ticker {self.asset} - Current price = $ {round(ticker_price['Close'][-1], 2)}")
        logging.info(time_now)
        logging.info(ticker_price)
        return time_now, ticker_price['Close'][-1]

    def check_price(self):
        try:
            current_price = self.getting_price()[1]
            if round(current_price, 2) <= self.price_below[-1]:
                message_alert(self.asset, price=round(current_price, 2))
                quit()
            if round(current_price, 2) >= self.price_above[-1]:
                message_alert(self.asset, price=round(current_price, 2))
                quit()

        except TypeError as e:
            print(e)
            print('Please enter a float number: 10.0')
            quit()

    def price_alert_request(self):
        header(msg='Price Alert')
        print('Example: ticker= MSFT ')
        print(f'Make a new request in {self.waiting_time} seconds.')
        current_price = self.getting_price()[1]
        logging.info(current_price)
        price_above = float(input(f"Type a price bigger than {round(current_price, 2)}: "))
        logging.info(price_above)
        self.price_above.append(price_above)
        price_below = float(input(f"Type a price less than {round(current_price, 2)}: "))
        logging.info(price_below)
        self.price_below.append(price_below)
        schedule_function(function=self.check_price, time_seconds=self.waiting_time)


if __name__ == '__main__':
    price = PriceAlert(asset='TSLA', waiting_time=2)
    price.price_alert_request()
