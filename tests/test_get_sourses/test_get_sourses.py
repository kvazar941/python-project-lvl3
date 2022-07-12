"""test_get_sourses."""
import os
import tempfile

from page_loader.engine import get_sourses
from page_loader.name_maker import make_name_path

CODE = 200
INTERCEPTED_LINK = 'https://ru.hexlet.io/assets/menu.css'
HEAD = {'content-type': 'text/html; charset=utf-8'}


def test_get_sourses(requests_mock):
    requests_mock.get(INTERCEPTED_LINK, status_code=CODE, text='content')
    requests_mock.head(INTERCEPTED_LINK, text='content', headers=HEAD)
    test_list = ['https://ru.hexlet.io/assets/menu.css']
    with tempfile.TemporaryDirectory() as tmpdirname:
        dir_name = make_name_path('https://ru.hexlet.io/courses')
        way_to_dir = '/'.join([tmpdirname, dir_name])
        assert not os.path.exists(way_to_dir)
        os.mkdir(way_to_dir)
        get_sourses(test_list, way_to_dir)
        assert os.path.exists(way_to_dir)
