import requests, re
from bs4 import BeautifulSoup

class ExchangeRate():
    def __init__(self) -> None:
        self._url = f'https://www.google.com/search?q='
        self._cookies = {'CONSENT': 'YES+'}
        self._pattern = re.compile('(^\d+,\d+)')

    def get(self, currency_from: str , currency_to: str, number: bool = False) -> str | float:
        if type(currency_from) != str or type(currency_to) != str:
            raise TypeError('expected string')

        url = f'{self._url}{currency_from}+to+{currency_to}'
        response = requests.get(url, cookies=self._cookies)
        if response.status_code != 200:
            return "Couldn't reach Googogogle."

        html = BeautifulSoup(response.text, 'html.parser')
        matching = html.find(text=self._pattern)
        if not matching:
            return "Can't find currency."

        parsed = matching.split(' ', 1)[0]

        if number:
            return float(parsed.replace(',','.'))

        return parsed

if __name__ == '__main__':
    rate = ExchangeRate()
    print(rate.get('EUR', 'HUF'))
    print(rate.get('huf', 'gbp'))
    print(rate.get('huf', 'gbp', number=True))
    print(rate.get(1, 'gbp'))
