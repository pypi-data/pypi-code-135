import codecs
import os
from pprint import pprint

import cv2
import ffmpeg
from moviepy.editor import CompositeVideoClip, VideoFileClip
from moviepy.video.VideoClip import TextClip

import videotools


def mkdir_if_parent_not_exists(output_file):
    parent_path = os.path.dirname(output_file)
    if not os.path.exists(parent_path):
        os.makedirs(parent_path)


# 添加文本水印
def add_text_clip(input, output, text):
    video = VideoFileClip(input)
    txt_clip = TextClip(text, fontsize = 5, color = 'black')\
        .set_position(('left', 'bottom'))\
        .set_duration(10)
    result = CompositeVideoClip([video, txt_clip])
    
    mkdir_if_parent_not_exists(output)
    result.write_videofile(output)


# 读取视频文件元数据
def read_video_meta(input):
    pprint(ffmpeg.probe(input)["streams"])


# 读取视频文件参数信息
def read_video_params(input):
    capture = cv2.VideoCapture(input)
    
    # 帧率
    fps = int(round(capture.get(cv2.CAP_PROP_FPS)))
    # 分辨率-宽度
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 分辨率-高度
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 总帧数
    frame_counter = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    # 时长，单位s
    duration = frame_counter / fps

    capture.release()
    cv2.destroyAllWindows()

    print(f"帧率: {fps}, 宽: {width}, 高: {height}, 总帧数: {frame_counter}, 时长: {duration}")
