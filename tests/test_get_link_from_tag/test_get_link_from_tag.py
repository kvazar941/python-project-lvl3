"""test_get_link_from_tag"""
import requests
import requests_mock
import os.path
from bs4 import BeautifulSoup
from loader.engine import get_link_from_tag
from loader.file_reader import read_file

TEST_CONTENT = 'tests/test_get_link_from_tag/fixtures/test_content.html'


def test_get_link_from_tag():
    content = read_file(TEST_CONTENT)
    reseived_img = ["/assets/professions/nodejs.png"]
    reseived_links = ["https://cdn2.hexlet.io/assets/menu.css",
                "/assets/application.css",
                "/courses",
                 ]
    reseived_scripts = ["https://js.stripe.com/v3/",
                        "https://ru.hexlet.io/packs/js/runtime.js"
                        ]
    assert get_link_from_tag(content, 'src', 'img') == reseived_img    
    assert get_link_from_tag(content, 'href', 'link') == reseived_links
    assert get_link_from_tag(content, 'src', 'script') == reseived_scripts
