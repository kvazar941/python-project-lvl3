"""test_download."""
import tempfile

from page_loader.engine import download

LINK = 'https://ru.hexlet.io/courses'
RESEIVED_CODE = 200


def test_download(requests_mock):
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
        requests_mock.get(LINK, status_code=RESEIVED_CODE, text='content')
        for link in links:
            requests_mock.get(link, status_code=RESEIVED_CODE, text='')
        reseived_result = '/'.join([tmpdirname, 'ru-hexlet-io-courses.html'])
        assert download(LINK, tmpdirname) == reseived_result
