"""data_recipient module."""
import requests

from page_loader.logger import log_debug, log_error

ERROR = 'The resource "{0}" is not available.'
CODE_VALID = [200, 300]
MESSAGE = 'The response to the resource {0} request was received'


def get_data(link):
    """
    Get data by link.

    Args:
        link: str

    Returns:
        str
    """
    link_data = requests.get(link)
    if link_data.status_code in CODE_VALID:
        log_debug(MESSAGE.format(link))
    else:
        log_error(ERROR.format(link))
        raise ConnectionError(ERROR.format(link))
    return link_data


def get_text(link):
    """
    Get data by link.

    Args:
        link: str

    Returns:
        str
    """
    return get_data(link).text


def get_content(link):
    """
    Get data by link.

    Args:
        link: str

    Returns:
        bin
    """
    return get_data(link).content
