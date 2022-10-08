from typing import Any, Tuple

import numpy as np


def compute_volume_stats(vol: np.array) -> Tuple[Any]:
    """Compute basic stats of a volume. 
    Args:
        vol: volume to compute stats for.
    Returns:
        median, mean, std, min, max, percentiles of the volume.
    """
    median: np.array = np.median(vol)
    mean: np.array = np.mean(vol)
    std: np.array = np.std(vol)
    minimum: np.array = np.min(vol)
    maximum: np.array = np.max(vol)
    percentile_99_5: np.array = np.percentile(vol, 99.5)
    percentile_00_5: np.array = np.percentile(vol, 00.5)
    
    return {"median": median, "mean": mean, "std": std, "min": minimum, "max": maximum, 
            "percentile_99_5": percentile_99_5, "percentile_00_5": percentile_00_5}