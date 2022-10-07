""" jouissance.util.conf: configs utils """

import hashlib
import json
import os

import yaml


def read_conf(conf_path=None):
    """ read the yaml configs """

    if conf_path is not None:
        return yaml.safe_load(open(conf_path, "r", encoding="utf8"))

    if os.environ.get("PDGM_CONFIGS_PATH") is not None:
        conf_path = os.environ.get("PDGM_CONFIGS_PATH")
        return yaml.safe_load(open(conf_path, "r", encoding="utf8"))

    con_dir = os.environ.get("PDGM_CONFIGS_DIR", os.getcwd())

    configs_path = f"{con_dir}/configs.yaml" if \
        os.path.exists(f"{con_dir}/configs.yaml") else \
        f"{os.path.dirname(__file__)}/_configs.yaml"

    return yaml.safe_load(open(configs_path, "r", encoding="utf8"))


def make_hash(con=None):
    """ make a hash from the dict for caching """

    _hash = hashlib.md5()
    dumped = json.dumps(con, sort_keys=True).encode()
    _hash.update(dumped)

    return f".cache{_hash.hexdigest()}"


def edit_conf(con):
    """ edit the configs and export them """

    filename = make_hash(con)

    with open(f"{filename}.yaml", "w", encoding="utf8") as _fo:
        yaml.dump(con, _fo)

    return f"{filename}.yaml"
