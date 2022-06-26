"""test_get_link_from_tag."""
from page_loader.file_reader import read_file
from page_loader.page_object import get_link_from_tag

TEST_CONTENT = 'tests/test_get_link_from_tag/fixtures/test_content.html'
NETLOC = 'ru.hexlet.io'


def test_get_link_from_tag():
    content_url = read_file(TEST_CONTENT)
    images = ['/assets/professions/nodejs.png']
    links = ['/assets/application.css', '/courses']
    scripts = ['https://ru.hexlet.io/packs/js/runtime.js']
    assert get_link_from_tag(content_url, 'src', 'img', NETLOC) == images
    assert get_link_from_tag(content_url, 'href', 'link', NETLOC) == links
    assert get_link_from_tag(content_url, 'src', 'script', NETLOC) == scripts
