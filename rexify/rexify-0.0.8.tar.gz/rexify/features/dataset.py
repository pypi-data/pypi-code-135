from abc import abstractmethod
from typing import Callable

import numpy as np
import tensorflow as tf

from rexify.features.base import HasSchemaInput
from rexify.utils import get_first, get_target_id


class TFDatasetGenerator(HasSchemaInput):
    def make_dataset(self, X) -> tf.data.Dataset:
        feature_names = self._get_feature_names_out()

        ratings_idx = self._get_ratings_features_idx(feature_names)
        sequential_idx = self._get_sequential_feature_idx(feature_names)

        features = X[
            :,
            ~np.in1d(
                np.array(list(range(X.shape[1]))),
                np.concatenate([ratings_idx, sequential_idx]),
            ),
        ]
        ratings = X[:, ratings_idx]
        sequential = np.stack(X[:, sequential_idx].reshape(-1).tolist()).reshape(
            (-1, 3)
        )

        features = self._get_features_dataset(features)
        sequential = tf.data.Dataset.from_tensor_slices(sequential)
        ratings = self._get_ratings_dataset(ratings)
        ds = self._concatenate(features, ratings, sequential)
        return ds

    def _get_features_dataset(self, features):
        ds = tf.data.Dataset.from_tensor_slices(features.astype(float))
        ds = ds.map(self._get_header_fn())
        return ds

    @staticmethod
    def _get_ratings_dataset(x: np.ndarray) -> tf.data.Dataset:
        return tf.data.Dataset.zip(
            (
                tf.data.Dataset.from_tensor_slices(x[:, 0]),
                tf.data.Dataset.from_tensor_slices(x[:, 1].astype(float)),
            )
        )

    @staticmethod
    def _concatenate(
        features: tf.data.Dataset, ratings: tf.data.Dataset, sequential: tf.data.Dataset
    ):
        def concatenate(x: dict, event_rating: tuple, sequences):
            event_type, rating = event_rating
            x["event_type"] = event_type
            x["rating"] = rating
            x["query"]["history"] = sequences
            return x

        return tf.data.Dataset.zip((features, ratings, sequential)).map(concatenate)

    def _get_header_fn(self):
        user_id = get_target_id(self.schema, "user")[0]
        item_id = get_target_id(self.schema, "item")[0]

        (
            user_id_idx,
            user_features_idx,
            item_id_idx,
            item_features_idx,
            context_features_idx,
        ) = self._get_indices()

        def add_header(x):
            header = {
                "query": {
                    user_id: tf.gather(x, user_id_idx)[0],
                },
                "candidate": {
                    item_id: tf.gather(x, item_id_idx)[0],
                },
            }

            header["query"]["user_features"] = (
                tf.gather(x, user_features_idx)
                if len(user_features_idx) != 0
                else tf.constant([])
            )

            header["query"]["context_features"] = (
                tf.gather(x, context_features_idx)
                if len(context_features_idx) != 0
                else tf.constant([])
            )

            header["candidate"]["item_features"] = (
                tf.gather(x, item_features_idx)
                if len(item_features_idx) != 0
                else tf.constant([])
            )

            return header

        return add_header

    def _get_indices(self):
        feature_names = self._get_feature_names_out()
        feature_names = np.delete(
            feature_names, self._get_sequential_feature_idx(feature_names)
        )
        feature_names = np.delete(
            feature_names, self._get_ratings_features_idx(feature_names)
        )

        pipeline_split = self._filter_array(feature_names, lambda x: x.split("_"))
        target_feature_names = self._filter_array(pipeline_split, get_first)

        def get_target_indices(target):
            feature_mask = target_feature_names == target
            target_idx = np.array([])
            if (target == "user") or (target == "item"):
                target_id = get_target_id(self._schema, target)[0]
                target_idx = np.argwhere(
                    np.array([target_id in feat for feat in feature_names], dtype=bool)
                ).reshape(-1)
            features_idx = np.argwhere(feature_mask).reshape(-1)
            return target_idx, features_idx

        user_ids, user_features = get_target_indices("user")
        item_ids, item_features = get_target_indices("item")
        context_features = np.argwhere(target_feature_names == "context").reshape(-1)

        return (
            user_ids,
            user_features,
            item_ids,
            item_features,
            context_features,
        )

    @abstractmethod
    def _get_feature_names_out(self) -> list[str]:
        pass

    @staticmethod
    def _filter_array(array: np.ndarray | list, fn: Callable):
        return np.array([fn(x) for x in array], dtype=object)

    @staticmethod
    def _get_ratings_features_idx(feature_names: list[str]):
        mask = [
            [feat in feature_name for feature_name in feature_names]
            for feat in ["event_type", "rating"]
        ]
        return np.argwhere(mask)[:, 1]

    @staticmethod
    def _get_sequential_feature_idx(feature_names: list[str]):
        return np.argwhere(["history" in feat for feat in feature_names]).reshape(-1)
