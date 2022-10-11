# -*- coding: utf-8 -*-
# @Author        : lk
# @Email         : 9428.al@gmail.com
# @Created Date  : 2019-09-03 15:40:54
# @Last Modified : 2022-07-18 16:10:36
# @Description   :

import os
import cv2
import time
import numpy as np
# import tensorflow as tf

# import grpc
# from tensorflow_serving.apis import predict_pb2
# from tensorflow_serving.apis import prediction_service_pb2_grpc

import tritonclient.grpc as grpcclient


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    '''
    Resize the input image according to the dimensions and keep aspect ratio of this image
    '''
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

    return resized

def predict(image):
    
    ROTATE = [0, 90, 180, 270]

    # pre-process the image for classification
    # Test 1: 直接resize到目标尺寸
    # image = cv2.resize(image, (512, 512))
    
    # Test 2: 按照短边resize到目标尺寸,长边按比例缩放
    short_side = 768
    if min(image.shape[:2]) > short_side:
        image = resize(image, width=short_side) if image.shape[0] > image.shape[1] else resize(image, height=short_side)
    
    # Test 3: 带padding的resize策略
    # image = resize_image_with_pad(image, 1024, 1024)
    
    # Test 4: 直接使用原图
    # image = image

    image = np.array(image, dtype="float32")
    image = 2 * (image / 255.0) - 1  # Let data input to be  normalized to the [-1,1] range
    input_data = np.expand_dims(image, 0)

    # options = [('grpc.max_send_message_length', 1000 * 1024 * 1024),
    #            ('grpc.max_receive_message_length', 1000 * 1024 * 1024)]
    # channel = grpc.insecure_channel('localhost:8500', options=options)
    # stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

    # request = predict_pb2.PredictRequest()
    # request.model_spec.name = 'adc_model'
    # request.model_spec.signature_name = 'serving_default'
    # request.inputs['input_1'].CopyFrom(tf.make_tensor_proto(inputs))

    # result = stub.Predict(request, 100.0)  # 100 secs timeout

    # preds = tf.make_ndarray(result.outputs['dense'])

    triton_client = grpcclient.InferenceServerClient("localhost:8001")

    # Initialize the data
    inputs = [grpcclient.InferInput('input_1', input_data.shape, "FP32")]               # [InferInput 类的一个对象用于描述推理请求的输入张量。]
    inputs[0].set_data_from_numpy(input_data)                                       # 从指定的numpy数组中获取张量数据与此对象关联的输入
    outputs = [grpcclient.InferRequestedOutput("dense")]

    # Inference
    results = triton_client.infer(
        model_name="adc_model",
        inputs=inputs,
        outputs=outputs
    )
    # Get the output arrays from the results
    preds = results.as_numpy("dense")
    
    index = np.argmax(preds, axis=-1)[0]

    return index
    # return ROTATE[index]

def DegreeTrans(theta):
    '''
    Convert radians to angles
    '''
    res = theta / np.pi * 180
    return res

def rotateImage(src, degree):
    '''
    Calculate the rotation matrix and rotate the image
    param src:image after rot90
    param degree:the Hough degree
    '''
    h, w = src.shape[:2]
    RotateMatrix = cv2.getRotationMatrix2D((w/2.0, h/2.0), degree, 1)
    # affine transformation, background color fills white
    rotate = cv2.warpAffine(src, RotateMatrix, (w, h), borderValue=(255, 255, 255))
    return rotate

def CalcDegree(srcImage):
    '''
    Calculating angles by Hough transform
    param srcImage:image after rot90
    '''
    midImage = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
    dstImage = cv2.Canny(midImage, 100, 300, 3)
    lineimage = srcImage.copy()
 
    # 通过霍夫变换检测直线
    # 第4个参数(th)就是阈值，阈值越大，检测精度越高 
    th = 500
    while True:
        if th > 0:
            lines = cv2.HoughLines(dstImage, 1, np.pi/180, th)
        else:
            lines = None
            break
        if lines is not None:
            if len(lines) > 10:
                break
            else:
                th -=  50
                # print ('阈值是：', th)
        else:
            th -= 100
            # print ('阈值是：', th)
        continue
    
    sum_theta = 0
    num_theta = 0
    if lines is not None:
        for i in range(len(lines)):
            for rho, theta in lines[i]:
                # control the angle of line between -30 to +30
                if theta > 1 and theta < 2.1:
                    sum_theta += theta
                    num_theta += 1
    # Average all angles
    if num_theta == 0:
        average = np.pi/2
    else:
        average = sum_theta / num_theta

    return DegreeTrans(average) - 90

def ADC(image, fine_degree=False):
    '''
    return param rotate: Corrected image
    return param angle_degree：image offset image
    '''
    
    # Return a wide angle index
    img = np.copy(image)
    angle_index = predict(img)
    img_rot = np.rot90(img, -angle_index)
    
    # if fine_degree then the image will be corrected more accurately based on character line features.
    if fine_degree:
        degree = CalcDegree(img_rot)
        angle_degree = (angle_index * 90 - degree) % 360
        rotate = rotateImage(img_rot, degree)
        return rotate, angle_degree
    
    return img_rot, int(angle_index*90)
