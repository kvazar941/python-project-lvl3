"""checker module."""
import logging
import os

import requests

VALID_CODE = 200


def check_url(url):
    expected_url = requests.get(url)
    if expected_url.status_code != VALID_CODE:
        logging.error('"{0}" is not available.'.format(url))
        raise ConnectionError('"{0}" is not available.'.format(url))
    else:
        logging.error('The url was obtained: "{0}"'.format(url))


def check_way(way):
    if not os.path.exists(way):
        logging.info('The directory {0} does not exist'.format(way))
        raise FileNotFoundError('The directory {0} does not exist'.format(way))
    if way in {'/sys', '/bin'}:
        logging.info('write to directory {0} is not available'.format(way))
        raise OSError('write to directory {0} is not available'.format(way))
    if not os.path.isdir(way):
        logging.info('way {0} is not directory'.format(way))
        raise OSError('way {0} is not directory'.format(way))
    else:
        logging.info('The download path was obtained: "{0}"'.format(way))
