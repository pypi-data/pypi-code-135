import unittest

from sklearn.svm import LinearSVC
import torch
from torch.utils.data import DataLoader
from torchvision.models import vgg11

from fne.fne_torch import FullNetworkEmbedding, L2Norm
from test.resources.imagedataset_torch import TrainImageDataset, TestImageDataset


class TestFitPredict(unittest.TestCase):
    def setUp(self) -> None:
        self.model = vgg11()
        self.train_data = DataLoader(TrainImageDataset(), batch_size=2, shuffle=False)
        self.test_data = DataLoader(TestImageDataset(), batch_size=2, shuffle=False)

    def test_fne_fit_does_not_break(self):
        fne = FullNetworkEmbedding(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        fne.fit(self.train_data)

    def test_l2_fit_does_not_break(self):
        l2 = L2Norm(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        l2.fit(self.train_data)

    def test_fne_fit_saves_features(self):
        fne = FullNetworkEmbedding(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        fne.fit(self.train_data)
        self.assertEqual(
            torch.Size([4, 64 + 512 + 4096]),
            fne._all_features.shape
        )

    def test_l2_fit_saves_features(self):
        l2 = L2Norm(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        l2.fit(self.train_data)
        self.assertEqual(
            torch.Size([4, 64 + 512 + 4096]),
            l2._all_features.shape
        )

    def test_fne_fit_predict_does_not_break(self):
        fne = FullNetworkEmbedding(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        fne.fit(self.train_data)
        fne.predict(self.test_data)

    def test_l2_fit_predict_does_not_break(self):
        l2 = L2Norm(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        l2.fit(self.train_data)
        l2.predict(self.test_data)

    def test_fne_fit_predict_with_crops_does_not_break(self):
        fne = FullNetworkEmbedding(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        fne.fit(self.train_data)
        fne.predict(self.test_data, with_crops=True, crop_size=(224, 224))

    def test_l2_fit_predict_with_crops_does_not_break(self):
        l2 = L2Norm(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        l2.fit(self.train_data)
        l2.predict(self.test_data, with_crops=True, crop_size=(224, 224))

    def test_fne_fit_predict_predictions_have_correct_shape(self):
        fne = FullNetworkEmbedding(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        fne.fit(self.train_data)
        self.assertEqual(
            (4, ),
            fne.predict(self.test_data).shape
        )

    def test_l2_fit_predict_predictions_have_correct_shape(self):
        l2 = L2Norm(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        l2.fit(self.train_data)
        self.assertEqual(
            (4, ),
            l2.predict(self.test_data).shape
        )

    def test_fne_fit_predict_with_crops_predictions_have_correct_shape(self):
        fne = FullNetworkEmbedding(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        fne.fit(self.train_data)
        self.assertEqual(
            (4, 10),
            fne.predict(self.test_data, with_crops=True, crop_size=(224, 224)).shape
        )

    def test_l2_fit_predict_with_crops_predictions_have_correct_shape(self):
        l2 = L2Norm(
            self.model,
            ['features.0', 'features.11', 'classifier.0'],
            LinearSVC()
        )
        l2.fit(self.train_data)
        self.assertEqual(
            (4, 10),
            l2.predict(self.test_data, with_crops=True, crop_size=(224, 224)).shape
        )


if __name__ == '__main__':
    unittest.main()
