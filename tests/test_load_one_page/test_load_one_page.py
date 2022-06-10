"""test_load_one_page"""
import requests
import requests_mock
import os.path
import tempfile
from loader.engine import load_one_page
from loader.file_reader import read_file

LINK = 'https://ru.hexlet.io/courses'
LINKS = ['https://ru.hexlet.io/courses',
         'https://ru.hexlet.io/courses/assets/professions/nodejs.png',
         'https://ru.hexlet.io/courses/https:/cdn2.hexlet.io/assets/menu.css',
         'https://ru.hexlet.io/courses/assets/application.css',
         'https://ru.hexlet.io/courses/courses',
         'https://ru.hexlet.io/courses/https:/js.stripe.com/v3/',
         'https://ru.hexlet.io/courses/https:/ru.hexlet.io/packs/js/runtime.js']


def test_load_one_page(requests_mock):
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = tmpdirname
        requests_mock.get(LINK, status_code=200, text='content')
        for link in LINKS:
            requests_mock.get(link, status_code=200, text='')
        reseived_result = way_result + '/' + 'ru-hexlet-io-courses.html'
        assert load_one_page(LINK, tmpdirname + '/') == reseived_result
