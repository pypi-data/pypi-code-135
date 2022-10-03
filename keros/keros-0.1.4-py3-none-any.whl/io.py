import glob
from .dataset import dataset

class Io:
    """Classe para leitura de imagens do dataset.

    Esta classe fica responsável por ler as imagens do dataset e retornar um objeto dataset.

    Methods
    -------
    read(path, batch_size=10)
        Lê um conjunto de imagens de um diretório.
    """

    def read(path, batch_size=10):
        """Lê um conjunto de imagens de um diretório.

        Parameters
        ----------
        path : str
            Diretório do dataset.
        batch_size : int 
            Tamanho do lote de imagens.

        Returns
        -------
            Objeto dataset.
        """
        batchs = {}
        files = glob.glob(path)

        if len(files) < batch_size:
            raise Exception("O tamanho do lote é maior que o número de imagens no diretório.")

        count = 0
        for batch in range(0, len(files), batch_size):
            batchs[str(count)] = files[batch:batch+batch_size]

            count += 1

        return dataset(batchs)

        

        


