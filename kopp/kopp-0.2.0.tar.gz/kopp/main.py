from __future__ import annotations

import re

pair: dict[str, tuple[str, str]] = {
    "(이)가": ("이", "가"),
    "(와)과": ("과", "와"),
    "(을)를": ("을", "를"),
    "(은)는": ("은", "는"),
    "(으)로": ("으로", "로"),
    "(아)야": ("아", "야"),
    "(이)여": ("이여", "여"),
    "(이)라": ("이라", "라"),
}

key_pattern = "|".join(re.escape(k) for k in pair.keys())
pattern = re.compile(
    rf"(?P<prev>.?)(?P<key>{key_pattern})",
)


def is_hangle(char: str) -> bool:
    """
    check if char is hangle
    "가" ~ "힣"

    Parameters
    ----------
    char : str
        str: string to check, must be length 1

    Returns
    -------
    bool
        True if char is hangle
    """
    code = ord(char)
    return 0xAC00 <= code <= 0xD7A3


def replace(m: re.Match) -> str:
    """
    replace function used in re.sub
    """
    prev = m.group("prev")
    key = m.group("key")

    # No previous string or not hangle
    if not prev or not is_hangle(prev):
        return prev + pair[key][1]

    char_code = (ord(prev) - 0xAC00) % 28

    # prev doesn't have postposition or
    # key is '(으)로' and prev's final consonant is 'ㄹ'
    if char_code == 0 or (key == "(으)로" and char_code == 8):
        return prev + pair[key][1]

    return prev + pair[key][0]


def kopp(text: str) -> str:
    """
    '(이)가', '(와)과', '(을)를', '(은)는', '(으)로', '(아)야', '(이)여', '(이)라'
    postposition converter

    Parameters
    ----------
    text : str
        text to convert

    Returns
    -------
    str
        converted text

    Examples
    --------

    >>> kopp("오늘(은)는 날씨(이)가 좋네요.")
    '오늘은 날씨가 좋네요.'
    >>> kopp("doctest 모듈(은)는 대화형 파이썬 세션처럼 보이(은)는 텍스트(을)를 검색한 다음")
    'doctest 모듈은 대화형 파이썬 세션처럼 보이는 텍스트를 검색한 다음'
    >>> kopp("이 프로젝트(은)는 pdm(으)로 관리됩니다.")
    '이 프로젝트는 pdm로 관리됩니다.'
    """
    return pattern.sub(replace, text)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
