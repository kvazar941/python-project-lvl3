"""page_object module."""
import logging
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from loader.data_recipient import get_data
from loader.renamer import rename_to_html

logging.basicConfig(filename='report.log', filemode='w', level=logging.INFO)

TEXT_IMG = 'Downloading images'
TEXT_LINKS = 'Downloading links'
TEXT_SCRIPTS = 'Downloading scripts'


def get_link_from_tag(content_html, source, tag, netloc):
    soup = BeautifulSoup(content_html, 'html.parser')
    list_tags = soup.find_all(tag)
    links = [atr[source] for atr in list_tags if atr.get(source)]
    list_result = []
    for link in links:
        if urlparse(link).netloc == netloc:
            list_result.append(link)
        if urlparse(link).netloc == '':
            list_result.append(link)
    return list_result


class Page():
    """
    Page.

    Args:
        name: str

    Returns:
        str
    """

    def __init__(self, url):
        """
        Init.

        Args:
            url: str

        Returns:
           str
        """
        self.url = url

    def valid_name(self):
        return rename_to_html(self.url)

    def get_netloc(self):
        return urlparse(self.url).netloc

    def response(self):
        return get_data(self.url)

    def content_url(self):
        return self.response().text

    def links_img(self):
        netloc = self.get_netloc()
        return get_link_from_tag(self.content_url(), 'src', 'img', netloc)

    def links_link(self):
        netloc = self.get_netloc()
        return get_link_from_tag(self.content_url(), 'href', 'link', netloc)

    def links_script(self):
        netloc = self.get_netloc()
        return get_link_from_tag(self.content_url(), 'src', 'script', netloc)
