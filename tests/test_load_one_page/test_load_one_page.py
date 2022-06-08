"""test_load_one_page"""
import requests
import requests_mock
import os.path
from loader.engine import load_one_page
from loader.file_reader import read_file

LINK = 'https://ru.hexlet.io/courses'
RESEIVED_RESULT = './ru-hexlet-io-courses.html'
TEST_CONTENT = 'tests/test_load_one_page/fixtures/content.html'
WAY = 'tests/test_load_one_page/fixtures'

def test_load_one_page(requests_mock):
    requests_mock.get(LINK, 
                      status_code=200,
                      text=read_file(TEST_CONTENT)
                      )
    assert load_one_page(LINK, WAY) == RESEIVED_RESULT
