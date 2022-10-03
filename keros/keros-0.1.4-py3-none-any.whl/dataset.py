from skimage.io import imread
import numpy as np

class dataset:
    """Objeto dataset para alocação de imagens em lotes.

    O objeto dataset é responsável por ler os lotes de imagens baseado em seus diretórios.

    Attributes
    ----------
    _files : list
        Lista com todos os diretórios dos arquivos do dataset.
    _batches : dict
        Dicionário com os lotes de diretórios da imagens.
    _n_batches : int
        Número de lotes.
    
    Methods
    -------
    read_batch(batch)
        Lê um lote de imagens do dataset.
    _read_files()
        Lê todos os diretórios dos arquivos do dataset.
    """
    def __init__(self, batches):
        """
        Parameters
        ----------
        batches : dict
            Dicionário com os lotes de diretórios da imagens.
        """
        self._files = []
        self._batches = batches
        self._n_batches = len(batches)
        self._read_files()

    def read_batch(self, batch):
        """Lê um lote de imagens do dataset.

        Parameters
        ----------
            batch : int 
                Id do lote.
        Returns
        -------
            Array numpy contendo as imagens.
        """
        images = []
        for file in self._batches[str(batch)]:
            images.append(imread(file))
        
        return np.asarray(images)


    def _read_files(self):
        """Lê todos os diretórios dos arquivos do dataset.

        Returns
        -------
            Lista com diretórios.
        """
        for batch in self._batches:
            for file in self._batches[batch]:
                self._files.append(file)

        self._files = np.asarray(self._files)

    @property
    def files(self):
        return self._files

    @property
    def n_batches(self):
        return self._n_batches



