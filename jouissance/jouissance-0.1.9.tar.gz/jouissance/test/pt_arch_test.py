""" test: jouissance.pt.arch """

import os

if os.environ.get("PDGM_BACK", "tf") in ["pt", "cf"]:
    import torch
    from jouissance.pt.arch import DownSample, UpSample, DenseDisc, UNetModel


def test_downsample_block():
    """ test: a downsampling block """
    if os.environ.get("PDGM_BACK", "tf") == "tf":
        return
    result = DownSample(
        _in=128, filters=64, size=3, stride=2, drop_rate=0.0, apply_batchnorm=True,
    )
    assert result(
        torch.rand((2, 128, 32, 64))  # pylint: disable=no-member
    ).shape == (2, 64, 16, 32)


def test_upsample_block():
    """ test: an upsampling block """
    if os.environ.get("PDGM_BACK", "tf") == "tf":
        return
    result = UpSample(
        _in=1, stride=2, drop_rate=0.0, act="normal",
    )
    assert result(
        torch.rand((1, 1, 1, 1))  # pylint: disable=no-member
    ).shape == (1, 1, 2, 2)


def test_dense_disc():
    """ test: dense disc """
    # pylint: disable=no-member
    if os.environ.get("PDGM_BACK", "tf") == "tf":
        return
    _con1 = torch.rand((5, 5, 32, 64))
    _sce = torch.rand((5, 1, 64, 128))
    disc1 = DenseDisc(
        scenes_shape=list(_sce.shape[1:]),
        conditions_shape=list(_con1.shape[1:]),
    )
    assert tuple(disc1(_con1, _sce).shape) == (5, 1)
    _con2 = torch.rand((5, 5, 64, 128))
    _sce = torch.rand((5, 1, 64, 128))
    disc2 = DenseDisc(
        scenes_shape=list(_sce.shape[1:]),
        conditions_shape=list(_con2.shape[1:]),
    )
    assert tuple(disc2(_con2, _sce).shape) == (5, 1)


def test_unet_model():
    """ test: unet generator """
    # pylint: disable=no-member
    if os.environ.get("PDGM_BACK", "tf") == "tf":
        return
    scenes = torch.rand((5, 1, 32, 64))
    conditions = torch.rand((5, 5, 32, 64))
    unet_no_latent = UNetModel(
        scenes_shape=scenes.shape[1:],
        conditions_shape=conditions.shape[1:],
        use_latent=False,
    )
    unet_latent = UNetModel(
        scenes_shape=scenes.shape[1:],
        conditions_shape=conditions.shape[1:],
        use_latent=True,
    )
    assert unet_no_latent(conditions).shape == scenes.shape
    assert unet_latent(conditions, conditions).shape == scenes.shape


def test_unet_shapes():
    """ test: unet model """
    # pylint: disable=no-member
    if os.environ.get("PDGM_BACK", "tf") == "tf":
        return
    conditions = [
        (9, 2**idx, 2**(jdx+1)) for idx, jdx in zip(range(2, 7), range(2, 7))
    ]
    scenes = [
        (3, 2**idx, 2**(jdx+1)) for idx, jdx in zip(range(2, 7), range(2, 7))
    ]

    for idx, con in enumerate(conditions):
        for sce in scenes[idx:]:
            csample = torch.rand((5, 9, con[1], con[2]))
            ssample = torch.rand((5, 3, sce[1], sce[2]))
            unet_latent = UNetModel(
                scenes_shape=sce,
                conditions_shape=con,
                use_latent=True
            )
            unet_no_latent = UNetModel(
                scenes_shape=sce,
                conditions_shape=con,
                use_latent=False
            )
            assert unet_no_latent(csample).shape == ssample.shape
            assert unet_latent(csample, csample).shape == ssample.shape
