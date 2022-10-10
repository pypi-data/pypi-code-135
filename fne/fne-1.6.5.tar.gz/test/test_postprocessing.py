import unittest

import torch
from torch.utils.data import DataLoader
from torchvision.models.vgg import vgg11

from test.resources.imagedataset_torch import TrainImageDataset
from fne.fne_torch import FullNetworkEmbedding, L2Norm


class TestPostprocessing(unittest.TestCase):
    def setUp(self) -> None:
        self.model = vgg11()
        self.features = torch.tensor(
            [[0.1, 0.2, -0.3, 0.5],
             [-0.6, 0.5, 0.4, 0.1]]
        )
        self.train_data = DataLoader(TrainImageDataset(), batch_size=2, shuffle=False)

    def test_fne_standarize(self):
        fne = FullNetworkEmbedding(
            self.model,
            [],
            None
        )
        fne._means = torch.mean(self.features, 0)
        fne._stds = torch.std(self.features, 0)
        torch.testing.assert_close(
            fne._standarize(self.features, train=False),
            torch.Tensor([[0.7071, -0.7071, -0.7071, 0.7071],
                          [-0.7071, 0.7071, 0.7071, -0.7071]])
        )

    def test_fne_standarize_train(self):
        fne = FullNetworkEmbedding(
            self.model,
            [],
            None
        )
        torch.testing.assert_close(
            fne._standarize(self.features),
            torch.Tensor([[0.7071, -0.7071, -0.7071, 0.7071],
                          [-0.7071, 0.7071, 0.7071, -0.7071]])
        )

    def test_fne_standarize_train_saves_mean_and_std(self):
        fne = FullNetworkEmbedding(
            self.model,
            [],
            None
        )
        _ = fne._standarize(self.features)
        torch.testing.assert_close(
            fne._means,
            torch.tensor([-0.25, 0.35, 0.05, 0.3])
        )
        torch.testing.assert_close(
            fne._stds,
            torch.tensor([0.49497475, 0.21213203, 0.49497475, 0.28284271])
        )

    def test_fne_discretize(self):
        fne = FullNetworkEmbedding(
            self.model,
            [],
            None
        )
        torch.testing.assert_close(
            fne._discretize(self.features),
            torch.tensor([[0, 1, -1, 1],
                          [-1, 1, 1, 0]],
                         dtype=torch.int64)
        )

    def test_l2_postprocess(self):
        l2 = L2Norm(
            self.model,
            [],
            None
        )
        torch.testing.assert_close(
            l2._postprocess(self.features),
            torch.tensor([[0.16012815, 0.32025631, -0.48038446, 0.80064077],
                          [-0.67936622, 0.56613852, 0.45291081, 0.1132277]])
        )

    def test_l2_postprocess_l2norm_is_actually_1(self):
        l2 = L2Norm(
            self.model,
            [],
            None
        )
        features = l2._postprocess(self.features)
        torch.testing.assert_close(
            torch.tensor([1, 1], dtype=torch.float32),
            torch.tensor([torch.norm(features[0], p=2),
                          torch.norm(features[1], p=2)]),
        )

    def test_fne_postprocessing_equal_shape(self):
        fne = FullNetworkEmbedding(
            self.model,
            [],
            None
        )
        self.assertEqual(
            self.features.shape,
            fne._postprocess(self.features).shape
        )

    def test_l2_postprocessing_equal_shape(self):
        l2 = L2Norm(
            self.model,
            [],
            None
        )
        self.assertEqual(
            self.features.shape,
            l2._postprocess(self.features).shape
        )


if __name__ == '__main__':
    unittest.main()
