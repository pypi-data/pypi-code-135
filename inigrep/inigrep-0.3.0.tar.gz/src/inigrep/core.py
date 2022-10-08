#!/usr/bin/python3

import functools
import os
import re
import sys

import neaty.log


__doc__ = """
inigrep
=======

grep for (some) INIs

inigrep is designed to read a particular simplistic dialect of
INI configuration files. In a sense, it can be considered as
a "grep for INIs", in that rather than parsing the file into
a typed memory structure for later access, it passes file each
time a query is done, and spits out relevant parts; treating
everything as text. Hence, it's not intended as replacement
for a full-blown configuration system but rather a quick & dirty
"swiss axe" for quick & dirty scripts.

That's not to say that you cannot do things nicely; but don't
count on speed -- well since you're using bash you obviously
don't -- and compliance -- simple things are simple, but there
are a bit unusual pitfalls.


The format by examples
----------------------

The most basic example understood by inigrep is identical
to most INI formats:

    # Let's call this simple.ini

    [foo]
        bar = baz
        qux = quux

    [corge]
        grault = graply

Structure here is obvious: two sections named `foo` and `corge`,
the first one has two key/value pairs and the other has one pair.

Getting values from this file is trivial:

    inigrep foo.bar simple.ini
    inigrep foo.qux simple.ini
    inigrep corge.grault simple.ini

would list `baz`, `quux` and `graply`.

This is where 80% of use cases are covered.


Multi-line
----------

Multi-line values are rather unusual but very simple:

    [lipsum]

        latin = Lorem ipsum dolor sit amet, consectetur adipiscing
        latin = elit, sed do eiusmod tempor incididunt ut labore et
        latin = dolore magna aliqua. Ut enim ad minim veniam, quis
        latin = ...

        english = [32] But I must explain to you how all this mistaken
        english = idea of denouncing of a pleasure and praising pain
        english = was born and I will give you a complete account of
        english = ...

This file can be read as:

    inigrep lipsum.latin lipsum.ini
    inigrep lipsum.english lipsum.ini


Exploration
-----------

Other than basic value retrieval, inigrep allows you to look around
first. For example, to list all keypaths available in a file:

    inigrep -P simple.ini

In case of simple.ini, this would print:

    foo.bar
    foo.qux
    corge.grault

Similarly:

    inigrep -S simple.ini

would list just the section names:

    foo
    corge

and

    inigrep -K foo simple.ini

would list all keys from section 'foo'

    bar
    qux
"""


class KeypathError(ValueError):
    pass


class Pipe(neaty.log.Debuggable):
    """
    Filter pipe of potential parts; call run() to get result.
    """

    _dscalar = ['reader', 'wanted_section', 'wanted_key']
    _dlist = ['filters']

    def __init__(self, reader, kpath='.', strict=False, listing=False):
        self.reader = reader
        self.strict = strict
        self.listing = listing
        self.filters = []
        section, key = kpath.rsplit('.', 1)
        if r'\\'[0] in key:
            raise KeypathError(r"invalid char '\' in key name: %r" % key)
        if r'[' in key:
            raise KeypathError(r"invalid char '[' in key name: %r" % key)
        if r'=' in key:
            raise KeypathError(r"invalid char '=' in key name: %r" % key)
        if r']' in section:
            raise KeypathError(r"invalid char ']' in section name: %r" % section)
        self.wanted_section = section
        self.wanted_key = key
        if not strict:
            self._add_filter(CommentFilter)
        if section:
            self._add_filter(SectionFilter)
        if key:
            self._add_filter(KeyFilter)
        if listing:
            self._add_filter(ListingFilter)
            self._add_filter(DedupFilter)
        if not strict:
            self._add_filter(NeFilter)
        if not self.filters:
            self._add_filter(NonFilter)
        self._log_birth()

    def _add_filter(self, fcls):
        """
        Append filter of class *fcls* to list of filters.
        """
        self.filters.append(fcls(self))

    def run(self):
        """
        Run pipe, reading, filtering and yielding all lines.
        """
        for oline in self.reader:
            for f in self.filters:
                nline = f.flt(oline)
                if nline is None:
                    break
                else:
                    oline = nline
            if nline is None:
                continue
            else:
                yield nline


