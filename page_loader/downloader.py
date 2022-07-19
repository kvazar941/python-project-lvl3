"""downloader module."""
import os

from bs4 import BeautifulSoup

from page_loader.data_recipient import get_content
from page_loader.file_writer import write_file
from page_loader.logger import log_debug


def download_file(link, way_to_file):
    """
    Upload the file from the link to the file.

    Args:
        link: str
        way_to_file: str

    Returns:
        recorded file
    """
    write_file(way_to_file, get_content(link), 'wb')


def download_html(way_to_file, cont):
    """
    Record the content from to the file.

    Args:
        cont: str
        way_to_file: str

    Returns:
        recorded file
    """
    soup = BeautifulSoup(cont, 'html.parser')
    write_file(way_to_file, soup.prettify(formatter='html5'))


def make_directory(way):
    """
    Make directory to way.

    Args:
        way: str

    Returns:
        created directory or exit of programm
    """
    if not os.path.exists(way):
        log_debug('Directory {0} not found. Create directory.'.format(way))
        os.mkdir(way)
        log_debug('Directory {0} created.'.format(way))
    else:
        log_debug('Directory {0} found.'.format(way))
