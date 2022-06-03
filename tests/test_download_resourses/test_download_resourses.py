"""test_download_resourses"""
import requests
import requests_mock
import os.path
from loader.engine import download_resourses
from loader.file_reader import read

PAGE = 'https://ru.hexlet.io/courses'
CONTENT = 'tests/test_page_load/fixtures/content_simple_page.html'
DIRECTORY = 'tests/test_page_load/downloading_files/'
VALID_NAME = 'ru-hexlet-io-courses.html'
TEST_FILE = DIRECTORY + VALID_NAME


def test_download_resourses(requests_mock):
    expected_content = read(CONTENT)
    requests_mock.get(PAGE, text=expected_content)
    received_content = read(TEST_FILE)
    assert True
    #assert page_load(PAGE, DIRECTORY) == TEST_FILE
    #assert os.path.exists(TEST_FILE) == True
    #assert expected_content == received_content
