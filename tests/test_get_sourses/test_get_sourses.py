"""test_get_sourses."""
import os
import tempfile

from page_loader.engine import get_sourses

CODE = 200
INTERCEPTED_LINK = 'https://ru.hexlet.io/assets/menu.css'


def test_get_sourses(requests_mock):
    requests_mock.get(INTERCEPTED_LINK, status_code=CODE, text='content')
    test_list = ['https://ru.hexlet.io/assets/menu.css']
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = '/'.join([tmpdirname, 'ru-hexlet-io-assets-menu.css'])
        assert not os.path.exists(way_result)
        get_sourses(test_list, tmpdirname, 'texst')
        assert os.path.exists(way_result)
