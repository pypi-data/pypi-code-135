"""sonusai mkwav

usage: mkwav [-hvtn] (-d MIXDB) [-i MIXID] [-o OUTPUT]

options:
    -h, --help
    -v, --verbose                   Be verbose.
    -d MIXDB, --mixdb MIXDB         Mixture database JSON file.
    -i MIXID, --mixid MIXID         Mixture ID(s) to generate. [default: *].
    -o OUTPUT, --output OUTPUT      Output directory.
    -t, --target                    Write target file.
    -n, --noise                     Write noise file.

The mkwav command creates WAV files from a SonusAI database.

Inputs:
    MIXDB       A SonusAI mixture database JSON file.
    MIXID       A glob of mixture ID(s) to generate.

Outputs:
    OUTPUT/     A directory containing:
                    <id>_mixture.wav:   mixture
                    <id>_target.wav:    target (optional)
                    <id>_noise.wav:     noise (optional)
                    mkwav.log

"""
from typing import List

import numpy as np

from sonusai import logger
from sonusai.mixture import MixtureDatabase

# NOTE: multiprocessing dictionary is required for run-time performance; using 'partial' is much slower.
MP_DICT = {}


def mkwav(mixdb: MixtureDatabase,
          mixid: int,
          target_audios: List[np.ndarray] = None,
          noise_audios: List[List[np.ndarray]] = None) -> (np.ndarray, np.ndarray, np.ndarray):
    from sonusai.genmix import genmix

    mixture, _, target, noise, _ = genmix(mixdb=mixdb,
                                          mixid=mixid,
                                          target_audios=target_audios,
                                          noise_audios=noise_audios)
    return mixture, target, noise


def _process_mixture(mixid: int) -> None:
    from os.path import exists
    from os.path import join

    import h5py

    from sonusai.mixture import get_mixid_padded_name
    from sonusai.mixture import get_mixture_metadata

    mixdb = MP_DICT['mixdb']
    output_dir = MP_DICT['output_dir']
    target_audios = MP_DICT['target_audios']
    noise_audios = MP_DICT['noise_audios']
    write_target = MP_DICT['write_target']
    write_noise = MP_DICT['write_noise']

    mixid_padded_name = get_mixid_padded_name(mixdb, mixid)
    mixture_base = join(output_dir, mixid_padded_name + '_mixture')
    target_base = join(output_dir, mixid_padded_name + '_target')
    noise_base = join(output_dir, mixid_padded_name + '_noise')

    target = None
    noise = None

    if not exists(mixture_base + '.h5') \
            or (write_target and not exists(target_base + '.h5')) \
            or (write_noise and not exists(noise_base + '.h5')):
        mixture, target, noise = mkwav(mixdb=mixdb,
                                       mixid=mixid,
                                       target_audios=target_audios,
                                       noise_audios=noise_audios)
    else:
        with h5py.File(mixture_base + '.h5', 'r') as f:
            mixture = np.array(f['mixture'])

        if write_target:
            with h5py.File(target_base + '.h5', 'r') as f:
                target = np.array(f['target'])

        if write_noise:
            with h5py.File(noise_base + '.h5', 'r') as f:
                noise = np.array(f['noise'])

    _write_wav(name=mixture_base + '.wav', data=mixture)

    if write_target:
        _write_wav(name=target_base + '.wav', data=target)

    if write_noise:
        _write_wav(name=noise_base + '.wav', data=noise)

    with open(file=join(output_dir, mixid_padded_name + '.txt'), mode='w') as f:
        f.write(get_mixture_metadata(mixdb, mixid))


def _write_wav(name: str, data: np.ndarray) -> None:
    import wave

    from sonusai.mixture import CHANNEL_COUNT
    from sonusai.mixture import SAMPLE_BYTES
    from sonusai.mixture import SAMPLE_RATE

    with wave.open(name, mode='w') as f:
        f.setnchannels(CHANNEL_COUNT)
        f.setsampwidth(SAMPLE_BYTES)
        f.setframerate(SAMPLE_RATE)
        f.writeframesraw(data)


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
    write_target = args['--target']
    write_noise = args['--noise']

    if not output_dir:
        output_dir = splitext(mixdb_name)[0]

    if exists(output_dir) and not isdir(output_dir):
        remove(output_dir)

    if not isdir(output_dir):
        makedirs(output_dir)

    start_time = time.monotonic()

    log_name = join(output_dir, 'mkwav.log')
    create_file_handler(log_name)
    update_console_handler(verbose)
    initial_log_messages('mkwav')

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
    MP_DICT['write_target'] = write_target
    MP_DICT['write_noise'] = write_noise

    progress = tqdm(total=len(mixid), desc='mkwav')
    p_tqdm_map(_process_mixture, mixid, progress=progress)
    progress.close()

    logger.info(f'Wrote {len(mixid)} mixtures to {output_dir}')
    logger.info('')
    logger.info(f'Duration: {seconds_to_hms(seconds=duration)}')
    logger.info(f'mixture:  {human_readable_size(total_samples * 2, 1)}')
    if write_target:
        logger.info(f'target:   {human_readable_size(total_samples * 2, 1)}')
    if write_noise:
        logger.info(f'noise:    {human_readable_size(total_samples * 2, 1)}')

    end_time = time.monotonic()
    logger.info(f'Completed in {seconds_to_hms(seconds=end_time - start_time)}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        raise SystemExit(0)
