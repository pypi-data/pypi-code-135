import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageOps

def flip(path,x_size,y_size,title):


    pic = Image.open(path)

    #all transpose modes
    flip = {"Flip left right": Image.FLIP_LEFT_RIGHT,
            "Flip Top Bottom": Image.FLIP_TOP_BOTTOM,
            "Rotate 90": Image.ROTATE_90,
            "Rotate 180": Image.ROTATE_180,
            "Rotate 270": Image.ROTATE_270,
            "Transpose": Image.TRANSPOSE, 
            "Transverse": Image.TRANSVERSE}

    #impress all transpose modes image
    for key, values in flip.items():
        plt.figure(figsize=(x_size,y_size))
        plt.subplot(1,2,1)
        plt.imshow(pic)
        plt.title(title)
        plt.subplot(1,2,2)
        plt.imshow(pic.transpose(values))
        plt.title(key)
        plt.show()
