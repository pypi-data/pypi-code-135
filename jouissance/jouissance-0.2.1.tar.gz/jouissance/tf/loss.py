""" jouissance.tf.loss """

import tensorflow as tf

from jouissance.util import read_conf


def genopt(con=None):
    """ generator optimizer """
    con = read_conf() if con is None else con
    _opt = tf.keras.optimizers.Adam(
        learning_rate=con["genopt_learning_rate"],
        beta_1=con["genopt_beta1"],
        beta_2=con["genopt_beta2"]
    )
    return tf.keras.mixed_precision.LossScaleOptimizer(
        _opt) if con["use_amp"] else _opt


def disopt(con=None):
    """ discriminator optimizer """
    con = read_conf() if con is None else con
    _opt = tf.keras.optimizers.Adam(
        learning_rate=con["disopt_learning_rate"],
        beta_1=con["disopt_beta1"],
        beta_2=con["disopt_beta2"]
    )
    return tf.keras.mixed_precision.LossScaleOptimizer(
        _opt) if con["use_amp"] else _opt


def genloss(fake_log, real_img, fake_img):
    """ loss function for generator """
    return -tf.reduce_mean(fake_log) + tf.reduce_mean(
        tf.keras.losses.mse(real_img, fake_img))


def disloss(real_log, fake_log, real_img, fake_img):
    """ loss function for discriminator """
    real_loss = tf.reduce_mean(real_log)
    fake_loss = tf.reduce_mean(fake_log)
    return fake_loss - real_loss - tf.reduce_mean(
        tf.keras.losses.mse(real_img, fake_img))
