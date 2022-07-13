"""test_make_name_dir."""
from page_loader.name_maker import make_name_dir


def test_make_name_path():
    page_one = 'https://ru.hexlet.io/courses'
    result_name = 'ru-hexlet-io-courses_files'
    assert make_name_dir(page_one) == result_name
