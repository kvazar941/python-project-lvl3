"""test_make_simple_name."""
from page_loader.name_maker import make_simple_name


def test_make_simple_name():
    name_one = 'https://ru.hexlet.io/courses'
    name_two = 'ru.hexlet.io/courses'
    name_three = 'ru.hexlet.io/courses.html'
    assert make_simple_name(name_one) == 'ru-hexlet-io-courses'
    assert make_simple_name(name_two) == 'ru-hexlet-io-courses'
    assert make_simple_name(name_three) == 'ru-hexlet-io-courses-html'
