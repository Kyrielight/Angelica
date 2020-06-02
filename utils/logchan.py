"""
Handles logging control across the entire application
"""

import logging

from inspect import stack, getmodule
from os.path import basename
from typing import Tuple

class LoggingColors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'

    LRED = '\033[91m'
    LGREEN = '\033[92m'
    LYELLOW = '\033[93m'
    LBLUE = '\033[94m'
    LMAGENTA = '\033[95m'
    LCYAN = '\033[96m'

    _ENDC = '\033[0m'

logging.basicConfig(format="[%(asctime)s][%(levelname)s]: %(message)s",
                    datefmt="%a|%b%y|%X|%Z")
_logger = logging.getLogger(name="Izumi")
_logger.setLevel(logging.DEBUG)

_LOGGING_STR = "[{}:{}]: {}"

def debug(msg: str, color: str = "") -> None:
    _logger.debug("{}{}{}".format(color, _LOGGING_STR.format(
        *_get_calling_details(), msg), LoggingColors._ENDC))


def info(msg: str, color: str = "") -> None:
    _logger.info("{}{}{}".format(color, _LOGGING_STR.format(
        *_get_calling_details(), msg), LoggingColors._ENDC))


def warning(msg: str, color: str = "") -> None:
    _logger.warning("{}{}{}".format(color, _LOGGING_STR.format(
        *_get_calling_details(), msg), LoggingColors._ENDC))


def error(msg: str, color: str = "") -> None:
    _logger.error("{}{}{}".format(color, _LOGGING_STR.format(
        *_get_calling_details(), msg), LoggingColors._ENDC))


def critical(msg: str, color: str = "") -> None:
    _logger.critical("{}{}{}".format(color, _LOGGING_STR.format(
        *_get_calling_details(), msg), LoggingColors._ENDC))


def _get_calling_details() -> Tuple[str, str]:
    """Gets the name of the file that called a logging function for logging output"""
    
    # Set to 2, because it's a second level up calling trace
    frame = stack()[2]
    # The third object in the tuple is the function name
    functionname = str(frame[3])
    module = getmodule(frame[0])
    filename = _get_base_filename(module.__file__)
    return (filename, functionname)


def _get_base_filename(filename: str) -> str:
    """Gets the basename of the filename, used for logging purposes"""
    return basename(filename)
