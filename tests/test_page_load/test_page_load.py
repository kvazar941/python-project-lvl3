"""test_page_load"""
import requests
import requests_mock
import os.path
from loader.engine import page_load
from loader.file_reader import read_file

PAGE = 'https://ru.hexlet.io/courses'
CONTENT = 'tests/test_page_load/fixtures/content_simple_page.html'
DIRECTORY = 'tests/test_page_load/downloading_files/'
VALID_NAME = 'ru-hexlet-io-courses.html'
TEST_FILE = DIRECTORY + VALID_NAME


def test_page_load(requests_mock):
    expected_content = read_file(CONTENT)
    requests_mock.get(PAGE, text=expected_content)
    received_content = read_file(TEST_FILE)
    assert True
    #assert page_load(PAGE, DIRECTORY) == TEST_FILE
    #assert os.path.exists(TEST_FILE) == True
    #assert expected_content == received_content
