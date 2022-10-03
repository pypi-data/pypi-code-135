import os
from PIL import Image
import urllib

from shiftlab_ocr.doc2text.crop import Crop
from shiftlab_ocr.doc2text.recognition import Recognizer
from shiftlab_ocr.doc2text.segmentation import Detector


class Reader:
    def __init__(
      self,
      yolo_path = os.path.join(os.path.dirname(__file__), "yolov5"),
      detector_weights = os.path.join(os.path.dirname(__file__), "weights/weights.pt"),
      recognizer_weights = os.path.join(os.path.dirname(__file__), "weights/ocr_transformer_4h2l_simple_conv_64x256.pt"),
      ):

        if os.path.isfile(detector_weights) == False:
            print('downloading detector weights ...')
            url = "https://github.com/konverner/shiftlab_ocr/blob/main/doc2text/weights/weights.pt?raw=true"
            urllib.request.urlretrieve(url, filename=detector_weights)

        if os.path.isfile(recognizer_weights) == False:
            print('downloading recognizer weights ...')
            url = "https://github.com/konverner/shiftlab_ocr/blob/main/doc2text/weights/ocr_transformer_4h2l_simple_conv_64x256.pt?raw=true"
            urllib.request.urlretrieve(url, filename=recognizer_weights)

        self.recognizer = Recognizer()
        self.recognizer.load_model(recognizer_weights)
        self.detector = Detector(yolo_path, detector_weights)

    def doc2text(self, image_path):
      """
      params
      ---
      image_path : str
      path to .png or .jpg file with image to read

      returns
      ---
      text : str
      crops : list of PIL.image objects
      crops are sorted
      """
      text = ''
      image = Image.open(image_path)
      boxes = self.detector.run(image_path)
      crops = []
      for box in boxes:
          cropped = image.crop((box[0], box[1],
                                box[2], box[3]))

          crops.append(Crop([[box[0], box[1]], [box[2], box[3]]], img=cropped))
      crops = sorted(crops)
      for crop in crops:
          text += self.recognizer.run(crop.img) + ' '

      return text, crops
