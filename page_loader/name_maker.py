"""name_maker module."""
from urllib.parse import urlparse

import requests


def make_simple_name(name):
    """
    Convert 'https://ru.hexlet.io' format to 'ru-hexlet-io' format.

    Args:
        name: str

    Returns:
        str
    """
    url = urlparse(name)
    full_way = ''.join([url.netloc + url.path])
    way = full_way.replace('.', '-')
    return way.replace('/', '-')


def make_name_html(name):
    if not name.endswith('.html'):
        return '.'.join([make_simple_name(name), 'html'])
    return '.'.join([make_simple_name(name)[:-5], 'html'])


def make_name_path(name):
    return '_'.join([make_simple_name(name), 'files'])


def make_name_file(directory, name):
    url = requests.head(name)
    if url.headers['content-type'] == 'text/html; charset=utf-8':
        current_file_name = make_name_html(name)
    else:
        split_name = name.split('.')
        way = '.'.join(split_name[:-1])
        extension = f'.{split_name[-1]}'
        current_file_name = ''.join([make_simple_name(way), extension])
    return '/'.join([directory, current_file_name])
