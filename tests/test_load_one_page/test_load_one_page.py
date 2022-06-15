"""test_load_one_page."""
import tempfile

from loader.engine import load_one_page

LINK = 'https://ru.hexlet.io/courses'
RESEIVED_CODE = 200


def test_load_one_page(requests_mock):
    links = [
        'https://ru.hexlet.io/courses',
        'https://ru.hexlet.io/courses/assets/professions/nodejs.png',
        'https://ru.hexlet.io/courses/assets/menu.css',
        'https://ru.hexlet.io/courses/assets/application.css',
        'https://ru.hexlet.io/courses/courses',
        'https://ru.hexlet.io/courses/js.stripe.com/v3/',
        'https://ru.hexlet.io/courses/packs/js/runtime.js',
    ]
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = ''.join([tmpdirname, '/'])
        requests_mock.get(LINK, status_code=RESEIVED_CODE, text='content')
        for link in links:
            requests_mock.get(link, status_code=RESEIVED_CODE, text='')
        reseived_result = ''.join([way_result, 'ru-hexlet-io-courses.html'])
        assert load_one_page(LINK, way_result) == reseived_result
