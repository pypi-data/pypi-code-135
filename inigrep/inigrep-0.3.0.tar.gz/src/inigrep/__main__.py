import sys

import inigrep
import inigrep.core

import neaty.log


_USAGE = """
usage:
    inigrep [-1] [section].[key] [file]...
    inigrep [-1] -e|--basic [section].[key] [file]...
    inigrep [-1] -r|--raw [section].[key] [file]...
    inigrep [-1] -K|--lskey section [file]...
    inigrep [-1] -S|--lssct [file]...
    inigrep [-1] -P|--lspth [file]...
    inigrep --help
"""

__doc__ = """
Query INI file(s) for data

Usage:
    inigrep [-1] [section].[key] [file]...
    inigrep [-1] -e|--basic [section].[key] [file]...
    inigrep [-1] -r|--raw [section].[key] [file]...
    inigrep [-1] -K|--lskey section [file]...
    inigrep [-1] -S|--lssct [file]...
    inigrep [-1] -P|--lspth [file]...
    inigrep --help

First form implies the basic engine.

Option *-r* switches to raw mode, in which comments,
empty lines and whitespace are all preserved in applicable
contexts.

Key *keypath* consists of section name and key name delimited
by dot. Note that keypath may contain dots but key may not.

If *file* is not given or is a single dash, standard input
is read. Note that standard input is not duplicated in case
of multiple dashes.

If suitable key is found at multiple lines, all values
are printed, which allows for creating multi-line values.
Providing *-1* argument, however, always prints only one
line.

Options -K, -S and -P can be used for inspecting file structure;
-K needs an argument of section name and will list all keys from
that section. -S will list all sections and -P will list all
existing keypaths.


#### Examples ####

Having INI file such as

    [foo]
    bar=baz
    quux=qux
    quux=qux2
    quux=qux3

* `inigrep foo.bar ./file.ini` gives "bar".
* `inigrep foo.quux ./file.ini` gives three lines "qux", "qux2"
    and "qux3".
* `inigrep -P ./file.ini` gives two lines "foo.bar" and "foo.quux".
* `inigrep -K foo ./file.ini` gives two lines "bar" and "quux".
* `inigrep -S ./file.ini` gives "foo".
"""


class UsageError(RuntimeError):
    pass


class HelpNeeded(RuntimeError):
    pass


class VersionNeeded(RuntimeError):
    pass


class Args(neaty.log.Debuggable):

    _dscalar = ['args']

    def __init__(self, args):
        self.args = args
        self._log_birth()

    def take1(self):
        if not self.args:
            raise UsageError('missing argument')
        return self.args.pop(0)

    def take2(self):
        if len(self.args) < 2:
            raise UsageError('missing arguments')
        return self.args.pop(0), self.args.pop(0)

    def next(self):
        return self.args[0]

    def next_is(self, *cases):
        return self.args[0] in cases

    def rest(self):
        return self.args[:]


class Options(neaty.log.Debuggable):

    _dscalar = ['engine', 'oneline', 'kpath', 'reader']

    @classmethod
    def from_args(cls, args):
        o = cls()
        a = Args(args)
        while a.rest():
            if a.next_is('--help'): raise HelpNeeded()
            if a.next_is('--version'): raise VersionNeeded()
            elif a.next_is('-1'):             o.oneline = True; a.take1()
            elif a.next_is('-e', '--basic'):  o.engine = inigrep.core.values;        o.kpath = a.take2()[1]
            elif a.next_is('-r', '--raw'):    o.engine = inigrep.core.raw_values;    o.kpath = a.take2()[1]
            elif a.next_is('-K', '--lskey'):  o.engine = inigrep.core.list_keys;     o.kpath = a.take2()[1]
            elif a.next_is('-S', '--lssct'):  o.engine = inigrep.core.list_sections; o.kpath = '.'; a.take1()
            elif a.next_is('-P', '--lspth'):  o.engine = inigrep.core.list_paths;    o.kpath = '.'; a.take1()
            elif a.next().startswith('-'):
                raise UsageError('unknown engine: %s' % a.next())
            else: break
        if o.kpath is None:
            o.kpath = a.take1()
        files = a.rest()
        if not files:
            files = ['-']
        elif files == ['']:
            #FIXME: this is strange but turns out saturnin relies on it
            files = ['-']
        o.reader = inigrep.core.FileReader(files)
        return o

    def __init__(self):
        self.engine = inigrep.core.values
        self.oneline = False
        self.kpath = None
        self.reader = []
        self._log_birth()


def main():

    try:
        options = Options.from_args(sys.argv[1:])
    except UsageError as e:
        sys.stderr.write('%s\n' % _USAGE[1:])
        sys.stderr.write('error: %s\n' % e)
        sys.exit(2)
    except HelpNeeded as e:
        sys.stderr.write('%s\n' % __doc__)
        sys.stderr.write('%s\n' % e)
        sys.exit(0)
    except VersionNeeded:
        sys.stderr.write('%s\n' % inigrep.VERSION)
        sys.exit(0)

    gen = options.engine(options.kpath, options.reader)

    try:
        for line in gen:
            print(line)
            if options.oneline:
                break
    except inigrep.core.KeypathError as e:
        neaty.log.warn(e)
        sys.exit(2)


if __name__ == "__main__":
    main()
