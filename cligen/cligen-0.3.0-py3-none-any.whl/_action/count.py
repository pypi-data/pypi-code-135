import argparse
import typing

_parameters = """\
nargs: 0
default: 0
"""


class CountAction(argparse.Action):
    # argparse action for counting up and down
    #
    # standard argparse action='count', only increments with +1, this action uses
    # the value of self.const if provided, and +1 if not provided
    #
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--verbose', '-v', action=CountAction, const=1,
    #         nargs=0)
    # parser.add_argument('--quiet', '-q', action=CountAction, dest='verbose',
    #         const=-1, nargs=0)

    def __call__(
        self,
        parser: typing.Any,
        namespace: argparse.Namespace,
        values: typing.Union[str, typing.Sequence[str], None],
        option_string: typing.Optional[str] = None,
    ) -> None:
        if self.const is None:
            self.const = 1
        try:
            val = getattr(namespace, self.dest) + self.const
        except TypeError:  # probably None
            val = self.const
        setattr(namespace, self.dest, val)
