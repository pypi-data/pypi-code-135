""" jouissance.tf.runs """

import tensorflow as tf

from jouissance.util.conf import read_conf

from jouissance.tf.arch import dense_disc, unet_model
from jouissance.tf.loss import genopt, disopt, genloss, disloss
from jouissance.tf.wgan import UNetWGAN
from jouissance.tf.data import make_data


def run_it():
    """ run it """

    configs = read_conf()

    gen_opt = genopt()
    dis_opt = disopt()

    con_shape = (
        int(configs["reanalysis_reshape1"]),
        int(configs["reanalysis_reshape2"]),
        len(configs["reanalysis_products"]) *
        len(configs["reanalysis_levels"])
    )

    sce_shape = (
        int(configs["scene_reshape1"]),
        int(configs["scene_reshape2"]),
        len(configs["channels"])
    )

    dis = dense_disc(
        conditions_shape=con_shape,
        scenes_shape=sce_shape,
    )

    gen = unet_model(
        conditions_shape=con_shape,
        scenes_shape=sce_shape,
    )

    wgan = UNetWGAN(
        discriminator=dis,
        generator=gen,
        d_optimizer=dis_opt,
        g_optimizer=gen_opt,
        g_loss_fn=genloss,
        d_loss_fn=disloss,
        discriminator_extra_steps=int(configs["dis_extra"]),
    )

    wgan.compile()

    model = wgan

    cp_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=".",
        save_weights_only=True,
        save_freq=int(configs["save_freq"]),
        verbose=1
    )

    callbacks = [cp_callback]

    train_ds, _ = make_data()

    print("EPOCHS: ", int(configs["epochs"]))

    if configs["continue"]:
        model.load_weights(tf.train.latest_checkpoint(configs["save_ckpt_path"]))

    return model.fit(
        train_ds, epochs=int(configs["epochs"]), callbacks=callbacks
    )
