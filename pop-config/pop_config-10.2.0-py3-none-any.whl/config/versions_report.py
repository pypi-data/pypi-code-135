import locale
import os
import platform
import subprocess
import sys

try:
    from pip._internal.operations.freeze import freeze

    HAS_PIP = True
except ImportError:
    HAS_PIP = False


def run(hub, opts: dict, primary: str):
    """
    Output a config file based on the current command
    :param hub:
    :param opts: The parsed config from os vars, cli options, and config file
    :param primary: The plugin with the authoritative cli

    Returns:
        argv: The exact command ran from the cli
        config: Everything on hub.OPT (which comes from relevant os vars, cli options, and config options)
        freeze: The output of pip freeze
        name: The name of the project with the authoritative cli
        version: The version of the project with the authoritative cli
        python: The python version
        logs: The contents of the most recent log file
    """
    hub.pop.sub.add(dyne_name="rend")
    outputter = opts.get("rend", {}).get("output") or "yaml"

    if HAS_PIP:
        # Get the freeze information from pip internals
        pip_freeze = [line for line in freeze()]
    else:
        # Shell out to pip
        ret = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
        pip_freeze = ret.decode("utf-8").strip().split("\n")

    log_file = opts.get("pop_config", {}).get("log_file")
    if log_file and os.path.exists(log_file):
        with open(log_file) as fh:
            contents = fh.readlines()
            logs = [c.strip() for c in contents]
    else:
        logs = []

    output = {
        "name": primary,
        "version": hub.config.version.get(primary),
        "argv": " ".join(a for a in sys.argv if a != "--versions-report"),
        "config": hub.config.template.get(opts),
        "python": sys.version,
        "freeze": pip_freeze,
        "locale": locale.getlocale(),
        "platform": {
            "os": os.name,
            "machine": platform.machine(),
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
        },
        "logs": logs,
    }

    out = hub.output[outputter].display(output)

    print(out)
    sys.exit(0)
