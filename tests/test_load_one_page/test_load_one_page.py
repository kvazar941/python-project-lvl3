"""test_load_one_page"""
import requests
import requests_mock
import os.path
from loader.engine import load_one_page
from loader.file_reader import read_file

LINK = 'https://ru.hexlet.io/courses'
links = ['https://ru.hexlet.io/courses',
         'https://ru.hexlet.io/courses/assets/professions/nodejs.png',
         'https://ru.hexlet.io/courses/https:/cdn2.hexlet.io/assets/menu.css',
         'https://ru.hexlet.io/courses/assets/application.css',
         'https://ru.hexlet.io/courses/courses',
         'https://ru.hexlet.io/courses/https:/js.stripe.com/v3/',
         'https://ru.hexlet.io/courses/https:/ru.hexlet.io/packs/js/runtime.js']
RESEIVED_RESULT = 'tests/test_load_one_page/fixtures/ru-hexlet-io-courses.html'
TEST_CONTENT = 'tests/test_load_one_page/fixtures/original_content.html'
WAY = 'tests/test_load_one_page/fixtures/'

def test_load_one_page(requests_mock):
    requests_mock.get(LINK,
                      status_code=200,
                      text=read_file(TEST_CONTENT)
                      )
    for a in links:
        requests_mock.get(a,
                      status_code=200,
                      text=''
                      )
    assert load_one_page(LINK, WAY) == RESEIVED_RESULT
