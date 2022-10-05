"""Functions for tasks and a few general async tasks."""

import warnings

from django.conf import settings
from django.core.exceptions import AppRegistryNotReady
from django.db.utils import OperationalError, ProgrammingError

from src.accu.core.helpers.logging import LOGGER


def schedule_task(taskname, **kwargs):
    """Create a scheduled task.

    If the task has already been scheduled, ignore!
    """
    # If unspecified, repeat indefinitely
    repeats = kwargs.pop("repeats", -1)
    kwargs["repeats"] = repeats

    try:
        from django_q.models import Schedule
    except AppRegistryNotReady:  # pragma: no cover
        LOGGER.info("Could not start background tasks - App registry not ready")
        return

    try:
        # If this task is already scheduled, don't schedule it again
        # Instead, update the scheduling parameters
        if Schedule.objects.filter(func=taskname).exists():
            LOGGER.debug(f"Scheduled task '{taskname}' already exists - updating!")

            Schedule.objects.filter(func=taskname).update(**kwargs)
        else:
            LOGGER.info(f"Creating scheduled task '{taskname}'")

            Schedule.objects.create(name=taskname, func=taskname, **kwargs)
    except (OperationalError, ProgrammingError):  # pragma: no cover
        # Required if the DB is not ready yet
        pass


def raise_warning(msg):
    """Log and raise a warning."""
    LOGGER.warning(msg)

    # If testing is running raise a warning that can be asserted
    if settings.TESTING:
        warnings.warn(msg)


def offload_task(taskname, *args, force_async=False, force_sync=False, **kwargs):
    """Create an AsyncTask if workers are running. This is different to a 'scheduled' task, in that it only runs once!

    If workers are not running or force_sync flag
    is set then the task is ran synchronously.
    """
    try:
        import importlib

        from django_q.tasks import AsyncTask

        from InvenTree.status import is_worker_running
    except AppRegistryNotReady:  # pragma: no cover
        LOGGER.warning(f"Could not offload task '{taskname}' - app registry not ready")
        return
    except (OperationalError, ProgrammingError):  # pragma: no cover
        raise_warning(f"Could not offload task '{taskname}' - database not ready")

    if force_async or (is_worker_running() and not force_sync):
        # Running as asynchronous task
        try:
            task = AsyncTask(taskname, *args, **kwargs)
            task.run()
        except ImportError:
            raise_warning(f"WARNING: '{taskname}' not started - Function not found")
    else:

        if callable(taskname):
            # function was passed - use that
            _func = taskname
        else:
            # Split path
            try:
                app, mod, func = taskname.split(".")
                app_mod = app + "." + mod
            except ValueError:
                raise_warning(
                    f"WARNING: '{taskname}' not started - Malformed function path"
                )
                return

            # Import module from app
            try:
                _mod = importlib.import_module(app_mod)
            except ModuleNotFoundError:
                raise_warning(
                    f"WARNING: '{taskname}' not started - No module named '{app_mod}'"
                )
                return

            # Retrieve function
            try:
                _func = getattr(_mod, func)
            except AttributeError:  # pragma: no cover
                # getattr does not work for local import
                _func = None

            try:
                if not _func:
                    _func = eval(func)  # pragma: no cover
            except NameError:
                raise_warning(
                    f"WARNING: '{taskname}' not started - No function named '{func}'"
                )
                return

        # Workers are not running: run it as synchronous task
        _func(*args, **kwargs)
