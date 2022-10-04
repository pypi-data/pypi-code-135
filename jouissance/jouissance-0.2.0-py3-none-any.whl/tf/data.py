""" jouissance.tf.data """

import tensorflow as tf

from jouissance.util import read_conf, make_hash
from jouissance.util import get_scenes_conditions_h5py
from jouissance.util import get_scenes_conditions_netcdf4
from jouissance.util import make_glob


class MyData(tf.data.Dataset):  # pylint: disable=abstract-method
    """ https://www.tensorflow.org/guide/data_performance """

    def _generator(self):
        con = read_conf()
        if con["provider"] == "file":
            yield get_scenes_conditions_netcdf4(self)
        else:
            yield get_scenes_conditions_h5py(self)

    def __new__(cls, file_paths=None):
        if file_paths is None:
            raise ValueError("file_paths is required")
        con = read_conf()
        scenes_shape = (
            int(con["scene_shape1"]), int(con["scene_shape2"]),
            len(con["channels"])
        )
        conditions_shape = (
            int(con["reanalysis_shape1"]), int(con["reanalysis_shape2"]),
            len(con["reanalysis_products"])*len(con["reanalysis_levels"])
        )
        return tf.data.Dataset.from_generator(
            cls._generator,
            output_signature=(
                tf.TensorSpec(
                    shape=tf.TensorShape(scenes_shape),
                    dtype=tf.float32),
                tf.TensorSpec(
                    shape=tf.TensorShape(conditions_shape),
                    dtype=tf.float32),
            ),
            args=(file_paths,),
        )


def make_data():
    """ https://www.tensorflow.org/guide/data_performance """
    configs = read_conf()

    files = make_glob(con=configs)

    nsamples = len(files)
    tds = tf.data.Dataset.from_tensor_slices(files)
    # pylint: disable=abstract-class-instantiated
    tds = tds.interleave(
        lambda file: MyData(file),  # pylint: disable=unnecessary-lambda
        num_parallel_calls=tf.data.experimental.AUTOTUNE,
        deterministic=False,
    )

    sshape = (
        int(configs["scene_reshape1"]),
        int(configs["scene_reshape2"])
    )
    cshape = (
        int(configs["reanalysis_reshape1"]),
        int(configs["reanalysis_reshape2"])
    )
    tds = tds.map(
        lambda _scene, _condition: (
            tf.image.resize(_scene, sshape),
            tf.image.resize(_condition, cshape)
        ), num_parallel_calls=tf.data.experimental.AUTOTUNE
    )

    tds = tds.map(lambda _scene, _cond: (
        (_scene - tf.math.reduce_mean(_scene, axis=[1, 2], keepdims=True)) /
        tf.math.reduce_std(_scene, axis=[1, 2], keepdims=True),
        (_cond - tf.math.reduce_min(_cond, axis=[1, 2], keepdims=True)) /
        (
            tf.math.reduce_max(_cond, axis=[1, 2], keepdims=True) -
            tf.math.reduce_min(_cond, axis=[1, 2], keepdims=True)
        )
    ), num_parallel_calls=tf.data.experimental.AUTOTUNE)

    tds = tds.batch(
        batch_size=int(configs["batch_size"]), drop_remainder=True
    )

    tds = tds.prefetch(tf.data.AUTOTUNE)

    train_take = int(
        float(configs["train_split"]) * nsamples // int(configs["batch_size"])
    )

    cache_file = configs["cache_prefix"] + make_hash(configs)

    if configs["if_shuffle"]:
        training_ds = tds.take(train_take).cache(cache_file).shuffle(
            int(configs["shuffle_size"]),
            reshuffle_each_iteration=configs["reshuffle_iter"],
        )
        validating_ds = tds.skip(train_take).cache(cache_file).shuffle(
            int(configs["shuffle_size"]),
            reshuffle_each_iteration=configs["reshuffle_iter"],
        )
    else:
        training_ds = tds.take(train_take).cache(cache_file)
        validating_ds = tds.skip(train_take).cache(cache_file)

    return training_ds, validating_ds
