import tensorflow as tf

from rexify.models.tower import TowerModel


class QueryModel(TowerModel):
    """Tower model responsible for computing the query representations

    Args:
        user_id (str): the user ID feature
        n_users (str): number possible values for the ID feature
        embedding_dim (int): output dimension of the embedding layer
        output_layers (list): number of neurons in each layer for the output model
        feature_layers (list): number of neurons in each layer for the feature model

    Examples:

    >>> from rexify.models.query import QueryModel
    >>> model = QueryModel('user_id', 15)
    >>> model({"user_id": tf.constant([1]), "user_features": tf.constant([[1, 1]]), "context_features": tf.constant([[1]])})
    <tf.Tensor: shape=(1, 32), dtype=float32, numpy=
    array([[...]], dtype=float32)>
    """

    def __init__(
        self,
        user_id: str,
        n_users: int,
        n_items: int,
        embedding_dim: int = 32,
        output_layers: list[int] = None,
        feature_layers: list[int] = None,
        recurrent_layers: list[int] = None,
        sequential_dense_layers: list[int] = None,
    ):
        super().__init__(user_id, n_users, embedding_dim, output_layers, feature_layers)
        self._n_items = n_items
        self._recurrent_layers = recurrent_layers or [32] * 2
        self._sequential_dense_layers = sequential_dense_layers or []
        self.sequential_model = self._get_sequential_model(
            n_items,
            embedding_dim,
            self._recurrent_layers,
            self._sequential_dense_layers,
        )

    def call(self, inputs: dict[str, tf.Tensor]) -> tf.Tensor:
        x = self.embedding_layer(inputs[self._id_feature])

        features = []
        if inputs["user_features"].shape[-1] != 0:
            features.append(inputs["user_features"])

        if inputs["context_features"].shape[-1] != 0:
            features.append(inputs["context_features"])

        if "history" in inputs.keys():
            sequential_embedding = self.sequential_model(inputs["history"])
            x = tf.concat([x, sequential_embedding], axis=1)

        if len(features) != 0:
            features = tf.concat(features, axis=1) if len(features) > 1 else features[0]
            feature_embedding = self.feature_model(features)
            x = tf.concat([x, feature_embedding], axis=1)
        else:
            self.feature_model.build(input_shape=tf.TensorShape([]))

        x = self.output_model(x)
        return x

    def get_config(self):
        config = super().get_config()
        config["user_id"] = self._id_feature
        config["n_users"] = self._n_dims
        config["n_items"] = self._n_items
        return config

    @staticmethod
    def _get_sequential_model(item_dims, embedding_dim, recurrent_layers, dense_layers):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Embedding(item_dims, embedding_dim))
        for num_neurons in recurrent_layers[:-1]:
            model.add(tf.keras.layers.LSTM(num_neurons, return_sequences=True))
        model.add(tf.keras.layers.LSTM(recurrent_layers[-1]))
        for num_neurons in dense_layers:
            model.add(tf.keras.layers.Dense(num_neurons))
        return model
