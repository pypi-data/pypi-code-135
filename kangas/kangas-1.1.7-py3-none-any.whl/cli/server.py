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

import argparse
import os
import subprocess
import sys
import urllib
import webbrowser

import datagrid.server
from datagrid import get_localhost

ADDITIONAL_ARGS = False
HERE = os.path.abspath(os.path.dirname(__file__))


def get_parser_arguments(parser):
    parser.add_argument(
        "DATAGRID",
        help="Open a particular DataGrid; optional, you can select which DataGrid to use in UI",
        type=str,
        nargs="?",
        default=None,
    )
    parser.add_argument(
        "-r",
        "--root",
        help="The directory from which to server datagrid files; also can use DATAGRID_ROOT env variable",
        type=str,
        default=None,
    )
    parser.add_argument(
        "-b",
        "--backend",
        help="The backend to use; use 'no' for no backend",
        type=str,
        default="tornado",
    )
    parser.add_argument(
        "-bp",
        "--backend-port",
        help="The backend port to use; default is frontend port + 1",
        type=int,
        default=None,
    )
    parser.add_argument(
        "-f",
        "--frontend",
        help="The frontend to use; use 'no' for no frontend",
        type=str,
        default="next",
    )
    parser.add_argument(
        "-fp",
        "--frontend-port",
        help="The frontend port to use",
        type=int,
        default=4000,
    )
    parser.add_argument(
        "-o",
        "--open",
        help="How to open page in a webbrowser; 'tab', 'window', or 'no'",
        type=str,
        default="tab",
    )
    parser.add_argument(
        "--host",
        help="The name or IP the servers will listen on",
        type=str,
        default=None,
    )
    parser.add_argument(
        "--debug",
        help="Use this flag to display output from servers",
        default=False,
        action="store_true",
    )


def server(parsed_args, remaining=None):
    # Called via `datagrid server ...`
    try:
        import nodejs
    except Exception:
        nodejs = None

    DATAGRID_FRONTEND_PORT = parsed_args.frontend_port
    DATAGRID_HOST = (
        parsed_args.host if parsed_args.host is not None else get_localhost()
    )
    if parsed_args.backend_port is None:
        DATAGRID_BACKEND_PORT = parsed_args.frontend_port + 1
    else:
        DATAGRID_BACKEND_PORT = parsed_args.backend_port

    print(
        "Serving DataGrids from directory: %r"
        % (parsed_args.root or datagrid.server.DATAGRID_ROOT)
    )

    if parsed_args.frontend != "no":
        NODE_SERVER_PATH = os.path.join(HERE, "../frontend/standalone/server.js")
        print(
            "DataGrid frontend is now running on http:/%s:%s/..."
            % (DATAGRID_HOST, DATAGRID_FRONTEND_PORT)
        )
        # node uses PORT to listen on; this is a local process
        # so shouldn't effect any other node servers

        env = os.environ.copy()
        env.update(
            {
                "NODE_ENV": "production",
                "PORT": str(DATAGRID_FRONTEND_PORT),
                "DATAGRID_BACKEND_PORT": str(DATAGRID_BACKEND_PORT),
                "DATAGRID_HOST": str(DATAGRID_HOST),
            }
        )

        # first, check to see if nodejs is good:
        result = (
            nodejs.node.call(
                ["--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            if nodejs is not None
            else 1
        )

        if result == 0:  # Good! We'll use the pip-installed nodejs
            if not parsed_args.debug:
                node_process = nodejs.node.Popen(
                    [NODE_SERVER_PATH],
                    env=env,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            else:
                node_process = nodejs.node.Popen([NODE_SERVER_PATH], env=env)
        else:  # Nope, we'll look for node in the path
            executable = "node.exe" if sys.platform == "win32" else "node"
            result = subprocess.call([executable, "--version"])

            if result == 1:
                raise Exception("Unable to find node executable")

            if not parsed_args.debug:
                node_process = subprocess.Popen(
                    [executable, NODE_SERVER_PATH],
                    env=env,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            else:
                node_process = subprocess.Popen([executable, NODE_SERVER_PATH], env=env)

    if parsed_args.open != "no":
        new = {"tab": 0, "window": 1}[parsed_args.open]
        host = "http://%s:%s/" % (DATAGRID_HOST, DATAGRID_FRONTEND_PORT)
        query_vars = {}
        if parsed_args.DATAGRID is not None:
            query_vars["datagrid"] = parsed_args.DATAGRID
        if query_vars:
            url = "%s?%s" % (host, urllib.parse.urlencode(query_vars))
        else:
            url = host
        webbrowser.open(url, new=new, autoraise=True)

    if parsed_args.backend != "no":
        print(
            "DataGrid backend is now running on http://%s:%s/..."
            % (DATAGRID_HOST, DATAGRID_BACKEND_PORT)
        )
        datagrid.server.start_tornado_server(
            port=DATAGRID_BACKEND_PORT, debug=parsed_args.debug
        )
        print("Stopping backend...")
        if parsed_args.frontend != "no":
            print("Stopping frontend...")
            node_process.terminate()
    elif parsed_args.frontend != "no":
        node_process.wait()


def main(args):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    get_parser_arguments(parser)
    parsed_args = parser.parse_args(args)

    server(parsed_args)


if __name__ == "__main__":
    # Called via `python -m datagrid.cli.server ...`
    # Called via `datagrid server ...`
    main(sys.argv[1:])
