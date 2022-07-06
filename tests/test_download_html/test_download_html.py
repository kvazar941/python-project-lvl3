"""test_download_html."""
import os
import tempfile

from page_loader.downloader import download_html
from page_loader.file_reader import read_file

TEST_NAME = 'test_file.html'


def test_download_html():
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = tmpdirname + TEST_NAME
        assert not os.path.exists(way_result)
        download_html(way_result, 'content')
        assert os.path.exists(way_result)
        assert read_file(way_result) == 'content\n'
