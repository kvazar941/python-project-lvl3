"""test_make_directory"""
import os.path
from loader.engine import make_directory
from loader.file_reader import read_file

DIRECTORY = 'tests/test_make_directory/test_directory/test/'


def test_make_directory():
    assert os.path.exists(DIRECTORY) == False
    make_directory(DIRECTORY)
    assert os.path.exists(DIRECTORY) == True
    os.rmdir(DIRECTORY)
