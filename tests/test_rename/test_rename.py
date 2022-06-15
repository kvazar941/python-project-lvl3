"""test_rename."""
from loader.renamer import rename


def test_rename():
    name_one = 'https://ru.hexlet.io/courses'
    name_two = 'ru.hexlet.io/courses'
    name_three = 'ru.hexlet.io/courses.html'
    assert rename(name_one) == 'ru-hexlet-io-courses'
    assert rename(name_two) == 'ru-hexlet-io-courses'
    assert rename(name_three) == 'ru-hexlet-io-courses-html'
