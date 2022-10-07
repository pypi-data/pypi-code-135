from encodings import normalize_encoding
import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2): #função achar diferença entre 2 imagens
    assert image1.shape == image2.shape, "Specify 2 images with de same shape." #verificacar se os shapes são iguais
    gray_image1 = rgb2gray(image1) #conversão de imagem para tons de cinza
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True) # achar o score(entre 0 e 1) e a diferença entre as duas imagens    
    print("Similarity of the images:", score) 
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    return normalized_difference_image #normalizando para ficar mais facil a vizualizacao da != das imagens

def transfer_histogram(image1, image2): #Transferencia de histograma
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image
    
