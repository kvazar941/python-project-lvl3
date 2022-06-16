"""logging module."""
import logging

from loader.downloader import make_directory

LOGGER_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DIRECTORY_LOGS = 'logs/'
NAME_REPORT_INFO = 'report_info.log'
NAME_REPORT_DEBUG = 'report_debug.log'


def log(message):
    make_directory(DIRECTORY_LOGS)
    logger = create_logger(DIRECTORY_LOGS)
    logger.info(message)
    logger.debug(message)


def create_logger(directory):
    """
    Create logger.

    Args:
        directory: str

    Returns:
        logger object
    """
    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)
    fi = logging.FileHandler(''.join([directory, NAME_REPORT_INFO]))
    fi.setLevel(logging.INFO)
    fd = logging.FileHandler(''.join([directory, NAME_REPORT_DEBUG]))
    fd.setLevel(logging.DEBUG)
    formatter = logging.Formatter(LOGGER_FORMAT)
    fi.setFormatter(formatter)
    fd.setFormatter(formatter)
    logger.addHandler(fi)
    logger.addHandler(fd)
    return logger
