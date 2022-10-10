import copy
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)


def log_action(logger: logging.Logger, context: str, **query):
    query = copy.copy(query)
    query = strip_boring_kwargs(**query)
    if query:
        logger.info("%s (%s)", context, stringify_kwargs(**query))
    else:
        logger.info("%s", context)


def log_result(logger: logging.Logger, context: str, **kwargs):
    kwargs = copy.copy(kwargs)
    if kwargs:
        logger.info("%s (%s)", context, stringify_kwargs(**kwargs))
    else:
        logger.info(context)


def strip_boring_kwargs(**kwargs) -> dict:
    return dict([(k, v) for (k, v) in kwargs.items() if v or isinstance(v, bool)])


def stringify_kwargs(**kwargs) -> str:
    return ', '.join(sorted(['{}: {}'.format(k, v) for (k, v) in kwargs.items()]))
