"""test_make_name_html."""
from page_loader.name_maker import make_name_html


def test_make_name_html():
    page_one = 'https://ru.hexlet.io/courses'
    page_two = 'https://ru.hexlet.io/courses.html'
    page_three = 'https://ru.hexlet.io'
    assert make_name_html(page_one) == 'ru-hexlet-io-courses.html'
    assert make_name_html(page_two) == 'ru-hexlet-io-courses.html'
    assert make_name_html(page_three) == 'ru-hexlet-io.html'
