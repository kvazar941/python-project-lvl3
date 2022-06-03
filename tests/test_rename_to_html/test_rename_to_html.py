"""test_rename_to_html"""
from loader.engine import rename_to_html


def test_rename_to_html():
    page_one = 'https://ru.hexlet.io/courses'
    page_two = 'https://ru.hexlet.io/courses.html'
    page_three = 'https://ru.hexlet.io/'
    result_name = 'ru-hexlet-io-courses.html'
    assert rename_to_html(page_one) == result_name
    #assert rename_to_html(page_two) == result_name
    #assert rename_to_html(page_three) == result_name
