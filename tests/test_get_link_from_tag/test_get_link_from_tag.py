"""test_get_link_from_tag"""
import requests
import requests_mock
import os.path
from bs4 import BeautifulSoup
from loader.page_object import get_link_from_tag
from loader.file_reader import read_file

TEST_CONTENT = 'tests/test_get_link_from_tag/fixtures/test_content.html'


def test_get_link_from_tag():
    content = read_file(TEST_CONTENT)
    reseived_img = ['/assets/professions/nodejs.png']
    reseived_links = ['/assets/application.css', '/courses']
    reseived_scripts = ['https://ru.hexlet.io/packs/js/runtime.js']
    assert get_link_from_tag(content, 'src', 'img', 'ru.hexlet.io') == reseived_img    
    assert get_link_from_tag(content, 'href', 'link', 'ru.hexlet.io') == reseived_links
    assert get_link_from_tag(content, 'src', 'script', 'ru.hexlet.io') == reseived_scripts
