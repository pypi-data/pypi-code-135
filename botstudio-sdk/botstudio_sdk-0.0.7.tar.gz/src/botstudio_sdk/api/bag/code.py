"""
More info:
    https://github.com/lvbag/BAG-API/blob/master/Features/paginering.feature
    https://www.kadaster.nl/documents/1953498/2762071/Productbeschrijving+BAG+API+Individuele+Bevragingen.pdf/cf35e5fd-ddb0-bc82-ffc5-6e7877a58ffa?t=1638438344305
    https://lvbag.github.io/BAG-API/Technische%20specificatie/#/Adres%20uitgebreid/zoekAdresUitgebreid
    https://lvbag.github.io/BAG-API/Technische%20specificatie/
"""

import requests


URL_PRODUCTIE = "https://api.bag.kadaster.nl/lvbag/individuelebevragingen/v2/"


def adres_uitgebreid(
    api_key: str,
    postcode: str,
    huisnummer: str,
    huisnummertoevoeging: str = None,
    huisletter: str = None,
    exacteMatch: bool = False,
    adresseerbaarObjectIdentificatie: str = None,
    woonplaatsNaam: str = None,
    openbareRuimteNaam: str = None,
    page: int = None,
    pageSize: int = 100,
    q: str = None,
) -> object:
    """Query extensive information an address based on different combinations of parameters.

    For API key: https://formulieren.kadaster.nl/aanvraag_bag_api_individuele_bevragingen_productie

    :param api_key: bag api key
    :type api_key: str
    :param postcode: zip code
    :type postcode: str
    :param huisnummer: house number
    :type huisnummer: str
    :param huisnummertoevoeging: house number suffix
    :type huisnummertoevoeging: str
    :param huisletter: house letter
    :type huisletter: str
    :param exacteMatch:
    :type exacteMatch: bool
    :param adresseerbaarObjectIdentificatie:
    :type adresseerbaarObjectIdentificatie: str
    :param woonplaatsNaam: residence
    :type woonplaatsNaam: str
    :param openbareRuimteNaam: street
    :type openbareRuimteNaam: str
    :param page: default 1 page, minimum 1 page
    :type page: int
    :param pageSize: default 20 results per page, minimum 10 results per page, maximum 100 results per page
    :type pageSize: int
    :param q:
    :type q: str
    :return: reponse.json()
    :rtype: dict
    """

    headers = {
        "X-Api-Key": api_key,
        "Accept-Crs": "epsg:28992",
        "accept": "application/hal+json",
    }

    params = {
        "postcode": postcode,
        "huisnummer": huisnummer,
        "huisnummertoevoeging": huisnummertoevoeging,
        "huisletter": huisletter,
        "exacteMatch": exacteMatch,
        "adresseerbaarObjectIdentificatie": adresseerbaarObjectIdentificatie,
        "woonplaatsNaam": woonplaatsNaam,
        "openbareRuimteNaam": openbareRuimteNaam,
        "page": page,
        "pageSize": pageSize,
        "q": q,
    }

    url = URL_PRODUCTIE + "adressenuitgebreid"

    reponse = requests.get(url, headers=headers, params=params)

    if reponse.status_code == 200:
        return reponse.json()


if __name__ == "__main__":
    import pprint

    key_productie = "l73550f472b0e943ceb15e8071e7bb1462"

    postcode = "3039SG"
    huisnummer = "53"

    # postcode = "3011BH"
    # huisnummer = "154"

    postcode = "3286LT"
    huisnummer = "37"

    x = adres_uitgebreid(
        api_key=key_productie, postcode=postcode, huisnummer=huisnummer
    )
    # pprint.pprint(type(x))
    pprint.pprint(x)
    pprint.pprint(x)
    pprint.pprint(x)
    pprint.pprint(x)
    pprint.pprint(x)
    pprint.pprint(x)

    print(len(x["_embedded"]["adressen"]))
    for item in x["_embedded"]["adressen"]:
        print()
        pprint.pprint(item)
        bouwjaar = item["oorspronkelijkBouwjaar"]
        oppervlakte = item["oppervlakte"]
        gebruiksdoelen = item["gebruiksdoelen"]
        print(f"bouwjaar = {bouwjaar}")
        print(f"oppervlakte = {oppervlakte}")
        print(f"gebruiksdoelen = {gebruiksdoelen}")
