"""checker module."""
import os

from page_loader.logger import log_error, log_info


def check_way(way):
    if not os.path.exists(way):
        log_error('The directory {0} does not exist'.format(way))
        raise FileNotFoundError('The directory {0} does not exist'.format(way))
    if way in {'/sys', '/bin'}:
        log_error('write to directory {0} is not available'.format(way))
        raise OSError('write to directory {0} is not available'.format(way))
    if not os.path.isdir(way):
        log_error('way {0} is not directory'.format(way))
        raise OSError('way {0} is not directory'.format(way))
    else:
        log_info("The download path was obtained: '{0}'".format(way))
