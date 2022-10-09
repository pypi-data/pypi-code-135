import sys
import os
import subprocess
import importlib

from .adapter import STDIO, ArgsInAdapter, ArgsOutAdapter

from .sysutil import get_argv, check_argv, opt_argv, merge_os_env
from .ctxenv import CtxEnv

from smog.file import FileStat


PYTHON = sys.executable
PYTHON_EXT = ".py"


def is_python_ctx(args):
    return args[0].endswith(PYTHON_EXT)


def normalize_args(args):
    """
    strip away ".py" ending at args[0]
    the other args are not touched
    """
    args = list(args)
    if is_python_ctx(args):
        args[0], _ = FileStat(args[0]).splitext()
    return args


def get_call_context(args):
    return [PYTHON] if is_python_ctx(args) else []


def convert_module():
    import smogconvert

    return smogconvert


def convert_package():
    return convert_module().__package__


def is_predefined(fnam):
    package = FileStat(convert_module().__spec__.origin).dirname()
    path = FileStat(package).join([fnam])
    if path.exists():
        if path.is_dir():
            raise Exception("is directory", path.name)
        return path.name


def procrun(args, input=None, env=None, capture_output=True, raise_err=True):
    rc = subprocess.run(
        args=args,
        input=input,
        env=env,
        capture_output=capture_output,
    )

    if raise_err and (rc is None or rc.returncode > 0):
        raise Exception("failed", rc)

    return rc


def convert(args, input=None, container=None, env=None, open_external=True):

    _env = merge_os_env(env)

    exprefnam = is_predefined(args[0])
    if not exprefnam:
        exprefnam = args[0]
        raise NotImplementedError("not found", args[0])  # todo

    if open_external:
        _exec_ctx = get_call_context(args)
        _exec_ctx.extend([exprefnam, *args[1:]])

        cap_mode = args[2] == STDIO

        if container:
            print("external run. drop container", container)

        rc = procrun(
            args=_exec_ctx,
            input=input,
            env=_env,
            capture_output=cap_mode,
        )

    else:
        # todo

        raise NotImplementedError("todo")

        nargs = normalize_args(args)
        mod = importlib.import_module(convert_module().__package__ + "." + nargs[0])

        with CtxEnv(_env) as ctxenv:
            # bump env
            try:
                rc = mod.convert(nargs, container)
            except Exception as ex:
                print(ex, file=sys.stderr)
                rc = ex

    return rc


def run_piped(converters, args, open_external=True, debug=False):

    if not open_external:
        raise NotImplementedError("untested")

    if len(args) < 2:
        raise Exception("wrong arguments")

    cmds = []

    # set stdin stdout processing
    # so everything is processed in memory (where possible)
    for conv in converters:
        if conv:
            cmds.append([conv, "-", "-"])

    # patch stdin stdout for first and last
    cmds[0][1] = args[1]
    cmds[-1][2] = args[2]

    debug and print("cmds", cmds)

    inp = None
    for cmd in cmds:
        if type(cmd[0]) in [tuple, list]:
            # add the tail of optional args from the tuple, or list
            proc = cmd[0][0]
            eargs = cmd[0][1] if len(cmd[0]) > 1 else None
            cmd[0] = proc
            if eargs:
                if type(eargs) is not list:
                    raise Exception("wrong type. list expected")
                # add as tail
                cmd.extend(eargs)

        debug and print(cmd)
        try:
            rc = convert(cmd, open_external=open_external, input=inp)
        except Exception as ex:
            return ex

        # set output as input for next in the pipe
        inp = rc.stdout

    return inp
