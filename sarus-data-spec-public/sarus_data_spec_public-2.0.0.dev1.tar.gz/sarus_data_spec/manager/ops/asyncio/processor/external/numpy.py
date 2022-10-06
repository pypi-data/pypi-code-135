from typing import Any

import numpy as np


async def np_mean(*args: Any, **kwargs: Any) -> Any:
    return np.mean(*args, **kwargs)


async def np_std(*args: Any, **kwargs: Any) -> Any:
    return np.std(*args, **kwargs)


async def np_rand(*args: int) -> Any:
    return np.random.rand(*args)


async def np_array(*args: Any, **kwargs: Any) -> Any:
    return np.array(*args, **kwargs)
