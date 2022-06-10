"""test_make_directory"""
import os.path
import tempfile
from loader.engine import make_directory

DIRECTORY = 'test_directory'


def test_make_directory():
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = tmpdirname + '/' + DIRECTORY
        assert os.path.exists(way_result) == False
        make_directory(way_result)
        assert os.path.exists(way_result) == True