class Filter(neaty.log.Debuggable):
    """
    Simple stateful filter with access to parent Pipe and data
    cache.

    Sub-class this to implement meaningful flt() method, which
    should take single line of input and based on its contents,
    state of the filter and pipe, decide whether to return the
    same line, altered line, or None.
    """

    _dscalar = ['_state']

    class _S_OFF:
        pass

    class _S_ON:
        pass

    def __init__(self, pipe):
        self.pipe = pipe
        self._state = self._S_OFF
        self._data = {}
        self._log_birth()

    def flt(self, line):
        if self.is_on():
            return line

    def turn_off(self):
        self._state = self._S_OFF

    def turn_on(self):
        self._state = self._S_ON

    def is_on(self):
        return self._state == self._S_ON


class SectionFilter(Filter):
    """
    Filter out only the wanted section body

    In listing modes returns also section name
    """

    def flt(self, line):
        if re.match(r'^\s*\[[^]]*\].*', line):
            tmp = line.lstrip()[1:]
            section, _ = tmp.split(']', 1)
            if section == self.pipe.wanted_section:
                self.turn_on()
                if self.pipe.listing:
                    return '[' + section + ']'
            else:
                self.turn_off()
        else:
            if not self.is_on():
                return
            if self.pipe.strict:
                return line
            else:
                return line.lstrip()


class KeyFilter(Filter):
    """
    Filter values from `key = value` pairs

    In listing modes, returns *key names* instead
    """

    def flt(self, line):
        line = line.lstrip()
        if '=' not in line:
            return
        tmp, value = line.split('=', 1)
        key = tmp.rstrip()
        if not self.pipe.strict:
            value = value.lstrip()
        if key != self.pipe.wanted_key:
            return
        if self.pipe.listing:
            return key
        else:
            return value


class DedupFilter(Filter):
    """
    Pass on values seen for first times.

    Used for section/key/path listing modes.
    """

    def flt(self, line):
        self._data['seen'] = self._data.get('seen', set())
        if line in self._data['seen']:
            return
        self._data['seen'].add(line)
        return line


class Symbol:

    instances = {}

    @classmethod
    def make(cls, value):
        if value not in cls.instances:
            cls.instances[value] = cls(value)
        return cls.instances[value]

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class ListingFilter(Filter):
    """
    Filter only section/keys/path names from the stream
    """

    AnySection = Symbol('__ANYSCT__')
    AnyKey = Symbol('__ANYKEY__')
    NoSection = Symbol('__NOSCT__')
    NoKey = Symbol('__NOKEY__')

    @property
    def section(self):
        if 'section' not in self._data:
            return self.NoSection
        return self._data.get('section')

    @section.setter
    def section(self, section):
        self._data['section'] = section

    def flt(self, line):
        #FIXME: this method is wayy more complicated than it needs to be
        if line.startswith('[') and line.endswith(']'):
            self.section = line[1:-1]
            key = self.NoKey
        elif '=' in line:
            tmp, _ = line.split('=', 1)
            key = tmp.strip()
        else:
            return

        def case(l, s, k):
            if l != self.pipe.listing:
                return False
            if (s, self.section) == (self.NoSection, self.NoSection):
                pass
            elif s == self.AnySection and self.section is not self.NoSection:
                pass
            else:
                return False
            if (k, key) == (self.NoKey, self.NoKey):
                pass
            elif k == self.AnyKey and key is not self.NoKey:
                pass
            else:
                return False
            return True
        if case('pth', self.NoSection, self.AnyKey):
            return '%s.%s' % (self.section, key)
        if case('pth', self.AnySection, self.NoKey):
            return
        if case('pth', self.AnySection, self.AnyKey):
            return '%s.%s' % (self.section, key)
        if case('sct', self.NoSection, self.AnyKey):
            return self.section
        if case('sct', self.AnySection, self.NoKey):
            return self.section
        if case('sct', self.AnySection, self.AnyKey):
            return
        if case('key', self.NoSection, self.NoKey):
            return
        if case('key', self.NoSection, self.AnyKey):
            return key
        if case('key', self.NoSection, self.AnyKey):
            return
        if case('key', self.AnySection, self.AnyKey):
            return key


