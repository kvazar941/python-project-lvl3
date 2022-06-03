"""test_rename"""
from loader.engine import rename

PAGE = 'https://ru.hexlet.io/courses'
VALID_NAME = 'ru-hexlet-io-courses'


def test_rename():
    expected = [PAGE]
    for item in expected:
        assert rename(item) == VALID_NAME
