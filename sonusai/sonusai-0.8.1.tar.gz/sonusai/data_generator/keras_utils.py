from sonusai.mixture import MixtureDatabase
from sonusai.mixture import Mixtures


def get_frames_per_batch(mixdb: MixtureDatabase,
                         mixtures: Mixtures,
                         batch_size: int,
                         timesteps: int) -> (int, int):
    from sonusai import SonusAIError

    frames = sum([sub.samples for sub in mixtures]) // mixdb.feature_step_samples
    frames_per_batch = batch_size if timesteps == 0 else batch_size * timesteps
    total_batches = frames // frames_per_batch
    if total_batches == 0:
        raise SonusAIError(
            f'Error: dataset only contains {frames} frames which is not enough to fill a batch size of '
            f'{frames_per_batch}. Either provide more data or decrease the batch size')

    return frames_per_batch, total_batches
