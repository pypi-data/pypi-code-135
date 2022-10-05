"""sonusai genmix

usage: genmix [-hvts] (-d MIXDB) [-i MIXID] [-o OUTPUT]

options:
    -h, --help
    -v, --verbose                   Be verbose.
    -d MIXDB, --mixdb MIXDB         Mixture database JSON file.
    -i MIXID, --mixid MIXID         Mixture ID(s) to generate. [default: *].
    -o OUTPUT, --output OUTPUT      Output directory.
    -t, --truth                     Save truth_t. [default: False].
    -s, --segsnr                    Save segsnr. [default: False].

Generate SonusAI mixture data from a SonusAI mixture database.

Inputs:
    MIXDB       A SonusAI mixture database JSON file.
    MIXID       A glob of mixture ID(s) to generate.

Outputs:
    OUTPUT/     A directory containing:
                    <id>_mixture.h5:    mixture
                    <id>_target.h5:     target
                    <id>_noise.h5:      noise
                    <id>_truth_t.h5:    truth_t (optional)
                    <id>_segsnr.h5:     segsnr (optional)
                    genmix.log
"""
from typing import List

import numpy as np

from sonusai import logger
from sonusai.mixture import MixtureDatabase

# NOTE: multiprocessing dictionary is required for run-time performance; using 'partial' is much slower.
MP_DICT = {}


def genmix(mixdb: MixtureDatabase,
           mixid: int,
           target_audios: List[np.ndarray] = None,
           noise_audios: List[List[np.ndarray]] = None,
           compute_segsnr: bool = False,
           compute_truth: bool = False) -> (np.ndarray,
                                            np.ndarray,
                                            np.ndarray,
                                            np.ndarray,
                                            np.ndarray):
    from sonusai.mixture import get_audio_and_truth_t

    # Get mixture and truth_t
    (mixture,
     truth_t,
     target,
     noise,
     segsnr) = get_audio_and_truth_t(mixdb=mixdb,
                                     mixture=mixdb.mixtures[mixid],
                                     raw_target_audios=target_audios,
                                     raw_noise_audios=noise_audios,
                                     compute_truth=compute_truth,
                                     compute_segsnr=compute_segsnr)

    return mixture, truth_t, target, noise, segsnr


def _process_mixture(mixid: int) -> None:
    from os.path import join

    import h5py

    from sonusai import SonusAIError
    from sonusai.mixture import get_mixid_padded_name
    from sonusai.mixture import get_mixture_metadata

    mixdb = MP_DICT['mixdb']
    output_dir = MP_DICT['output_dir']
    target_audios = MP_DICT['target_audios']
    noise_audios = MP_DICT['noise_audios']
    compute_truth = MP_DICT['compute_truth']
    compute_segsnr = MP_DICT['compute_segsnr']

    mixid_padded_name = get_mixid_padded_name(mixdb, mixid)
    output_base = join(output_dir, mixid_padded_name)

    mixture, truth_t, target, noise, segsnr_t = genmix(mixdb=mixdb,
                                                       mixid=mixid,
                                                       target_audios=target_audios,
                                                       noise_audios=noise_audios,
                                                       compute_segsnr=compute_segsnr,
                                                       compute_truth=compute_truth)

    samples = mixture.shape[0]
    if compute_truth:
        if samples != truth_t.shape[0]:
            raise SonusAIError(
                f'truth_t samples does not match mixture samples: {truth_t.shape[0]} != {samples}')
        if mixdb.num_classes != truth_t.shape[1]:
            raise SonusAIError(
                f'truth_t num_classes is incorrect: {truth_t.shape[1]} != {mixdb.num_classes}')
    if samples != target.shape[0]:
        raise SonusAIError(f'target samples does not match mixture samples: {target.shape[0]} != {samples}')
    if samples != noise.shape[0]:
        raise SonusAIError(f'noise samples does not match mixture samples: {noise.shape[0]} != {samples}')
    if compute_segsnr and samples != segsnr_t.shape[0]:
        raise SonusAIError(f'segsnr_t samples does not match mixture samples: {segsnr_t.shape[0]} != {samples}')

    with h5py.File(output_base + '_mixture.h5', 'w') as f:
        f.create_dataset(name='mixture', data=mixture, dtype=np.int16)

    if compute_truth:
        with h5py.File(output_base + '_truth_t.h5', 'w') as f:
            f.create_dataset(name='truth_t', data=truth_t, dtype=np.single)

    with h5py.File(output_base + '_target.h5', 'w') as f:
        f.create_dataset(name='target', data=target, dtype=np.int16)

    with h5py.File(output_base + '_noise.h5', 'w') as f:
        f.create_dataset(name='noise', data=noise, dtype=np.int16)

    if compute_segsnr:
        with h5py.File(output_base + '_segsnr_t.h5', 'w') as f:
            f.create_dataset(name='segsnr_t', data=segsnr_t, dtype=np.single)

    with open(file=output_base + '.txt', mode='w') as f:
        f.write(get_mixture_metadata(mixdb, mixid))


