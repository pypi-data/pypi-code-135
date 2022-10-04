""" test: jouissance.tf.data """

import os

from jouissance.util import read_conf, edit_conf, save_conditions

if os.environ.get("PDGM_BACK", "tf") in ["tf", "cf", "jx"]:
    from jouissance.tf import MyData, make_data


def test_my_data():
    """ test: MyData class """
    if os.environ.get("PDGM_BACK", "tf") == "pt":
        return
    _path = "gcp-public-data-goes-17/ABI-L2-CMIPC/" + \
        "2020/001/00/OR_ABI-L2-CMIPC-M6C01_G17_" + \
        "s20200010046212_e20200010048585_c20200010049042.nc"
    # pylint: disable=abstract-class-instantiated
    assert MyData(_path).element_spec[0].shape == (1500, 2500, 2)
    assert MyData(_path).element_spec[1].shape == (73, 144, 27)
    con = read_conf()
    new_con = con.copy()
    new_con["reanalysis_presave"] = True
    _fn_con = edit_conf(new_con)
    os.environ["PDGM_CONFIGS_PATH"] = _fn_con
    assert MyData(_path).element_spec[0].shape == (1500, 2500, 2)
    assert MyData(_path).element_spec[1].shape == (73, 144, 27)
    new_con["reanalysis_presave"] = False
    _fn_con = edit_conf(new_con)
    os.environ["PDGM_CONFIGS_PATH"] = _fn_con


def test_make_data():
    """ test: make_data function """
    if os.environ.get("PDGM_BACK", "tf") == "pt":
        return
    assert make_data()[0].element_spec[0].shape == (2, 32, 64, 2)
    assert make_data()[0].element_spec[1].shape == (2, 32, 64, 27)
    con = read_conf()
    new_con = con.copy()
    new_con["reanalysis_presave"] = True
    _fn_con = edit_conf(new_con)
    os.environ["PDGM_CONFIGS_PATH"] = _fn_con
    assert make_data()[0].element_spec[0].shape == (2, 32, 64, 2)
    assert make_data()[0].element_spec[1].shape == (2, 32, 64, 27)
    new_con["reanalysis_presave"] = False
    _fn_con = edit_conf(new_con)
    os.environ["PDGM_CONFIGS_PATH"] = _fn_con


def test_make_data_loop():
    """ test: make_data function with loops """
    if os.environ.get("PDGM_BACK", "tf") == "pt":
        return
    save_conditions()
    tds, _ = make_data()
    for idx, jdx in tds:
        assert idx.shape == (2, 32, 64, 2)
        assert jdx.shape == (2, 32, 64, 27)
        break

    con = read_conf()
    new_con = con.copy()
    new_con["reanalysis_presave"] = True
    _fn_con = edit_conf(new_con)
    os.environ["PDGM_CONFIGS_PATH"] = _fn_con

    tds2, _ = make_data()
    for idx, jdx in tds2:
        assert idx.shape == (2, 32, 64, 2)
        assert jdx.shape == (2, 32, 64, 27)
        break

    new_con["reanalysis_presave"] = False
    _fn_con = edit_conf(new_con)
    os.environ["PDGM_CONFIGS_PATH"] = _fn_con
