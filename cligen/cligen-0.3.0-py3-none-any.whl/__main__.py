# coding: utf-8
# flake8: noqa
# cligen: 0.2.0, dd: 2022-10-09


import argparse
import importlib
import sys
import typing

from . import __version__


class HelpFormatter(argparse.RawDescriptionHelpFormatter):
    def __init__(self, *args: typing.Any, **kw: typing.Any):
        kw['max_help_position'] = 40
        super().__init__(*args, **kw)

    def _fill_text(self, text: str, width: int, indent: str) -> str:
        import textwrap

        paragraphs = []
        for paragraph in text.splitlines():
            paragraphs.append(textwrap.fill(paragraph, width,
                             initial_indent=indent,
                             subsequent_indent=indent))
        return '\n'.join(paragraphs)


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args: typing.Any, **kw: typing.Any):
        kw['formatter_class'] = HelpFormatter
        super().__init__(*args, **kw)


class DefaultVal(str):
    def __init__(self, val: typing.Any):
        self.val = val

    def __str__(self) -> str:
        return str(self.val)


class CountAction(argparse.Action):
    """argparse action for counting up and down

    standard argparse action='count', only increments with +1, this action uses
    the value of self.const if provided, and +1 if not provided

    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action=CountAction, const=1,
            nargs=0)
    parser.add_argument('--quiet', '-q', action=CountAction, dest='verbose',
            const=-1, nargs=0)
    """

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


def main(cmdarg: typing.Optional[typing.List[str]]=None) -> int:
    cmdarg = sys.argv if cmdarg is None else cmdarg
    parsers = []
    parsers.append(ArgumentParser())
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), dest='_gl_verbose', metavar='VERBOSE', nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=None, dest='_gl_comment', action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=None, dest='_gl_debug', action='store_true', help='insert debug statements in generated code')
    parsers[-1].add_argument('--version', action='store_true', help='show program\'s version number and exit')
    subp = parsers[-1].add_subparsers()
    px = subp.add_parser('gen', description='execute show related commands', help='execute show related commands')
    px.set_defaults(subparser_func='gen')
    parsers.append(px)
    parsers[-1].add_argument('--meld', action='store_true', help='present output as diff for inspection')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(False), action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(False), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('replace', description='replace a string in the _cligen_data/cli.yaml', help='replace a string in the _cligen_data/cli.yaml')
    px.set_defaults(subparser_func='replace')
    parsers.append(px)
    parsers[-1].add_argument('--from', dest='frm', help='original string to match (default: %(default)s)', required=True)
    parsers[-1].add_argument('--to', help='replacement string (default: %(default)s)', required=True)
    parsers[-1].add_argument('--backup', action='store_true', help='make a timestamped backup of the file (.YYYYMMDD-HHMMSS)')
    parsers[-1].add_argument('path', default=['**/__init__.py', '**/cli.yaml', '**/cligen/_test/data/*.yaml'], nargs='*', help='path pattern to scan for replacement (default: %(default)s) (default: %(default)s)')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(False), action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(False), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('convert', description='analyse argument file that uses ruamel.std.argparse and generate cligen data\n- commands currently cannot have a different name (using set first @subparser argument)\n', help='analyse argument file that uses ruamel.std.argparse and generate cligen data\n- commands currently cannot have a different name (using set first @subparser argument)\n')
    px.set_defaults(subparser_func='convert')
    parsers.append(px)
    parsers[-1].add_argument('--append', action='store_true', help='append _cligen_data to __init__.py')
    parsers[-1].add_argument('path')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(False), action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(False), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('comment', description='show cligen_data comments (from cligen.__init__.py)', help='show cligen_data comments (from cligen.__init__.py)')
    px.set_defaults(subparser_func='comment')
    parsers.append(px)
    parsers[-1].add_argument('--update', help='update cligen_data comments in __init__.py (argument can be directory or file) (default: %(default)s)')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(0), nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(False), action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(False), action='store_true', help='insert debug statements in generated code')
    parsers.pop()
    # sp: gen
    _subparser_found = False
    for arg in cmdarg[1:]:
        if arg in ['-h', '--help', '--version']:  # global help if no subparser
            break
    else:
        end_pos = None if '--' not in cmdarg else cmdarg.index('--')
        for sp_name in ['gen', 'replace', 'convert', 'comment']:
            if sp_name in cmdarg[1:end_pos]:
                break
        else:
            # insert default in first position, this implies no
            # global options without a sub_parsers specified
            cmdarg.insert(1, 'gen')
    if '--version' in cmdarg[1:]:
        if '-v' in cmdarg[1:] or '--verbose' in cmdarg[1:]:
            return list_versions(pkg_name='cligen', version=None, pkgs=['ruamel.yaml'])
        print(__version__)
        return 0
    if '--help-all' in cmdarg[1:]:
        try:
            parsers[0].parse_args(['--help'])
        except SystemExit:
            pass
        for sc in parsers[1:]:
            print('-' * 72)
            try:
                parsers[0].parse_args([sc.prog.split()[1], '--help'])
            except SystemExit:
                pass
        sys.exit(0)
    args = parsers[0].parse_args(args=cmdarg[1:])
    for gl in ['verbose', 'comment', 'debug']:
        glv = getattr(args, '_gl_' + gl, None)
        if isinstance(getattr(args, gl, None), (DefaultVal, type(None))) and glv is not None:
            setattr(args, gl, glv)
        delattr(args, '_gl_' + gl)
        if isinstance(getattr(args, gl, None), DefaultVal):
            setattr(args, gl, getattr(args, gl).val)
    cls = getattr(importlib.import_module('cligen.cligen'), 'CligenLoader')
    obj = cls(args)
    funcname = getattr(args, 'subparser_func', None)
    if funcname is None:
        parsers[0].parse_args(['--help'])
    fun = getattr(obj, funcname + '_subcommand', None)
    if fun is None:
        fun = getattr(obj, funcname)
    ret_val = fun()
    if ret_val is None:
        return 0
    if isinstance(ret_val, int):
        return ret_val
    return -1

def list_versions(pkg_name: str, version: typing.Union[str, None], pkgs: typing.Sequence[str]) -> int:
    version_data = [
        ('Python', '{v.major}.{v.minor}.{v.micro}'.format(v=sys.version_info)),
        (pkg_name, __version__ if version is None else version),
    ]
    for pkg in pkgs:
        try:
            version_data.append(
                (pkg,  getattr(importlib.import_module(pkg), '__version__', '--'))
            )
        except ModuleNotFoundError:
            version_data.append((pkg, 'NA'))
        except KeyError:
            pass
    longest = max([len(x[0]) for x in version_data]) + 1
    for pkg, ver in version_data:
        print('{:{}s} {}'.format(pkg + ':', longest, ver))
    return 0


if __name__ == '__main__':
    sys.exit(main())
