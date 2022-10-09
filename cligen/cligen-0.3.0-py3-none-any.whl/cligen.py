# coding: utf-8

import sys
import os
import io
import datetime
from pathlib import Path
from _ast import *  # NOQA
from ast import parse
from textwrap import dedent
import warnings

from . import __version__

import ruamel.yaml
warnings.simplefilter("ignore", ruamel.yaml.error.ReusedAnchorWarning)


# the imports are dynamically generated, primarily from imports needed for included actions
# verimp, normally gets __version__ and _package_data from the __init__.py file (import . )
# but this can be changed to some other file

VERSION = '__version__'
PKG_DATA = '_package_data'

# to store informaton about standard argparse actions
# metavar: add setting metavar if global opt
# defaults: add %(default)s if !AddDefaults
_standard_actions = dict(
    store=dict(metavar=True, defaults=True),
    store_const=dict(metavar=True, defaults=True),
    store_true=dict(metavar=False, defaults=False),
    store_false=dict(metavar=False, defaults=False),
    append=dict(metavar=True, defaults=True),
    append_const=dict(metavar=True, defaults=True),
    count=dict(metavar=False, defaults=True),
    extend=dict(metavar=True, defaults=True),
)

# the ArgumentParser is inherited by the subparsers, so any
# arguments need a subclass. The HelpFormatter formats
# prologues and epilogues differently, filling each
# paragraph (e.g. use block style folded scalar with blank line)
_pregen = """\
# coding: utf-8
# flake8: noqa
# cligen: {version}, dd: {today}, args: {args}

{imports}{verimp}

class HelpFormatter(argparse.RawDescriptionHelpFormatter):
    def __init__(self, *args: typing.Any, **kw: typing.Any):
        kw['max_help_position'] = {max_help_position}
        super().__init__(*args, **kw)

    def _fill_text(self, text: str, width: int, indent: str) -> str:
        import textwrap

        paragraphs = []
        for paragraph in text.splitlines():
            paragraphs.append(textwrap.fill(paragraph, width,
                             initial_indent=indent,
                             subsequent_indent=indent))
        return '\\n'.join(paragraphs)


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args: typing.Any, **kw: typing.Any):
        kw['formatter_class'] = HelpFormatter
        super().__init__(*args, **kw)

"""

_list_versions = """\

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

"""

# older dynamic version, should be phased out
# _list_versions1 = """\
#
# def list_versions():
#    xxxxx
#    version_data = [
#        ('Python', '{v.major}.{v.minor}.{v.micro}'.format(v=sys.version_info)),
#        (_package_data['full_package_name'], __version__),
#    ]
#    # longest = len(version_data[0][0])
#    if isinstance(_package_data.get('install_requires', []), list):
#        pkgs = _package_data.get('install_requires', [])
#    else:
#        pkgs = _package_data['install_requires'].get('any', [])
#    for pkg in pkgs:
#        for x in '=!<>':
#            pkg = pkg.split(x, 1)[0]
#        try:
#            version_data.append((pkg,  getattr(importlib.import_module(pkg), '__version__', '--')))
#        except KeyError:
#            pass
#    longest = max([len(x[0]) for x in version_data])
#    for pkg, ver in version_data:
#        print('{:{}s} {}'.format(pkg + ':', longest + 1, ver))
#
# """

_postgen = """\

if __name__ == '__main__':
    sys.exit(main())
"""

smart_formatter = '''

class SmartFormatter(argparse.HelpFormatter):
    """
    you can only specify one formatter in standard argparse, so you cannot
    both have pre-formatted description (RawDescriptionHelpFormatter)
    and ArgumentDefaultsHelpFormatter.
    The SmartFormatter has sensible defaults (RawDescriptionFormatter) and
    the individual help text can be marked ( help="R|" ) for
    variations in formatting.
    version string is formatted using _split_lines and preserves any
    line breaks in the version string.
    If one help string starts with D|, defaults will be added to those help
    lines that do not have %(default)s in them
    """

    _add_defaults = True  # make True parameter based on tag?

    def __init__(self, *args, **kw):
        super(SmartFormatter, self).__init__(*args, **kw)

    def _fill_text(self, text, width, indent):
        return ''.join([indent + line for line in text.splitlines(True)])

    def _split_lines(self, text, width):
        if text.startswith('D|'):
            SmartFormatter._add_defaults = True
            text = text[2:]
        elif text.startswith('*|'):
            text = text[2:]
        if text.startswith('R|'):
            return text[2:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)

    def _get_help_string(self, action):
        if SmartFormatter._add_defaults is None:
            return argparse.HelpFormatter._get_help_string(self, action)
        help = action.help
        if '%(default)' not in action.help:
            if action.default is not argparse.SUPPRESS:
                defaulting_nargs = [argparse.OPTIONAL, argparse.ZERO_OR_MORE]
                if action.option_strings or action.nargs in defaulting_nargs:
                    help += ' (default: %(default)s)'
        return help

    def _expand_help(self, action):
        """mark a password help with '*|' at the start, so that
        when global default adding is activated (e.g. through a helpstring
        starting with 'D|') no password is show by default.
        Orginal marking used in repo cannot be used because of decorators.
        """
        hs = self._get_help_string(action)
        if hs.startswith('*|'):
            params = dict(vars(action), prog=self._prog)
            if params.get('default') is not None:
                # you can update params, this will change the default, but we
                # are printing help only after this
                params['default'] = '*' * len(params['default'])
            return self._get_help_string(action) % params
        return super(SmartFormatter, self)._expand_help(action)

'''

# could optimize this to notice an shorthand was used
# only check for sp_name until -- encountered, probably only until
# the first argument after those starting with a single '-'
default_sub_parser_resolution = """\
{bi}# sp: {sp}
{bi}_subparser_found = False
{bi}for arg in cmdarg[1:]:
{bi}    if arg in ['-h', '--help', '--version']:  # global help if no subparser
{bi}        break
{bi}else:
{bi}    end_pos = None if '--' not in cmdarg else cmdarg.index('--')
{bi}    for sp_name in {sp_names}:
{bi}        if sp_name in cmdarg[1:end_pos]:
{bi}            break
{bi}    else:
{bi}        # insert default in first position, this implies no
{bi}        # global options without a sub_parsers specified
{bi}        cmdarg.insert(1, '{sp}')
"""

