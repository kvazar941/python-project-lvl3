"""test_download_file."""
import os
import tempfile

from loader.downloader import download_file
from loader.file_reader import read_file

NAME = 'downloaded_file.css'
SOURCE_ONE = 'https://ru.hexlet.io/courses/assets/application.css'


def test_download_file(requests_mock):
    requests_mock.get(SOURCE_ONE, text='text')
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = tmpdirname + NAME
        assert not os.path.exists(way_result)
        download_file(SOURCE_ONE, way_result)
        assert os.path.exists(way_result)
        assert read_file(way_result) == 'text'
