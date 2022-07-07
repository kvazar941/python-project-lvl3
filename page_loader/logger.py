"""logging module."""
import logging

from page_loader.downloader import make_directory

LOGGER_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # noqa WPS323
NAME_REPORT_DEBUG = 'report_debug.log'


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
    fd = logging.FileHandler(''.join([directory, NAME_REPORT_DEBUG]))
    fd.setLevel(logging.DEBUG)
    formatter = logging.Formatter(LOGGER_FORMAT)
    fd.setFormatter(formatter)
    logger.addHandler(fd)
    return logger


def log(message, directory='logs/'):
    make_directory(directory)
    logger = create_logger(directory)
    logger.debug(message)
