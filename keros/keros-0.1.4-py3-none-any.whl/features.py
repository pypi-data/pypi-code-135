from skimage.feature import graycomatrix, graycoprops
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

class Features:
    """Esta classe é responsável por extrair as features de um dataset.

    Esta classe extrai as features através da matriz de co-ocorrência de níveis de cinza.

    Methods
    -------
    GLCM(dataset, steps = 1)
        Calcula a matriz de co-ocorrência de níveis de cinza.
    GLCM_props(matrix)
        Calcula as seis propriedades de haralick da matriz de co-ocorrência de níveis de cinza.
    categorize(dataset)
        Categoriza os bits de imagens de um dataset.
    PCA(dataset, n_components = 2)
        Aplica a técnica de redução de dimensionalidade PCA.
    """

    @staticmethod
    def GLCM(dataset, steps = 1):
        """Calcula a matriz de Co-ocorrencia de níveis de cinza de um dataset.

        Parameters
        ----------
        dataset : Array numpy
            Lista com imagens.
        steps : int
            Número de passos para a matriz de co-ocorrência.

        Returns
        -------
            Matriz isotrópica.
        """
        matrix = []

        for img in dataset:
            matrix0 = graycomatrix(img, [steps], [0], normed=True)
            matrix1 = graycomatrix(img, [steps], [np.pi/4], normed=True)
            matrix2 = graycomatrix(img, [steps], [np.pi/2], normed=True)
            matrix3 = graycomatrix(img, [steps], [3*np.pi/4], normed=True)
            matrix.append((matrix0+matrix1+matrix2+matrix3)/4)
        
        return np.asarray(matrix)
    
    @staticmethod
    def GLCM_props(matrix):
        """Calcula as seis propriedades de haralick da matriz de Co-ocorrencia de níveis de cinza.

        Parameters
        ----------
        matrix : Array numpy
            Matriz de co-ocorrência de níveis de cinza.
        
        Returns
        -------
            Matriz com as propriedades de contraste, dissimilaridade, homogeneidade, 
            energia, correlação e ASM.
        """
        props = []

        for mat in matrix:
            prop = np.zeros((6))
            prop[0] = graycoprops(mat,'contrast')
            prop[1] = graycoprops(mat,'dissimilarity')
            prop[2] = graycoprops(mat,'homogeneity')
            prop[3] = graycoprops(mat,'energy')
            prop[4] = graycoprops(mat,'correlation')
            prop[5] = graycoprops(mat,'ASM')
            props.append(prop)
        
        return np.asarray(props)

    @staticmethod
    def categorize(dataset, new_value_bit, old_value_bit):
        """Categoriza os bits de imagens de um dataset.

        Parameters
        ----------
        dataset : Array numpy
            Lista com imagens.
        new_value_bit : int
            Novo valor para o bit.
        old_value_bit : int
            Valor antigo do bit.
        
        Returns
        -------
            Array com as imagens categorizadas.
        """
        categorized = []

        for img in dataset:

            #Guardando as dimensões da imagem original.
            Lines,Columns = img.shape;

            img = np.array(img, dtype=np.float64)

            #Categorizando os bits.
            for line in range(Lines):
                for Colum in range(Columns):
                    img[line, Colum] = (((2**new_value_bit)-1) * img[line, Colum]) // ((2**old_value_bit)-1)

            img = np.array(img, dtype=np.uint8)

            categorized.append(img)

        return np.asarray(categorized)
    @staticmethod
    def PCA(X, n_components):
        """Aplica o algoritmo de redução de dimensionalidade PCA em uma matriz de características.

        Parameters
        ----------
        X : Array numpy
            Matriz de características.
        n_components : int
            Número de componentes principais.
    
        Returns
        -------
            Matriz de características reduzida.
        """
        
        X = StandardScaler().fit_transform(X)

        pca = PCA(n_components=n_components)
        components = pca.fit_transform(X)
        
        return components