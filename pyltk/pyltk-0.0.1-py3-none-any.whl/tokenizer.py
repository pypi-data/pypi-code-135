from typing import Callable, List, Generator

_accept_byte = lambda c: not (
    c < 122 if c > 96 else c > 64 or c < 33 or c == 45 if c < 91 else False
)

def word_tokenize(text: str):
    for char in ("-", "—"):
        text = text.replace(char, " ")
    for char in (
        char
        for char in set(text)
        if not _accept_byte(ord(char))
    ):
        text = text.replace(char, "")
    return text.split()
