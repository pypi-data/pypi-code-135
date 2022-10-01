""" test: jouissance.pt.data """

import os

if os.environ.get("PDGM_BACK", "tf") in ["pt", "cf"]:
    from jouissance.pt.data import make_data
    from jouissance.util.file import save_conditions


def test_make_data():
    """ test: make data """

    if os.environ.get("PDGM_BACK", "tf") not in ["pt", "cf"]:
        return

    save_conditions()

    tds = make_data()

    for val in tds:
        assert val[0].shape == (2, 2, 32, 64)
        assert val[1].shape == (2, 27, 32, 64)
