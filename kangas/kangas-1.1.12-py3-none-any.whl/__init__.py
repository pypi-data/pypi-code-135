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
from .utils import _in_colab_environment, _in_jupyter_environment, get_localhost

DATAGRID_PROCESS = None


def _is_running(name, command):
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)
        except Exception:
            continue
        if process.name().startswith(name) and command in process.cmdline():
            return process.is_running() and process.status() != psutil.STATUS_ZOMBIE
    return False


def _process_method(name, command, method):
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)
        except Exception:
            continue
        if process.name().startswith(name) and command in process.cmdline():
            getattr(process, method)()


def terminate():
    """
    Terminate the DataGrid servers.
    """
    global DATAGRID_PROCESS
    _process_method("node", "datagrid", "terminate")
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

    if not _is_running("node", "datagrid"):
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


def show(
    datagrid=None, host=None, port=4000, debug=False, height="750px", width="100%"
):
    """
    Start the DataGrid servers and show the DatGrid UI
    in an IFrame or browser.
    """
    from IPython.display import IFrame, Javascript, display

    url = launch(host, port, debug)

    if datagrid:
        query_vars = {"datagrid": datagrid}
        qvs = urllib.parse.urlencode(query_vars)
        url = "%s?%s" % (url, qvs)
    else:
        qvs = ""

    if _in_colab_environment():
        display(
            Javascript(
                """
(async ()=>{
    fm = document.createElement('iframe');
    fm.src = (await google.colab.kernel.proxyPort(%s));
    fm.width = '%s';
    fm.height = '%s';
    fm.frameBorder = 0;
    document.body.append(fm);
})();
"""
                % (port, width, height)
            )
        )

    elif _in_jupyter_environment():
        display(IFrame(src=url, width=width, height=height))

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


def download(url, ext=None):
    """
    Downloads a file, and unzips, untars, or ungzips it.
    """
    return DataGrid.download(url, ext)


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