class NonFilter(Filter):
    """
    Fallback filter to return all lines
    """

    def flt(self, line):
        return line


class CommentFilter(Filter):
    """
    Just strip comments
    """

    def flt(self, line):
        if re.match(r'^\s*[#;]', line):
            return
        line = re.sub(r'  *#.*', '', line)
        line = re.sub(r'  *;.*', '', line)
        if line:
            return line


class NeFilter(Filter):
    """
    Filter only non-empty lines.
    """

    def flt(self, line):
        if line:
            return line
        return


def values(kpath, reader):
    """
    Return list of values found by *reader* at key path *kpath*.

    *kpath* must be key path, i.e. string containing section and
    key names delimited by period.

    *reader* must be instance of FileReader generator or any similar
    generator that will yield lines.
    """
    pipe = Pipe(
        reader=reader,
        kpath=kpath,
        strict=False,
        listing=False,
    )
    for line in pipe.run():
        yield line


def raw_values(kpath, reader):
    """
    Return list of raw values found by *reader* at key path *kpath*.

    Same as values(), but uses raw inigrep engine (keeps comments
    and value leading/trailing whitespace).
    """
    pipe = Pipe(
        reader=reader,
        kpath=kpath,
        strict=True,
    )
    for line in pipe.run():
        yield line


def list_sections(kpath, reader):
    """
    Return list of sections found by *reader*.
    """
    pipe = Pipe(
        reader=reader,
        kpath='.',
        listing='sct',
    )
    for line in pipe.run():
        yield line


def list_keys(section, reader):
    """
    Return list of keys found by *reader* under *section*.
    """
    pipe = Pipe(
        reader=reader,
        kpath=section + '.',
        listing='key',
    )
    for line in pipe.run():
        yield line


def list_paths(kpath, reader):
    """
    Return list of all key paths found by *reader*.
    """
    pipe = Pipe(
        reader=reader,
        listing='pth',
    )
    for line in pipe.run():
        yield line


def FileReader(files):
    """
    Line generator that reads multiple files
    """
    for file in files:
        for line in _g_1file(file):
            yield line


def ExistingFileReader(files):
    """
    Line generator that reads multiple existent files

    Non-existent files are silently ignored.
    """
    for file in files:
        if not os.path.exists(file):
            continue
        for line in _g_1file(file):
            yield line


def _g_1file(file):
    """
    Line generator that reads single file
    """
    if file == '-':
        while True:
            line = sys.stdin.readline()
            if line:
                yield line[:-1]
            else:
                return
    else:
        with open(file, 'r') as fp:
            while True:
                line = fp.readline()
                if line:
                    yield line[:-1]
                else:
                    return


def load(files):
    """
    Create Ini file from concatenated files at paths *files*.

    Same as Ini.from_files().
    """
    return Ini.from_files(files)


def load_existent(files):
    """
    Create Ini file from concatenated files at paths *files*.

    Same as Ini.from_existent_files().
    """
    return Ini.from_existent_files(files)


