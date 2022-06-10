"""test_download_file"""
import requests
import requests_mock
import os.path
import tempfile
from loader.engine import download_file
from loader.file_reader import read_file
NAME = 'downloaded_file.css'
SOURCE_ONE = 'https://ru.hexlet.io/courses/assets/application.css'


def test_download_file(requests_mock):
    requests_mock.get(SOURCE_ONE, text='text')
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = tmpdirname + NAME
        assert os.path.exists(way_result) == False
        download_file(SOURCE_ONE, way_result)
        assert os.path.exists(way_result) == True
        assert read_file(way_result) == 'text'
