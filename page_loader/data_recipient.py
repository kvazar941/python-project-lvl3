"""data_recipient module."""
import logging

import requests

ERROR = 'The resource "{0}" is not available.'
CODE_VALID = 200
MESSAGE = 'The response to the resource {0} request was received'


def get_data(link):
    """
    Get data by link.

    Args:
        link: str

    Returns:
        requests object or exit of programm
    """
    try:
        link_data = requests.get(link)
        assert link_data.status_code == CODE_VALID
        logging.info(MESSAGE.format(link))
    except ConnectionError:
        logging.error(ERROR.format(link))
        raise ConnectionError(ERROR.format(link))
    return link_data
