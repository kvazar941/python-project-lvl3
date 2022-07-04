"""downloader module."""
import logging
import os
from bs4 import BeautifulSoup

from page_loader.data_recipient import get_data
from page_loader.file_reader import read_file
from page_loader.file_writer import write_file

ERROR = 'Unable to create a directory {0}.'


def download_file(link, way_to_file):
    """
    Upload the file from the link to the file.

    Args:
        link: str
        way_to_file: str

    Returns:
        recorded file
    """
    if os.path.exists(way_to_file):
        if get_data(link).content == read_file(way_to_file, 'rb'):
            return
    write_file(way_to_file, get_data(link).content, 'wb')


def download_html(way_to_file, cont):
    """
    Record the content from to the file.

    Args:
        cont: str
        way_to_file: str

    Returns:
        recorded file
    """
    if os.path.exists(way_to_file):
        if cont == read_file(way_to_file, 'rb'):
            return
    soup = BeautifulSoup (cont, 'html.parser')
    write_file(way_to_file, soup.prettify(formatter="html5"))


def make_directory(way):
    """
    Make directory to way.

    Args:
        way: str

    Returns:
        created directory or exit of programm
    """
    #try:
    if not os.path.exists(way):
        logging.info('directory {0} not found'.format(way))
        os.mkdir(way)
        logging.info('directory {0} created'.format(way))
    else:
        logging.info('directory {0} found'.format(way))
    #except Exception:
    #    logging.info(ERROR.format(way))
    #    raise FileNotFoundError(ERROR.format(way))
