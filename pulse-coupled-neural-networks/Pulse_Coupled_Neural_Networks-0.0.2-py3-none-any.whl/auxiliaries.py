import numpy as np
from astropy.convolution import RickerWavelet2DKernel
from scipy.ndimage.filters import gaussian_filter


def choose_kernel(kernel_type, size=3):
    if kernel_type == 'gaussian':
        return gkern(size=size)
    if kernel_type == 'mexican_hat':
        return ricker(size=size)



def gaussian_kernel(size=3, sigma=1.):
    if size % 2 == 0:
        size += 1
    k = np.zeros((size,size))
    k[size//2, size//2] = 1
    k = gaussian_filter(k, sigma)
    return k

def gkern(size=5, sigma=1.):
    """\
    creates gaussian kernel with side length `l` and a sigma of `sig`
    """
    ax = np.linspace(-(size - 1) / 2., (size - 1) / 2., size)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)


def ricker(size=3, sigma=1.):
    return RickerWavelet2DKernel(width=sigma, x_size=size, y_size=size)
