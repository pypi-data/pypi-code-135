""" test: jouissance.tf.runs """

import os

from jouissance.util.conf import read_conf
from jouissance.util.file import save_conditions

if os.environ.get("PDGM_BACK", "tf") in ["tf", "cf"]:
    from jouissance.tf.runs import run_it


def test_run_it():
    """ test run """
    save_conditions()

    if os.environ.get("PDGM_BACK", "tf") in ["pt", "jx"]:
        return

    con = read_conf()
    hist = run_it()
    assert len(hist.history["d_loss"]) == int(con["epochs"])
