"""test_rename_to_dir."""
from loader.engine import rename_to_dir


def test_rename_to_dir():
    page_one = 'https://ru.hexlet.io/courses'
    result_name = 'ru-hexlet-io-courses_files'
    assert rename_to_dir(page_one) == result_name
