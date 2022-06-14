"""test_download_html"""
import os.path
import tempfile
from loader.downloader import download_html
from loader.file_reader import read_file

TEST_NAME = 'test_file.html'


def test_download_html():
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = tmpdirname + TEST_NAME
        assert os.path.exists(way_result) == False
        download_html(way_result, 'content')
        assert os.path.exists(way_result) == True
        assert read_file(way_result) == 'content'
