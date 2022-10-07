import numpy as np
from numpy import ndarray
from scipy.ndimage import grey_dilation
from skimage.segmentation import find_boundaries

from seg2link import parameters


def labels_with_boundary(labels: ndarray) -> ndarray:
    if parameters.pars.add_boundary_mode != "2D":
        result = find_boundaries(labels, mode="outer", connectivity=3)
    else:
        result = np.zeros_like(labels)
        for z in range(result.shape[2]):
            result[..., z] = find_boundaries(labels[..., z], mode="outer", connectivity=2)
    result = np.logical_not(result)
    return result * labels


def remove_boundary_scipy(labels: ndarray) -> ndarray:
    """Faster than using skimage"""
    labels_dilate = grey_dilation(labels, parameters.pars.labels_dilate_kernel_r2)
    labels_dilate *= (labels == 0)
    labels += labels_dilate
    return labels