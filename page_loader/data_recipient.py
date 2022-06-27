"""data_recipient module."""
import requests

ERROR = 'The resource "{0}" is not available.'
CODE_ERROR = '<Response [404]>'
CODE_ERROR2 = '<Response [500]>'
CODE_VALID = 200


def get_data(link):
    """
    Get data by link.

    Args:
        link: str

    Returns:
        requests object or exit of programm
    """
    text_explanation = '\n'.join([
        'Check the network connection.',
        'Check availability of the resource or page.',
        'The program terminates, the page and resource is not loaded.',
    ])
    try:
        link_data = requests.get(link)
        assert link_data.status_code == CODE_VALID
    except ConnectionError:
        raise ConnectionError(''.join([ERROR.format(link), text_explanation]))
    return link_data
