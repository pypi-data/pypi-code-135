# CODEBASE: https://github.com/kentaroy47/frcnn-from-scratch-with-keras

from __future__ import absolute_import
import numpy as np
import cv2
import random
import copy
import threading
import itertools
import numpy as np
import pdb
import math
import time

def apply_regr(x, y, w, h, tx, ty, tw, th):
    try:
        cx = x + w/2.
        cy = y + h/2.
        cx1 = tx * w + cx
        cy1 = ty * h + cy
        w1 = math.exp(tw) * w
        h1 = math.exp(th) * h
        x1 = cx1 - w1/2.
        y1 = cy1 - h1/2.
        x1 = int(round(x1))
        y1 = int(round(y1))
        w1 = int(round(w1))
        h1 = int(round(h1))

        return x1, y1, w1, h1

    except ValueError:
        return x, y, w, h
    except OverflowError:
        return x, y, w, h
    except Exception as e:
        print(e)
        return x, y, w, h

def apply_regr_np(X, T):
    try:
        x = X[0, :, :]
        y = X[1, :, :]
        w = X[2, :, :]
        h = X[3, :, :]

        tx = T[0, :, :]
        ty = T[1, :, :]
        tw = T[2, :, :]
        th = T[3, :, :]

        cx = x + w/2.
        cy = y + h/2.
        cx1 = tx * w + cx
        cy1 = ty * h + cy

        w1 = np.exp(tw.astype(np.float64)) * w
        h1 = np.exp(th.astype(np.float64)) * h
        x1 = cx1 - w1/2.
        y1 = cy1 - h1/2.

        x1 = np.round(x1)
        y1 = np.round(y1)
        w1 = np.round(w1)
        h1 = np.round(h1)
        return np.stack([x1, y1, w1, h1])
    except Exception as e:
        print(e)
        return X

def non_max_suppression_fast (boxes, probs, overlap_thresh=0.9, max_boxes=300):
    # code used from here: http://www.pyimagesearch.com/2015/02/16/faster-non-maximum-suppression-python/
    # if there are no boxes, return an empty list
    if len(boxes) == 0:
        return []

    # grab the coordinates of the bounding boxes
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    np.testing.assert_array_less(x1, x2)
    np.testing.assert_array_less(y1, y2)

    # if the bounding boxes integers, convert them to floats --
    # this is important since we'll be doing a bunch of divisions
    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")

    # initialize the list of picked indexes
    pick = []

    # calculate the areas
    area = (x2 - x1) * (y2 - y1)

    # sort the bounding boxes
    idxs = np.argsort(probs)

    # keep looping while some indexes still remain in the indexes
    # list
    while len(idxs) > 0:
        # grab the last index in the indexes list and add the
        # index value to the list of picked indexes
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        # find the intersection

        xx1_int = np.maximum(x1[i], x1[idxs[:last]])
        yy1_int = np.maximum(y1[i], y1[idxs[:last]])
        xx2_int = np.minimum(x2[i], x2[idxs[:last]])
        yy2_int = np.minimum(y2[i], y2[idxs[:last]])

        ww_int = np.maximum(0, xx2_int - xx1_int)
        hh_int = np.maximum(0, yy2_int - yy1_int)

        area_int = ww_int * hh_int

        # find the union
        area_union = area[i] + area[idxs[:last]] - area_int

        # compute the ratio of overlap
        overlap = area_int/(area_union + 1e-6)

        # delete all indexes from the index list that have
        idxs = np.delete(idxs, np.concatenate(([last],
            np.where(overlap > overlap_thresh)[0])))

        if len(pick) >= max_boxes:
            break

    # return only the bounding boxes that were picked using the integer data type
    boxes = boxes[pick].astype("int")
    probs = probs[pick]
    return boxes, probs

def union(au, bu, area_intersection):
    area_a = (au[2] - au[0]) * (au[3] - au[1])
    area_b = (bu[2] - bu[0]) * (bu[3] - bu[1])
    area_union = area_a + area_b - area_intersection
    return area_union

def intersection(ai, bi):
    x = max(ai[0], bi[0])
    y = max(ai[1], bi[1])
    w = min(ai[2], bi[2]) - x
    h = min(ai[3], bi[3]) - y
    if w < 0 or h < 0:
        return 0
    return w*h

