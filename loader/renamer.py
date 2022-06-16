"""renamer module."""
import os
from urllib.parse import urlparse


def rename(name):
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


def rename_to_html(name):
    if name.endswith('.html'):
        name = name[:-5]
    return '.'.join([rename(name), 'html'])


def rename_to_dir(name):
    return '_'.join([rename(name), 'files'])


def rename_to_file(directory, name):
    way, extension = os.path.splitext(name)
    if extension == '':
        current_file_name = rename_to_html(way)
    else:
        current_file_name = ''.join([rename(way), extension])
    return '/'.join([directory, current_file_name])
