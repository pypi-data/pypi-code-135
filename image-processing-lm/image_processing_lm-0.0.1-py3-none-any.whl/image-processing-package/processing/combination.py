#Combinação das Imagens

import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histogrtams
from skimage.metrics import structural_similarity

def find_difference (image1, image2): # achando a diferença entre duas imagens
    assert image1.shape == image2.shape , "Specify 2 images with the same shape" 
        #verificando se as imagens estão com a mesma dimensão
    gray_image1 = rgb2gray(image1) 
    gray_image2 = rgb2gray(image2)
        # Convertendo as imagens para os tons de cinxza
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full = True)
        # Encontrando o valor do score = taxa de semelhança entre as imagens (0,1) e a imageme de diferença entre as duas imagens
    print("Similarity of the images:", score)
    normalized_difference_image = ( difference_image - np.min(difference_image))/(np.max(difference_image) - np.min(difference_image))
        #Normalizando a diferença de imagem
    return normalized_difference_image

def transfer_histogram (image1, image2):
    matched_image = match_histogrtams(image1, image2, multichannel = True)
    return matched_image