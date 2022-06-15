"""test_get_data."""
from loader.data_recipient import get_data

LINK = 'https://ru.hexlet.io/courses'
RESEIVED_CODE = 200


def test_get_data(requests_mock):
    requests_mock.get(LINK, status_code=RESEIVED_CODE, text='content')
    assert get_data(LINK).status_code == RESEIVED_CODE
    assert get_data(LINK).text == 'content'
