"""test_get_sourses."""
import os
import tempfile

from page_loader.engine import get_sourses
from page_loader.renamer import rename_to_dir

CODE = 200
INTERCEPTED_LINK = 'https://ru.hexlet.io/assets/menu.css'


def test_get_sourses(requests_mock):
    requests_mock.get(INTERCEPTED_LINK, status_code=CODE, text='content')
    test_list = ['https://ru.hexlet.io/assets/menu.css']
    with tempfile.TemporaryDirectory() as tmpdirname:
        dir_name = rename_to_dir('https://ru.hexlet.io/courses')
        way_to_dir = ''.join([tmpdirname, dir_name])
        assert not os.path.exists(way_to_dir)
        get_sourses(test_list, way_to_dir, 'texst')
        assert os.path.exists(way_to_dir)
