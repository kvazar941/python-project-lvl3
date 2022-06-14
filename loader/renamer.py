"""Engine module."""
import logging
import os
import sys
from urllib.parse import urlparse, urlunparse

import requests
from bs4 import BeautifulSoup
from progress.bar import Bar

from loader.file_reader import read_file
from loader.file_writer import write_file

logging.basicConfig(filename='report.log', filemode='w', level=logging.INFO)


def rename(name):
    """
    Convert a format to a format.

    'https://ru.hexlet.io/courses' to 'ru-hexlet-io-courses'.

    Args:
        name: str

    Returns:
        str
    """
    url = urlparse(name)
    full_way = url.netloc + url.path
    result_way = full_way.replace('.', '-')
    result_way = result_way.replace('/', '-')
    logging.info('message')
    return result_way


def rename_to_html(name):
    return '.'.join([rename(name), 'html'])


def rename_to_dir(name):
    return '_'.join([rename(name), 'files'])


def rename_to_file(dir_, name):
    way, extension = os.path.splitext(name)
    if extension == '':
        current_file_name = rename_to_html(way)
    else:
        current_file_name = rename(way) + extension
    return '/'.join([dir_, current_file_name])
