from typing import Dict, Tuple

HEADER: Dict = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
}

BASE_URL: str = ("https://www.coastcapitalsavings.com/"
                 "umbraco/surface/ATMSurface/GetATMByBounds/"
                 )

DATABITS: Dict = {"lat1": "67.13491194425603", "lat2": "34.14399616088567",
                  "long1": "-30.209727299100052", "long2": "-140.9538697122394"
                  }

DETAIL_KEYS: Tuple = ('StreetNumber', 'Street', 'StreetType',
                      'StreetDirection', 'City', 'Province')
