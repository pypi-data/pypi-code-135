import argparse
import typing


class SplitAppendAction(argparse._AppendAction):
    # append to list, like normal "append", but split first
    # (default split on ',')
    #
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-d', action=SplitAppendAction)
    #
    # the following argument have the same list as result:
    #    -d ab -d cd -d kl -d mn
    #    -d ab,cd,kl,mn
    #    -d ab,cd -d kl,mn

    def __init__(self, *args: typing.Any, **kw: typing.Any) -> None:
        self._split_chr = ','
        argparse.Action.__init__(self, *args, **kw)

    def __call__(
        self,
        parser: typing.Any,
        namespace: argparse.Namespace,
        values: typing.Union[str, typing.Sequence[str], None],
        option_string: typing.Optional[str] = None,
    ) -> None:
        # _AppendAction does not return a value
        assert isinstance(values, str)
        for value in values.split(self._split_chr):
            argparse._AppendAction.__call__(self, parser, namespace, value, option_string)
