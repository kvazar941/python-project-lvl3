"""test_make_name_file."""
from page_loader.name_maker import make_name_file


def test_rename_to_file():
    dir_ = './ru-hexlet-io-courses_files'
    link = 'https://ru.hexlet.io/lessons.rss'
    result_name = './ru-hexlet-io-courses_files/ru-hexlet-io-lessons.rss'
    assert make_name_file(dir_, link) == result_name
