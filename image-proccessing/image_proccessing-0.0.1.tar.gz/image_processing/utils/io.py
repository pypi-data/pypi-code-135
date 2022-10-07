from email.mime import image
from skimage.io import imread, imsave
#chamadas de leitura e escrita de imagem
def read_image(path, is_gray = False):
    image = imread(path, as_gray = is_gray)
    return image

def save_image(image, path):
    imsave(path, image)