"""test_rename"""
from loader.engine import rename

PAGES = ['https://ru.hexlet.io/courses',
         'ru.hexlet.io/courses']

VALID_NAME = 'ru-hexlet-io-courses'


def test_rename():
    for item in PAGES:
        assert rename(item) == VALID_NAME
