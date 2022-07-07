"""page_object module."""
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from page_loader.data_recipient import get_data


def get_link_from_tag(content_html, source, tag, netloc):
    """
    Get links from tags 'tag' containing attributes 'source'.

    Args:
        content_html: str
        source: str
        tag: str
        netloc: str

    Returns:
        list
    """
    soup = BeautifulSoup(content_html, 'html.parser')
    list_tags = soup.find_all(tag)
    links = [atr[source] for atr in list_tags if atr.get(source)]
    filtered_links = []
    for link in links:
        if urlparse(link).netloc in {netloc, ''}:
            filtered_links.append(link)
    return filtered_links


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

    def all_links(self):
        links_all = []
        links_all.extend(self.links_img())
        links_all.extend(self.links_link())
        links_all.extend(self.links_script())
        return links_all
