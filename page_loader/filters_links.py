"""page_object module."""
from urllib.parse import urlparse, urlunparse

from bs4 import BeautifulSoup

TAGS = {'img': 'src', 'link': 'href', 'script': 'src'}


def filter_links(content_html, netloc):
    """
    Get links from content_html.

    Args:
        content_html: str
        netloc: str

    Returns:
        list
    """
    soup = BeautifulSoup(content_html, 'html.parser')
    tags = soup.find_all(TAGS.keys())
    links = [tag.get(TAGS[tag.name]) for tag in tags]
    return [link for link in links if urlparse(link).netloc in {netloc, ''}]


def get_full_link(url, short_link):
    url_link = urlparse(url)
    url_short = urlparse(short_link)
    return url_short._replace(scheme=url_link.scheme, netloc=url_link.netloc)


def restore_links(url, links):
    return [urlunparse(get_full_link(url, link)) for link in links]
