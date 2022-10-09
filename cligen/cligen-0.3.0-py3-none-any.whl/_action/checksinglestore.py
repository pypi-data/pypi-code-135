import argparse
import typing


class CheckSingleStoreAction(argparse.Action):
    # issue a warning when the store action is called multiple times

    def __call__(
        self,
        parser: typing.Any,
        namespace: argparse.Namespace,
        values: typing.Union[str, typing.Sequence[str], None],
        option_string: typing.Optional[str] = None,
    ) -> None:
        if getattr(namespace, self.dest, None) is not None:
            print(
                'WARNING: previous optional argument "'
                + str(option_string)
                + ' '
                + str(getattr(namespace, self.dest))
                + '" overwritten by "'
                + str(option_string)
                + ' '
                + str(values)
                + '"'
            )
        setattr(namespace, self.dest, values)
