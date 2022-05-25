"""test_page_load"""
import requests
import pook
from loader.engine import page_load
from loader.file_reader import read

TEST_SIMPLE_PAGE = 'https://ru.hexlet.io/courses'
TEST_SIMPLE_RESPONSE = read('tests/fixtures/ru-hexlet-io-courses.html')
DEFAULT_DIRECTORY = './tests/downloading_files/'


@pook.on
def test_page_load_response():
    mock = pook.get(TEST_SIMPLE_PAGE, reply = 200)
    response = TEST_SIMPLE_RESPONSE
    assert page_load(TEST_SIMPLE_PAGE, DEFAULT_DIRECTORY) == '<Response [200]>'
    

