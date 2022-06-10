"""test_get_sourses"""
import requests
import requests_mock
import os.path
import tempfile
from loader.engine import get_sourses
from loader.file_reader import read_file

TEST_LIST = ["https://cdn2.hexlet.io/assets/menu.css"]


def test_get_sourses(requests_mock):
    requests_mock.get("https://cdn2.hexlet.io/assets/menu.css", 
                      status_code=200, 
                      text='content'
                      )
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = tmpdirname + '/' + 'cdn2-hexlet-io-assets-menu.css'
        assert os.path.exists(way_result) == False
        result_dict = {'https://cdn2.hexlet.io/assets/menu.css': way_result}
        assert get_sourses(TEST_LIST, tmpdirname, 'TEXT') == result_dict
        assert os.path.exists(way_result) == True
    
