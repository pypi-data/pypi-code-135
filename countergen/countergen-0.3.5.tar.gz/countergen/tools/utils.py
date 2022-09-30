from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Mapping, Optional, Sequence, TypeVar, Tuple

from tqdm import tqdm  # type: ignore
import openai

import countergen.config

T = TypeVar("T")


def other(t: Tuple[T, T], x: T) -> T:
    if x == t[0]:
        if x == t[1]:
            raise ValueError(f"{t} contains two copies of {x}")
        return t[1]
    if x != t[1]:
        raise ValueError(f"{t} does not contain {x}")
    return t[0]


def unwrap_or(maybe: Optional[T], default: T) -> T:
    return default if maybe is None else maybe


def all_same(l: Sequence[Any]) -> bool:
    return all(x == l[0] for x in l[1:])


def maybe_tqdm(it: Iterable[T], do_tqdm: bool = False, **kwargs) -> Iterable[T]:
    if do_tqdm:
        return tqdm(it, **kwargs)
    else:
        return it


def estimate_paraphrase_length(text: str):
    average_token_length = 3
    safety_margin = 50
    return len(text) // average_token_length + safety_margin


def set_and_check_oai_key(key: Optional[str] = None, base: Optional[str] = None):
    """Set the key (and the base) of the openai api.

    If not explictely passed, takes arguments from the config.

    Checks that the key is not None."""

    key = unwrap_or(key, countergen.config.OPENAI_API_KEY)
    base = unwrap_or(base, countergen.config.OPENAI_API_BASE)

    if key is None:
        raise RuntimeError(
            "Please provide openai key to use its api! Use `countergen.config.OPENAI_API_KEY = YOUR_KEY`"
        )
    openai.api_key = key
    openai.api_base = base
