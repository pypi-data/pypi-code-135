import urllib.parse


def check_for_special_chars(quote: str, encoding: str = "utf-8") -> str:
    """
    Checks if a string contains a special character and converts it.

    Args:
        quote: the text to check for a special character.
        encoding: the encoding to be used.

    Returns: encoded text

    """
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    if isinstance(quote, str) and any(c in special_chars for c in quote):
        q: bytes = quote.encode(encoding)
        q: str = urllib.parse.quote(q)
    else:
        q: str = quote

    return q
