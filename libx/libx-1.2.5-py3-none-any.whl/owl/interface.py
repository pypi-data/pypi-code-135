"""
Type interface for the mailer module.
"""
from dataclasses import astuple, dataclass


@dataclass()
class Sender:
    uname: str
    passwd: str

    def __iter__(self):
        return iter(astuple(self))

    def __getitem__(self, keys):
        return iter(getattr(self, k) for k in keys)


@dataclass()
class Recipient:
    uname: str

    def __iter__(self):
        return iter(astuple(self))

    def __getitem__(self, keys):
        return iter(getattr(self, k) for k in keys)


@dataclass()
class MailArgs:
    sender: Sender
    recipient: Recipient
    subj: str
    content: str

    def __iter__(self):
        return iter(astuple(self))

    def __getitem__(self, keys):
        return iter(getattr(self, k) for k in keys)