def iou(a, b):
    # a and b should be (x1,y1,x2,y2)
    if a[0] >= a[2] or a[1] >= a[3] or b[0] >= b[2] or b[1] >= b[3]:
        return 0.0
    area_i = intersection(a, b)
    area_u = union(a, b, area_i)
    return float(area_i) / float(area_u + 1e-6)


# public ----------------------------------------------------------

def rescale_roi (rois, width, height, rpn_stride):
    # get the GT box coordinates, and resize to account for image resizing
    r = rois
    r [:, 0] = np.round(r [:, 0] * rpn_stride)
    r [:, 1] = np.round(r [:, 1] * rpn_stride)
    r [:, 2] = np.round(r [:, 2] * rpn_stride)
    r [:, 3] = np.round(r [:, 3] * rpn_stride)
    return r

def rpn_to_roi (rpn_layer, regr_layer,
    rpn_stride, anchor_sizes, anchor_ratios, std_scaling,
    use_regr=True, max_boxes=300, overlap_thresh=0.9, fit_to_image = False
):
    regr_layer = regr_layer / std_scaling
    assert rpn_layer.shape[0] == 1
    (rows, cols) = rpn_layer.shape[1:3]
    curr_layer = 0
    A = np.zeros((4, rpn_layer.shape[1], rpn_layer.shape[2], rpn_layer.shape[3]))
    for anchor_size in anchor_sizes:
        for anchor_ratio in anchor_ratios:
            anchor_x = (anchor_size * anchor_ratio[0])/rpn_stride
            anchor_y = (anchor_size * anchor_ratio[1])/rpn_stride
            regr = regr_layer[0, :, :, 4 * curr_layer:4 * curr_layer + 4]
            regr = np.transpose(regr, (2, 0, 1))

            X, Y = np.meshgrid(np.arange(cols),np. arange(rows))

            A[0, :, :, curr_layer] = X - anchor_x/2
            A[1, :, :, curr_layer] = Y - anchor_y/2
            A[2, :, :, curr_layer] = anchor_x
            A[3, :, :, curr_layer] = anchor_y

            if use_regr:
                A[:, :, :, curr_layer] = apply_regr_np(A[:, :, :, curr_layer], regr)

            A[2, :, :, curr_layer] = np.maximum(1, A[2, :, :, curr_layer])
            A[3, :, :, curr_layer] = np.maximum(1, A[3, :, :, curr_layer])
            A[2, :, :, curr_layer] += A[0, :, :, curr_layer]
            A[3, :, :, curr_layer] += A[1, :, :, curr_layer]

            A[0, :, :, curr_layer] = np.maximum(0, A[0, :, :, curr_layer])
            A[1, :, :, curr_layer] = np.maximum(0, A[1, :, :, curr_layer])
            A[2, :, :, curr_layer] = np.minimum(cols-1, A[2, :, :, curr_layer])
            A[3, :, :, curr_layer] = np.minimum(rows-1, A[3, :, :, curr_layer])

            curr_layer += 1

    all_boxes = np.reshape(A.transpose((0, 3, 1, 2)), (4, -1)).transpose((1, 0))
    all_probs = rpn_layer.transpose((0, 3, 1, 2)).reshape((-1))

    x1 = all_boxes[:, 0]
    y1 = all_boxes[:, 1]
    x2 = all_boxes[:, 2]
    y2 = all_boxes[:, 3]

    idxs = np.where((x1 - x2 >= 0) | (y1 - y2 >= 0))
    all_boxes = np.delete(all_boxes, idxs, 0)
    all_probs = np.delete(all_probs, idxs, 0)
    boxes, scores = non_max_suppression_fast(all_boxes, all_probs, overlap_thresh=overlap_thresh, max_boxes=max_boxes)

    nboxes = np.zeros_like (boxes)
    nboxes [:,0] = boxes [:,0]
    nboxes [:,1] = boxes [:,2]
    nboxes [:,2] = boxes [:,1]
    nboxes [:,3] = boxes [:,3]
    return nboxes, scores # xmin, xmax, ymin, ymax

