"""page_object module."""
from urllib.parse import urlparse, urlunparse

from bs4 import BeautifulSoup

TAGS = {'img', 'link', 'script'}
ATTRIBUTES = {'src', 'href'}


def pre_filter_tag(tag):
    return any([tag.has_attr(atr) for atr in ATTRIBUTES if tag.name in TAGS])


def get_links(content_html, netloc):
    """
    Get links from content_html.

    Args:
        content_html: str
        netloc: str

    Returns:
        list
    """
    soup = BeautifulSoup(content_html, 'html.parser')
    tags = soup.find_all(pre_filter_tag)
    links = [tag[atr] for tag in tags for atr in ATTRIBUTES if tag.get(atr)]
    return [link for link in links if urlparse(link).netloc in {netloc, ''}]


def get_full_link(url, short_link):
    url_link = urlparse(url)
    url_short = urlparse(short_link)
    return url_short._replace(scheme=url_link.scheme, netloc=url_link.netloc)


def restore_links(url, links):
    return [urlunparse(get_full_link(url, link)) for link in links]
