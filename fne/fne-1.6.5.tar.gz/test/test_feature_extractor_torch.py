import unittest

import torch
from torch.utils.data import DataLoader
from torchvision.models.vgg import vgg11

from test.resources.imagedataset_torch import TrainImageDataset
from fne.fne_torch import FeatureExtractor


class TestFeatureExtractorTorch(unittest.TestCase):
    def setUp(self) -> None:
        self.model = vgg11()
        self.train_data = DataLoader(TrainImageDataset(), batch_size=2, shuffle=False)

    def test_compute_crops_of_batch(self):
        batch, _ = next(iter(self.train_data))
        crops = FeatureExtractor._compute_crops(batch, crop_size=(224, 224))
        self.assertEqual(
            torch.Size([20, 3, 224, 224]),
            crops.shape
        )

    def test_crops_of_one_image_are_adjacent(self):
        t = torch.zeros((3, 224, 224))
        u = torch.ones((3, 224, 224))
        batch = torch.stack((t, u))
        crops = FeatureExtractor._compute_crops(batch, crop_size=(224, 224))
        self.assertEqual(
            tuple(crops[i][0][0][0] for i in range(len(crops))),
            tuple(10 * [0] + 10 * [1])
        )

    def test_extract_conv2d_features(self):
        fe = FeatureExtractor(
            self.model,
            ['features.11'],
            None
        )
        features, _ = fe._extract_features(self.train_data)
        self.assertEqual(
            torch.Size([4, 512]),
            features.shape
        )

    def test_extract_fc_activation(self):
        fe = FeatureExtractor(
            self.model,
            ['classifier.0'],
            None
        )
        features, _ = fe._extract_features(self.train_data)
        self.assertEqual(
            torch.Size([4, 4096]),
            features.shape
        )

    def test_extract_specified_tensors(self):
        fe = FeatureExtractor(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            None
        )
        features, _ = fe._extract_features(self.train_data)
        self.assertEqual(
            torch.Size([4, 64 + 512 + 4096]),
            features.shape
        )

    def test_extract_features_labels(self):
        fe = FeatureExtractor(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            None
        )
        _, labels = fe._extract_features(self.train_data)
        self.assertEqual(
            torch.Size([4]),
            labels.shape
        )

    def test_extract_features_with_crops(self):
        fe = FeatureExtractor(
            self.model,
            ['features.0', 'features.11'],
            None
        )
        features, _ = fe._extract_features(self.train_data, train=False, with_crops=True, crop_size=(224, 224))
        self.assertEqual(
            torch.Size([40, 576]),
            features.shape
        )


if __name__ == '__main__':
    unittest.main()
