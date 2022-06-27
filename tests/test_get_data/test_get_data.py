"""test_get_data."""
import pytest

from page_loader.data_recipient import get_data

LINK = 'https://ru.hexlet.io/courses'
RESEIVED_CODE = 200
RESEIVED_CODE_ERROR = 404


def test_get_data(requests_mock):
    requests_mock.get(LINK, status_code=RESEIVED_CODE, text='content')
    assert get_data(LINK).status_code == RESEIVED_CODE
    assert get_data(LINK).text == 'content'


def test_get_data_errors(requests_mock):
    requests_mock.get(LINK, status_code=RESEIVED_CODE_ERROR, text='content')
    with pytest.raises(Exception):
        get_data(LINK)
