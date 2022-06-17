"""test_get_data."""
from loader.data_recipient import get_data

LINK = 'https://ru.hexlet.io/courses'
RESEIVED_CODE = 200
RESEIVED_CODE_ERROR = 300


def test_get_data(requests_mock):
    requests_mock.get(LINK, status_code=RESEIVED_CODE, text='content')
    assert get_data(LINK).status_code == RESEIVED_CODE
    assert get_data(LINK).text == 'content'


def test_get_data_errors(requests_mock):
    requests_mock.get(LINK, status_code=RESEIVED_CODE_ERROR, text='content')
    assert get_data(LINK).status_code == RESEIVED_CODE_ERROR
    assert get_data(LINK).text == 'content'
