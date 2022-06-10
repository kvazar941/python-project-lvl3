"""test_get_data"""
import requests
import requests_mock
import os.path
from loader.engine import get_data
from loader.file_reader import read_file

LINK = 'https://ru.hexlet.io/courses'


def test_get_data(requests_mock):
    requests_mock.get(LINK, 
                      status_code=200, 
                      text='content'
                      )
    assert get_data(LINK).status_code == 200
    assert get_data(LINK).text == 'content'
