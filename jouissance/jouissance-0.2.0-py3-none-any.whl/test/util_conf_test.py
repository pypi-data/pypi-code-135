""" test: jouissance.util.conf """

import pytest

from jouissance.util.conf import read_conf, make_hash, edit_conf


def test_read_conf():
    """ test: read the yaml configs """

    assert read_conf()["default"]

    with pytest.raises(FileNotFoundError):
        read_conf(conf_path="/tmp/some_configs.yaml")


def test_make_hash():
    """ test: make a hash from the dict for caching """
    assert make_hash("test") != "something"


def test_edit_conf():
    """ test: edit the configs and export them """
    con = read_conf()
    fn_con = edit_conf(con)
    assert con == read_conf(fn_con)
    new_con = con.copy()
    new_con["something_new"] = "hello"
    fn_new_con = edit_conf(new_con)
    assert read_conf(fn_new_con)["something_new"] == "hello"