help_all_text = """\
{bi}if '--help-all' in cmdarg[1:]:
{bi}    try:
{bi}        parsers[0].parse_args(['--help'])
{bi}    except SystemExit:
{bi}        pass
{bi}    for sc in parsers[1:]:
{bi}        print('-' * 72)
{bi}        try:
{bi}            parsers[0].parse_args([sc.prog.split()[1], '--help'])
{bi}        except SystemExit:
{bi}            pass
{bi}    sys.exit(0)
"""

# formatter_class=SmartFormatter


class CligenLoader(object):
    def __init__(self, args, config=None):
        self._args = args
        self._config = config
        self.verimp_file = None
        self._extend_main = None
        self._pd = None

    def gen(self):
        # self._args often not available when called from import
        verbose = getattr(self._args, 'verbose', 0)
        if verbose > 1:
            print('cwd:', os.getcwd())
        yaml = ruamel.yaml.YAML()
        yaml.width = 132
        datas_found = []
        cli_yaml_file = Path('cli.yaml')
        if cli_yaml_file.exists():
            if verbose > 0:
                print('found:', cli_yaml_file)
            datas_found.append(yaml.load(cli_yaml_file))
        init_file = Path('__init__.py')
        if init_file.exists():
            # extract both package data and YAML in one go
            _end = None
            pds = None  # package data
            ys = None  # yaml string
            for line in init_file.open():
                if pds is None and PKG_DATA in line:
                    _end = ')' if 'dict(' in line else '}'
                    pds = collect = [line.split('=')[1].lstrip()]
                    continue
                if ys is None and '_cligen_data' in line:
                    ys = collect = []
                    _end = line.split('=')[1].lstrip()[:3]
                    if verbose > 0:
                        print('found: _cligen_data in', init_file)
                    continue
                if _end is None:
                    continue
                # if line.strip().startswith(_end):  # not working on develop
                if line.startswith(_end):
                    if pds is collect:
                        pds.append(line)
                    _end = None
                    continue
                if collect is not None:
                    collect.append(line)
            if pds is not None:
                try:
                    self._pd = literal_eval(''.join(pds))
                except SyntaxError as e:
                    print(f'{e=}')
                    for idx, line in enumerate(pds):
                        print(f'{idx:2}: {line}', end='')
                    raise

            if ys is not None:
                datas_found.append(yaml.load(''.join(ys)))
        # make sure only one data source exists
        if len(datas_found) == 0:
            print('no input found ( __init__.py with _cligen_data / cli.yaml )')
            return
        elif len(datas_found) == 2:
            print('multiple input found ( __init__.py with _cligen_data / cli.yaml )')
            return
        if isinstance(datas_found[0], dict):
            for k, v in datas_found[0].items():
                try:
                    if k.tag.value == '!Cli':
                        version = int(k.value)
                        data = v
                except (KeyError, AttributeError):
                    continue
                try:
                    if k.tag.value in ['!File', '!ImportFile']:
                        assert isinstance(k.value, str)
                        assert isinstance(v, str)
                        path = Path(k.value)
                        if path.name == '__main__.py':
                            self._extend_main = '\n\n' + v + '\n'
                            continue
                        if k.tag.value == '!ImportFile':
                            self.verimp_file = path
                        if path.parent != '.':
                            path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text(v)
                except KeyError:
                    pass
            if verbose > 0:
                print('data from dict version:', version)
        elif isinstance(datas_found[0], list):
            data = datas_found[0]
            assert data.tag.value == '!Cli'
            data = list(data)
            version = 0
        else:
            print('data typ unknown', type(data))
            return

        if version == 0:
            dbg = getattr(self._args, 'debug', None)
            comment = getattr(self._args, 'comment', False)
            cligen = CliGen0(
                data,
                verimp_file=self.verimp_file,
                extend_main=self._extend_main,
                pkg_data=self._pd,
                debug=dbg,
                comment=comment,
            )
        else:
            print('unknown !Cli version', version)
            return
        # cligen.walk()
        buf = io.StringIO()
        cligen.gen_parser(fp=buf)  # have to run gen_parser first to set lists for gen_pre
        # print(buf.getvalue())

        test_py = Path('__main__.py')
        if test_py.exists() and self._args.meld:
            import tempfile

            with tempfile.NamedTemporaryFile("w", prefix="oitnb_") as fp:
                cligen.gen_pre(fp=fp)
                fp.write(buf.getvalue())
                cligen.gen_post(fp=fp)
                fp.flush()
                os.system(f'meld -n "{fp.name}" "{test_py!s}"')
            return
        if verbose > 0:
            print('writing __main__.py')
        with test_py.open('w') as fp:
            cligen.gen_pre(fp=fp)
            fp.write(buf.getvalue())
            cligen.gen_post(fp=fp)


    def replace(self):
        from .scanner import Scanner

        scanner = Scanner(self._args.path)
        for found in scanner():
            found.replace(self._args.frm, self._args.to, backup=self._args.backup)

    def convert(self):
        import subprocess

        mdl = 'eppa.ooo'
        if self._args.path == '.':
            try:
                mdl = os.getcwd().split('/py/')[1].replace('/', '.')
            except:
                mdl = os.getcwd().split('/site-packages/')[1].replace('/', '.')
            initpy = Path(os.getcwd()) / '__init__.py'
        else:
            mdl = self._args.path
            initpy = Path(self._args.path).resolve() / '__init__.py'
        os.chdir('/')
        os.environ['CLIGENCONVERT'] = '1'
        print('setting env.: CLIGENCONVERT=1')
        cmd = [sys.executable, '-m', mdl, '--cligen']
        print('cmd:', ' '.join(cmd), end='\n\n')
        try:
            res = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8')
        except Exception as e:
            print('exception res:\n', e.output.decode('utf-8'), '\n', e, sep='')
        else:
            print('res:\n', sep='')

        lines = []
        for line in res.splitlines():
            print(line)
            if line.startswith('_cligen_data'):
                if self._args.append:
                    lines.append(line)
                self.insert_comments_from_cligen_init(lines if self._args.append else None, verbose=1)
                continue
            if self._args.append and lines:
                lines.append(line)
            if line.startswith('"""'):
                break

        if self._args.append:
            if lines:
                assert initpy.exists()
                with initpy.open('a') as fp:
                    fp.write('\n')
                    fp.write('\n'.join(lines))
                    fp.write('\n')
        return

    def comment(self, update=None):
        update = self._args.update if update is None else update
        if update is None:
            self.insert_comments_from_cligen_init(None, verbose=1)
            return
        path = Path(update)
        if path.is_dir():
            path /= '__init__.py'
        pos = -1
        lines = []
        doit = False
        for idx, line in enumerate(path.read_text().splitlines()):
            if doit and line.lstrip().startswith('#'):
                continue
            elif line.startswith('_cligen_data'):
                pos = idx+1
                doit = True
            elif doit:
                doit = False
            lines.append(line)
        assert pos != -1

        add_lines = []
        self.insert_comments_from_cligen_init(add_lines, verbose=0)
        lines[pos:pos] = add_lines
        path.write_text('\n'.join(lines) + '\n')
        

    def insert_comments_from_cligen_init(self, lines, verbose=0):
        """show and append commentlines at top of cligen_data in cligen's __init__.py"""
        ununinit = Path(__file__).parent / '__init__.py'
        doit = False
        for line in ununinit.open():
            if doit and line.lstrip().startswith('#'):
                if verbose > 0:
                    print(line, end='')
                if lines is not None:
                    lines.append(line.rstrip())
                continue
            elif line.startswith('_cligen_data'):
                doit = True
                continue
            doit = False


