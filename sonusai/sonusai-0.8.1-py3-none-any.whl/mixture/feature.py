from dataclasses import dataclass
from os import PathLike
from typing import Union

import numpy as np
from pyaaware import Predict

from sonusai.mixture.mixdb import MixtureDatabase
from sonusai.mixture.mixdb import MixtureID

MP_DICT = {}


def _get_ft(mixid: int) -> (np.ndarray, np.ndarray):
    """Get feature/truth for a given mixid from a directory containing genft data"""
    from os.path import join

    import h5py

    from sonusai.mixture.mixdb import get_mixid_padded_name

    mixid_padded_name = get_mixid_padded_name(MP_DICT['mixdb'], mixid)

    filename = join(MP_DICT['location'], mixid_padded_name + '_feature.h5')
    with h5py.File(filename, 'r') as f:
        feature = np.array(f['feature'])

    filename = join(MP_DICT['location'], mixid_padded_name + '_truth_f.h5')
    with h5py.File(filename, 'r') as f:
        truth_f = np.array(f['truth_f'])

    return feature, truth_f


def get_ft_from_dir(mixdb: MixtureDatabase,
                    location: Union[str, bytes, PathLike],
                    mixid: MixtureID = ':') -> (np.ndarray, np.ndarray):
    """Get feature/truth for given mixids from a directory containing genft data"""
    from sonusai.mixture.mixdb import convert_mixid_to_list
    from sonusai.utils.parallel import p_map

    MP_DICT['mixdb'] = mixdb
    MP_DICT['location'] = location
    mixid = convert_mixid_to_list(mixdb, mixid)
    result = p_map(_get_ft, mixid)

    feature = np.vstack([result[i][0] for i in range(len(result))])
    truth_f = np.vstack([result[i][1] for i in range(len(result))])

    return feature, truth_f


def get_feature_from_audio(audio: np.ndarray, model: Predict) -> np.ndarray:
    import h5py

    import sonusai
    from sonusai.mixture import get_pad_length
    from sonusai.mixture import Mixture

    fs = get_feature_stats(feature_mode=model.feature,
                           frame_size=sonusai.mixture.DEFAULT_FRAME_SIZE,
                           num_classes=1,
                           truth_mutex=model.mutex)
    audio = np.pad(array=audio,
                   pad_width=(0, get_pad_length(len(audio), fs.feature_step_samples)),
                   mode='constant',
                   constant_values=0)
    mixdb = MixtureDatabase(feature=model.feature,
                            mixtures=[Mixture(samples=len(audio))],
                            feature_samples=fs.feature_samples,
                            feature_step_samples=fs.feature_step_samples,
                            frame_size=sonusai.mixture.DEFAULT_FRAME_SIZE,
                            num_classes=1,
                            truth_mutex=model.mutex,
                            truth_reduction_function='max')
    feature, _ = get_feature_and_truth_f(mixdb=mixdb, mixid=0, audio=audio)
    return feature


def read_feature_data(filename: str) -> (MixtureDatabase, np.ndarray, np.ndarray, np.ndarray):
    """Read mixdb, feature, truth_f, and segsnr data from given HDF5 file and return them as a tuple."""
    import h5py

    from sonusai.mixture import mixdb_from_json

    with h5py.File(filename, 'r') as f:
        return (mixdb_from_json(f.attrs['mixdb']),
                np.array(f['/feature']),
                np.array(f['/truth_f']),
                np.array(f['/segsnr']))


def get_feature_and_truth_f(mixdb: MixtureDatabase,
                            mixid: int,
                            audio: np.ndarray,
                            truth_t: Union[np.ndarray, None] = None) -> (np.ndarray, np.ndarray):
    from pyaaware import FeatureGenerator
    from pyaaware import ForwardTransform

    from sonusai import SonusAIError
    from sonusai.mixture import get_feature_frames_in_mixture
    from sonusai.mixture import get_transform_frames_in_mixture
    from sonusai.mixture import truth_reduction
    from sonusai.utils import int16_to_float

    if len(audio) != mixdb.mixtures[mixid].samples:
        raise SonusAIError(f'Wrong number of samples in audio')

    fft = ForwardTransform(N=mixdb.frame_size * 4,
                           R=mixdb.frame_size)

    fg = FeatureGenerator(frame_size=mixdb.frame_size,
                          feature_mode=mixdb.feature,
                          num_classes=mixdb.num_classes,
                          truth_mutex=mixdb.truth_mutex)

    transform_frames = get_transform_frames_in_mixture(mixdb, mixid)
    feature_frames = get_feature_frames_in_mixture(mixdb, mixid)

    if truth_t is None:
        truth_t = np.zeros((mixdb.mixtures[mixid].samples, mixdb.num_classes), dtype=np.single)

    feature = np.empty((feature_frames, fg.stride, fg.num_bands), dtype=np.single)
    truth_f = np.empty((feature_frames, mixdb.num_classes), dtype=np.single)

    feature_frame = 0
    for transform_frame in range(transform_frames):
        indices = slice(transform_frame * mixdb.frame_size,
                        (transform_frame + 1) * mixdb.frame_size)
        fd = fft.execute(int16_to_float(audio[indices]))

        fg.execute(fd, truth_reduction(truth_t[indices], mixdb.truth_reduction_function))

        if fg.eof():
            feature[feature_frame] = fg.feature()
            truth_f[feature_frame] = fg.truth()
            feature_frame += 1

    return feature, truth_f


@dataclass(frozen=True)
class FeatureStats:
    feature_ms: float
    feature_samples: int
    feature_step_ms: float
    feature_step_samples: int
    num_bands: int
    stride: int
    step: int
    decimation: int


def get_feature_stats(feature_mode: str,
                      frame_size: int,
                      num_classes: int,
                      truth_mutex: bool) -> FeatureStats:
    import h5py
    from pyaaware import FeatureGenerator

    import sonusai

    fg = FeatureGenerator(feature_mode=feature_mode,
                          frame_size=frame_size,
                          num_classes=num_classes,
                          truth_mutex=truth_mutex)

    transform_frame_ms = float(frame_size) / float(sonusai.mixture.SAMPLE_RATE / 1000)

    return FeatureStats(feature_ms=transform_frame_ms * fg.decimation * fg.stride,
                        feature_samples=frame_size * fg.decimation * fg.stride,
                        feature_step_ms=transform_frame_ms * fg.decimation * fg.step,
                        feature_step_samples=frame_size * fg.decimation * fg.step,
                        num_bands=fg.num_bands,
                        stride=fg.stride,
                        step=fg.step,
                        decimation=fg.decimation)