def calc_iou (rois, boxes, classifier_min_overlap, classifier_max_overlap, classifier_regr_std):
    gta = boxes [:,:4]
    x_roi = []
    y_class_num = []
    y_class_regr_coords = []
    y_class_regr_label = []
    IoUs = [] # for debugging only

    for ix in range(rois.shape[0]):
        (x1, y1, x2, y2) = rois [ix, :]
        x1 = int(round(x1))
        y1 = int(round(y1))
        x2 = int(round(x2))
        y2 = int(round(y2))

        best_iou = 0.0
        best_bbox = -1
        for bbox_num in range(len(boxes)):
            curr_iou = iou([gta[bbox_num, 0], gta[bbox_num, 2], gta[bbox_num, 1], gta[bbox_num, 3]], [x1, y1, x2, y2])
            if curr_iou > best_iou:
                best_iou = curr_iou
                best_bbox = bbox_num

        if best_iou < classifier_min_overlap:
            continue
        else:
            w = x2 - x1
            h = y2 - y1
            x_roi.append([x1, y1, w, h])
            IoUs.append(best_iou)

            if classifier_min_overlap <= best_iou < classifier_max_overlap:
                # hard negative example
                cls_name = 0
            elif classifier_max_overlap <= best_iou:
                cls_name = boxes[best_bbox][-1]
                cxg = (gta[best_bbox, 0] + gta[best_bbox, 1]) / 2.0
                cyg = (gta[best_bbox, 2] + gta[best_bbox, 3]) / 2.0

                cx = x1 + w / 2.0
                cy = y1 + h / 2.0

                tx = (cxg - cx) / float(w)
                ty = (cyg - cy) / float(h)
                tw = np.log((gta[best_bbox, 1] - gta[best_bbox, 0]) / float(w))
                th = np.log((gta[best_bbox, 3] - gta[best_bbox, 2]) / float(h))
            else:
                print('roi = {}'.format(best_iou))
                raise RuntimeError

        y_class_num.append(cls_name)
        if cls_name == 1:
            sx, sy, sw, sh = classifier_regr_std
            coords = [sx*tx, sy*ty, sw*tw, sh*th]
            y_class_regr_coords.append(copy.deepcopy(coords))
        else:
            coords = [0] * 4
            y_class_regr_coords.append(copy.deepcopy(coords))

    if len(x_roi) == 0:
        return None, None, None, None

    X = np.array(x_roi)
    Y1 = np.array(y_class_num)
    Y2 = np.array(y_class_regr_coords)

    return np.expand_dims(X, axis=0), np.expand_dims(Y1, axis=0), np.expand_dims(Y2, axis=0), np.array (IoUs)

