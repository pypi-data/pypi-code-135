"""
Created on 2022-09-30.

@author: Mike K
"""
import h5py
import os
import numpy as np
import xarray as xr
# from time import time
# from datetime import datetime
import cftime
# import dateutil.parser as dparser
# import numcodecs
# import utils
from hdf5tools import utils
try:
    import hdf5plugin
    # compressor = hdf5plugin.Blosc()
    compressor = hdf5plugin.Zstd(1)
    # compressor = hdf5plugin.LZ4()
except:
    compressor = {'compression': 'lzf'}


##############################################
### Parameters



##############################################
### Functions


def create_nc_dataset(hdf, xr_dataset, var_name, chunks, compressor, unlimited_dims):
    """

    """
    shape = xr_dataset[var_name].shape
    dims = xr_dataset[var_name].dims
    maxshape = tuple([s if dims[i] not in unlimited_dims else None for i, s in enumerate(shape)])

    encoding = xr_dataset[var_name].encoding.copy()
    if 'dtype' not in encoding:
        encoding['dtype'] = xr_dataset[var_name].dtype
    attrs = xr_dataset[var_name].attrs.copy()

    enc = {k: v for k, v in encoding.items() if k in utils.encode_data.__code__.co_varnames}
    enc['dtype'] = enc['dtype'].name

    if 'calendar' in enc:
        enc['units'] = 'seconds since 1970-01-01 00:00:00'

    if 'missing_value' in enc:
        enc['_FillValue'] = enc['missing_value']
        fillvalue = enc['missing_value']
    else:
        fillvalue = None

    chunks1 = utils.guess_chunk(shape, maxshape, encoding['dtype'])
    # chunks1 = None

    if isinstance(chunks, dict):
        if var_name in chunks:
            chunks1 = chunks[var_name]

    ds = hdf.create_dataset(var_name, shape, chunks=chunks1, maxshape=maxshape, dtype=encoding['dtype'], fillvalue=fillvalue, **compressor)

    # if (chunks1 is None):
    #     old_chunks = ds.chunks
    #     _ = hdf.pop(var_name)
    #     new_chunks = tuple([int(c*dim_chunk_mupliplier) if int(c*dim_chunk_mupliplier) <= shape[i] else shape[i] for i, c in enumerate(old_chunks)])
    #     ds = hdf.create_dataset(var_name, shape, chunks=new_chunks, maxshape=maxshape, dtype=encoding['dtype'], **compressor)

    if ('scale_factor' in enc) or ('add_offset' in enc) or ('calendar' in enc):
        if ds.chunks == shape:
            ds[:] = utils.encode_data(xr_dataset[var_name].copy().load().values, **enc)
        else:
            new_slices, source_slices = utils.copy_chunks(shape, chunks1)

            for new_slice, source_slice in zip(new_slices, source_slices):
                # print(new_slice, source_slice)
                ds[new_slice] = utils.encode_data(xr_dataset[var_name][source_slice].copy().load().values, **enc)

            # for chunk in ds.iter_chunks():
                # print(chunk)

                # data = xr_dataset[var_name][chunk].copy().load().values
                # data_bool = ~np.isnan(data)

                # if np.any(data_bool):
                #     slice_arrays = [(s.min(), s.max() + 1) for s in np.where(data_bool)]
                #     slices = tuple([slice(chunk[i].start + s[0], chunk[i].start + s[1]) for i, s in enumerate(slice_arrays)])
                #     source_slices = tuple([slice(s[0], s[1]) for s in slice_arrays])
                #     ds[slices] = encode_data(data[source_slices], **enc)

                # ds[chunk] = encode_data(xr_dataset[var_name][chunk].copy().load().values, **enc)
    else:
        if ds.chunks == shape:
            ds[:] = xr_dataset[var_name].copy().load().values
        else:
            new_slices, source_slices = utils.copy_chunks(shape, chunks1)

            for new_slice, source_slice in zip(new_slices, source_slices):
                # print(new_slice, source_slice)
                ds[new_slice] = xr_dataset[var_name][source_slice].copy().load().values

            # for chunk in ds.iter_chunks():
                # print(chunk)
                # data = xr_dataset[var_name][chunk].copy().load().values
                # data_bool = ~np.isnan(data)
                # if np.any(data_bool):
                #     slice_arrays = [(s.min(), s.max() + 1) for s in np.where(data_bool)]
                #     slices = tuple([slice(chunk[i].start + s[0], chunk[i].start + s[1]) for i, s in enumerate(slice_arrays)])
                #     source_slices = tuple([slice(s[0], s[1]) for s in slice_arrays])
                #     ds[slices] = encode_data(data[source_slices], **enc)
                # ds[chunk] = xr_dataset[var_name][chunk].copy().load().values

    # elif 'float' in enc['dtype']:
    #     enc['_FillValue'] = np.array([np.nan], dtype='float32')

    _ = enc.pop('dtype')
    # print(enc)
    attrs.update(enc)

    ds.attrs.update(attrs)

    if var_name in xr_dataset.dims:
        # p = list(xr_dataset.dims).index(var_name)
        # ds_attrs = {'_Netcdf4Coordinates': np.array([p], dtype='int16'), '_Netcdf4Dimid': p}
        # ds_attrs = {'_Netcdf4Dimid': p}

        # ds.attrs.update(ds_attrs)

        ds.make_scale(var_name)
    # else:
    #     ds_dims = list(xr_dataset.dims)

    #     ds_attrs = {'_Netcdf4Coordinates': np.array([ds_dims.index(dim) for dim in dims], dtype='int16'), '_Netcdf4Dimid': 2}

    #     ds.attrs.update(ds_attrs)

    ds_dims = ds.dims
    for i, dim in enumerate(dims):
        if dim != var_name:
            ds_dims[i].attach_scale(hdf[dim])
            ds_dims[i].label = dim

    return ds


