import numpy as np
from skimage.color import rgb2gray

class Preprocessing:

    """Classe destinada ao pré-processamento de imagens.

    Esta classe fica responsável por realizar o pré-processamento das imagens do dataset.

    Methods
    -------
    normalize(dataset)
        Normaliza as imagens de um dataset.
    label_encoder(names, class1, class2)
        Codifica as classes de um dataset.
    to_gray(dataset)
        Transforma as imagens de um dataset para tons de cinza.
    convert_to_integer(dataset)
        Converte as imagens de um dataset para inteiro.
    contrast_flare(dataset, k, e)
        Aplica o efeito flare nas imagens de um dataset.
    negatives(dataset)
        Aplica o efeito negativo nas imagens de um dataset.
    log_transform(dataset, c)
        Aplica a transformação logarítmica nas imagens de um dataset.
    gamma_transform(dataset, c, g)
        Aplica a transformação gamma nas imagens de um dataset.
    """

    @staticmethod
    def normalize(dataset):
        """Normaliza os valores de um dataset.

        Parameters
        ----------
        dataset : Array numpy 
            Lista com imagens 2D-dimensional.

        Returns
        -------
            Dataset normalizado.
        """
        normalized = []

        for img in dataset:
            normalized.append((img - np.min(img)) / (np.max(img) - np.min(img)))

        return np.asarray(normalized)

    @staticmethod
    def label_encoder(names, class_1, class_2):
        """Codifica os valores de um dataset entre 0 e 1.

        Parameters
        ----------
        names : Array numpy 
            Dataset com o nome das classes de cada imagem.
        class_1 : String
            Nome da primeira classe.
        class_2 : String
            Nome da segunda classe.

        Returns
        -------
            Dataset codificado.
        """
        encoded = []

        for name in names:
        
            if name.lower() == class_1.lower():
                encoded.append([1])

            elif name.lower() == class_2.lower():
                encoded.append([0])

        return np.asarray(encoded)

    @staticmethod
    def to_gray(dataset):
        """Converte um dataset de imagens RGB para escala de cinza.

        Parameters
        ----------
        dataset : Array numpy 
            Lista com imagens 3D-dimensional.

        Returns
        -------
            Dataset convertido.
        """
        gray = []

        for img in dataset:
            gray.append((rgb2gray(img)))

        return np.asarray(gray)

    @staticmethod
    def convert_to_integer(dataset):
        """Converte um dataset de imagens float para int entre 0 e 255.

        Parameters
        ----------
        dataset : Array numpy 
            Dataset com imagens 2D-dimensional.

        Returns
        -------
            Dataset convertido.
        """
        integer = []

        for img in dataset:
            integer.append((img*255).astype(np.uint8))

        return np.asarray(integer)

    @staticmethod
    def contrast_flare(dataset, k, e):
        """Aplica o alargamento de contraste nas imagens de um dataset.

        Parameters
        ----------
        dataset : Array numpy 
            Lista com imagens 2D-dimensional no intervalo de 0 a 255.
        k : Float
            Valor de constante.
        e : Float
            Valor de expoente.
        
        Returns
        -------
            Dataset com imagens com o efeito flare.
        """
        contrast = []
        for img in dataset:
            contrast.append(1/(1+(k/img)**e))
        
        return np.asarray(contrast)

    @staticmethod
    def negatives(dataset):
        """Aplica o negativo nas imagens de um dataset.

        Parameters
        ----------
        dataset : Array numpy 
            Dataset com imagens 2D-dimensional no intervalo de 0 a 255.

        Returns
        -------
            Lista com imagens 2D-dimensional com o efeito negativo.
        """
        negatives = []
        for img in dataset:
            negatives.append(255-img)
        
        return np.asarray(negatives)

    def log_transform(dataset, c):
        """Aplica a transformação logarítmica nas imagens de um dataset.

        Parameters
        ----------
        dataset : Array numpy
            Lista com imagens 2D-dimensional.
        c : Float
            Valor de constante.

        Returns
        -------
            Dataset com imagens com o efeito logarítmico.
        """
        log = []
        for img in dataset:
            log.append(c*np.log(1+img))
        
        return np.asarray(log)

    def gamma_transform(dataset, c, g):
        """Aplica a transformação gamma nas imagens de um dataset.

        Parameters
        ----------
        dataset : Array numpy
            Lista com imagens 2D-dimensional.
        c : Float
            Valor de constante.
        g : Float
            Valor de gamma.
        
        Returns
        -------
            Dataset com imagens com o efeito gamma.
        """
        gamma = []
        for img in dataset:
            gamma.append(c*(img**g))
        
        return np.asarray(gamma)

    