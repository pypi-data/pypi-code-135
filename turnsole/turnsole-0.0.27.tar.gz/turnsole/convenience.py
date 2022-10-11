import cv2
import numpy as np

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized

def resize_with_pad(image, target_width, target_height):
    """Resuzes and pads an image to a target width and height.

    Resizes an image to a target width and height by keeping the aspect ratio the same 
    without distortion. 
    ratio must be less than 1.0.
    width and height will pad with zeroes.

    Args:
        image (Array): RGB/BGR
        target_width (Int): Target width.
        target_height (Int): Target height.

    Returns:
        Array: Resized and padded image. The image paded with zeroes.
        Float: Image resized ratio. The ratio must be less than 1.0.
    """
    height, width, _ = image.shape

    min_ratio = min(target_height/height, target_width/width)
    ratio = min_ratio if min_ratio < 1.0 else 1.0

    # To shrink an image, it will generally look best with INTER_AREA interpolation.
    resized = cv2.resize(image, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_AREA)
    h, w, _ = resized.shape
    canvas = np.zeros((target_height, target_width, 3), image.dtype)
    canvas[:h, :w, :] = resized
    return canvas, ratio

def image_crop(image, bbox, perspective=False):
    """根据 Bbox 在 image 上进行切片，如果指定 perspective 为 True 则切片方式为透视变换（可以切旋转目标）

    Args:
        image (array): 三通道图片，切片结果保持原图颜色通道
        bbox (array/list): 支持两点矩形框和四点旋转矩形框
            支持以下两种格式：
            1. bbox = [xmin, ymin, xmax, ymax]
            2. bbox = [x0, y0, x1, y1, x2, y2, x3, y3]
        perspective (bool, optional): 是否切出旋转目标. Defaults to False.

    Returns:
        array: 小切图，和原图颜色通道一致
    """
    # 按照 bbox 的正外接矩形切图
    bbox = np.array(bbox, dtype=np.int32).reshape((-1, 2))
    xmin, ymin, xmax, ymax = [min(bbox[:, 0]),
                              min(bbox[:, 1]), 
                              max(bbox[:, 0]), 
                              max(bbox[:, 1])]
    xmin, ymin = max(0, xmin), max(0, ymin)
    im_slice = image[ymin:ymax, xmin:xmax, :]

    if perspective and bbox.shape[0] == 4:
        # 获得旋转矩形的宽和高
        w, h = [int(np.linalg.norm(bbox[0] - bbox[1])),
                int(np.linalg.norm(bbox[3] - bbox[0]))]
        # 把 bbox 平移到正切图的对应位置上
        bbox[:, 0] -= xmin
        bbox[:, 1] -= ymin
        # 执行透视切图
        pts1 = np.float32(bbox)
        pts2 = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        im_slice = cv2.warpPerspective(im_slice, M, (w, h))

    return im_slice
