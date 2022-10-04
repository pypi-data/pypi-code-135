from typing import Callable, Iterable, TypeVar, Generator, Any
from collections import defaultdict
from . import constants
from .tokenizer import word_tokenize as _word_tokenize

K = TypeVar(name="K")
V = TypeVar(name="V")

_tie = "".join
_next = lambda __i: next(__i, None)


class _StemData(list[str]):
    def __index_property(i: int):
        return property(fget=lambda v: v[i], fset=lambda b, v: b.__setitem__(i, v))

    w: str = __index_property(i=0)
    lhs: str = __index_property(i=1)
    rhs: str = __index_property(i=2)


def _transform(sd: _StemData, length: int, new: str, fallback: str = ""):
    sd.w = _tie((sd.w[:-length], new))
    sd.lhs = "" if len(sd.lhs) < length else _tie((sd.lhs[:-length], new))
    sd.rhs = fallback if len(sd.rhs) < length else _tie((sd.rhs[:-length], new))


def _unaffix(sd: _StemData, i: int):
    for (index, e) in enumerate(sd):
        sd[index] = e[:-i]


def _preformat(w: str) -> str:
    if w:
        if "y" in w:
            if w[0] == "y":
                w = _tie(("Y", w[1:]))
            for (i, char) in enumerate(w):
                if char == "y" and w[i - 1] in constants.VOWELS:
                    w = _tie((w[:i], "Y", w[i + 1 :]))
    return w


_next_vowel_index: Callable[[str], int | None] = lambda w: _next(
    i
    for i in range(1, len(w))
    if not (w[i] in constants.VOWELS) and w[i - 1] in constants.VOWELS
)


def _init_sd(w: str):

    w, lhs, rhs = _preformat(w=w), "", ""
    if w.startswith(("gener", "commun", "arsen")):
        lhs = w[6 if w[0] == "c" else 5 :]
        i = _next_vowel_index(w=lhs)
        if i is not None:
            rhs = lhs[i + 1 :]
    else:
        i = _next_vowel_index(w=w)
        if i is not None:
            lhs = w[i + 1 :]
            j = _next_vowel_index(w=lhs)
            if j is not None:
                rhs = lhs[j + 1 :]
    return _StemData((w, lhs, rhs))


def _get_suffix(sd: _StemData, i: int):
    suffixes = constants.SUFFIX_FIRST_LETTER_MAP[i].get(sd.w[-1]) if sd.w else None
    return (
        None
        if suffixes is None
        else _next(suff for suff in suffixes if sd.w.endswith(suff))
    )