def main():
    import time
    from os import makedirs
    from os import remove
    from os.path import exists
    from os.path import isdir
    from os.path import join
    from os.path import splitext

    from docopt import docopt
    from tqdm import tqdm

    import sonusai
    from sonusai import create_file_handler
    from sonusai import initial_log_messages
    from sonusai import update_console_handler
    from sonusai.mixture import build_noise_audios
    from sonusai.mixture import build_target_audios
    from sonusai.mixture import check_audio_files_exist
    from sonusai.mixture import load_mixdb
    from sonusai.utils import expand_range
    from sonusai.utils import p_tqdm_map
    from sonusai.utils import human_readable_size
    from sonusai.utils import seconds_to_hms
    from sonusai.utils import trim_docstring

    args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

    verbose = args['--verbose']
    mixdb_name = args['--mixdb']
    mixid = args['--mixid']
    output_dir = args['--output']
    compute_segsnr = args['--segsnr']
    compute_truth = args['--truth']

    if not output_dir:
        output_dir = splitext(mixdb_name)[0]

    if exists(output_dir) and not isdir(output_dir):
        remove(output_dir)

    if not isdir(output_dir):
        makedirs(output_dir)

    start_time = time.monotonic()

    log_name = join(output_dir, 'genmix.log')
    create_file_handler(log_name)
    update_console_handler(verbose)
    initial_log_messages('genmix')

    logger.info(f'\nLoad mixture database from {mixdb_name}')
    mixdb = load_mixdb(name=mixdb_name)
    if mixid == '*':
        mixid = list(range(len(mixdb.mixtures)))
    else:
        mixid = expand_range(mixid)

    total_samples = sum([sub.samples for sub in [mixdb.mixtures[m] for m in mixid]])
    duration = total_samples / sonusai.mixture.SAMPLE_RATE

    logger.info('')
    logger.info(f'Found {len(mixid):,} mixtures to process')
    logger.info(f'{total_samples:,} samples')

    check_audio_files_exist(mixdb)

    MP_DICT['mixdb'] = mixdb
    MP_DICT['output_dir'] = output_dir
    MP_DICT['target_audios'] = build_target_audios(mixdb)
    MP_DICT['noise_audios'] = build_noise_audios(mixdb)
    MP_DICT['compute_truth'] = compute_truth
    MP_DICT['compute_segsnr'] = compute_segsnr

    progress = tqdm(total=len(mixid), desc='genmix')
    p_tqdm_map(_process_mixture, mixid, progress=progress)
    progress.close()

    logger.info(f'Wrote {len(mixid)} mixtures to {output_dir}')
    logger.info('')
    logger.info(f'Duration: {seconds_to_hms(seconds=duration)}')
    logger.info(f'mixture:  {human_readable_size(total_samples * 2, 1)}')
    if compute_truth:
        logger.info(f'truth_t:  {human_readable_size(total_samples * mixdb.num_classes * 4, 1)}')
    logger.info(f'target:   {human_readable_size(total_samples * 2, 1)}')
    logger.info(f'noise:    {human_readable_size(total_samples * 2, 1)}')
    if compute_segsnr:
        logger.info(f'segsnr:   {human_readable_size(total_samples * 4, 1)}')

    end_time = time.monotonic()
    logger.info(f'Completed in {seconds_to_hms(seconds=end_time - start_time)}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        raise SystemExit(0)
