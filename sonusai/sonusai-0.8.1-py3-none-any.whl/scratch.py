from os.path import join

import h5py
import numpy as np

from sonusai.genft import genft
from sonusai.mixture import build_noise_audios
from sonusai.mixture import build_target_audios
from sonusai.mixture import get_mixid_padded_name
from sonusai.mixture import load_mixdb
from sonusai.utils import p_map

MP_DICT = {}


def _process_mixture(mixid: int) -> (np.ndarray, np.ndarray, np.ndarray):
    return genft(mixdb=MP_DICT['mixdb'],
                 mixid=mixid,
                 target_audios=MP_DICT['target_audios'],
                 noise_audios=MP_DICT['noise_audios'],
                 compute_segsnr=True)


def main():
    data_dir = '/opt/Aaware/sonusai/tests/data'
    output_dir = join(data_dir, 'test_advanced')
    mixdb = load_mixdb(data_dir + '/test_advanced.json')

    mixid = [0, 3, 174]

    MP_DICT['mixdb'] = mixdb
    MP_DICT['target_audios'] = build_target_audios(mixdb)
    MP_DICT['noise_audios'] = build_noise_audios(mixdb)

    result = p_map(_process_mixture, mixid)

    for idx, val in enumerate(mixid):
        mixid_padded_name = get_mixid_padded_name(mixdb, val)
        output_base = join(output_dir, mixid_padded_name)
        (feature, truth_f, segsnr) = result[idx]

        with h5py.File(output_base + '_feature.h5', 'r') as f:
            exp_feature = np.array(f['/feature'])
        np.testing.assert_array_equal(feature, exp_feature)

        with h5py.File(output_base + '_truth_f.h5', 'r') as f:
            exp_truth_f = np.array(f['/truth_f'])
        np.testing.assert_array_equal(truth_f, exp_truth_f)

        with h5py.File(output_base + '_segsnr.h5', 'r') as f:
            exp_segsnr = np.array(f['/segsnr'])
        np.testing.assert_array_equal(segsnr, exp_segsnr)

    features = [result[i][0] for i in range(len(result))]
    truth_fs = [result[i][1] for i in range(len(result))]
    feature = np.vstack(features)
    truth_f = np.vstack(truth_fs)
    print(f'feature {feature.shape}')
    print(f'truth_f {truth_f.shape}')


if __name__ == '__main__':
    main()
