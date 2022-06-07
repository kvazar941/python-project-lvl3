"""test_download_file"""
import requests
import requests_mock
import os.path
from loader.engine import download_file
from loader.file_reader import read_file
WAY = 'tests/test_download_file/fixtures/downloaded_file.css'
SOURCE_ONE = 'https://ru.hexlet.io/courses/assets/application.css'
TEXT_RESULT = 'tests/test_download_file/fixtures/TEXT_RESULT.css'


def test_download_file(requests_mock):
    requests_mock.get(SOURCE_ONE, text=read_file(TEXT_RESULT))
    assert os.path.exists(WAY) == False
    download_file(SOURCE_ONE, WAY)
    assert os.path.exists(WAY) == True
    assert read_file(WAY) == read_file(TEXT_RESULT)
    os.remove(WAY)
