""" mcli modify api-key functions """
import argparse
import logging

from mcli.config import MESSAGE, MCLIConfig, MCLIConfigError
from mcli.utils.utils_interactive import query_yes_no
from mcli.utils.utils_logging import FAIL, OK

logger = logging.getLogger(__name__)


def modify_api_key(
    api_key_value: str,
    force: bool = False,
    **kwargs,
) -> int:
    """Create or updates api key

    Args:
        api_key_value: Value to set the api key to
        force: If True, will overwrite existing API key values without asking

    Returns:
        0 if creation succeeded, else 1
    """
    del kwargs

    # Get the current api key
    try:
        conf = MCLIConfig.load_config()
    except MCLIConfigError:
        logger.error(MESSAGE.MCLI_NOT_INITIALIZED)
        return 1

    current_api_key = conf.MOSAICML_API_KEY
    if conf.MOSAICML_API_KEY == api_key_value:
        logger.info(f"{OK} The API Key has already been created with this value")
        return 0

    # Don't override existing values without confirmation
    if not force and current_api_key:
        confirm = query_yes_no(f'The value of api-key is currently set to "{current_api_key}". \n'
                               'Would you like to override this?')
        if not confirm:
            logger.error(f'{FAIL} Canceling API Key creation')
            return 1

    # Update the api key
    conf.api_key = api_key_value
    conf.save_config()

    logger.info(f"{OK} Updated API Key")
    return 0


def configure_api_key_argparser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        'api_key_value',
        help='API Key value',
    )
    parser.add_argument(
        '-y',
        '--force',
        dest='force',
        action='store_true',
        help='Skip confirmation dialog before overwriting existing api key value',
    )
