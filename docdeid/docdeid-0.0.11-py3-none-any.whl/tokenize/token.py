from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class Token:

    text: str
    start_char: int
    end_char: int

    _previous_token: Optional["Token"] = field(default=None, repr=False, compare=False)
    _next_token: Optional["Token"] = field(default=None, repr=False, compare=False)

    def __post_init__(self):

        if len(self.text) != (self.end_char - self.start_char):
            raise ValueError("The span does not match the length of the text.")

    def set_previous_token(self, token: "Token"):
        object.__setattr__(self, "_previous_token", token)

    def set_next_token(self, token: "Token"):
        object.__setattr__(self, "_next_token", token)

    def _get_linked_token(self, num: int, attr: str):

        token = self

        for _ in range(num):
            token = getattr(token, attr)

            if token is None:
                return None

        return token

    def previous(self, num=1):
        return self._get_linked_token(num=num, attr="_previous_token")

    def next(self, num=1):
        return self._get_linked_token(num=num, attr="_next_token")

    def __len__(self):
        return len(self.text)