class CliGenBase:
    def __init__(self, data, verimp_file=None, extend_main=None, pkg_data=None, debug=False, comment=False):
        self._data = data
        self.extend_main = extend_main
        self._pkg_data = pkg_data
        self._debug = debug
        self._import_line = self.scan_import_file(verimp_file)
        self._global_options = []
        self.sub_parsers = None  # list of single key-value pairs
        self._default_subparser = None
        self._global_default_options = []
        self._import_from_module = self._instantiate = self._no_sub_parser = None
        self.smart_formatter = False
        self._help_all = True
        self._pre_subparser_option_tags = set(('!PreSubparserOption', '!PSO'))
        self._option_tags = set(('!Option', '!Opt', '!O', '!ReqOption', '!ReqOpt'))
        self._arg_tags = set(('!Argument', '!Arg', '!A'))
        self._all_option_tags = self._pre_subparser_option_tags | self._option_tags
        self._tag_map = {}
        self.add_tag('Help H')
        self.add_tag('AddDefaults')
        self.add_tag('Prolog', 'description')
        self.add_tag('Epilog')
        self.add_tag('Action')
        self.add_tag('Nargs N')
        self._no_quotes = set(['some_action', 'float', 'int'])
        self._add_defaults = None
        self._shorthands = {}
        self._actions = self.load_actions(comment=comment)  # _actions.copy()
        self._actions_used = set()
        self._configs = self.load_configs(comment=comment)
        self._configs_used = []
        self._max_help_position = 40
        # only full imports, no 'from xx' import, to simplify parsing of actions & configs,
        # that add to the list of imports
        self._imports = set(['', 'sys', 'argparse', 'importlib'])
        # print(self._all_option_tags)

    @property
    def debug(self):
        return self._debug

    def add_tag(self, tags, key=None):
        # if key not given use first tag -> lowercase
        if not isinstance(tags, list):
            tags = tags.split()
        if key is None:
            key = tags[0].lower()
        for t in tags:
            self._tag_map[t] = key

    def load_actions(self, comment=False):
        # returns a mapping of class name to imports/class_body/filename_stem/default_parameters
        # might be better off using the stem as the lookup
        # - import lines and parameters should come before the class statement
        # - any comments before the class statement are dropped
        # - comments after the class statement are dropped unless comment is True
        # this cannot handle # as the first non-blank line within a multiline python string!
        res = {}
        actions_dir = Path(__file__).parent / '_action'
        # print('ad', actions_dir)
        for action_file in sorted(actions_dir.glob('*.py')):
            if action_file.name == '__init__.py':
                continue
            params = {}
            in_params = []
            import_lines, body = action_file.read_text().split('class ')
            imports = set()
            for line in import_lines.splitlines():
                # handle YAML that specifies default parameters for action
                if line.startswith('_parameters = '):
                    in_params.append(line)
                    # print('xxx', line[15])
                    continue
                if in_params:
                    if line.startswith(in_params[0][15] * 3):
                        params = ruamel.yaml.YAML(typ='safe').load('\n'.join(in_params[1:]))
                        in_params = None
                    else:
                        in_params.append(line)
                    continue
                if line.startswith('import '):
                    for x in line.split(' ', 1)[1].split(','):
                        imports.add(x)
            name = body.split('(', 1)[0]
            if not comment:
               body = ''.join([l for l in body.splitlines(True) if not l.lstrip().startswith('#')])
            res[name] = dict(
                imports=imports, body='class ' + body, stem=action_file.stem, params=params
            )
        return res

    def load_configs(self, comment=False):
        # returns a mapping of file_name_stem name to imports/class_name/class_body
        # might be better off using the stem as the lookup
        # - import lines should come before the class statement
        # - any comments before the class statement are dropped
        # - comments after the class statement are dropped unless comment is True
        # this cannot handle # as the first non-blank line within a multiline python string!
        res = {}
        configs_dir = Path(__file__).parent / '_config'
        for config_file in sorted(configs_dir.glob('*.py')):
            if config_file.name == '__init__.py':
                continue
            import_lines, body = config_file.read_text().split('class ')
            imports = set()
            for line in import_lines.splitlines():
                # handle YAML that specifies default parameters for config
                if line.startswith('import '):
                    for x in line.split(' ', 1)[1].split(','):
                        imports.add(x)
            name = body.split('(', 1)[0]
            if ':' in name:
                name = body.split(':')[0]
            if not comment:
               body = ''.join([l for l in body.splitlines(True) if not l.lstrip().startswith('#')])
            res[config_file.stem] = dict(imports=imports, name=name, body='class ' + body)
        return res

    def scan_import_file(self, fn):
        """
        return the string used for importing version data
        """
        imp_fn = '.' if fn is None else str(fn.with_suffix(''))
        imports = []
        try:
            for line in open('__init__.py' if fn is None else fn):
                if line.startswith(VERSION):
                    imports.append(VERSION)
                if not self._pkg_data and line.startswith(PKG_DATA):
                    imports.append(PKG_DATA)
            if imports:
                return f'\n\nfrom {imp_fn} import {", ".join(imports)}\n'
        except FileNotFoundError:
            pass
        return ''

    def clean_name(self, s):
        """cannot have dash in name -> underscore"""
        for k, v in {'-': '_'}.items():
            s = s.replace(k, v)
        return s


    def gen_parser(self, data=None, name=None, fp=sys.stdout, base_indent=4):
        if data is None:
            return self.gen_parser(self._data, fp=fp, base_indent=base_indent)
        bi = ' ' * base_indent
        kw, optargs, self.sub_parsers = self.get_kw(data)
        print(f'{bi}parsers = []', file=fp)
        if self._configs_used:
            config_name = self._configs[self._configs_used[-1]]['name']
            print(
                f'{bi}config = {config_name}(path={quoted(self._config_file)})',
                file=fp,
            )
            # testing
            # print(f'{bi}print(config.data)', file=fp)
            # print(f'{bi}print("testing", config.get("global", "keep", pd=3))', file=fp)
            # print(f'{bi}print("testing", config.get("global", "bla", pd=4))', file=fp)
        if name is None:
            if self.smart_formatter:
                if kw:
                    kw += ', '
                kw += 'formatter_class=SmartFormatter'
            # this is the ArgumentParser as defined in _pregen
            print(f'{bi}parsers.append(ArgumentParser({kw}))', file=fp)
        for oa in optargs:
            oas = self.optarg_str(*oa)
            print(f'{bi}parsers[-1].add_argument({oas})', file=fp)
        # print(f"{bi}parsers[-1].add_argument('--version', action='version', version=__version__)", file=fp)
        if VERSION in self._import_line:
            print(
                f"{bi}parsers[-1].add_argument('--version', action='store_true', help='show program\\'s version number and exit')",
                file=fp,
            )
        if self.sub_parsers:
            print(f'{bi}subp = parsers[-1].add_subparsers()', file=fp)
        for subparser in self.sub_parsers:
            sp_name, subparser_data = list(subparser.items())[0]
            kw, optargs, subparsers = self.get_kw(
                subparser_data, top_level=False, sp_name=sp_name
            )
            if self.smart_formatter:
                if kw:
                    kw += ', '
                kw += 'formatter_class=SmartFormatter'
            kwcomma = ', ' if kw else ''
            print(f"{bi}px = subp.add_parser('{sp_name}'{kwcomma}{kw})", file=fp)
            # the following line might not be needed for alternate defaults setting using config.get()
            # that line adds the name of the subparser to the subparser
            sp_name_clean = self.clean_name(sp_name)
            print(f"{bi}px.set_defaults(subparser_func='{sp_name_clean}')", file=fp)
            print(f'{bi}parsers.append(px)', file=fp)
            # print('optargs 1', optargs)
            for oa in optargs + self._global_options:
                oas = self.optarg_str(*oa, subparser=sp_name)
                print(f'{bi}parsers[-1].add_argument({oas})', file=fp)
        if self.sub_parsers:
            print(f'{bi}parsers.pop()', file=fp)
        if self._configs_used:
            # print(f'{bi}config.set_defaults(parser=parsers[0])', file=fp)
            cfg_parm = ', config=config'   # so that the main code has access to the config file
        else:
            cfg_parm = ''
        if name is None:
            if self._default_subparser:
                sp = self._default_subparser
                spn = repr([list(k.keys())[0] for k in self.sub_parsers])
                fp.write(default_sub_parser_resolution.format(bi=bi, sp=sp, sp_names=spn))
            if VERSION in self._import_line:
                print(f"{bi}if '--version' in cmdarg[1:]:", file=fp)
                if self._pkg_data:
                    # if ver is static generated during cligen, you need to regenerate even if
                    # a version is updated without commandline change
                    ver = None  # "'" + self._pkg_data['__version__'] + "'"
                    fpn = self._pkg_data['full_package_name']
                    if isinstance(self._pkg_data.get('install_requires', []), list):
                        to_inst = self._pkg_data.get('install_requires', [])
                    elif self._pkg_data.get('install_requires') is not None:
                        to_inst = self._pkg_data['install_requires'].get('any', [])
                    else:
                        to_inst = []
                    pkgs = []
                    for pkg in to_inst:
                        for x in '=!<>~':
                            pkg = pkg.split(x, 1)[0]
                        if pkg in ['ruamel.std.argparse', 'ruamel.appconfig']:
                            print(
                                f'found required package "{pkg}" which is not needed with cligen'
                            )
                        pkgs.append(pkg)
                    print(
                        f"{bi}{bi}if '-v' in cmdarg[1:] or '--verbose' in cmdarg[1:]:", file=fp
                    )
                    print(
                        f"{bi}{bi}{bi}return list_versions(pkg_name='{fpn}', version={ver}, pkgs={pkgs})",
                        file=fp,
                    )
                elif PKG_DATA in self._import_line:
                    print(
                        f"{bi}{bi}if '-v' in cmdarg[1:] or '--verbose' in cmdarg[1:]:", file=fp
                    )
                    print(f'{bi}{bi}{bi}return list_versions()', file=fp)
                print(f'{bi}{bi}print(__version__)', file=fp)
                print(f'{bi}{bi}return 0', file=fp)
            if self._help_all:
                fp.write(help_all_text.format(bi=bi))
            # print(f'{bi}print(\'cmdarg:\', cmdarg)', file=fp)
            print(f'{bi}args = parsers[0].parse_args(args=cmdarg[1:])', file=fp)
            if self.debug:
                print(f"{bi}debug('args 1:', args)", file=fp)
            # global options processing
            if self._global_default_options:
                print(f'{bi}for gl in {self._global_default_options}:', file=fp)
                print(f"{bi}{bi}glv = getattr(args, '_gl_' + gl, None)", file=fp)
                if self.sub_parsers:
                    print(f'{bi}{bi}if isinstance(getattr(args, gl, None), (DefaultVal, type(None))) and glv is not None:', file=fp)
                    print(f'{bi}{bi}{bi}setattr(args, gl, glv)', file=fp)
                else:
                    print(f'{bi}{bi}setattr(args, gl, glv)', file=fp)
                print(f"{bi}{bi}delattr(args, '_gl_' + gl)", file=fp)
                print(f"{bi}{bi}if isinstance(getattr(args, gl, None), DefaultVal):", file=fp)
                print(f"{bi}{bi}{bi}setattr(args, gl, getattr(args, gl).val)", file=fp)
            if self.debug:
                print(f"{bi}debug('args 2:', args)", file=fp)
            if False and self._required_options:
                print(f'{bi}req_options_found = True', file=fp)
                qo = ', '.join([f"'{o}'" for o in self._required_options])
                print(f'{bi}for attr in [{qo}]:', file=fp)
                print(f'{bi}{bi}if getattr(args, attr, None) is None:', file=fp)
                print(f"{bi}{bi}{bi}attr = ('--' if len(attr) > 1 else '-') + attr", file=fp)
                print(f"{bi}{bi}{bi}print('missing required option', attr)", file=fp)
                print(f'{bi}{bi}{bi}req_options_found = False', file=fp)
                print(f'{bi}{bi}if not req_options_found:', file=fp)
                print(f'{bi}{bi}{bi}sys.exit(1)', file=fp)
                # self._required_options:
                # if not hassatr
            if self._import_from_module is not None:
                ifm = self._import_from_module
                print(f"{bi}funcname = getattr(args, 'subparser_func', None)", file=fp)
                print(f'{bi}if funcname is None:', file=fp)
                print(f"{bi*2}parsers[0].parse_args(['--help'])", file=fp)
                if ifm:
                    print(
                        f'{bi}fun = getattr(importlib.import_module("{ifm}"), funcname)',
                        file=fp,
                    )
                    print(f'{bi}ret_val = fun(args)', file=fp)   # add config?
                else:  # inserted in __main__ itself
                    print(f'{bi}ret_val = globals()[funcname](args)', file=fp)   # add config?
                print(f'{bi}if ret_val is None:', file=fp)
                print(f'{bi}{bi}return 0', file=fp)
                print(f'{bi}if isinstance(ret_val, int):', file=fp)
                print(f'{bi}{bi}return ret_val', file=fp)
                print(f'{bi}return -1', file=fp)
            elif self._instantiate is not None:
                try:
                    m, c = self._instantiate.rsplit('.', 1)
                    print(
                        f"""{bi}cls = getattr(importlib.import_module('{m}'), '{c}')""",
                        file=fp,
                    )
                    print(f'{bi}obj = cls(args{cfg_parm})', file=fp)
                except ValueError:
                    c = self._instantiate
                    print(f'{bi}obj = {c}(args{cfg_parm})', file=fp)
                print(f"{bi}funcname = getattr(args, 'subparser_func', None)", file=fp)
                # print(f'{bi}if funcname == \'version\' and not hasattr(obj, \'version\'):', file=fp)
                # print(f'{bi}{bi}return list_versions()', file=fp)
                print(f'{bi}if funcname is None:', file=fp)
                if self.sub_parsers:
                    print(f"{bi*2}parsers[0].parse_args(['--help'])", file=fp)
                else:
                    # if no subparsers you need to have a run method, or do everything from init() and exit()
                    print(f"{bi*2}funcname = 'run'", file=fp)
                # print(f'{bi}fun = getattr(obj, args.subparser_func)', file=fp)
                print(f"{bi}fun = getattr(obj, funcname + '_subcommand', None)", file=fp)
                print(f'{bi}if fun is None:', file=fp)
                # print(f"{bi*2}print('no _subcommand')", file=fp)
                print(f'{bi*2}fun = getattr(obj, funcname)', file=fp)
                # print(f'{bi}else:', file=fp)
                # print(f"{bi*2}print('found _subcommand')", file=fp)
                print(f'{bi}ret_val = fun()', file=fp)
                print(f'{bi}if ret_val is None:', file=fp)
                print(f'{bi}{bi}return 0', file=fp)
                print(f'{bi}if isinstance(ret_val, int):', file=fp)
                print(f'{bi}{bi}return ret_val', file=fp)
                print(f'{bi}return -1', file=fp)
            elif self._no_sub_parser is not None:
                try:
                    m, c = self._no_sub_parser.rsplit('.', 1)
                    print(
                        f"""{bi}entry = getattr(importlib.import_module('{m}'), '{c}')""",
                        file=fp,
                    )
                    print(f'{bi}res = entry(args{cfg_parm})', file=fp)
                except ValueError:
                    c = self._no_sub_parser
                    print(f'{bi}res = {c}(args{cfg_parm})', file=fp)
                print('>>>>>>>>> resolve exit value, if not int assuming .retval attribute')
                print(f'{bi}return res if isinstance(res, int) else getattr(res, \'retval\', 0)', file=fp)
            else:
                print('need to have either !Module, !Instance, or !Main in cli YAML')
                sys.exit(1)

    def gen_opt(self, orgtag, data, argument=False):
        # print('gen_opt: elem', orgtag, data)
        args = []
        kw = {}
        attribute = None
        for elem in data:
            tag = None
            try:
                tag = elem.tag.value
            except AttributeError:
                if isinstance(elem, str):
                    if '=' in elem:
                        print(f'\n>>>>> there is an equal sign in {elem},', end='')
                        alt = elem.replace('=', ': ')
                        print(f' are you sure this should not be: {alt} ?\n')
                    if attribute is None:
                        attribute = elem
                    if argument:
                        args.append("'" + elem + "'")
                    elif len(elem) == 1:
                        args.append("'-" + elem + "'")
                    else:
                        args.append("'--" + elem + "'")
                    continue
            if tag is None:
                if isinstance(elem, dict):
                    assert len(elem) == 1
                    if 'required' in elem and elem['required']:
                        print('cannot use "required: True", use tag option with !ReqOption')
                        sys.exit(1)
                    kw.update(elem)
            else:
                if tag == '!Action':
                    for k1, v1 in self._actions.items():
                        if elem.value == k1:
                            print(f'change "!Action {tag}" to "!Action {v1["stem"]}')
                            sys.exit(1)
                        if elem.value == v1['stem']:
                            elem.value = k1
                            break
                    else:
                        if elem.value not in _standard_actions:
                            print('unknown action:', elem.value)
                try:
                    key = self._tag_map[tag[1:]]
                except Exception as e:
                    print('exception', e)
                    print(self._tag_map)
                    sys.exit(0)
                if key == 'help':
                    if self._add_defaults is None:
                        if elem.value.startswith('D|'):
                            self.smart_formatter = True
                        elif elem.value.startswith('R|'):
                            self.smart_formatter = True
                        elif elem.value.startswith('*|'):
                            self.smart_formatter = True
                kw[key] = elem.value
        # only add global options when not processing subparsers
        if self.sub_parsers is None and orgtag not in self._pre_subparser_option_tags:
            self._global_options.append((args, kw))
            if orgtag.startswith('!Req'):
                print('cannot have global !ReqOption, replicate for each subparser')
                sys.exit(1)
        else:
            if orgtag.startswith('!Req'):
                kw['required'] = True
        return (args, kw)

    def get_kw(self, data, top_level=True, sp_name=None):
        res = {}
        optarg = []
        subparsers = []
        todo = []
        for elem in data:
            # print('get_kw: elem', elem, elem.tag.value)
            tag = elem.tag.value
            if tag is None:
                assert isinstance(elem, dict)
                if isinstance(elem, dict) and isinstance(list(elem.values())[0], list):
                    subparsers.append(elem)
                    continue  # skip subparsers
                res.update(elem)  # key-value pair
                continue
            if not top_level and tag == '!DefaultSubparser':
                assert sp_name is not None
                if self._default_subparser not in [None, sp_name]:
                    print(f'cannot have !DefaultSubparser for both "{self._default_subparser}" and "{sp_name}"')
                    sys.exit(1)
                self._default_subparser = sp_name
                continue
            if not top_level and tag == '!Alias':
                res.setdefault('aliases', []).extend(
                    elem if isinstance(elem, list) else [elem.value]
                )
                continue
            if not top_level and tag == '!Shorthand':
                v = elem.value
                if elem.value in self._shorthands:
                    print(
                        f'shorthand {v!r}, for subparser {sp_name!r} reused for {self._shorthands[v]!r}'
                    )
                    sys.exit(1)
                self._shorthands[v] = sp_name
                continue
            if top_level and tag == '!HelpWidth':
                self._max_help_position = int(elem.value)
                continue
            if top_level and tag == '!Module':
                todo.append(tag)
                self._import_from_module = elem.value
                continue
            if top_level and tag == '!Instance':
                todo.append(tag)
                self._instantiate = elem.value
                continue
            if top_level and tag == '!Main':
                todo.append(tag)
                self._no_sub_parser = elem.value
                continue
            if top_level and tag == '!AddDefaults':
                self._add_defaults = elem.value
                continue
            # if top_level and tag == '!HelpAll':
            #    self._help_all = True
            #    continue
            if top_level and tag == '!Config':
                # determine config file type and path, don't expand paths at cligen run time!
                if isinstance(elem, list):
                    v = elem[0]
                    self._config_file = Path(elem[1])
                else:
                    if elem.value[0] in '~/':
                        # assume a full path with extension determining config typ
                        self._config_file = Path(elem.value)
                        v = self._config_file.suffix.lstrip('.')
                    elif '/' in elem.value:
                        # assume a partial path with extension determining config typ
                        self._config_file = elem.value
                        v = Path(self._config_file).suffix.lstrip('.')
                    else:
                        v = elem.value
                        if self._pkg_data:
                            self._config_file = self._pkg_data.get(
                                'config_subdir', self._pkg_data['full_package_name']
                            )
                        elif PKG_DATA in self._import_line:
                            self._config_file = "_package_data['full_package_name']"
                if v not in self._configs and v.lower() in self._configs:
                    v = elem.value = v.lower()
                if v not in self._configs:
                    print('unknown config format', v)
                    sys.exit(1)
                if '_base' not in self._configs_used:
                    if self._configs['_base']['name'] in self._configs[v]['body']:
                        self._configs_used.insert(0, '_base')
                        self._imports.update(self._configs['_base']['imports'])
                self._configs_used.append(v)
                self._imports.update(self._configs[v]['imports'])
                continue
            if tag in self._all_option_tags:
                optarg.append(self.gen_opt(tag, elem))
                continue
            if tag in self._arg_tags:
                optarg.append(self.gen_opt(tag, elem, argument=True))
                continue
            key = self._tag_map[tag[1:]]
            try:
                res[key] = elem.value
            except AttributeError as e:
                # you can tag an anchored scalar, but if you do "!Help &name text1 text2"
                # you get the same result as "&name !Help text1 text2"
                # so you cannot do "!Prolog *name", but in cligen you can do "!Prolog [*name]"
                try:
                    res[key] = elem[0].value
                except Exception:
                    raise e
        # return ', '.join(['{k}={v!r}'.format(k=k, v=v) for k,v in res.items()]), optarg
        if sp_name:
            # print('get_kw', sp_name, res, optarg, subparsers)
            if 'description' in res and 'help' not in res:
                res['help'] = res['description']
        if len(todo) > 1:
            print('you can have only one of\n-', '\n- '.join(todo))
            sys.exit(1)
        if self._add_defaults is not None:
            for oa in optarg:
                if not isinstance(oa[1], dict):
                    continue
                oa = oa[1]
                act = oa.get('action')
                if act in _standard_actions:
                    if not _standard_actions[act]['defaults']:
                        continue
                elif act:
                    if act in ['CountAction']:  # ToDo load from file into self._actions
                        continue
                if 'help' in oa:
                    oa['help'] += self._add_defaults

        return self.kws(res), optarg, subparsers

    def optarg_str(self, args, kw, subparser=None):
        res = ''
        assert bool(args)
        if args:
            res += ', '.join(args)
        if kw:
            # the following did not work for '--unlock-file', because of the dash before "file"
            # dest_val = args[0].replace('-', '').replace("'", '')
            dest_val = args[0].replace("'", '').lstrip('-').replace('-', '_')
            kws = self.kws(kw, value=dest_val, subparser=subparser, argument="'-" not in res)
            if kws:
                res += ', ' + kws
        return res

    def kws(self, kworg, value=None, subparser=None, argument=False):
        # if self.debug:
        #    print('subp', subparser, repr(value), kworg)
        kw = kworg.copy()  # so you can e.g. do del kw['default'], but keep value for subparsers
        kw_strs = []
        if 'action' in kw:
            # assign here so checking for default works
            if kw['action'] in self._actions:  # not for standard actions
                x = self._actions[kw['action']]['params'].copy()
                x.update(kw)
                kw = x
        if subparser is None and value is not None and 'action' not in kw:
            kw['action'] = 'store'
        if subparser is None and self._no_sub_parser is None \
           and ('default' in kw or kw.get('action', None) in _standard_actions):
            if 'dest' not in kw and not argument:
                #if 'default' in kw:
                #    del kw['default']
                # kw_strs.append(f'default=None')
                if self._configs_used and kw.get('nargs') == '+':
                    print('?????????????????????????')
                if 'default' in kw:
                    defval = kw.pop('default')
                    if self._configs_used:
                        kw_strs.append(f'default=DefaultVal(config.get(\'global\', {value!r}, pd={defval!r}))')
                    else:
                        kw_strs.append(f'default=DefaultVal({defval!r})')
                else:
                    if self._configs_used:
                        kw_strs.append(f'default=DefaultVal(config.get(\'global\', {value!r}, pd={None!r}))')
                    else:
                        kw_strs.append(f'default=None') # necessary for global store_true/store_false
                if self.debug:
                    print('_gl', value, kw)
                kw_strs.append(f"dest='_gl_{value}'")
                # needed for postprocessing _gl
                self._global_default_options.append(value)
                # store_true/false actions don't have metavar
                # if 'metavar' not in kw and v not in ['store_true', 'store_false']:
                if 'metavar' not in kw and _standard_actions.get(
                    kw.get('action', None), {}
                ).get('metavar', True):
                    # print('sa', kw.get('action'), _standard_actions.get(kw.get('action', None), {}))
                    # prevent metavar from getting _GL_ prefix

                    kw_strs.append(f"metavar='{value.upper()}'")
        # if subparser is not None and self._configs_used:
        #     # get default values from config if availble
        #     if 'default' in kw:
        #         defval = kw.pop('default')
        #     else:
        #         defval = None
        #     kw_strs.append(f'default=config.get({subparser!r}, {value!r}, pd={defval!r})')
        if subparser is not None:
            add_default = False
            if self._configs_used and kw.get('nargs') == '+':
                # setting a default on nargs='+' with a positional results in you still needing
                # to provide a positional, wiping the default
                del kw['nargs']
                defval = kw.get('default')
                if value in self._global_default_options:
                     kw_strs.append(f'nargs=\'+\' if DefaultVal(config.get({subparser!r}, {value!r}, pd={defval!r}))=={defval!r} else \'*\'')
                elif self._configs_used:  # but not global
                     kw_strs.append(f'nargs=\'+\' if config.get({subparser!r}, {value!r}, pd={defval!r})=={defval!r} else \'*\'')
                print('?????????????????????????')
            if 'default' in kw:
                add_default = True
                defval = kw.pop('default')
            else:
                if  kw.get('action') in _standard_actions:
                    defval = _standard_actions[kw['action']]['defaults']
                else:
                    defval = None
            # get default values from config if availble
            if value in self._global_default_options and self._configs_used:
                 kw_strs.append(f'default=DefaultVal(config.get({subparser!r}, {value!r}, pd={defval!r}))')
            elif self._configs_used:  # but not global
                 kw_strs.append(f'default=config.get({subparser!r}, {value!r}, pd={defval!r})')
            elif value in self._global_default_options:  # global but no config
                 kw_strs.append(f'default=DefaultVal({defval!r})')
            elif add_default:  # necessary for None in tri-state boolean
                q = ""
                if isinstance(defval, str) and not defval.isalpha():
                    q = '"'
                kw_strs.append(f'default={q}{defval}{q}')
        for k, v in kw.items():
            if False and k == 'default':  #  or isinstance(v, str) and v.startswith('store'):
                if subparser is not None:
                    continue
                # print('kw', kw)
                if 'dest' not in kw:
                    kw_strs.append(f"dest='_gl_{value}'")
                    self._global_default_options.append(value)
                    # store_true/false actions don't have metavar
                    if 'metavar' not in kw and v not in ['store_true', 'store_false']:
                        # if 'metavar' not in kw:
                        # prevent metavar from getting _GL_ prefix
                        kw_strs.append(f"metavar='{value.upper()}'")
            if isinstance(v, list):
                kw_strs.append(f'{k}={v!r}')
            elif v in self._actions:
                kw_strs.append(f'{k}={v}')
                # for k1, v1 in self._actions[v]['params'].items():
                #    if k1 not in kw:
                #       kw_strs.append(f'{k1}={v1!r}')
                self._actions_used.add(v)
                self._imports.update(self._actions[v]['imports'])
            elif k == 'type':
                # if the full path is provided e.g. pathlib.Path, make sure the module is imported
                if '.' in v:
                    self._imports.add(v.rsplit('.', 1)[0])
                kw_strs.append(f'{k}={v}')
            elif v in self._no_quotes:
                kw_strs.append(f'{k}={v}')
            elif isinstance(v, ruamel.yaml.comments.TaggedScalar) and v.tag.value == '!NQS':
                # non quoted scalar e.g. for method/function values
                kw_strs.append(f'{k}={v}')
            else:
                kw_strs.append(f'{k}={v!r}')
        return ', '.join(kw_strs)

    def gen_pre(self, fp=sys.stdout, base_indent=4):
        # include everything before the actual parsing code
        fp.write(
            _pregen.format(
                version=__version__,
                today=datetime.date.today(),
                imports='\nimport '.join(sorted(self._imports)),
                verimp=self._import_line,
                max_help_position=self._max_help_position,
                args=' '.join(sys.argv[1:]),  # invocation arguments
            )
        )
        if self._import_from_module:
            mn = self._import_from_module
            funs = ', '.join([list(k.keys())[0] for k in self.sub_parsers])
            print(f'from {mn} import {funs}', file=fp)
        if self._debug:
            fp.write('debug = print\n\n')
        # needed for defaults of global options
        if self._global_default_options:
            # DefaultVal might not be there, if it is it can be tested with isinstance(X, str)i
            # e.g. in DateAction, to do conversion 
            fp.write(dedent("""
                class DefaultVal(str):
                    def __init__(self, val: typing.Any):
                        self.val = val

                    def __str__(self) -> str:
                        return str(self.val)

            """))
        for c in self._configs_used:
            fp.write('\n')
            fp.write(self._configs[c]['body'])
            fp.write('\n')
        for a in sorted(self._actions_used):
            # assume no newlines before and after each class definition in action/*.py
            fp.write('\n')
            fp.write(self._actions[a]['body'])
            fp.write('\n')
        bi = ' ' * base_indent
        print(f'\ndef main(cmdarg: typing.Optional[typing.List[str]]=None) -> int:', file=fp)
        print(f'{bi}cmdarg = sys.argv if cmdarg is None else cmdarg', file=fp)
        if self._shorthands:
            print(
                f'{bi}sh_subp = {self._shorthands}.get(cmdarg[0].rsplit(os.sep, 1)[-1])',
                file=fp,
            )
            print(f'{bi}if sh_subp is not None:', file=fp)
            print(f'{bi}{bi}cmdarg.insert(1, sh_subp)', file=fp)

    def gen_post(self, fp=sys.stdout):
        if self.smart_formatter:
            fp.write(smart_formatter)
        if self.extend_main:
            fp.write(self.extend_main)
        if self._pkg_data:
            fp.write(_list_versions)
        elif PKG_DATA in self._import_line:
            pass
            # fp.write(_list_versions1)
        fp.write(_postgen)


