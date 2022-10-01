""" jouissance.tf.arch """

import numpy as np
import tensorflow as tf


def set_initializer():
    """ set the initializer """
    return tf.random_normal_initializer(0.0, 0.02)


def downsample_block(
    filters, size, strides=2, drop_rate=0.0, apply_batchnorm=True,
):
    """ a downsampling block. """
    initializer = set_initializer()

    result = tf.keras.Sequential()

    result.add(tf.keras.layers.Conv2D(
        filters, size, strides=strides, padding="same",
        kernel_initializer=initializer, use_bias=False,
        data_format="channels_last"
    ))

    if apply_batchnorm:
        result.add(tf.keras.layers.BatchNormalization())

    if drop_rate > 0:
        result.add(tf.keras.layers.Dropout(drop_rate))

    result.add(tf.keras.layers.PReLU())

    return result


def upsample_block(
    filters, size, strides=2, drop_rate=0.0, act="normal",
):
    """ an upsampling block. """
    initializer = set_initializer()

    transpose = False

    result = tf.keras.Sequential()

    if transpose:
        result.add(tf.keras.layers.Conv2DTranspose(
            filters, size, strides=strides, padding="same",
            kernel_initializer=initializer, use_bias=False,
            data_format="channels_last"
        ))

    if not transpose:
        result.add(tf.keras.layers.UpSampling2D(
            size=strides, interpolation="bilinear",
        ))

    result.add(tf.keras.layers.BatchNormalization())

    if drop_rate > 0:
        result.add(tf.keras.layers.Dropout(drop_rate))

    if act == "exit":
        result.add(tf.keras.layers.Activation("tanh"))
    else:
        result.add(tf.keras.layers.PReLU())

    return result


def dense_disc(
    conditions_shape=(128, 256, 3),
    scenes_shape=(128, 256, 1),
    name=None,
):
    """ a dense discriminator """

    input_conditions = tf.keras.layers.Input(shape=conditions_shape)
    if scenes_shape[0] != conditions_shape[0] \
            or scenes_shape[1] != conditions_shape[1]:
        holding = upsample_block(
            filters=3,
            size=5,
            strides=(
                scenes_shape[0]//conditions_shape[0],
                scenes_shape[1]//conditions_shape[1]
            )
        )(input_conditions)
    else:
        holding = input_conditions
    input_scenes = tf.keras.layers.Input(shape=scenes_shape)
    inputs = tf.keras.layers.Concatenate()([input_scenes, holding])
    output = tf.keras.layers.BatchNormalization()(inputs)
    steps = int(np.log2(np.min([scenes_shape[0], scenes_shape[1]])))
    for _ in range(steps):
        output = downsample_block(
            filters=64, size=3, drop_rate=0.2,
            apply_batchnorm=False)(output)
        residual = output
        output = downsample_block(
            filters=64, size=3, strides=1,
            apply_batchnorm=False)(output)
        output = tf.keras.layers.add([residual, output])
        output = tf.keras.layers.BatchNormalization()(output)

    output = tf.keras.layers.Flatten()(output)
    output = tf.keras.layers.Dropout(.2)(output)

    output = tf.keras.layers.Dense(
        1,
        activation="tanh", dtype='float32'
    )(output)

    return tf.keras.Model(
        inputs=[input_conditions, input_scenes],
        outputs=[output], name=name)


def unet_model(
    conditions_shape=(128, 256, 3),
    scenes_shape=(128, 256, 1),
    use_latent=True,
    name=None,
):
    """ a unet-like generation model. """
    input_conditions = tf.keras.layers.Input(shape=conditions_shape)
    if use_latent:
        input_noise = tf.keras.layers.Input(shape=conditions_shape)
        inputs = tf.keras.layers.Concatenate()([input_conditions, input_noise])
    else:
        inputs = input_conditions
    output = inputs

    skips = []
    steps = int(np.log2(np.min([conditions_shape[0], conditions_shape[1]])))
    for _ in range(steps):
        output = downsample_block(
            filters=64, size=3, drop_rate=0.2)(output)
        residual = output
        output = downsample_block(
            filters=64, size=3, strides=1)(output)
        output = tf.keras.layers.add([residual, output])
        skips.append(output)

    skips = reversed(skips[:-1])

    stepsagain = int(np.log2(np.min([scenes_shape[0], scenes_shape[1]])))
    for _, skip in zip(range(steps-1), skips):
        output = upsample_block(
            filters=64, size=3, drop_rate=0.2,)(output)
        residual = output
        output = upsample_block(
            filters=64, size=3, strides=1,)(output)
        output = tf.keras.layers.add([residual, output])
        output = tf.keras.layers.Concatenate()([output, skip])

    passcounter = 1
    for _ in range(steps, stepsagain):
        if passcounter == 1:
            output = upsample_block(
                filters=32, size=5, strides=4,)(output)
            residual = output
            output = upsample_block(
                filters=32, size=5, strides=1,)(output)
            output = tf.keras.layers.add([residual, output])
        passcounter = passcounter*-1

    if abs(stepsagain-steps) % 2 == 0:
        output = upsample_block(filters=32, size=3, strides=2,)(output)

    output = tf.keras.layers.Conv2D(
        scenes_shape[-1],
        3,
        strides=1,
        padding="same",
        activation="sigmoid",
        use_bias=True,
        data_format="channels_last"
    )(output)

    output = tf.keras.layers.Reshape(scenes_shape, dtype='float32')(output)
    if use_latent:
        return tf.keras.Model(
            inputs=[input_conditions, input_noise],
            outputs=[output], name=name)
    return tf.keras.Model(inputs=input_conditions, outputs=[output], name=name)