def xr_to_hdf5(xr_dataset, new_path, group=None, chunks=None, unlimited_dims=None):
    """
    
    Parameters
    ----------
    xr_dataset : xr.Dataset
        Xarray Dataset.
    new_path : str or pathlib
        Output path.
    group : str or None
        The group or group path within the hdf5 file to the datasets.
    chunks : dict of tuples
        The chunks per dataset. Must be a dictionary of dataset name keys with tuple values of appropriate dimensions. A value of None will perform auto-chunking.
    unlimited_dims : str, list of str, or None
        The dimensions that should be assigned as "unlimited".

    """
    if isinstance(unlimited_dims, str):
        unlimited_dims = [unlimited_dims]
    else:
        unlimited_dims = []

    xr_dims_list = list(xr_dataset.dims)

    with h5py.File(new_path, 'w', libver='latest', rdcc_nbytes=3*1024*1024) as f:

        if isinstance(group, str):
            g = f.create_group(group)
        else:
            g = f
    
        ## Create coords
        for coord in xr_dims_list:
            _ = create_nc_dataset(g, xr_dataset, coord, chunks, compressor, unlimited_dims)
    
        ## Create data vars
        for var in list(xr_dataset.data_vars):
            _ = create_nc_dataset(g, xr_dataset, var, chunks, compressor, unlimited_dims)
    
        ## Dataset attrs
        # attrs = {'_NCProperties': b'version=2,h5netcdf=1.0.2,hdf5=1.12.2,h5py=3.7.0'}
        attrs = {}
        attrs.update(xr_dataset.attrs)
        g.attrs.update(attrs)


