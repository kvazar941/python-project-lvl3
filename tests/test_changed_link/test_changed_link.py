"""test_changed_link"""
import os.path
from loader.engine import changed_link
from loader.file_reader import read_file

CONTENT = read_file('tests/test_changed_link/fixtures/original_file.html')
RESULT_CONTENT = read_file('tests/test_changed_link/fixtures/result_file.html')


def test_changed_link():
    dict_changed = {"/assets/application.css": "ru-hexlet-io-courses_files/ru-hexlet-io-assets-application.css",
    "/courses": "ru-hexlet-io-courses_files/ru-hexlet-io-courses.html",
    "/assets/professions/nodejs.png": "ru-hexlet-io-courses_files/ru-hexlet-io-assets-professions-nodejs.png",
    "https://ru.hexlet.io/packs/js/runtime.js": "ru-hexlet-io-courses_files/ru-hexlet-io-packs-js-runtime.js"
    }
    assert changed_link(dict_changed, CONTENT) == RESULT_CONTENT