def calc_rpn (
    boxes,
    width, height, img_length_calc_function,
    downscale = 16.0,
    anchor_sizes = [128, 256, 512],
    anchor_ratios = [[1, 1], [1, 2], [2, 1]],
    rpn_max_overlap = 0.7,
    rpn_min_overlap = 0.3
):
    # boxes = [xmin, xmax, ymin, ymax, class_id] # 0 must be bg
    num_anchors = len(anchor_sizes) * len(anchor_ratios)
    # calculate the output map size based on the network architecture

    (output_width, output_height) = img_length_calc_function(width, height)
    n_anchratios = len(anchor_ratios)

    # initialise empty output objectives
    y_rpn_overlap = np.zeros((output_height, output_width, num_anchors)).astype(int)
    y_is_box_valid = np.zeros((output_height, output_width, num_anchors)).astype(int)
    y_rpn_regr = np.zeros((output_height, output_width, num_anchors * 4))

    num_bboxes = len(boxes)
    num_anchors_for_bbox = np.zeros(num_bboxes).astype(int)
    best_anchor_for_bbox = -1*np.ones((num_bboxes, 4)).astype(int)
    best_iou_for_bbox = np.zeros(num_bboxes).astype(np.float32)
    best_x_for_bbox = np.zeros((num_bboxes, 4))
    best_dx_for_bbox = np.zeros((num_bboxes, 4))

    # get the GT box coordinates, and resize to account for image resizing
    gta = np.zeros((num_bboxes, 4))
    for bbox_num, bbox in enumerate(boxes):
        # get the GT box coordinates, and resize to account for image resizing
        # gta = [xmin, xmax, ymin, ymax]
        gta[bbox_num, 0] = bbox[0]
        gta[bbox_num, 1] = bbox[1]
        gta[bbox_num, 2] = bbox[2]
        gta[bbox_num, 3] = bbox[3]

    # rpn ground truth
    for anchor_size_idx in range(len(anchor_sizes)):
        for anchor_ratio_idx in range(n_anchratios):
            anchor_x = anchor_sizes[anchor_size_idx] * anchor_ratios[anchor_ratio_idx][0]
            anchor_y = anchor_sizes[anchor_size_idx] * anchor_ratios[anchor_ratio_idx][1]

            for ix in range(output_width):
                # x-coordinates of the current anchor box
                x1_anc = downscale * (ix + 0.5) - anchor_x / 2
                x2_anc = downscale * (ix + 0.5) + anchor_x / 2

                # ignore boxes that go across image boundaries
                if x1_anc < 0 or x2_anc > width:
                    continue

                for jy in range(output_height):

                    # y-coordinates of the current anchor box
                    y1_anc = downscale * (jy + 0.5) - anchor_y / 2
                    y2_anc = downscale * (jy + 0.5) + anchor_y / 2

                    # ignore boxes that go across image boundaries
                    if y1_anc < 0 or y2_anc > height:
                        continue

                    # bbox_type indicates whether an anchor should be a target
                    bbox_type = 'neg'

                    # this is the best IOU for the (x,y) coord and the current anchor
                    # note that this is different from the best IOU for a GT bbox
                    best_iou_for_loc = 0.0

                    for bbox_num in range(num_bboxes):
                        # get IOU of the current GT box and the current anchor box
                        curr_iou = iou([gta[bbox_num, 0], gta[bbox_num, 2], gta[bbox_num, 1], gta[bbox_num, 3]], [x1_anc, y1_anc, x2_anc, y2_anc])
                        # calculate the regression targets if they will be needed
                        if curr_iou > best_iou_for_bbox[bbox_num] or curr_iou > rpn_max_overlap:
                            cx = (gta[bbox_num, 0] + gta[bbox_num, 1]) / 2.0
                            cy = (gta[bbox_num, 2] + gta[bbox_num, 3]) / 2.0
                            cxa = (x1_anc + x2_anc)/2.0
                            cya = (y1_anc + y2_anc)/2.0

                            tx = (cx - cxa) / (x2_anc - x1_anc)
                            ty = (cy - cya) / (y2_anc - y1_anc)
                            #calculate log of tw and th later
                            tw = 1.0*(gta[bbox_num, 1] - gta[bbox_num, 0]) / (x2_anc - x1_anc)
                            th = 1.0*(gta[bbox_num, 3] - gta[bbox_num, 2]) / (y2_anc - y1_anc)

                        if int (boxes[bbox_num][-1]) != 0: # not bg
                            # all GT boxes should be mapped to an anchor box, so we keep track of which anchor box was best
                            if curr_iou > best_iou_for_bbox[bbox_num]:
                                best_anchor_for_bbox[bbox_num] = [jy, ix, anchor_ratio_idx, anchor_size_idx]
                                best_iou_for_bbox[bbox_num] = curr_iou
                                best_x_for_bbox[bbox_num,:] = [x1_anc, x2_anc, y1_anc, y2_anc]
                                best_dx_for_bbox[bbox_num,:] = [tx, ty, tw, th]

                            # we set the anchor to positive if the IOU is >0.7 (it does not matter if there was another better box, it just indicates overlap)
                            if curr_iou > rpn_max_overlap:
                                bbox_type = 'pos'
                                num_anchors_for_bbox[bbox_num] += 1
                                # we update the regression layer target if this IOU is the best for the current (x,y) and anchor position
                                if curr_iou > best_iou_for_loc:
                                    best_iou_for_loc = curr_iou
                                    best_regr = (tx, ty, tw, th)

                            # if the IOU is >0.3 and <0.7, it is ambiguous and no included in the objective
                            if rpn_min_overlap < curr_iou < rpn_max_overlap:
                                # gray zone between neg and pos
                                if bbox_type != 'pos':
                                    bbox_type = 'neutral'

                    # turn on or off outputs depending on IOUs
                    if bbox_type == 'neg':
                        y_is_box_valid[jy, ix, anchor_ratio_idx + n_anchratios * anchor_size_idx] = 1
                        y_rpn_overlap[jy, ix, anchor_ratio_idx + n_anchratios * anchor_size_idx] = 0
                    elif bbox_type == 'neutral':
                        y_is_box_valid[jy, ix, anchor_ratio_idx + n_anchratios * anchor_size_idx] = 0
                        y_rpn_overlap[jy, ix, anchor_ratio_idx + n_anchratios * anchor_size_idx] = 0
                    elif bbox_type == 'pos':
                        y_is_box_valid[jy, ix, anchor_ratio_idx + n_anchratios * anchor_size_idx] = 1
                        y_rpn_overlap[jy, ix, anchor_ratio_idx + n_anchratios * anchor_size_idx] = 1
                        start = 4 * (anchor_ratio_idx + n_anchratios * anchor_size_idx)
                        y_rpn_regr[jy, ix, start:start+2 ] = best_regr[0:2]
                        y_rpn_regr[jy, ix, start+2:start+4 ] = np.log(best_regr[2:])

    # we ensure that every bbox has at least one positive RPN region

    for idx in range(num_anchors_for_bbox.shape[0]):
        if num_anchors_for_bbox[idx] == 0:
            # no box with an IOU greater than zero ...
            if best_anchor_for_bbox[idx, 0] == -1:
                continue
            y_is_box_valid[
                best_anchor_for_bbox[idx,0], best_anchor_for_bbox[idx,1], best_anchor_for_bbox[idx,2] + n_anchratios *
                best_anchor_for_bbox[idx,3]] = 1
            y_rpn_overlap[
                best_anchor_for_bbox[idx,0], best_anchor_for_bbox[idx,1], best_anchor_for_bbox[idx,2] + n_anchratios *
                best_anchor_for_bbox[idx,3]] = 1
            start = 4 * (best_anchor_for_bbox[idx,2] + n_anchratios * best_anchor_for_bbox[idx,3])
            y_rpn_regr[
                best_anchor_for_bbox[idx,0], best_anchor_for_bbox[idx,1], start:start+2] = best_dx_for_bbox[idx, 0:2]
            y_rpn_regr[
                best_anchor_for_bbox[idx,0], best_anchor_for_bbox[idx,1], start+2:start+4] = np.log(best_dx_for_bbox[idx, 2:4])

    y_rpn_overlap = np.transpose(y_rpn_overlap, (2, 0, 1))
    y_rpn_overlap = np.expand_dims(y_rpn_overlap, axis=0)

    y_is_box_valid = np.transpose(y_is_box_valid, (2, 0, 1))
    y_is_box_valid = np.expand_dims(y_is_box_valid, axis=0)

    y_rpn_regr = np.transpose(y_rpn_regr, (2, 0, 1))
    y_rpn_regr = np.expand_dims(y_rpn_regr, axis=0)

    pos_locs = np.where(np.logical_and(y_rpn_overlap[0, :, :, :] == 1, y_is_box_valid[0, :, :, :] == 1))
    neg_locs = np.where(np.logical_and(y_rpn_overlap[0, :, :, :] == 0, y_is_box_valid[0, :, :, :] == 1))

    num_pos = len(pos_locs[0])

    # one issue is that the RPN has many more negative than positive regions, so we turn off some of the negative
    # regions. We also limit it to 256 regions.
    num_regions = 256

    if len(pos_locs[0]) > num_regions/2:
        val_locs = random.sample(range(len(pos_locs[0])), len(pos_locs[0]) - num_regions/2)
        y_is_box_valid[0, pos_locs[0][val_locs], pos_locs[1][val_locs], pos_locs[2][val_locs]] = 0
        num_pos = num_regions/2

    if len(neg_locs[0]) + num_pos > num_regions:
        val_locs = random.sample(range(len(neg_locs[0])), len(neg_locs[0]) - num_pos)
        y_is_box_valid[0, neg_locs[0][val_locs], neg_locs[1][val_locs], neg_locs[2][val_locs]] = 0

    y_rpn_cls = np.concatenate([y_is_box_valid, y_rpn_overlap], axis=1)
    y_rpn_regr = np.concatenate([np.repeat(y_rpn_overlap, 4, axis=1), y_rpn_regr], axis=1)

    return np.copy(y_rpn_cls), np.copy(y_rpn_regr)
