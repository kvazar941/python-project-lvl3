"""engine module."""
import logging
import os
from urllib.parse import urlparse, urlunparse

from progress.bar import Bar

from page_loader.checker import check_url, check_way
from page_loader.downloader import download_file, download_html, make_directory
from page_loader.page_object import Page
from page_loader.renamer import rename_to_dir, rename_to_file

TEXT_IMG = 'Downloading images'
TEXT_LINK = 'Downloading source of links'
TEXT_SCRIPT = 'Downloading source of scripts'
VALID_CODE = 200
DEFAULT_WAY = os.getcwd()


def get_full_link(url, short_link):
    url_link = urlparse(url)
    url_short = urlparse(short_link)
    return url_short._replace(scheme=url_link.scheme, netloc=url_link.netloc)


def restore_links(url, links):
    return [urlunparse(get_full_link(url, link)) for link in links]


def get_sourses(list_links, directory, text_progress):
    """
    Download resources by links and return the dictionary with changed links.

    Args:
        list_links: list
        directory: str
        text_progress: str
    """
    logging.debug('Run get_sourses.')
    make_directory(directory)
    with Bar(text_progress, max=len(list_links)) as progress_bar:
        for link in list_links:
            logging.info('Downloading file "{0}".'.format(link))
            download_file(link, rename_to_file(directory, link))
            logging.info('File "{0}" download.'.format(link))
            progress_bar.next()
    logging.debug('Get_sourses complete.')


def changed_link(dict_changed, content_html):
    """
    Replace the links in the html content with local ones.

    Args:
        dict_changed: dict
        content_html: str

    Returns:
        str
    """
    new_content = content_html
    for link in dict_changed:
        new_content = new_content.replace(link, dict_changed[link])
    return new_content


def load_one_page(url, way):
    """
    Load the page and its resources..

    Args:
        url: str
        way: str

    Returns:
        str
    """
    logging.info('Run load one page.')
    page = Page(url)
    page_dir = rename_to_dir(page.url)
    dir_ = '/'.join([way, page_dir])
    texts = [TEXT_IMG, TEXT_LINK, TEXT_SCRIPT]
    lists = [page.links_img(), page.links_link(), page.links_script()]
    replased = {}
    for list_, text in zip(lists, texts):
        if list_:
            logging.info(' '.join(list_))
            links = restore_links(page.url, list_)
            logging.info(' '.join(links))
            get_sourses(links, dir_, text)
            for link_new, link_old in zip(links, list_):
                replased[link_old] = rename_to_file(page_dir, link_new)
    logging.info(replased)
    way_to_html = '/'.join([way, page.valid_name()])
    logging.info('Download_html, way: {0}.'.format(way_to_html))
    download_html(way_to_html, changed_link(replased, page.content_url()))
    logging.info('Html downloaded.')
    logging.info('Loaded one page.')
    return str(way_to_html)


def download(url_page, way_to_dir=DEFAULT_WAY):
    logging.info('Program launch.')
    check_url(url_page)
    check_way(way_to_dir)
    work_result = load_one_page(url_page, way_to_dir)
    logging.info('Program shutdown.')
    return work_result
