#!/usr/bin/env python
from numpydoc.docscrape import NumpyDocString
from numpydoc.docscrape import FunctionDoc
import argparse


def merge_parameters(existing: list, new: list) -> list:
    """Merge the sections of two docstrings."""
    result = []
    # We'll check all new parameters.
    for i, param in enumerate(new):
        # If there is a non-empty description, we'll consider it an updated parameter
        # and remove it from existing.
        # If empty, we'll continue to use the existing description.
        if param.desc != []:
            # existing = [e for e in existing if e.name != param.name]
            result.append(param)  # The parameter is in the correct position.
        else:
            # In this case we need to find the corresponding parameter in existing.
            for existing_param in existing:
                if existing_param.name == param.name:
                    result.append(existing_param)
    return result


def merge(existing: FunctionDoc, new: FunctionDoc) -> FunctionDoc:
    """
    Merge two FunctionDocs.

    Prioritizes the new docs

    Parameters
    ----------
    existing : FunctionDoc
    new : FunctionDoc

    Returns
    -------
    FunctionDoc

    Examples
    --------
    FIXME: Add docs.


    """
    new["Parameters"] = merge_parameters(existing["Parameters"], new["Parameters"])
    for k, v in new.items():
        if k in ["Parameters"]:
            continue
        # If a field in new is empty we put in what was there before.
        if not v and k in existing:
            new[k] = existing[k]
    return new


def main():
    """Quiet."""
    parser = argparse.ArgumentParser(
        description="Merge an old docstring with a new one. Prioritizes the new one."
    )
    parser.add_argument("existing", type=str, help="The existing docstring.")
    parser.add_argument("new", type=str, help="The new docstring.")
    args = parser.parse_args()
    print(merge(NumpyDocString(args.existing), NumpyDocString(args.new)))


if __name__ == "__main__":
    main()
