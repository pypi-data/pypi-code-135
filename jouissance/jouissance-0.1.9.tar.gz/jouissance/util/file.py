""" jouissance.util.file """

import os
import glob
import urllib
import urllib.request
import itertools

import cftime
import fsspec
import netCDF4
import h5py
import numpy as np

from jouissance.util.conf import read_conf


def fsspec_fs(provider=None, con=None):
    """ get the fsspec filesystem """

    con = read_conf() if con is None else con
    provider = con["provider"] if provider is None else provider

    if provider == "abfs":
        return fsspec.filesystem(
            provider, account_name=con["abfs_account_name"])

    if con["provider"] == "file":
        return fsspec.filesystem(
            provider)

    return fsspec.filesystem(
        provider, token="anon", anon=True)


def make_name(_pr=None, _dn=None, con=None):
    """ get the provider from the path """

    con = read_conf() if con is None else con
    _pr = con["provider"] if _pr is None else _pr
    _dn = "goes-17" if _dn is None else _dn

    if _pr.lower() not in ["gs", "gcs", "s3", "abfs", "file"]:
        raise ValueError(f"{_pr} must be gs, s3, abfs, or file")

    if _pr.lower() == "file":
        return con["data_folder"]

    if not _dn.lower().startswith("goes"):
        raise ValueError("only goes-?? data is supported")

    return f"gcp-public-data-{_dn.lower()}" if _pr.lower().startswith("g") \
        else "noaa-" + _dn.lower().replace("-", "")


def parse_days(_dys):
    """ return a list of applicable days """

    _dys = _dys*3 if len(_dys) < 3 else _dys
    pos0, pos1, pos2 = _dys[0], _dys[1], _dys[2]
    perms = list(itertools.product('0123456789', repeat=3))
    return [
        f"{perm[0]}{perm[1]}{perm[2]}"
        for perm in perms if
        (perm[0] == str(pos0) or pos0 in ["?", "*"]) and
        (perm[1] == str(pos1) or pos1 in ["?", "*"]) and
        (perm[2] == str(pos2) or pos2 in ["?", "*"]) and
        int(f"{perm[0]}{perm[1]}{perm[2]}") > 0 and
        int(f"{perm[0]}{perm[1]}{perm[2]}") < 366
    ]


def make_glob(_fs=None, _dn=None, con=None):
    """ make a glob """

    con = read_conf() if con is None else con
    _dn = make_name(con=con) if _dn is None else _dn
    _fs = fsspec_fs(con=con) if _fs is None else _fs
    _fs = _fs if con["force_glob_provider"] is False else glob

    _px = con["products"][0]
    _gb = []

    if len(con["days"]) < 3 or "?" in con["days"] or "*" in con["days"]:
        _dys = parse_days(con["days"][0])
    else:
        _dys = con["days"]
    for _yr in con["years"]:
        for _hr in con["hours"]:
            for _dy in _dys:
                _gb += _fs.glob(
                    f"{_dn}/*{_px}*{_yr}{_dy}{_hr}*.nc"
                ) if con["provider"] == "file" else _fs.glob(
                    f"{_dn}/{_px}/{_yr}/{_dy}/{_hr}/*.nc"
                )

    return _gb


def get_scenes_conditions_netcdf4(file, bck="tf", con=None):
    """ return the scenes and conditions """
    # pylint: disable=no-member

    con = read_conf() if con is None else con

    file = file if isinstance(file, str) else file.decode("utf-8")

    scenes, conditions = [], []

    if file[:len(con["scene_folder"])] != con["scene_folder"]:
        _ncs = netCDF4.Dataset(f"{con['scene_folder']}/{file}")
    else:
        _ncs = netCDF4.Dataset(f"{file}")
    scenes.extend(
        np.expand_dims(_ncs[f"CMI_C{_ch}"][:].data, axis=-1)
        for _ch in con["channels"]
    )

    _nctime = _ncs["t"][:].data.copy()
    _ncunit = _ncs["t"].units
    time = cftime.num2date(_nctime, _ncunit)
    _ci = (time.dayofyr - 1)*4 + (time.hour//6)
    _ncs.close()

    for _pd in con["reanalysis_products"]:
        _ncc = netCDF4.Dataset(
            f"{con['cond_folder']}/{_pd}.{time.year}.nc"
        )
        conditions.append(
            _ncc[_pd][_ci, con["reanalysis_levels"], :, :].data.copy())
        _ncc.close()

    if bck == "pt":
        return (
            np.moveaxis(np.concatenate(scenes, axis=-1), -1, 0),
            np.concatenate(conditions)
        )

    return (
        np.concatenate(scenes, axis=-1),
        np.moveaxis(np.concatenate(conditions), 0, -1)
    )


def get_scenes_conditions_h5py(file, bck="tf", con=None):
    """ return the scenes and conditions """
    # pylint: disable=no-member

    con = read_conf() if con is None else con
    _fs = fsspec_fs()

    file = file if isinstance(file, str) else file.decode("utf-8")

    scenes, conditions = [], []

    _ncs = h5py.File(_fs.open(file, "rb"), "r")

    scenes.extend(
        np.expand_dims(
            _ncs[f"CMI_C{_ch}"][:] *
            _ncs[f"CMI_C{_ch}"].attrs["scale_factor"] +
            _ncs[f"CMI_C{_ch}"].attrs["add_offset"],
            axis=-1
        ) for _ch in con["channels"]
    )

    _nctime = _ncs["t"][()]
    _ncunit = _ncs["t"].attrs["units"].decode("utf-8")
    time = cftime.num2date(_nctime, _ncunit)
    _ci = (time.dayofyr - 1)*4 + (time.hour//6)
    _ncs.close()

    for _pd in con["reanalysis_products"]:
        _ncc = h5py.File(
            f"{con['cond_folder']}/{_pd}.{time.year}.nc"
        )
        conditions.append(
            _ncc[_pd][_ci, con["reanalysis_levels"], :, :].copy())
        _ncc.close()

    if bck == "pt":
        return (
            np.moveaxis(np.concatenate(scenes, axis=-1), -1, 0),
            np.concatenate(conditions)
        )

    return (
        np.concatenate(scenes, axis=-1),
        np.moveaxis(np.concatenate(conditions), 0, -1)
    )


def save_conditions(con=None):
    """ save the conditions """

    con = read_conf() if con is None else con
    _pxs = con["reanalysis_products"]
    _yrs = con["years"]
    _vr = con["reanalysis_version"]
    _fol = con["cond_folder"]
    version = "" if _vr == "1" else f"{_vr}"
    _fns = [f"{_px}.{_yr}.nc" for _px in _pxs for _yr in _yrs]
    base_url = "https://downloads.psl.noaa.gov/Datasets/ncep.reanalysis"
    for _fn in _fns:
        if not os.path.exists(f"{_fol}/{_fn}"):
            os.makedirs(_fol, exist_ok=True)
            urllib.request.urlretrieve(
                f"{base_url}{version}/pressure/{_fn}",
                f"{_fol}/{_fn}")


def save_scenes(_glb=None, _fs=None, con=None):
    """ save scenes via glob """

    con = read_conf() if con is None else con
    _fs = fsspec_fs(con=con) if _fs is None else _fs
    _glb = make_glob(_fs, con=con) if _glb is None else _glb

    _fol = con["scene_folder"]

    for _fn in _glb:
        _fnx = _fn.split("/")[-1]
        if not os.path.exists(f"{_fol}/{_fnx}"):
            os.makedirs(_fol, exist_ok=True)
            _fs.get(_fn, f"{_fol}/{_fnx}")
