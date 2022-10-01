""" test: jouissance.tf.arch """

import os

if os.environ.get("PDGM_BACK", "tf") in ["tf", "cf", "jx"]:
    import tensorflow as tf

    from jouissance.tf import set_initializer
    from jouissance.tf import upsample_block, downsample_block
    from jouissance.tf import dense_disc, unet_model


def test_set_initializer():
    """ test: set the initializer """
    if os.environ.get("PDGM_BACK", "tf") == "pt":
        return
    assert set_initializer().mean == 0.
    assert set_initializer().stddev == 0.02


def test_upsample_block():
    """ test: an upsampling block """
    if os.environ.get("PDGM_BACK", "tf") == "pt":
        return
    result = upsample_block(
        filters=64, size=3, strides=2, drop_rate=0.0, act="normal",
    )
    assert result(
        tf.random.normal(shape=(1, 1, 1, 1))
    ).shape == (1, 2, 2, 1)


def test_downsample_block():
    """ test: a downsampling block """
    if os.environ.get("PDGM_BACK", "tf") == "pt":
        return
    result = downsample_block(
        filters=64, size=3, strides=2, drop_rate=0.0, apply_batchnorm=True,
    )
    assert result(
        tf.random.normal(shape=(1, 32, 64, 128))
    ).shape == (1, 16, 32, 64)


def test_dense_disc():
    """ test: dense disc """
    if os.environ.get("PDGM_BACK", "tf") == "pt":
        return
    scenes = tf.random.normal(shape=(5, 32, 64, 1))
    conditions = tf.random.normal(shape=(5, 32, 64, 5))
    disc = dense_disc(
        scenes_shape=scenes.shape[1:],
        conditions_shape=conditions.shape[1:],
    )
    assert disc([conditions, scenes]).shape == (5, 1)
    scenes = tf.random.normal(shape=(5, 64, 128, 1))
    conditions = tf.random.normal(shape=(5, 32, 64, 5))
    disc = dense_disc(
        scenes_shape=scenes.shape[1:],
        conditions_shape=conditions.shape[1:],
    )
    assert disc([conditions, scenes]).shape == (5, 1)


def test_unet_model():
    """ test: unet model """
    if os.environ.get("PDGM_BACK", "tf") == "pt":
        return
    scenes = tf.random.normal(shape=(5, 32, 64, 1))
    conditions = tf.random.normal(shape=(5, 32, 64, 5))
    unet_no_latent = unet_model(
        scenes_shape=scenes.shape[1:],
        conditions_shape=conditions.shape[1:],
        use_latent=False,
    )
    unet_latent = unet_model(
        scenes_shape=scenes.shape[1:],
        conditions_shape=conditions.shape[1:],
        use_latent=True,
    )
    assert unet_no_latent(conditions).shape == scenes.shape
    assert unet_latent([conditions, conditions]).shape == scenes.shape


def test_unet_shapes():
    """ test: unet model """
    if os.environ.get("PDGM_BACK", "tf") == "pt":
        return
    conditions = [
        (2**idx, 2**(jdx+1), 9) for idx, jdx in zip(range(2, 7), range(2, 7))
    ]
    scenes = [
        (2**idx, 2**(jdx+1), 3) for idx, jdx in zip(range(2, 7), range(2, 7))
    ]

    for idx, con in enumerate(conditions):
        for sce in scenes[idx:]:
            csample = tf.random.normal(shape=(5, con[0], con[1], 9))
            ssample = tf.random.normal(shape=(5, sce[0], sce[1], 3))
            unet_latent = unet_model(
                scenes_shape=sce,
                conditions_shape=con,
                use_latent=True
            )
            unet_no_latent = unet_model(
                scenes_shape=sce,
                conditions_shape=con,
                use_latent=False
            )
            assert unet_no_latent(csample).shape == ssample.shape
            assert unet_latent([csample, csample]).shape == ssample.shape
