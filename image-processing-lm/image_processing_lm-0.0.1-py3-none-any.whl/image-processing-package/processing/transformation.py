# Transformação para uma imagem

from skimage.transform import resize

def resize_image(image, proportion):
        #Passa uma imgaem e uma proporção (0,1)
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1"
    height = round(image.shape[0] * proportion)
        #Altura
    width = round(image.shape[1] * proportion)
        #Largura
            #Como a função resize só aceita valor inteiro, utilizamos o round para retirar somente o valor inteiro
    image_resized = resize(image,(height,width), anti_aliasing = True)
    return image_resized