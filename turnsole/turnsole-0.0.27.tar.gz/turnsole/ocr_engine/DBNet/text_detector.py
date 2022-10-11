# -*- coding: utf-8 -*-
# @Author        : Lyu Kui
# @Email         : 9428.al@gmail.com
# @Create Date   : 2022-06-01 19:00:18
# @Last Modified : 2022-07-15 11:41:25
# @Description   : 

import os
import cv2
import time
import pyclipper
import numpy as np
# import tensorflow as tf
from shapely.geometry import Polygon

# import grpc
# from tensorflow_serving.apis import predict_pb2
# from tensorflow_serving.apis import prediction_service_pb2_grpc

import tritonclient.grpc as grpcclient


def resize_with_padding(src, limit_max=1024):
    '''限制长边不大于 limit_max 短边等比例缩放，以 0 填充'''
    img = src.copy()

    h, w, _ = img.shape
    max_side = max(h, w)
    ratio = limit_max / max_side if max_side > limit_max else 1
    h, w = int(h * ratio), int(w * ratio)
    proc = cv2.resize(img, (w, h))

    canvas = np.zeros((limit_max, limit_max, 3), dtype=np.float32)
    canvas[0:h, 0:w, :] = proc
    return canvas, ratio

def rectangle_boxes_zoom(boxes, offset=1):
    '''Scale the rectangle boxes via offset
    Input:
        boxes: with shape (-1, 4, 2)
        offset: how many pix do you wanna zoom, we recommend less than 5
    Output:
        boxes: zoomed
    '''
    boxes = np.array(boxes)
    boxes += [[[-offset,-offset], [offset,-offset], [offset,offset], [-offset,offset]]]
    return boxes

def polygons_from_probmap(preds, ratio):
    # 二值化
    prob_map_pred = np.array(preds, dtype=np.uint8)[0,:,:,0]
    # 输入：二值图、轮廓检索（层次）模式、轮廓渐进方法
    # 输出：轮廓、层级关系
    contours, hierarchy = cv2.findContours(prob_map_pred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    boxes = []
    for contour in contours:
        if len(contour) < 4:
            continue

        # Vatti clipping 
        polygon = Polygon(np.array(contour).reshape((-1, 2))).buffer(0)
        polygon = polygon.convex_hull if polygon.type == 'MultiPolygon' else polygon                        # Note: 这里不是 bug 是我们故意而为之

        if polygon.area < 10:
            continue

        distance = polygon.area * 1.5 / polygon.length
        offset = pyclipper.PyclipperOffset()
        offset.AddPath(list(polygon.exterior.coords), pyclipper.JT_ROUND, pyclipper.ET_CLOSEDPOLYGON)
        expanded = np.array(offset.Execute(distance)[0])                                                    # Note: 这里不是 bug 是我们故意而为之
        
        # Convert polygon to rectangle
        rect = cv2.minAreaRect(expanded)
        box = cv2.boxPoints(rect)
        # make clock-wise order
        box = np.roll(box, 4-box.sum(axis=1).argmin(), 0)
        box = np.array(box/ratio, dtype=np.int32)
        boxes.append(box)

    return boxes

def predict(image):

    image_resized, ratio = resize_with_padding(image, limit_max=1280)
    input_data = np.expand_dims(image_resized/255., axis=0)

    # options = [('grpc.max_send_message_length', 1000 * 1024 * 1024),
    #            ('grpc.max_receive_message_length', 1000 * 1024 * 1024)]
    # channel = grpc.insecure_channel('localhost:8500', options=options)
    # stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

    # request = predict_pb2.PredictRequest()
    # request.model_spec.name = 'dbnet_model'
    # request.model_spec.signature_name = 'serving_default'
    # request.inputs['input_1'].CopyFrom(tf.make_tensor_proto(inputs))

    # result = stub.Predict(request, 100.0)  # 100 secs timeout

    # preds = tf.make_ndarray(result.outputs['tf.math.greater'])

    triton_client = grpcclient.InferenceServerClient("localhost:8001")

    # Initialize the data
    inputs = [grpcclient.InferInput('input_1', input_data.shape, "FP32")]
    inputs[0].set_data_from_numpy(input_data)
    outputs = [grpcclient.InferRequestedOutput("tf.math.greater")]

    # Inference
    results = triton_client.infer(
        model_name="dbnet_model",
        inputs=inputs,
        outputs=outputs
    )
    # Get the output arrays from the results
    preds = results.as_numpy("tf.math.greater")

    boxes = polygons_from_probmap(preds, ratio)
    #boxes = rectangle_boxes_zoom(boxes, offset=0)

    return boxes
