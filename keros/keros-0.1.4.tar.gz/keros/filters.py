import numpy as np

class Filters:

    """Classe destinada para aplicação de filtros em imagens.

    Esta classe aplica filtros espaciais, que levam em conta os pixels da vizinhança.

    Methods
    -------
    conv2d(img, kernel)
        Aplica um filtro convolucional em uma imagem.
    vertical_sobel(img)
        Aplica o filtro de Sobel vertical em uma imagem.
    horizontal_sobel(img)
        Aplica o filtro de Sobel horizontal em uma imagem.
    laplace(img)
        Aplica o filtro de Laplace em uma imagem.
    horizontal_prewitt(img)
        Aplica o filtro de Prewitt horizontal em uma imagem.
    vertical_prewitt(img)
        Aplica o filtro de Prewitt vertical em uma imagem.
    horizontal_scharr(img)
        Aplica o filtro de Scharr horizontal em uma imagem.
    vertical_scharr(img)
        Aplica o filtro de Scharr vertical em uma imagem.
    median(img, kernel_size)
        Aplica o filtro mediana em uma imagem.
    maximum(img, kernel_size)
        Aplica o filtro máximo em uma imagem.
    minimum(img, kernel_size)
        Aplica o filtro mínimo em uma imagem.
    mean(img, kernel_size)
        Aplica o filtro média em uma imagem.
    """

    @staticmethod
    def conv2d(img, kernel):
        """Aplica um filtro convolucional em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        kernel : Array numpy
            Kernel 2D-dimensional.

        Returns
        -------
            Imagem filtrada.
        """
        # Aplica o filtro convolucional
        #Aplicando a convolucao na imagem.
        Filters._check_dimensions(img)
        Filters._check_dimensions_kernel(kernel)
        
        new_pixels = np.zeros(img.shape)
        bord = int(np.floor(kernel.shape[0]/2))

        for lines in range(img.shape[0] - (kernel.shape[0]-1)):
            for columns in range(img.shape[1] - (kernel.shape[1]-1)):
                new_pixels[lines + bord][columns + bord] = np.sum(kernel*img[lines:lines+kernel.shape[0], columns:columns+kernel.shape[1]])

        return new_pixels

    @staticmethod
    def vertical_sobel(img):
        """Aplica o filtro de Sobel em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.

        Returns
        -------
            Imagem com o filtro sobel vertical aplicado.
        """
        # Aplica o filtro de Sobel
        kernel = np.array([[-1, 0, 1], 
                           [-2, 0, 2], 
                           [-1, 0, 1]])
        sobel = Filters.conv2d(img, kernel)
        return sobel

    @staticmethod
    def horizontal_sobel(img):
        """Aplica o filtro de Sobel em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        
        Returns
        -------
            Imagem com o filtro sobel horizontal aplicado.
        """
        # Aplica o filtro de Sobel
        kernel = np.array([[-1, -2, -1], 
                           [ 0,  0,  0], 
                           [ 1,  2,  1]])
        sobel = Filters.conv2d(img, kernel)
        return sobel

    @staticmethod
    def laplace(img):
        """Aplica o filtro de Laplace em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        
        Returns
        -------
            Imagem com o filtro laplace aplicado.
        """
        # Aplica o filtro de Laplace
        kernel = np.array([[0,  1, 0], 
                           [1, -4, 1], 
                           [0,  1, 0]])
        laplace = Filters.conv2d(img, kernel)
        return laplace

    @staticmethod
    def horizontal_prewitt(img):
        """Aplica o filtro de Prewitt em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        
        Returns
        -------
            Imagem com o filtro prewitt horizontal aplicado.
        """
        # Aplica o filtro de Prewitt
        kernel = np.array([[ 1/3,   1/3,   1/3], 
                           [   0,     0,     0], 
                           [-1/3,  -1/3,  -1/3]])
        prewitt = Filters.conv2d(img, kernel)
        return prewitt

    @staticmethod
    def vertical_prewitt(img):
        """Aplica o filtro de Prewitt em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        
        Returns
        -------
            Imagem com o filtro prewitt vertical aplicado.
        """
        # Aplica o filtro de Prewitt
        kernel = np.array([[ 1/3,     0,  -1/3], 
                           [ 1/3,     0,  -1/3], 
                           [ 1/3,     0,  -1/3]])
        prewitt = Filters.conv2d(img, kernel)
        return prewitt

    @staticmethod
    def horizontal_scharr(img):
        """Aplica o filtro de Scharr em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        
        Returns
        -------
            Imagem com o filtro scharr horizontal aplicado.
        """
        # Aplica o filtro de Scharr
        kernel = np.array([[ 3,  10,  3], 
                           [ 0,   0,  0], 
                           [-3, -10, -3]])
        scharr = Filters.conv2d(img, kernel)
        return scharr
    
    @staticmethod
    def vertical_scharr(img):
        """Aplica o filtro de Scharr em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        
        Returns
        -------
            Imagem com o filtro scharr vertical aplicado.
        """
        # Aplica o filtro de Scharr
        kernel = np.array([[ 3,  0,  -3], 
                           [10,  0, -10], 
                           [ 3,  0,  -3]])
        scharr = Filters.conv2d(img, kernel)
        return scharr

    @staticmethod
    def median(img, kernel_size):
        """Aplica o filtro de mediana em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        kernel_size : int
            Tamanho do kernel.
        
        Returns
        -------
            Imagem com o filtro mediana aplicado.
        """
        # Aplica o filtro de mediana
        median = Filters._convNoLinear(img, kernel_size, 'median')
        return median 

    @staticmethod
    def maximum(img, kernel_size):
        """Aplica o filtro de máximo em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        kernel_size : int
            Tamanho do kernel.
        
        Returns
        -------
            Imagem com o filtro máximo aplicado.
        """
        # Aplica o filtro de máximo
        maximum = Filters._convNoLinear(img, kernel_size, 'max')
        return maximum

    @staticmethod
    def minimum(img, kernel_size):
        """Aplica o filtro de mínimo em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        kernel_size : int
            Tamanho do kernel.

        Returns
        -------
            Imagem com o filtro mínimo aplicado.
        """
        # Aplica o filtro de mínimo
        minimum = Filters._convNoLinear(img, kernel_size, 'min')
        return minimum
    
    @staticmethod
    def mean(img, kernel_size):
        """Aplica o filtro de média em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        kernel_size : int
            Tamanho do kernel.
        
        Returns
        -------
            Imagem com o filtro média aplicado.
        """
        # Aplica o filtro de média
        mean = Filters._convNoLinear(img, kernel_size, 'mean')
        return mean

    def _convNoLinear(img, kernel_shape, operation):
        """Aplica um filtro convolucional não linear em uma imagem.

        Parameters
        ----------
        img : Array numpy
            Imagem 2D-dimensional no intervalo de 0 a 255.
        kernel_shape : int
            Tamanho do kernel.
        operation : str
            Operação a ser realizada no kernel.

        Returns
        -------
            Imagem com o filtro convolucional não linear aplicado.
        """
        operations = {
            'max': np.max,
            'min': np.min,
            'mean': np.mean,
            'median': np.median
        }

        if kernel_shape % 2 == 0:
            raise ValueError('O tamanho do kernel deve ser ímpar.')

        Filters._check_dimensions(img)
        
        new_pixels = np.zeros(img.shape)
        bord = int(np.floor(kernel_shape/2))

        for lines in range(img.shape[0] - (kernel_shape-1)):
            for columns in range(img.shape[1] - (kernel_shape-1)):
                new_pixels[lines + bord][columns + bord] = operations[operation](img[lines:lines+kernel_shape, columns:columns+kernel_shape])

        return new_pixels
    
    def _check_dimensions(img):
        if len(img.shape) == 2:
            return True
        else:
            raise Exception("A imagem deve ser 2D-dimensional.")

    def _check_dimensions_kernel(kernel):
        if len(kernel.shape) == 2 and kernel.shape[0] == kernel.shape[1] and kernel.shape[0] % 2 != 0:
            return True
        else:
            raise Exception("O kernel deve ser 2D-dimensional, quadricular e com dimensões impar.")

    
