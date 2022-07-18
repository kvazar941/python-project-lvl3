"""test_get_text."""
import pytest

from page_loader.data_recipient import get_text

LINK = 'https://ru.hexlet.io/courses'
RESEIVED_CODE = 200
RESEIVED_CODE_ERROR = 404


def test_get_text(requests_mock):
    requests_mock.get(LINK, status_code=RESEIVED_CODE, text='content')
    assert get_text(LINK) == 'content'


def test_get_text_errors(requests_mock):
    requests_mock.get(LINK, status_code=RESEIVED_CODE_ERROR, text='content')
    with pytest.raises(Exception):
        get_text(LINK)
