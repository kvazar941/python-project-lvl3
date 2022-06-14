"""downloader module."""
import os
import sys

from loader.data_recipient import get_data
from loader.file_reader import read_file
from loader.file_writer import write_file


def download_file(link, way_to_file):
    if os.path.exists(way_to_file):
        if get_data(link).content == read_file(way_to_file, 'rb'):
            return
    write_file(way_to_file, get_data(link).content, 'wb')


def download_html(way_to_file, cont):
    if os.path.exists(way_to_file):
        if cont == read_file(way_to_file, 'rb'):
            return
    write_file(way_to_file, cont)


def make_directory(way):
    try:
        if os.path.exists(way):
            return
        else:
            os.mkdir(way)
    except Exception:
        print("Cannot create directory '{0}'.".format(way))
        print('Check the permissions on the path to the directory.')
        print("If it's a network drive,")
        print('check if the drive is accessible over the network.')
        print('The program terminates, the page and resource is not loaded.')
        sys.exit(1)
