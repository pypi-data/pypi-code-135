import os
import re
import sys
from argparse import ArgumentParser

from pandas import DataFrame, merge

pattern = re.compile(r'^.+_([a-zA-Z]*)\..*')

class CustomParser(ArgumentParser):

    def error(self, message: str):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def _extract_info(file_path: str, already_just_name: bool = False):
    if not already_just_name:
        file_name_w_ext = file_path[file_path.rindex('/') + 1:]
    else:
        file_name_w_ext = file_path
    assert re.match(
        pattern=pattern, string=file_name_w_ext
    ), f'{file_name_w_ext} => file name must be in the form "id_label.ext", where id is any combination of characters, but label must be alphabetical characters only.'
    _index = file_name_w_ext.rindex('_')
    ext_index = file_name_w_ext.rindex('.')
    id = file_name_w_ext[:_index]
    label = file_name_w_ext[_index + 1:ext_index]
    return os.path.realpath(file_path), id, label


def create_csv(main_dir: str, root: str = '.'):
    assert main_dir in os.listdir(
        root), f'{main_dir} must be a directory within {root}'
    dirs = [
        d for d in os.listdir(root)
        if d != main_dir and os.path.isdir(os.path.join(root, d))
    ]
    columns = ['path', 'id', 'label']

    main_dir_data = [
        _extract_info(os.path.join(root, main_dir, f_path))
        for f_path in os.listdir(os.path.join(root, main_dir))
    ]
    main_df = DataFrame(main_dir_data,
                        columns=columns).set_index(['id', 'label'])

    for directory in dirs:
        dir_data = [
            _extract_info(os.path.join(root, directory, f_path))
            for f_path in os.listdir(os.path.join(root, directory))
        ]
        tmp_df = DataFrame(dir_data,
                           columns=columns).set_index(['id', 'label'])
        main_df = merge(main_df,
                        tmp_df,
                        left_index=True,
                        right_index=True,
                        suffixes=['', f'_{directory}'])

    return main_df.reset_index()


def main():
    parser = CustomParser()
    parser.add_argument(
        '-m',
        '--main_dir',
        required=True,
        help=
        'The directory name containing the final version of the transformed files'
    )
    parser.add_argument('-o', '--output', required=True, help='Full path to output')
    parser.add_argument(
        '-r',
        '--root',
        default='.',
        help='The root directory to create a csv of all subdirs')

    args = parser.parse_args()
    if args.help:
        parser.print_help()
        sys.exit(0)
    
    final_df = create_csv(args.main_dir, args.root)
    final_df.to_csv(args.output, index=False)