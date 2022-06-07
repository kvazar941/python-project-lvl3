"""test_download_html"""
import os.path
from loader.engine import download_html
from loader.file_reader import read_file

CONTENT = 'tests/test_download_html/fixtures/content.html'
TEXT_RESULT = 'tests/test_download_html/fixtures/TEXT_RESULT.html'


def test_download_html():
    assert os.path.exists(TEXT_RESULT) == False
    download_html(TEXT_RESULT, read_file(CONTENT))
    assert os.path.exists(TEXT_RESULT) == True
    assert read_file(CONTENT) == read_file(TEXT_RESULT)
    os.remove(TEXT_RESULT)
