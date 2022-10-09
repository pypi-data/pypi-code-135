import sys
import os
import subprocess

FIRST_OPT_ARG = 3


def procrun(args, input=None, env=None, capture_output=True, raise_err=True):
    rc = subprocess.run(
        args=args,
        input=input,
        env=env,
        capture_output=capture_output,
    )
    if raise_err and rc.returncode > 0:
        raise Exception("failed", rc)
    return rc


def get_argv(args=None):
    if args is None:
        args = sys.argv
    return args


def check_argv(args=None, err_ok=False):
    args = get_argv(args)
    _chk = len(args) < FIRST_OPT_ARG
    if err_ok:
        return _chk
    if _chk:
        raise Exception("wrong number of call parameter")


def opt_argv(args=None):
    args = get_argv(args)
    return args[FIRST_OPT_ARG:]


def pop_argv(opts, default=None):
    if opts:
        if len(opts) > 0:
            return opts.pop(0)
    return default


def merge_os_env(env=None):
    _env = dict(os.environ)
    if env:
        for k, v in env.items():
            if v:
                _env[k] = str(v)
            else:
                del _env[k]
    return _env
