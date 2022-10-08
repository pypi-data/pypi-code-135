# 配置文件
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# intra_op_num_threads为CPU核数效能最佳
OP_NUM_THREADS = 4
IMAGE_INFER_MODEL_PATH = os.path.join(BASE_DIR, 'capture/local_models/ui_det_v2.onnx')
CLIP_MODEL_PATH = os.path.join(BASE_DIR, 'capture/local_models/clip_vit32_feat.onnx')
IMAGE_TEMP_DIR = os.path.join(BASE_DIR, 'capture/temp')
REC_CHAR_DICT_PATH = os.path.join(BASE_DIR, 'dbnet_crnn/ppocr/utils/keys.txt')
PREDICT_DET_PATH = os.path.join(BASE_DIR, 'dbnet_crnn/modelv1.1/det/')
PREDICT_REC_PATH = os.path.join(BASE_DIR, 'dbnet_crnn/modelv1.1/rec/')
