import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score

class Tools:

    """Esta classe tem como objetivo facilitar a criação de modelos e a avaliação deles.
    
    Esta classe permite salvar e carregar modelos, além de calcular métricas de avaliação.

    Methods
    -------
    metrics(y_true, y_pred)
        Calcula as métricas de avaliação.
    save(model, filename)
        Salva um modelo em um arquivo.
    load(filename)
        Carrega um modelo de um arquivo.
    """

    @staticmethod
    def metrics(y_true, y_pred):
        """Calcula as métricas de acurácia, precisão, recall, f1 e kappa.

        Parameters
        ----------
        y_true : Array numpy
            Array com os valores reais.
        y_pred : Array numpy
            Array com os valores preditos.
        
        Returns
        -------
            Retorna as métricas de avaliação.
        """
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        kappa = cohen_kappa_score(y_true, y_pred)

        return accuracy, precision, recall, f1, kappa

    @staticmethod
    def save(model, filename):
        """Salva o modelo em um arquivo pkl.

        Parameters
        ----------
        model : Objeto model
            Rede neural.
        filename : str
            path do arquivo.
        """
        with open(filename, 'wb') as f:
            pickle.dump(model, f)

    @staticmethod
    def load(filename):
        """Carrega o modelo salvo.

        Parameters
        ----------
        filename : str 
            Path com o caminho para o modelo.
        """
        with open(filename, 'rb') as f:
            return pickle.load(f)
