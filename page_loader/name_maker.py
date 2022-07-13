"""name_maker module."""
from pathlib import Path
from urllib.parse import urlparse


def make_simple_name(reseived_url):
    """
    Convert 'https://ru.hexlet.io' format to 'ru-hexlet-io' format.

    Args:
        reseived_url: str

    Returns:
        str
    """
    url = urlparse(reseived_url)
    full_way = ''.join([url.netloc + url.path])
    way = full_way.replace('.', '-')
    return way.replace('/', '-')


def make_name_html(url):
    if not url.endswith('.html'):
        return '.'.join([make_simple_name(url), 'html'])
    return '.'.join([make_simple_name(url)[:-5], 'html'])


def make_name_dir(url):
    return '_'.join([make_simple_name(url), 'files'])


def make_full_path_dir(url, way):
    return '/'.join([way, make_name_dir(url)])


def make_name_file(directory, name):
    extension = Path(urlparse(name).path).suffix
    if extension == '':
        current_file_name = make_name_html(name)
    else:
        way = name[:-len(extension)]
        current_file_name = ''.join([make_simple_name(way), extension])
    return '/'.join([directory, current_file_name])
