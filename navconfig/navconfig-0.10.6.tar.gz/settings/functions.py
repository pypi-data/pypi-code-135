"""
Basic Shared functions for all programs.

Functions not be implemented by other library.
"""


def get_worker_list(workers):
    """Convert a list of workers in a tuple of worker:port for Scheduler."""
    wl = []
    for worker in workers:
        w,p = worker.split(':')
        wl.append((w, p))
    return wl
