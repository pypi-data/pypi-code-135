from abc import abstractmethod
from typing import Iterable, Callable, Union

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision.transforms import TenCrop


class FeatureExtractor(nn.Module):
    def __init__(self, model: nn.Module, layers: Iterable[str], classifier):
        super(FeatureExtractor, self).__init__()
        self.model = model
        self.layers = layers
        self.classifier = classifier

        self._one_batch_features = torch.Tensor()
        self._all_features = torch.Tensor()

        for layer_name in self.layers:
            layer = dict([*self.model.named_modules()])[layer_name]
            layer.register_forward_hook(self._save_outputs_hook(layer))

    def _save_outputs_hook(self, layer) -> Callable:
        def _function_extract_conv2d_layer(_, __, output):
            batch_dim, channel_dim, height_dim, width_dim = 0, 1, 2, 3
            # Performs a channel-wise 2d average pooling
            features = output.mean((height_dim, width_dim))
            features = torch.squeeze(features)
            self._one_batch_features = torch.cat((self._one_batch_features, features), channel_dim)

        def _function_extract_linear_layer(_, __, output):
            batch_dim, channel_dim = 0, 1
            self._one_batch_features = torch.cat((self._one_batch_features, output), channel_dim)

        if isinstance(layer, nn.Conv2d):
            return _function_extract_conv2d_layer
        elif isinstance(layer, nn.Linear):
            return _function_extract_linear_layer
        else:
            raise NotImplementedError

    def _extract_features(self, data: DataLoader, train=True, with_crops=False, crop_size=None):
        def _extract_features_of_one_batch(batch):
            batch_dim, feature_dim = 0, 1
            self.model(batch)
            self._all_features = torch.cat((self._all_features, self._one_batch_features), batch_dim)
            self._one_batch_features = torch.Tensor()

        self._all_features = torch.Tensor()
        self._one_batch_features = torch.Tensor()
        if train:
            labels = torch.Tensor()

        if with_crops:
            for x, y in data:
                x = self._compute_crops(x, crop_size)
                # Returns a list of one element for some reason
                # Element is tensor of shape (bs, ch, h, w)
                crop_loader = DataLoader(TensorDataset(x), batch_size=data.batch_size, shuffle=False)
                for crop_x in crop_loader:
                    _extract_features_of_one_batch(crop_x[0])
                if train:
                    labels = torch.cat((labels, torch.tensor([10 * [label] for label in y]).view(-1)))
        else:
            for x, y in data:
                _extract_features_of_one_batch(x)
                if train:
                    labels = torch.cat((labels, y))

        return self._all_features, labels if train else None

    @staticmethod
    def _compute_crops(batch, crop_size: Union[int, Iterable[int]]):
        crops = TenCrop(crop_size, vertical_flip=False)(batch)

        crops = torch.stack([c for c in crops])

        crop_dim, batch_dim, channel_dim, height_dim, width_dim = 0, 1, 2, 3, 4
        crops = crops.permute(batch_dim, crop_dim, channel_dim, height_dim, width_dim)

        batch_size, crop_amount, _, _, _ = crops.shape
        crops = crops.reshape((batch_size * crop_amount, *crops.shape[channel_dim:]))

        return crops

    def fit(self, train_data: DataLoader, with_crops=False, crop_size=None):
        with torch.no_grad():
            features, labels = self._extract_features(train_data, train=True,
                                                      with_crops=with_crops, crop_size=crop_size)

            features = self._postprocess(features, train=True)
            features = features.numpy() if features.device.type == 'cpu' else features.cpu().numpy()
            labels = labels.numpy() if labels.device.type == 'cpu' else labels.cpu().numpy()

        self.classifier.fit(features, labels)

    def predict(self, test_data: DataLoader, with_crops=False, crop_size=None):
        with torch.no_grad():
            features, _ = self._extract_features(test_data, train=False,
                                                 with_crops=with_crops, crop_size=crop_size)

            features = self._postprocess(features, train=False)
            features = features.numpy() if features.device.type == 'cpu' else features.cpu().numpy()

        predicted = self.classifier.predict(features)
        if with_crops:
            predicted = predicted.reshape((-1, 10))
        return predicted

    @abstractmethod
    def _postprocess(self, features, train=True):
        pass


class FullNetworkEmbedding(FeatureExtractor):
    def __init__(self, model: nn.Module, layers: Iterable[str], classifier):
        super(FullNetworkEmbedding, self).__init__(model, layers, classifier)

        self.f_plus = 0.15
        self.f_minus = -0.25

    def _standarize(self, features, train=True):
        if train:
            self._means = torch.mean(features, 0)
            self._stds = torch.std(features, 0)
        features: torch.Tensor = (features - self._means) / self._stds
        return features

    def _discretize(self, features):
        return torch.bucketize(features, torch.Tensor([self.f_minus, self.f_plus])) - 1

    def _postprocess(self, features, train=True):
        features = self._standarize(features, train=train)
        features = self._discretize(features)
        return features


class L2Norm(FeatureExtractor):
    def __init__(self, model: nn.Module, layers: Iterable[str], classifier):
        super(L2Norm, self).__init__(model, layers, classifier)

    def _postprocess(self, features, train=True):
        # Instance-wise L2 normalization
        feature_wise, instance_wise = 0, 1
        return torch.nn.functional.normalize(features, p=2, dim=instance_wise)
