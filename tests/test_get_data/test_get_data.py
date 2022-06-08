"""test_get_data"""
import requests
import requests_mock
import os.path
from loader.engine import get_data
from loader.file_reader import read_file

LINK = 'https://ru.hexlet.io/courses'
RESEIVED_CONTENT = 'tests/test_get_data/fixtures/content.html'


def test_get_data(requests_mock):
    requests_mock.get(LINK, 
                      status_code=200, 
                      text=read_file(RESEIVED_CONTENT)
                      )
    assert get_data(LINK).status_code == 200
    assert get_data(LINK).text == read_file(RESEIVED_CONTENT)
