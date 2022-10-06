import re
from abc import ABC, abstractmethod
from typing import Optional

from docdeid.tokenize.token import Token


class BaseTokenizer(ABC):
    def __init__(self, link_tokens: bool = True):
        self.link_tokens = link_tokens

    @staticmethod
    def previous_token(position: int, tokens: list[Token]) -> Optional[Token]:

        if position == 0:
            return None

        return tokens[position - 1]

    @staticmethod
    def next_token(position: int, tokens: list[Token]) -> Optional[Token]:

        if position == len(tokens) - 1:
            return None

        return tokens[position + 1]

    def tokenize(self, text: str, **kwargs) -> list[Token]:

        tokens = self.split_text(text, **kwargs)

        if self.link_tokens:

            for i, token in enumerate(tokens):

                previous_token = self.previous_token(position=i, tokens=tokens)
                token.set_previous_token(previous_token)

                next_token = self.next_token(position=i, tokens=tokens)
                token.set_next_token(next_token)

        return tokens

    @abstractmethod
    def split_text(self, text: str, **kwargs) -> list[Token]:
        pass


class SpaceSplitTokenizer(BaseTokenizer):
    def split_text(self, text: str, **kwargs) -> list[Token]:

        return [
            Token(text=match.group(0), start_char=match.start(), end_char=match.end())
            for match in re.finditer(r"[^\s]+", text)
        ]


class WordBoundaryTokenizer(BaseTokenizer):
    def split_text(self, text: str, **kwargs) -> list[Token]:

        tokens = []
        matches = [*re.finditer(r"\b", text)]

        for start_match, end_match in zip(matches, matches[1:]):

            start_char = start_match.span(0)[0]
            end_char = end_match.span(0)[0]

            tokens.append(Token(text=text[start_char:end_char], start_char=start_char, end_char=end_char))

        return tokens