def _process_stem_steps(word: str):
    sd = _init_sd(w=word)
    if sd.w[-1] == "s" and sd.w[-2] == "'":
        _unaffix(sd=sd, i=2)

    # step0 suffix
    suff = (
        2
        if (sd.w[-1] == "s" and sd.w[-2] == "'")
        else (3 if sd.w[-2] == "s" and sd.w[-3] == "'" else 1)
        if sd.w[-1] == "'" and len(sd.w) >= 4
        else 1
        if sd.w[-1] == "’"
        else 0
    )
    if suff:
        _unaffix(sd=sd, i=suff)

    # step 1a
    suff = (
        (
            _next(suf for suf in ("sses", "ies", "us", "ss", "s") if sd.w.endswith(suf))
            if sd.w[-1] == "s"
            else "ied"
            if sd.w.endswith("ied")
            else None
        )
        if sd.w
        else None
    )
    if suff is not None:
        if suff == "sses":
            _unaffix(sd=sd, i=2)
        elif suff in ("ied", "ies"):
            dist = 2 if len(sd.w[:-3]) > 1 else 1
            _unaffix(sd=sd, i=dist)
        elif suff == "s":
            if _next(c for c in sd.w[:-2] if c in constants.VOWELS):
                _unaffix(sd=sd, i=1)

    # process step 1b
    suff = _get_suffix(sd=sd, i=1)
    if suff is not None:
        if suff in ("eed", "eedly"):
            if sd.lhs.endswith(suff):
                _transform(sd=sd, length=len(suff), new="ee")
        else:
            # contains a vowel
            if (
                _next(v for v in sd.w[: -len(suff)] if v in constants.VOWELS)
                is not None
            ):
                _unaffix(sd=sd, i=len(suff))
                if sd.w.endswith(("at", "bl", "iz")):
                    sd.w, sd.lhs = _tie((sd.w, "e")), _tie((sd.lhs, "e"))
                    if len(sd.w) > 5 or len(sd.lhs) >= 3:
                        sd.rhs = _tie((sd.rhs, "e"))
                elif sd.w.endswith(constants.DOUBLE_CONSONANTS):
                    _unaffix(sd=sd, i=1)
                elif (not sd.lhs or sd.lhs == "") and (
                    (
                        len(sd.w) >= 3
                        and (sd.w[-1] not in constants.VOWELS and sd.w[-1] not in "wxY")
                        and (
                            sd.w[-2] in constants.VOWELS
                            and sd.w[-3] not in constants.VOWELS
                        )
                    )
                    or (
                        len(sd.w) == 2
                        and sd.w[0] in constants.VOWELS
                        and sd.w[1] not in constants.VOWELS
                    )
                ):
                    sd.w = _tie((sd.w, "e"))
                    if len(sd.lhs):
                        sd.lhs = _tie((sd.lhs, "e"))
                    if len(sd.rhs):
                        sd.rhs = _tie((sd.rhs, "e"))

    if len(sd.w) > 2 and sd.w[-1] in "yY" and sd.w[-2] not in constants.VOWELS:
        _transform(sd=sd, length=1, new="i")

    # process step 2
    suff = _get_suffix(sd=sd, i=2)
    if suff is not None and sd.lhs.endswith(suff):
        if suff in ("tional", "entli", "fulli", "lessli"):
            _unaffix(sd=sd, i=2)
        elif suff == "anci":
            _unaffix(sd=sd, i=1)
        elif suff in ("ation", "ator", "ational"):
            _transform(sd=sd, length=len(suff), new="ate", fallback="e")
        elif suff in ("alism", "aliti", "alli"):
            _transform(sd=sd, length=len(suff), new="al")
        elif suff == "enci":
            _transform(sd=sd, length=1, new="e")
        elif suff in ("izer", "ization"):
            _transform(sd=sd, length=len(suff), new="ize")
        elif suff in ("iveness", "iviti"):
            _transform(sd=sd, length=len(suff), new="ive", fallback="e")
        elif suff == "fulness":
            _unaffix(sd=sd, i=4)
        elif suff == "abli":
            _unaffix(sd=sd, i=4)

        elif suff in ("ousli", "ousness"):
            _transform(sd=sd, length=len(suff), new="ous")
        elif suff == "ogi":
            if sd.w[-4] == "l":
                _unaffix(sd=sd, i=1)
        elif suff == "li":
            if sd.w[-3] in constants.LI_ENDINGS:
                _unaffix(sd=sd, i=2)
        elif suff in ("biliti", "bli"):
            _transform(sd=sd, length=len(suff), new="ble")

    # process step 3
    suff = _get_suffix(sd=sd, i=3)
    if suff is not None and sd.lhs.endswith(suff):
        if suff == "tional":
            _unaffix(sd=sd, i=2)
        elif suff == "ational":
            _transform(sd=sd, length=len(suff), new="ate")
        elif suff == "alize":
            _unaffix(sd=sd, i=3)
        elif suff == "ative":
            if sd.rhs.endswith(suff):
                _unaffix(sd=sd, i=5)
        elif suff in ("ful", "ness"):
            _unaffix(sd=sd, i=len(suff))
        elif suff in ("icate", "iciti", "ical"):
            _transform(sd=sd, length=len(suff), new="ic")

    # step 4
    suff = _get_suffix(sd=sd, i=4)
    if suff is not None and sd.rhs.endswith(suff):
        if suff == "ion":
            if sd.w[-4] in "st":
                _unaffix(sd=sd, i=3)
        else:
            _unaffix(sd=sd, i=len(suff))

    # step 5
    if (sd.rhs.endswith("e") or (sd.rhs.endswith("l") and sd.w[-2] == "l")) or (
        sd.lhs.endswith("e")
        and len(sd.w) >= 4
        and (
            (sd.w[-2] in constants.VOWELS or sd.w[-2] in "wxY")
            or sd.w[-3] not in constants.VOWELS
            or (len(sd.w) >= 5 and sd.w[-4] in constants.VOWELS)
        )
    ):
        sd.w = sd.w[:-1]
    result = sd.w.replace("Y", "y")
    return result


def _process_cached_generator(values: Iterable[V], getter: Callable[[V], K]):
    key = None

    def getvalue():
        return getter(key)

    cache = defaultdict(getvalue)
    for value in values:
        key = value
        result = cache[key]
        if result:
            yield result


def _form_stemming_algorithm(
    form_stem_tuples: bool = False,
    include_stopwords: bool = False,
    include_punctuation: bool = False,
    return_tokenstems: bool = False,
) -> Generator[str | tuple[Any, str], None, None]:
    _derive_stem: Callable[[str], str] = lambda w: (
        w
        if (w in constants.PUNCTUATION or len(w) < 3)
        else constants.EXCEPTIONS[w]
        if (w in constants.EXCEPTIONS)
        else _process_stem_steps(word=w)
    )
    get_value = (
        (lambda w: (w, _derive_stem(w)))
        if form_stem_tuples or return_tokenstems
        else _derive_stem
    )
    if include_punctuation or include_stopwords:
        predicate_base = (
            (
                lambda token: token not in constants.STOPWORDS
                if include_punctuation
                else lambda token: (
                    token not in constants.STOPWORDS
                    and token not in constants.PUNCTUATION
                )
            )
            if not include_stopwords
            else (lambda token: token not in constants.PUNCTUATION)
            if not include_punctuation
            else lambda token: True
        )
        if form_stem_tuples:

            def predicate(token: str):
                return predicate_base(token[0])

        else:
            predicate = predicate_base

        def iter_results(words: Iterable[str]):
            verdicts = {}
            for token in _process_cached_generator(words, get_value):
                if token in verdicts:
                    if verdicts[token] is True:
                        yield token
                else:
                    verdict = predicate(token)
                    verdicts[token] = verdict
                    if verdict is True:
                        yield token

    else:
        iter_results = lambda words: _process_cached_generator(words, get_value)
    return iter_results


_stemmer = _form_stemming_algorithm(include_stopwords=True, include_punctuation=True)

_tuple_stemmer = _form_stemming_algorithm(
    form_stem_tuples=True, include_stopwords=True, include_punctuation=True
)


def stem(__input: str | Iterable[str], tuple_results: bool = False):
    return (_tuple_stemmer if tuple_results else _stemmer)(
        words=(
            _word_tokenize(__input.strip().lower())
            if isinstance(__input, str)
            else __input
        )
    )
