"""downloader module."""
import os

from page_loader.data_recipient import get_data
from page_loader.file_reader import read_file
from page_loader.file_writer import write_file

ERROR = "Cannot create directory '{0}'."


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
    write_file(way_to_file, cont)


def make_directory(way):
    """
    Make directory to way.

    Args:
        way: str

    Returns:
        created directory or exit of programm
    """
    text_explanation = '\n'.join([
        'Check the permissions on the path to the directory.',
        "If it's a network drive,",
        'check if the drive is accessible over the network.',
        'The program terminates, the page and resource is not loaded.',
    ])
    try:
        os.mkdir(way)
    except FileExistsError:
        pass
