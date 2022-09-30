# -*- coding: utf-8 -*-
######################################################
#     _____                  _____      _     _      #
#    (____ \       _        |  ___)    (_)   | |     #
#     _   \ \ ____| |_  ____| | ___ ___ _  _ | |     #
#    | |  | )/ _  |  _)/ _  | |(_  / __) |/ || |     #
#    | |__/ ( ( | | | ( ( | | |__| | | | ( (_| |     #
#    |_____/ \_||_|___)\_||_|_____/|_| |_|\____|     #
#                                                    #
#    Copyright (c) 2022 DataGrid Development Team    #
#    All rights reserved                             #
######################################################

import subprocess
import sys
import time
import urllib
import webbrowser

import psutil

from ._version import __version__  # noqa
from .datatypes import Audio, Curve, DataGrid, Image, Text, Video  # noqa
from .utils import _in_jupyter_environment, get_localhost

DATAGRID_PROCESS = None


def _is_running(name):
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)
        except Exception:
            continue
        if process.name().startswith(name):
            return process.is_running() and process.status() != psutil.STATUS_ZOMBIE
    return False


def _process_method(name, method):
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)
        except Exception:
            continue
        if process.name().startswith(name):
            getattr(process, method)()


def terminate():
    """
    Terminate the DataGrid servers.
    """
    global DATAGRID_PROCESS
    _process_method("node", "terminate")
    if DATAGRID_PROCESS:
        DATAGRID_PROCESS.terminate()
        DATAGRID_PROCESS = None


def launch(host=None, port=4000, debug=False):
    """
    Launch the DataGrid servers.

    Args:
        port: (int) the port of the DataGrid frontend server. The
            backend server will start on port + 1.
    """
    global DATAGRID_PROCESS

    host = host if host is not None else get_localhost()

    if not _is_running("node"):
        DATAGRID_PROCESS = subprocess.Popen(
            (
                [
                    sys.executable,
                    "-m",
                    "datagrid.cli.server",
                    "--frontend-port",
                    str(port),
                    "--backend-port",
                    str(port + 1),
                    "--open",
                    "no",
                ]
                + (["--host", host] if host is not None else [])
                + (["--debug"] if debug else [])
            )
        )
        time.sleep(2)

    return "http://%s:%s/" % (host, port)


def show(datagrid=None, host=None, port=4000, debug=False):
    """
    Start the DataGrid servers and show the DatGrid UI
    in an IFrame.
    """
    from IPython.display import IFrame

    url = launch(host, port, debug)

    if datagrid:
        query_vars = {"datagrid": datagrid}
        url = "%s?%s" % (url, urllib.parse.urlencode(query_vars))

    if _in_jupyter_environment():
        return IFrame(src=url, width="100%", height="500px")
    else:
        webbrowser.open(url, autoraise=True)


def read_dataframe(dataframe, **kwargs):
    """
    Takes a columnar pandas dataframe and returns a DataGrid.
    """
    return DataGrid.read_dataframe(dataframe, **kwargs)


def read_datagrid(filename, **kwargs):
    """
    Reads a DataGrid from a filename. Returns
    the DataGrid.
    """
    return DataGrid.read_datagrid(filename, **kwargs)


def read_json(filename, **kwargs):
    """
    Reads JSON Lines from a filename. Returns
    the DataGrid.
    """
    return DataGrid.read_json(filename, **kwargs)


def download(url):
    """
    Downloads a file, and unzips, untars, or ungzips it.
    """
    return DataGrid.download(url)


def read_csv(
    filename,
    header=0,
    sep=",",
    quotechar='"',
    heuristics=True,
    datetime_format=None,
    converters=None,
):
    """
    Takes a CSV filename and returns a DataGrid.

    Args:
        filename: the CSV file to import
        header: if True, use the first row as column headings
        sep:  used in the CSV parsing
        quotechar: used in the CSV parsing
        heuristics: if True, guess that some numbers might be dates
        datetime_format: (str) the datetime format
        converters: (dict, optional) A dictionary of functions for converting
            values in certain columns. Keys are column labels.
    """
    return DataGrid.read_csv(
        filename, header, sep, quotechar, heuristics, datetime_format, converters
    )
