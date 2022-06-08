"""test_get_sourses"""
import requests
import requests_mock
import os.path
from loader.engine import get_sourses
from loader.file_reader import read_file

TEST_LIST = ["https://cdn2.hexlet.io/assets/menu.css"
             ]
TEST_DIRECTORY = 'tests/test_get_sourses/fixtures'
TEST_CONTENT = 'tests/test_get_sourses/fixtures/test_file.css'
RESEIVED_DICT = {'https://cdn2.hexlet.io/assets/menu.css': 'tests/test_get_sourses/fixtures/cdn2-hexlet-io-assets-menu.css'}


def test_get_sourses(requests_mock):
    requests_mock.get("https://cdn2.hexlet.io/assets/menu.css", 
                      status_code=200, 
                      text=read_file(TEST_CONTENT)
                      )
    assert get_sourses(TEST_LIST, TEST_DIRECTORY, 'TEXT') == RESEIVED_DICT
    
