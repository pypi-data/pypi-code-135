from functools import wraps
from contextlib import contextmanager
from typing import Optional

from silx.io import h5py_utils
from silx.utils import retry as retrymod


@contextmanager
def h5context(filename: str, h5path: Optional[str] = None, **openargs):
    with h5py_utils.File(filename, **openargs) as f:
        if h5path:
            yield f[h5path]
        else:
            yield f


def retry_iterator(
    retry_timeout=None, retry_period=None, retry_on_error=h5py_utils._retry_h5py_error
):
    """Decorator for a method that needs to be iterated until it not longer
    fails or until `retry_on_error` returns False.

    The method should have a `start_index` argument which allows the method
    to start iterating from the last failure when called on retry.

    The decorator arguments can be overriden by using them when calling the
    decorated method.

    :param num retry_timeout:
    :param num retry_period: sleep before retry
    :param callable or None retry_on_error: checks whether an exception is
                                            eligible for retry
    """

    if retry_period is None:
        retry_period = retrymod.RETRY_PERIOD

    def decorator(method):
        @wraps(method)
        def wrapper(*args, **kw):
            _retry_timeout = kw.pop("retry_timeout", retry_timeout)
            _retry_period = kw.pop("retry_period", retry_period)
            _retry_on_error = kw.pop("retry_on_error", retry_on_error)
            start_index = kw.pop("start_index", 0)
            if start_index is None:
                start_index = 0
            for options in retrymod._retry_loop(
                retry_timeout=_retry_timeout,
                retry_period=_retry_period,
                retry_on_error=_retry_on_error,
            ):
                with retrymod._handle_exception(options):
                    oretry_on_error = options["retry_on_error"]
                    it = method(*args, start_index=start_index, **kw)
                    while True:
                        try:
                            result = next(it)
                        except StopIteration:
                            return
                        start_index += 1
                        options["retry_on_error"] = None
                        yield result
                        options["retry_on_error"] = oretry_on_error

        return wrapper

    return decorator
