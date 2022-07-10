"""logging module."""
import logging
import sys

LOGGER_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # noqa WPS323


logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
log_handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter(LOGGER_FORMAT)
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)


def log_debug(message):
    logger.debug(message)


def log_info(message):
    logger.info(message)


def log_error(message):
    logger.error(message)
