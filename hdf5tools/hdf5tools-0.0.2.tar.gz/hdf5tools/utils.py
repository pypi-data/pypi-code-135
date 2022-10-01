#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:52:08 2022

@author: mike
"""
import h5py
import os
import numpy as np
# import xarray as xr
# from time import time
# from datetime import datetime
import cftime
# import dateutil.parser as dparser
# import numcodecs



########################################################
### Parmeters


CHUNK_BASE = 32*1024    # Multiplier by which chunks are adjusted
CHUNK_MIN = 32*1024      # Soft lower limit (32k)
CHUNK_MAX = 3*1024*1024   # Hard upper limit (4M)

time_str_conversion = {'days': 'datetime64[D]',
                       'hours': 'datetime64[h]',
                       'minutes': 'datetime64[m]',
                       'seconds': 'datetime64[s]',
                       'milliseconds': 'datetime64[ms]'}

#########################################################
### Functions


def encode_datetime(data, units=None, calendar='gregorian'):
    """

    """
    if units is None:
        output = data.astype('datetime64[s]').astype(int)
    else:
        if '1970-01-01' in units:
            time_unit = units.split()[0]
            output = data.astype(time_str_conversion[time_unit]).astype(int)
        else:
            output = cftime.date2num(data.astype('datetime64[s]').tolist(), units, calendar)

    return output


def decode_datetime(data, units=None, calendar='gregorian'):
    """

    """
    if units is None:
        output = data.astype('datetime64[s]')
    else:
        if '1970-01-01' in units:
            time_unit = units.split()[0]
            output = data.astype(time_str_conversion[time_unit])
        else:
            output = cftime.num2pydate(data, units, calendar).astype('datetime64[s]')

    return output


def encode_data(data, dtype, missing_value=None, add_offset=0, scale_factor=1, units=None, calendar=None, **kwargs):
    """

    """
    if 'datetime64' in data.dtype.name:
        if (calendar is None):
            raise TypeError('data is datetime, so calendar must be assigned.')
        output = encode_datetime(data, units, calendar)
    else:
        output = (data - add_offset)/scale_factor

        if isinstance(missing_value, (int, np.number)):
            output[np.isnan(output)] = missing_value

        output = output.astype(dtype)

    return output


def decode_data(data, dtype=None, missing_value=None, add_offset=0, scale_factor=1, units=None, calendar=None, **kwargs):
    """

    """
    if isinstance(calendar, str):
        output = decode_datetime(data, units, calendar)
    else:
        output = data.astype(dtype)

        if isinstance(missing_value, (int, np.number)):
            output[output == missing_value] = np.nan

        output = (output * scale_factor) + add_offset

    return output


def is_scale(dataset):
    """

    """
    check = h5py.h5ds.is_scale(dataset._id)

    return check


def extend_coords(paths, group=None):
    """

    """
    coords_dict = {}

    for path in paths:
        f = h5py.File(path, 'r')

        if isinstance(group, str):
            f1 = f[group]
        else:
            f1 = f

        ds_list = list(f1.keys())

        for ds_name in ds_list:
            if is_scale(f1[ds_name]):
                ds = f1[ds_name]

                if ds_name in coords_dict:
                    coords_dict[ds_name] = np.union1d(coords_dict[ds_name], ds[:])
                else:
                    coords_dict[ds_name] = ds[:]

        f.close()

    return coords_dict


def extend_variables(paths, coords_dict, group=None):
    """

    """
    vars_dict = {}

    for path in paths:
        f = h5py.File(path, 'r')

        if isinstance(group, str):
            f1 = f[group]
        else:
            f1 = f

        ds_list = list(f1.keys())

        for ds_name in ds_list:
            if not is_scale(f1[ds_name]):
                ds = f1[ds_name]

                dims = []
                slice_index = []

                for dim in ds.dims:
                    dim_name = dim[0].name.split('/')[-1]
                    dims.append(dim_name)
                    arr_index = np.where(np.isin(coords_dict[dim_name], dim[0][:]))[0]
                    slice1 = slice(arr_index.min(), arr_index.max() + 1)
                    slice_index.append(slice1)

                if ds_name in vars_dict:
                    if not np.in1d(vars_dict[ds_name]['dims'], dims).all():
                        raise ValueError('dims are not consistant between the same named datasets.')
                    if vars_dict[ds_name]['dtype'] != ds.dtype:
                        raise ValueError('dtypes are not consistant between the same named datasets.')

                    vars_dict[ds_name]['data'][path] = {'dims_order': tuple(dims), 'slice_index': tuple(slice_index)}
                else:
                    shape = tuple([coords_dict[dim_name].shape[0] for dim_name in dims])
                    vars_dict[ds_name] = {'data': {path: {'dims_order': tuple(dims), 'slice_index': tuple(slice_index)}}, 'dims': tuple(dims), 'shape': shape, 'dtype': ds.dtype, 'fillvalue': ds.fillvalue}

        f.close()

    return vars_dict


def index_coords(hdf_path: str, selection: dict, group: str = None):
    """

    """
    # with h5py.File(hdf_path, 'r') as f:
    f = h5py.File(hdf_path, 'r')

    if isinstance(group, str):
        f1 = f[group]
    else:
        f1 = f

    coords_list = [ds_name for ds_name in f1 if is_scale(f1[ds_name])]

    index_coords_dict = {}

    for coord, sel in selection.items():
        if coord not in coords_list:
            raise ValueError(coord + ' is not in the coordiantes of the hdf5 file.')

        attrs = dict(f1[coord].attrs)
        enc = {k: v for k, v in attrs.items() if k in decode_data.__code__.co_varnames}

        arr = decode_data(f1[coord][:], **enc)

        if isinstance(sel, slice):
            if 'datetime64' in arr.dtype.name:
                start = np.datetime64(sel.start, 's')
                end = np.datetime64(sel.stop, 's')
                bool_index = (start <= arr) & (arr < end)
            else:
                bool_index = (sel.start <= arr) & (arr < sel.stop)

        else:
            if isinstance(sel, (int, float)):
                sel = [sel]

            try:
                sel1 = np.array(sel)
            except:
                raise TypeError('selection input could not be coerced to an ndarray.')

            if sel1.dtype.name == 'bool':
                if sel1.shape[0] != arr.shape[0]:
                    raise ValueError('The boolean array does not have the same length as the coord array.')
                bool_index = sel1
            else:
                bool_index = np.in1d(arr, sel1)

        int_index = np.where(bool_index)[0]
        slice_index = slice(int_index.min(), int_index.max())

        index_coords_dict[coord] = {'bool_index': bool_index, 'int_index': int_index, 'slice_index': slice_index}

    return index_coords_dict


def guess_chunk(shape, maxshape, dtype):
    """ Guess an appropriate chunk layout for a dataset, given its shape and
    the size of each element in bytes.  Will allocate chunks only as large
    as MAX_SIZE.  Chunks are generally close to some power-of-2 fraction of
    each axis, slightly favoring bigger values for the last index.
    Undocumented and subject to change without warning.
    """
    # pylint: disable=unused-argument

    # For unlimited dimensions we have to guess 1024
    shape1 = []
    for i, x in enumerate(maxshape):
        if x is None:
            if shape[i] > 1024:
                shape1.append(shape[i])
            else:
                shape1.append(1024)
        else:
            shape1.append(x)

    shape = tuple(shape1)

    ndims = len(shape)
    if ndims == 0:
        raise ValueError("Chunks not allowed for scalar datasets.")

    chunks = np.array(shape, dtype='=f8')
    if not np.all(np.isfinite(chunks)):
        raise ValueError("Illegal value in chunk tuple")

    # Determine the optimal chunk size in bytes using a PyTables expression.
    # This is kept as a float.
    typesize = dtype.itemsize
    # dset_size = np.product(chunks)*typesize
    # target_size = CHUNK_BASE * (2**np.log10(dset_size/(1024.*1024)))

    # if target_size > CHUNK_MAX:
    #     target_size = CHUNK_MAX
    # elif target_size < CHUNK_MIN:
    #     target_size = CHUNK_MIN

    target_size = CHUNK_MAX

    idx = 0
    while True:
        # Repeatedly loop over the axes, dividing them by 2.  Stop when:
        # 1a. We're smaller than the target chunk size, OR
        # 1b. We're within 50% of the target chunk size, AND
        #  2. The chunk is smaller than the maximum chunk size

        chunk_bytes = np.product(chunks)*typesize

        if (chunk_bytes < target_size or \
         abs(chunk_bytes-target_size)/target_size < 0.5) and \
         chunk_bytes < CHUNK_MAX:
            break

        if np.product(chunks) == 1:
            break  # Element size larger than CHUNK_MAX

        chunks[idx%ndims] = np.ceil(chunks[idx%ndims] / 2.0)
        idx += 1

    return tuple(int(x) for x in chunks)


def copy_chunks(shape, chunks, source_slice_index=None, source_dim_index=None, factor=3):
    """

    """
    n_shapes = []

    if isinstance(source_slice_index, (list, tuple)) and isinstance(source_dim_index, (list, tuple)):
        copy_shape = tuple([s*factor if s*factor <= (source_slice_index[i].stop - source_slice_index[i].start) else (source_slice_index[i].stop - source_slice_index[i].start) for i, s in enumerate(chunks)])

        for i, s in enumerate(copy_shape):
            shapes = np.arange(source_slice_index[i].start, source_slice_index[i].stop, s)
            n_shapes.append(shapes)

        cart = cartesian(n_shapes)

        slices = []
        append = slices.append
        for arr in cart:
            slices1 = tuple([slice(s, s + copy_shape[i]) if s + copy_shape[i] <= source_slice_index[i].stop else slice(s, source_slice_index[i].stop) for i, s in enumerate(arr)])
            append(slices1)

        source_slices = []
        append = source_slices.append
        for s in slices:
            source_chunk = tuple([slice(s[i].start - source_slice_index[i].start, s[i].stop - source_slice_index[i].start) for i in source_dim_index])
            append(source_chunk)

    else:
        copy_shape = tuple([s*factor if s*factor <= shape[i] else shape[i] for i, s in enumerate(chunks)])
        for i, s in enumerate(copy_shape):
            shapes = np.arange(0, shape[i], s)
            n_shapes.append(shapes)

        cart = cartesian(n_shapes)

        slices = []
        append = slices.append
        for arr in cart:
            slices1 = tuple([slice(s, s + copy_shape[i]) if s + copy_shape[i] <= shape[i] else slice(s, shape[i]) for i, s in enumerate(arr)])
            append(slices1)
    
        source_slices = slices

    return slices, source_slices


def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.

    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])

    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = int(n / arrays[0].size)
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m, 1:])
        for j in range(1, arrays[0].size):
            out[j*m:(j+1)*m, 1:] = out[0:m, 1:]

    return out
































































































