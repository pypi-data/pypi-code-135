import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def find_differemce(img1, img2):
    assert img1.shape == img2.shape, "Specify 2 images with same shape"
    gray_img1 = rgb2gray(img1)
    gray_img2 = rgb2gray(img2)
    (score, difference_img) = structural_similarity(gray_img1, gray_img2, full=True)
    print(f"Similarity of the images: {score}")
    normalized_difference_img = (difference_img - np.min(difference_img)) / (
            np.max(difference_img) - np.min(difference_img))
    return normalized_difference_img


def transfer_histogram(img1, img2):
    return match_histograms(img1, img2, multichannel=True)
