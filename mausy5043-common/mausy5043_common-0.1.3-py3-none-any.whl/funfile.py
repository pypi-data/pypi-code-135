#!/usr/bin/env python3

"""Provide file operation functions."""

import os
import syslog


def cat(fname):
    """Read a file (line-by-line) into a variable.

    Args:
        fname (str) : file to read from

    Returns:
          (str) : file contents
    """
    ret = ""
    if os.path.isfile(fname):
        with open(fname, 'r') as fin:
            ret = fin.read().strip('\n')
    return ret


def syslog_trace(trace, logerr, out2console):
    """Log a (multi-line) message to syslog.
    Args:
        trace (str): Text to send to log
        logerr (int): syslog errornumber
        out2console (bool): If True, will also print the 'trace' to the screen
    Returns:
        None
    """
    log_lines = trace.split('\n')
    for line in log_lines:
        if line and logerr:
            syslog.syslog(logerr, line)
        if line and out2console:
            print(line)