def combine_hdf5(paths, new_path, group=None, chunks=None, unlimited_dims=None):
    """
    Function to combine hdf5 files with flattened datasets within a single group.

    Parameters
    ----------
    paths : list of str
        The list of input hdf5 paths to combine.
    new_path : str
        The output path of the new combined hdf5 fie.
    group : str or None
        The group or group path within the hdf5 file to the datasets.
    chunks : dict of tuples
        The chunks per dataset. Must be a dictionary of dataset name keys with tuple values of appropriate dimensions. A value of None will perform auto-chunking.
    unlimited_dims : str, list of str, or None
        The dimensions that should be assigned as "unlimited".

    Returns
    -------
    None
    """
    if isinstance(unlimited_dims, str):
        unlimited_dims = [unlimited_dims]
    else:
        unlimited_dims = []

    ## Create new file
    with h5py.File(new_path, 'w', libver='latest', rdcc_nbytes=3*1024*1024) as nf:

        if isinstance(group, str):
            nf1 = nf.create_group(group)
        else:
            nf1 = nf
    
        ## Get the extended coords
        coords_dict = utils.extend_coords(paths, group)
    
        ## Add the coords as datasets
        for coord, arr in coords_dict.items():
            shape = arr.shape

            maxshape = tuple([s if s not in unlimited_dims else None for s in shape])

            chunks1 = utils.guess_chunk(shape, maxshape, arr.dtype)
    
            if isinstance(chunks, dict):
                if coord in chunks:
                    chunks1 = chunks[coord]

            ds = nf1.create_dataset(coord, shape, chunks=chunks1, maxshape=maxshape, dtype=arr.dtype, **compressor)
    
            # old_chunks = ds.chunks
    
            # if (old_chunks != shape) and (chunks1 is None):
            #     _ = nf1.pop(coord)
            #     new_chunks = tuple([int(c*dim_chunk_mupliplier) if int(c*dim_chunk_mupliplier) <= shape[i] else shape[i] for i, c in enumerate(old_chunks)])
            #     ds = nf1.create_dataset(coord, shape, chunks=new_chunks, maxshape=maxshape, dtype=arr.dtype, **compressor)
    
            ds[:] = arr
    
            ds.make_scale(coord)
    
            # p = list(ds.dims).index(coord)
            # ds_attrs = {'_Netcdf4Coordinates': np.array([p], dtype='int16'), '_Netcdf4Dimid': p}
            # ds.attrs.update(ds_attrs)
    
        ## Add the variables as datasets
        vars_dict = utils.extend_variables(paths, coords_dict, group)
    
        for dim_name in vars_dict:
            shape = vars_dict[dim_name]['shape']
            dims = vars_dict[dim_name]['dims']
            maxshape = tuple([s if dims[i] not in unlimited_dims else None for i, s in enumerate(shape)])
    
            chunks1 = utils.guess_chunk(shape, maxshape, vars_dict[dim_name]['dtype'])
    
            if isinstance(chunks, dict):
                if dim_name in chunks:
                    chunks1 = chunks[dim_name]
    
            ds = nf1.create_dataset(dim_name, shape, chunks=chunks1, maxshape=maxshape, dtype=vars_dict[dim_name]['dtype'], fillvalue=vars_dict[dim_name]['fillvalue'], **compressor)
    
            # old_chunks = ds.chunks
    
            # if (old_chunks != shape) and (chunks1 is None):
            #     _ = nf1.pop(dim_name)
            #     new_chunks = tuple([int(c*dim_chunk_mupliplier) if int(c*dim_chunk_mupliplier) <= shape[i] else shape[i] for i, c in enumerate(old_chunks)])
            #     ds = nf1.create_dataset(dim_name, shape, chunks=new_chunks, maxshape=maxshape, dtype=vars_dict[dim_name]['dtype'], **compressor)
    
            ds_dims = ds.dims
            for i, dim in enumerate(dims):
                ds_dims[i].attach_scale(nf1[dim])
                ds_dims[i].label = dim
    
            # ds_dims = list(ds.dims)
    
            # ds_attrs = {'_Netcdf4Coordinates': np.array([ds_dims.index(dim) for dim in dims], dtype='int16')}
    
            # ds.attrs.update(ds_attrs)
    
            # Load the data by chunk
            for path in vars_dict[dim_name]['data']:
                f = h5py.File(path, 'r')
    
                if isinstance(group, str):
                    f1 = f[group]
                else:
                    f1 = f
    
                ds_old = f1[dim_name]
    
                source_slice_index = vars_dict[dim_name]['data'][path]['slice_index']
                dims_order = vars_dict[dim_name]['data'][path]['dims_order']
    
                source_dim_index = [dims_order.index(dim) for dim in dims]

                new_slices, source_slices = utils.copy_chunks(shape, chunks1, source_slice_index, source_dim_index)

                for new_slice, source_slice in zip(new_slices, source_slices):
                    # print(new_slice, source_slice)
                    ds[new_slice] = ds_old[source_slice]

                # for chunk in ds.iter_chunks(slice_index):
                #     # print(chunk)
                #     source_chunk = tuple([slice(chunk[i].start - slice_index[i].start, chunk[i].stop - slice_index[i].start) for i in dims_index])
                #     ds[chunk] = ds_old[source_chunk]
    
                f.close()
    
        ## Assign attrs
        global_attrs = {}
        for path in paths:
            f = h5py.File(path, 'r')
    
            if isinstance(group, str):
                f1 = f[group]
            else:
                f1 = f
    
            ds_list = list(f1.keys())
    
            for ds_name in ds_list:
                attrs = {k: v for k, v in f1[ds_name].attrs.items() if k not in ['DIMENSION_LABELS', 'DIMENSION_LIST', 'CLASS', 'NAME', '_Netcdf4Coordinates', '_Netcdf4Dimid', 'REFERENCE_LIST']}
                # print(attrs)
                nf1[ds_name].attrs.update(attrs)

            global_attrs.update(dict(f1.attrs))

        nf1.attrs.update(global_attrs)


def open_dataset(path, **kwargs):
    """
    The Xarray open_dataset function, but specifically with the h5netcdf engine to open hdf5 files.
    """
    ds = xr.open_dataset(path, engine='h5netcdf', **kwargs)

    return ds


def load_dataset(path, **kwargs):
    """
    The Xarray load_dataset function, but specifically with the h5netcdf engine to open hdf5 files.
    """
    ds = xr.load_dataset(path, engine='h5netcdf', **kwargs)

    return ds

























######################################
### Testing
