"""checker module."""
import logging
import os

from page_loader.data_recipient import get_data

VALID_CODE = 200


def check_url(url):
    get_data(url)


def check_way(way):
    if not os.path.exists(way):
        logging.error('The directory {0} does not exist'.format(way))
        raise FileNotFoundError('The directory {0} does not exist'.format(way))
    if way in {'/sys', '/bin'}:
        logging.error('write to directory {0} is not available'.format(way))
        raise OSError('write to directory {0} is not available'.format(way))
    if not os.path.isdir(way):
        logging.error('way {0} is not directory'.format(way))
        raise OSError('way {0} is not directory'.format(way))
    else:
        logging.info('The download path was obtained: "{0}"'.format(way))
