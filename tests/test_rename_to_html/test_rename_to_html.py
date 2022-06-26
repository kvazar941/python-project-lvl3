"""test_rename_to_html."""
from page_loader.renamer import rename_to_html


def test_rename_to_html():
    page_one = 'https://ru.hexlet.io/courses'
    page_two = 'https://ru.hexlet.io/courses.html'
    page_three = 'https://ru.hexlet.io'
    assert rename_to_html(page_one) == 'ru-hexlet-io-courses.html'
    assert rename_to_html(page_two) == 'ru-hexlet-io-courses.html'
    assert rename_to_html(page_three) == 'ru-hexlet-io.html'
