"""data_recipient module."""
import requests

ERROR = 'The resource "{0}" is not available.'


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
    except Exception:
        print(''.join([ERROR.format(link), text_explanation]))
        raise ConnectionError
    return link_data
