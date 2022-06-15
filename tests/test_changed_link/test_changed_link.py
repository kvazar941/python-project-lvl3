"""test_changed_link."""
from loader.engine import changed_link
from loader.file_reader import read_file

TEST_CONTENT = read_file('tests/test_changed_link/fixtures/original_file.html')
RESULT_RUN = read_file('tests/test_changed_link/fixtures/result_file.html')
DIRECTORY = 'ru-hexlet-io-courses_files'
WAY_ONE = '/'.join([DIRECTORY, 'ru-hexlet-io-assets-application.css'])
WAY_TWO = '/'.join([DIRECTORY, 'ru-hexlet-io-courses.html'])
WAY_THRE = '/'.join([DIRECTORY, 'ru-hexlet-io-assets-professions-nodejs.png'])
WAY_FOUR = '/'.join([DIRECTORY, 'ru-hexlet-io-packs-js-runtime.js'])


def test_changed_link():
    dict_changed = {
        '/assets/application.css': WAY_ONE,
        '/courses': WAY_TWO,
        '/assets/professions/nodejs.png': WAY_THRE,
        'https://ru.hexlet.io/packs/js/runtime.js': WAY_FOUR,
    }
    assert changed_link(dict_changed, TEST_CONTENT) == RESULT_RUN
