"""name_maker module."""
import os
from urllib.parse import urlparse


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
    way, extension = os.path.splitext(name)
    if extension == '':
        current_file_name = make_name_html(way)
    else:
        current_file_name = ''.join([make_simple_name(way), extension])
    return '/'.join([directory, current_file_name])
