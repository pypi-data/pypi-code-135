import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def achar_diferenca(imagem1, imagem2):
    assert imagem1.shape == imagem2.shape, "Especifique 2 imagens com o mesmo formato"
    gray_imagem1 = rgb2gray(imagem1)
    gray_imagem2 = rgb2gray(imagem2)
    (score, diferenca_imagem) = structural_similarity(
        gray_imagem1, gray_imagem2, full=True)
    print("Similaridade entre as imagens:", score)
    diferenca_imagem_normalizada = (diferenca_imagem-np.min(diferenca_imagem))/(
        np.max(diferenca_imagem)-np.min(diferenca_imagem))
    return diferenca_imagem_normalizada


def transferir_histograma(imagem1, imagem2):
    combinacao = match_histograms(imagem1, imagem2, multichannel=True)
    return combinacao
