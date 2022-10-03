"""Utilities helpers for this project."""

import sys
import logging


def assert_condition(condition: bool, error_message: str) -> None:
    """
    Return the error message if the condition is not met.

    Parameters:
        condition (bool): The condition for checking.
        error_message (str): The output message if the condition gone wrong.
    """
    if not condition:
        logging.error('%s Please see --help for more info.', error_message)
        sys.exit(1)
