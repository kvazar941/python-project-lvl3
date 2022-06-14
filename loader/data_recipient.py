"""data_recipient module."""
import sys

import requests


def get_data(link):
    try:
        link_data = requests.get(link)
    except Exception:
        print('The resource "{0}" is not available.'.format(link))
        print('Check the network connection.')
        print('Check availability of the resource or page.')
        print('The program terminates, the page and resource is not loaded.')
        sys.exit(1)
    return link_data