class CliGen0(CliGenBase):
    pass


def quoted(s, q="'"):
    s = str(s)  # could be Path or integer
    if s and (s[0] not in '"\'' or s[0] != s[-1]):
        s = q + s + q
    return s


if sys.version_info >= (3, 8):
    from ast import Str, Num, Bytes, NameConstant  # NOQA


def literal_eval(node_or_string):
    """
    Safely evaluate an expression node or a string containing a Python
    expression.  The string or node provided may only consist of the following
    Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
    sets, booleans, and None.

    Even when passing in Unicode, the resulting Str types parsed are 'str' in Python 2.
    I don't now how to set 'unicode_literals' on parse -> Str is explicitly converted.
    """
    _safe_names = {'None': None, 'True': True, 'False': False}
    if isinstance(node_or_string, str):
        node_or_string = parse(node_or_string, mode='eval')
    if isinstance(node_or_string, Expression):
        node_or_string = node_or_string.body
    else:
        raise TypeError('only string or AST nodes supported')

    def _convert(node):
        if isinstance(node, Str):
            if sys.version_info < (3,) and not isinstance(node.s, unicode):
                return node.s.decode('utf-8')
            return node.s
        elif isinstance(node, Bytes):
            return node.s
        elif isinstance(node, Num):
            return node.n
        elif isinstance(node, Tuple):
            return tuple(map(_convert, node.elts))
        elif isinstance(node, List):
            return list(map(_convert, node.elts))
        elif isinstance(node, Set):
            return set(map(_convert, node.elts))
        elif isinstance(node, Dict):
            return dict((_convert(k), _convert(v)) for k, v in zip(node.keys, node.values))
        elif isinstance(node, NameConstant):
            return node.value
        elif sys.version_info < (3, 4) and isinstance(node, Name):
            if node.id in _safe_names:
                return _safe_names[node.id]
        elif (
            isinstance(node, UnaryOp)
            and isinstance(node.op, (UAdd, USub))
            and isinstance(node.operand, (Num, UnaryOp, BinOp))
        ):  # NOQA
            operand = _convert(node.operand)
            if isinstance(node.op, UAdd):
                return +operand
            else:
                return -operand
        elif (
            isinstance(node, BinOp)
            and isinstance(node.op, (Add, Sub))
            and isinstance(node.right, (Num, UnaryOp, BinOp))
            and isinstance(node.left, (Num, UnaryOp, BinOp))
        ):  # NOQA
            left = _convert(node.left)
            right = _convert(node.right)
            if isinstance(node.op, Add):
                return left + right
            else:
                return left - right
        elif isinstance(node, Call):
            func_id = getattr(node.func, 'id', None)
            if func_id == 'dict':
                return dict((k.arg, _convert(k.value)) for k in node.keywords)
            elif func_id == 'set':
                return set(_convert(node.args[0]))
            elif func_id == 'date':
                return datetime.date(*[_convert(k) for k in node.args])
            elif func_id == 'datetime':
                return datetime.datetime(*[_convert(k) for k in node.args])
        err = SyntaxError('malformed node or string: ' + repr(node))
        err.filename = '<string>'
        err.lineno = node.lineno
        err.offset = node.col_offset
        err.text = repr(node)
        err.node = node
        raise err

    return _convert(node_or_string)
