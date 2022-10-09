import sys
import os

from io import BytesIO

from .sysutil import get_argv, check_argv, opt_argv

STDIO = "-"


class Adapter(object):
    def __init__(self):
        self.fd = None

    def open(self):
        if self.fd:
            raise Exception("already open")
        self.fd = self._open()

    def close(self):
        if self.fd:
            self._close(self.fd)
            self.fd = None

    def _open(self):
        pass

    def _close(self, fd):
        pass

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


class InAdapter(Adapter):
    def read(self, blen=-1):
        return self.fd.read(blen)


class OutAdapter(Adapter):
    def write(self, byts):
        return self.fd.write(byts)


class FileAdapter(Adapter):
    def __init__(self, fnam, mode):
        Adapter.__init__(self)
        fnam = expand_path(fnam)
        self.fnam = fnam
        self.mode = mode

    def set_mode(self, mode):
        self.mode = mode

    def _open(self):
        return open(self.fnam, self.mode)

    def _close(self, fd):
        fd.close()


def expand_path(fnam):
    fnam = os.path.expandvars(fnam)
    fnam = os.path.expanduser(fnam)
    return fnam


def ensure_path(fnam, exist_ok=True):
    try:
        rc = os.makedirs(os.path.dirname(fnam), exist_ok=exist_ok)
    except Exception as ex:
        print("ensure_path", fnam, ex, file=sys.stderr)
        raise ex
    if os.path.exists(fnam):
        if os.path.isdir(fnam):
            raise Exception("is folder", fnam)
        if not exist_ok:
            raise Exception("already exist", fnam)


class FileInAdapter(InAdapter, FileAdapter):
    def __init__(self, fnam, mode="rb"):
        InAdapter.__init__(self)
        FileAdapter.__init__(self, fnam, mode)


class FileOutAdapter(OutAdapter, FileAdapter):
    def __init__(self, fnam, mode="wb", make_dirs=True):
        OutAdapter.__init__(self)
        FileAdapter.__init__(self, fnam, mode)
        if make_dirs:
            ensure_path(self.fnam)


class StdinAdapter(InAdapter):
    def __init__(self):
        InAdapter.__init__(self)

    def _open(self):
        return sys.stdin.buffer


class StdoutAdapter(OutAdapter):
    def __init__(self):
        OutAdapter.__init__(self)

    def _open(self):
        return sys.stdout.buffer


class ArgAdapter(Adapter):
    def __init__(self, clsstd, clscust, argno, args=None):
        Adapter.__init__(self)

        if args is None:
            args = sys.argv
        self.args = args

        self.is_stdio = args[argno] == STDIO
        if self.is_stdio:
            self.ad = clsstd()
        else:
            if type(args[argno]) == str:
                self.ad = clscust(args[argno])
            elif type(args[argno]) == BytesIO:
                # todo testing
                self.ad = args[argno]
            else:
                raise NotImplementedError()

    def optargs(self):
        return self.args[FIRST_OPT_ARG:]

    def _open(self):
        return self.ad._open()

    def _close(self, fd):
        return self.ad._close(fd)


class ArgOneInAdapter(InAdapter, ArgAdapter):
    def __init__(self, args=None):
        InAdapter.__init__(self)
        ArgAdapter.__init__(self, StdinAdapter, FileInAdapter, 1, args)


class ArgTwoOutAdapter(OutAdapter, ArgAdapter):
    def __init__(self, args=None):
        OutAdapter.__init__(self)
        ArgAdapter.__init__(self, StdoutAdapter, FileOutAdapter, 2, args)


# use this rather than own impl with e.g. argparse
# to support "in-proc" dynamic loading with import lib (later feature)


class ArgsInAdapter(ArgOneInAdapter):
    pass


class ArgsOutAdapter(ArgTwoOutAdapter):
    pass


class ArgsOptsAdapter(object):
    """
    handling of positional and named parameter
    """

    def __init__(self, args):
        self.args = args
        self.opts = []
        self.kv = {}

        for arg in args:
            pos = arg.find("=")
            if pos < 0:
                if len(self.kv) > 0:
                    raise Exception("positional argument after named argument")
                self.opts.append(arg)
                continue
            k = arg[0:pos].strip()
            v = arg[pos + 1 :].strip()
            if k in self.kv:
                raise Exception("parameter already defined", k, v)
            self.kv[k] = v

    def pop(self, default=None):
        """get positional cmd-line argument"""
        if len(self.opts) > 0:
            return self.opts.pop(0)
        return default

    def get(self, k, default=None):
        """get keyword cmd-line argument"""
        # this will return always the first default requested with get
        return self.kv.setdefault(k, default)

    def get_bool(self, k, default=False):
        # this will return always the first default requested with get
        rc = self.get(k, default)
        if type(rc) == str:
            rc = rc.lower()
            rc = rc in ["1", "y", "yes", "true"]
        return rc


class ArgsTeeAdapter(object):
    def __init__(self, args):
        check_argv(args)
        self.args = args

        opts = opt_argv(self.args)
        self.opts = ArgsOptsAdapter(opts)

        self.outf = self.opts.get("out", None)
        if self.outf:
            self.outf = expand_path(self.outf)

        # pipe input unchanged to output
        self.pipeio = self.opts.get_bool("pipeio", False)

    def tee(self, inp, outp):
        if self.outf:
            ensure_path(self.outf)
            with open(self.outf, "wb") as f:
                f.write(outp)

        byts = outp if not self.pipeio else inp

        with ArgsOutAdapter(self.args) as fo:
            fo.write(byts)

        return byts
