"""test_make_directory."""
import os
import stat
import tempfile

import pytest

from page_loader.engine import make_directory

DIRECTORY = 'test_directory/'
DIRECTORY2 = 'test_directory/test/'


def test_make_directory():
    with tempfile.TemporaryDirectory() as tmpdirname:
        way_result = '/'.join([tmpdirname, DIRECTORY])
        assert not os.path.exists(way_result)
        make_directory(way_result)
        assert os.path.exists(way_result)


#def test_make_directory_error():
#    with tempfile.TemporaryDirectory() as tmpdirname:
#        way_result = '/'.join([tmpdirname, DIRECTORY])
#        os.mkdir(way_result)
#        os.chmod(way_result, stat.S_ENFMT)
#        with pytest.raises(Exception):
#            make_directory(way_result)
