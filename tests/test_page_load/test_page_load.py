"""test_page_load"""
import requests
import requests_mock
import os.path
from loader.engine import page_load
from loader.file_reader import read_file

LINK = 'https://ru.hexlet.io/courses'
CONTENT = 'tests/test_page_load/fixtures/content.html'
DIRECTORY = 'tests/test_page_load/downloading_files/'
VALID_NAME = 'ru-hexlet-io-courses.html'
RESEIVED_RESULT = DIRECTORY + VALID_NAME
RESEIVED_CONTENT = 'tests/test_page_load/fixtures/content.html'


def test_page_load(requests_mock):
    requests_mock.get(LINK, 
                      status_code=200, 
                      text=read_file(RESEIVED_CONTENT)
                      )
    assert page_load(LINK, DIRECTORY) == RESEIVED_RESULT
