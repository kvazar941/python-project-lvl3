"""data_recipient module."""
import sys

import requests

TEXT_ERROR = 'The resource "{0}" is not available.'


def get_data(link):
    text_explanation = '\n'.join([
        'Check the network connection.',
        'Check availability of the resource or page.',
        'The program terminates, the page and resource is not loaded.',
    ])
    try:
        link_data = requests.get(link)
    except Exception:
        print(''.join([TEXT_ERROR.format(link), text_explanation]))
        sys.exit(1)
    return link_data
