""" test: jouissance.util.file """

from jouissance.util.conf import read_conf
from jouissance.util.file import fsspec_fs, make_name, parse_days, make_glob
from jouissance.util.file import get_scenes_conditions_h5py, save_conditions
from jouissance.util.file import save_scenes, get_scenes_conditions_netcdf4


def test_fsspec_fs():
    """ test: get the fsspec filesystem """

    assert fsspec_fs(provider="gs").protocol[0] in ["gs", "gcs"]
    assert fsspec_fs(provider="s3").protocol[0] == "s3"
    assert fsspec_fs(provider="abfs").protocol == "abfs"
    assert fsspec_fs(provider="file").protocol == "file"


def test_make_name():
    """ test: get the provider from the path """

    assert make_name("gs", "goes-17") == "gcp-public-data-goes-17"
    assert make_name("gcs", "goes-17") == "gcp-public-data-goes-17"
    assert make_name("s3", "goes-17") == "noaa-goes17"
    assert make_name("abfs", "goes-17") == "noaa-goes17"
    assert make_name("abfs", "GOES-17") == "noaa-goes17"


def test_parse_days():
    """ test: return a list of applicable days """

    assert parse_days("111") == ["111"]
    assert parse_days("11*")[0] == "110"
    assert parse_days("11?")[-1] == "119"
    assert len(parse_days("11*")) == 10
    assert len(parse_days("***")) == 365


def test_make_glob():
    """ test: make a pattern for glob and return glob """

    _az = fsspec_fs(provider="abfs")
    _gs = fsspec_fs(provider="gs")
    _s3 = fsspec_fs(provider="s3")
    azdn = "noaa-goes17"
    gsdn = "gcp-public-data-goes-17"
    s3dn = "noaa-goes17"

    assert len(make_glob(_az, azdn)) == 12
    assert len(make_glob(_gs, gsdn)) == 12
    assert len(make_glob(_s3, s3dn)) == 12


def test_get_scenes_conditions_h5py():
    """ test h5py/netcdf4 scenes/conditions """

    save_conditions()
    con = read_conf()
    _fs = fsspec_fs(con=con)
    _dn = make_name("gs", "goes-17", con=con)
    _gb = make_glob(_fs, _dn, con=con)

    for _tool in ["h5py", "netcdf4"]:

        if _tool == "netcdf4":
            save_scenes(_gb, _fs, con=con)
            _goal = _gb[0].split("/")[-1]
            get_scenes_conditions = get_scenes_conditions_netcdf4
        else:
            _goal = _gb[0]
            get_scenes_conditions = get_scenes_conditions_h5py

        scenes, conditions = get_scenes_conditions(_goal)

        assert scenes.shape == (
            int(con["scene_shape1"]),
            int(con["scene_shape2"]),
            len(con["channels"])
        )

        assert conditions.shape == (
            int(con["reanalysis_shape1"]),
            int(con["reanalysis_shape2"]),
            len(con["reanalysis_levels"]) * len(con["reanalysis_products"])
        )
