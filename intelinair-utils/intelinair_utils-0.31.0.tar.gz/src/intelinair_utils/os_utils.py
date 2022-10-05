from typing import Tuple, Union
import logging
import subprocess
import os
import json
from intelinair_utils.pretty_popen import PrettyPopen

__all__ = ["get_error_message", "call_command"]

logger = logging.getLogger(__name__)


def get_error_message(output_folder: str, return_code: int) -> Union[str, None]:
    """Reads the error.json or error.txt file from the
    `output_folder` and returns the content

    Args:
        output_folder (str): folder where is located error.[json, txt] file
        return_code (int): process return code

    Returns:
        Union[str, None]: None if file doesn't exist or file content
    """
    filename = os.path.join(output_folder, 'error.json')
    if os.path.exists(filename):
        try:
            with open(filename) as FL:
                error_data = json.load(FL)
                if "error_code" in error_data and "message" in error_data:
                    return error_data
        except Exception:
            if return_code != 0:
                logger.error("Exception caught in get_error_message!")
                logger.exception("Error while reading error.json")
    else:
        filename = os.path.join(output_folder, 'error.txt')
        try:
            if not os.path.exists(filename):
                return None
            with open(filename) as f:
                error_code = f.readline()[:-1]
                error_message = f.readline().strip()
                return error_code + ": " + error_message
        except Exception:
            if return_code != 0:
                logger.error('Exception caught in get_error_message!')
                logger.exception("Error while reading error.txt")
    return


def call_command(cmd: str, command_name: str, output_folder: str = None,
                 silent: bool = False, print_command: bool = True) -> Tuple[int, str, str]:
    """Calls a shell command, prints stdout/stderr and returns the return code
    Known issue: stdout and stderr are not synced
    Also tries to read error.txt from output_folder and return it
    Finally, stderr is also returned

    Args:
        cmd (str): command (like in Unix shell)
        command_name (str): name of the command (for logging)
        output_folder (str, optional): The output folder where the command 
                                       will save error.[json,txt] outpur. Defaults to None.
        silent (bool, optional): Prints the command output on failure. Defaults to False.
        print_command (bool, optional): if true will print the command. Defaults to True.

    Returns:
        [Tuple]: exit code of the command, error message from error.txt, stderr output
    """
    if not silent and print_command:
        logger.info("Calling {}".format(cmd))

    # TODO: timeout?
    process = PrettyPopen(args=cmd,
                          shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)

    out, err = process.communicate()

    if out and not silent:
        logger.info(out.decode('utf-8', 'ignore'))
    if err:
        logger.info("Subprocess stderr:")
        logger.info(err.decode('utf-8', 'ignore'))

    if process.returncode != 0 or not silent:
        logger.info("Command {} is completed with error code {}".format(
            command_name, process.returncode))

    if output_folder is not None:
        error_msg_from_txt = get_error_message(output_folder, process.returncode)
        return process.returncode, error_msg_from_txt, err.decode('utf-8', 'ignore')
    error_message = None
    if process.returncode:
        error_message = f"Return code: {process.returncode}"

    return process.returncode, error_message, err.decode('utf-8', 'ignore')
