"""test_make_directory."""
import os
import tempfile

from page_loader.engine import make_directory

DIRECTORY = 'test_directory'


def test_make_directory():
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = '/'.join([tmpdirname, DIRECTORY])
        assert not os.path.exists(way_result)
        make_directory(way_result)
        assert os.path.exists(way_result)