class Ini:
    """
    Set of cached INI files
    """

    @classmethod
    def from_files(cls, files):
        """
        Initialize Ini object containing lines of all *files*.
        """
        cache = []
        for file in files:
            for line in _g_1file(file):
                cache.append(line)
        return cls(cache)

    @classmethod
    def from_existent_files(cls, files):
        """
        Initialize Ini object containing lines of all existent *files*.

        Similar to Ini.from_files(), but non-existent files are silently
        ignored.
        """
        cache = []
        for file in files:
            if not os.path.exists(file):
                continue
            for line in _g_1file(file):
                cache.append(line)
        return cls(cache)

    def __init__(self, cache):
        self._cache = cache

    def branch(self, prefix):
        """
        Create new Ini object containing only sections that
        start with *prefix*.
        """
        want_scts = []
        lines = []
        for sct in self.list_sections():
            if sct.startswith(prefix + '.'):
                want_scts.append(sct.replace(prefix + '.', '', 1))
        for sct in want_scts:
            lines.append('[%s]' % sct)
            for key in self.list_keys('%s.%s' % (prefix, sct)):
                for value in self.raw_values('%s.%s.%s' % (prefix, sct, key)):
                    lines.append('    %s =%s' % (key, value))
        return self.__class__(lines)

    def mkreader1(self, *kpath):
        """
        Create function to read single-line value at *kpath*.

        *kpath* must be list of the path elements.

        Return function which can be called without parameters and
        will return either single-line string corresponding to value
        at the key path *kpath*, or None, if there's no such value
        in the whole Ini object.
        """
        def _read1(*kpath):
            out = list(self.values('.'.join(kpath)))
            if out:
                return out[0]
            return None
        return functools.partial(_read1, *kpath)

    def mkreaderN(self, *kpath):
        """
        Create function to read multi-line value at *kpath*.

        *kpath* must be list of the path elements.

        Return function which can be called without parameters and
        will return either list of strings corresponding to values
        at the key path *kpath*, or None, if there's no such value
        in the whole Ini object.
        """
        def _readN(*kpath):
            return list(self.values('.'.join(kpath)))
        return functools.partial(_readN, *kpath)

    def _cache_reader(self):
        for line in self._cache:
            yield line

    def data(self):
        """
        Return dictionary containing all INI data

        Uses basic inigrep engine.

        A flat dictionary is returned, mapping all valid
        keypaths to lists of lines.
        """
        data = {}
        for kpath in self.list_paths():
            data[kpath] = list(self.values(kpath))
        return data

    def raw_data(self):
        """
        Return dictionary containing all raw INI data

        Same as Ini.data(), but uses raw inigrep engine (keeps
        comments and value leading/trailing whitespace).
        """
        data = {}
        for kpath in self.list_paths():
            data[kpath] = list(self.raw_values(kpath))
        return data

    def values(self, kpath):
        """
        Return list of values at key path *kpath*.

        Uses basic inigrep engine.
        """
        pipe = Pipe(
            reader=self._cache_reader(),
            kpath=kpath,
            strict=False,
            listing=False,
        )
        for line in pipe.run():
            yield line

    def raw_values(self, kpath):
        """
        Return list of values at key path *kpath*.

        Same as Ini.values(), but uses raw inigrep engine (keeps
        comments and value leading/trailing whitespace).
        """
        pipe = Pipe(
            reader=self._cache_reader(),
            kpath=kpath,
            strict=True,
        )
        for line in pipe.run():
            yield line

    def list_sections(self):
        """
        Return list of sections.

        Similar to Ini.values(), but uses section listing engine.
        """
        pipe = Pipe(
            reader=self._cache_reader(),
            kpath='.',
            listing='sct',
        )
        for line in pipe.run():
            yield line

    def list_keys(self, section):
        """
        Return list of keys under *section*.

        Similar to Ini.values(), but uses key listing engine.
        """
        pipe = Pipe(
            reader=self._cache_reader(),
            kpath=section + '.',
            listing='key',
        )
        for line in pipe.run():
            yield line

    def list_paths(self):
        """
        Return list of all defined key paths.

        Similar to Ini.values(), but uses key path listing engine.
        """
        pipe = Pipe(
            reader=self._cache_reader(),
            listing='pth',
        )
        for line in pipe.run():
            yield line
