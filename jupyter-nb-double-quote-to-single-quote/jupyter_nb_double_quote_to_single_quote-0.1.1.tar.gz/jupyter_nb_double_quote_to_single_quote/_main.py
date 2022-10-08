from __future__ import annotations

import argparse
import json
from typing import Sequence

from jupyter_notebook_parser import JupyterNotebookParser

from jupyter_nb_double_quote_to_single_quote._helper import (
    fix_double_quotes_in_file_contents,
)


def fix_double_quotes(filename: str) -> int:
    try:
        parser = JupyterNotebookParser(filename)
    except Exception as exc:
        print(f'{filename}: Failed to load ({exc})')
        return 1
    else:
        return_value = 0
        notebook_content = parser.notebook_content
        code_cell_indices = parser.get_code_cell_indices()
        code_cell_sources = parser.get_code_cell_sources()

        assert len(code_cell_indices) == len(code_cell_sources)

        for i in range(len(code_cell_indices)):
            this_source = code_cell_sources[i]
            this_index = code_cell_indices[i]
            fixed_source = fix_double_quotes_in_file_contents(this_source)

            if fixed_source != this_source:
                fixed_source_lines = fixed_source.split('\n')
                # fmt: off
                fixed_source_lines_ = (
                    [_ + '\n' for _ in fixed_source_lines[:-1]]
                    + [fixed_source_lines[-1]]
                )
                # fmt: on
                notebook_content['cells'][this_index]['source'] = fixed_source_lines_
                return_value = 1

        if return_value == 1:
            with open(filename, 'w') as fp:
                json.dump(notebook_content, fp, indent=1)
                # Jupyter notebooks (.ipynb) always ends with a new line
                # but json.dump does not.
                fp.write('\n')

        return return_value


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        return_value = fix_double_quotes(filename)
        if return_value != 0:
            print(f'Double quotes -> single quotes in: {filename}')
        retv |= return_value

    return retv


if __name__ == '__main__':
    raise SystemExit(main())
